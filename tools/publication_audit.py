"""Audit every staged blob. Owner approval is checked separately from privacy checks."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,re,subprocess,urllib.parse,urllib.request

ROOT=Path(__file__).resolve().parent.parent
FORBIDDEN={'inputs','raw_data','derived_analysis','private','workspace','history','publication-review'}
BLOCKED={'.pdf','.doc','.docx','.ppt','.pptx','.csv','.tsv','.xls','.xlsx','.h5','.hdf5','.npy','.npz','.mat','.zip','.7z','.exe','.dll','.pem','.key','.p12'}
TOPICS=['01-pmtj-saf-design','02-w-ferromagnetic-coupling','03-ru-antiferromagnetic-coupling','04-copt-pma-optimization','05-moment-and-reversal','06-models-and-criteria']
SECRETS=[('private_key',r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),('github_token',r'(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{30,})'),('api_token',r'sk-(?:proj-)?[A-Za-z0-9_-]{24,}')]
PERSONAL=[('windows_absolute_path',r'(?i)\b[A-Z]:[\\/]'),('personal_home',r'/(?:Users|home)/[^\s/]+'),('email',r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')]

def git(*args,check=True):
    return subprocess.run(['git','-C',str(ROOT),*args],capture_output=True,check=check).stdout

def blob(path):return git('show',':'+path)

def verify_public_remote(remote):
    match=re.fullmatch(r'(?:https://github\.com/|git@github\.com:)([^/]+)/pmtj-saf-knowledge-base(?:\.git)?',remote)
    if not match:return 'Remote is not a credential-free GitHub public-project URL'
    try:
        url='https://api.github.com/repos/'+match.group(1)+'/pmtj-saf-knowledge-base'
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'PMTJ-SAF-publication-audit'}),timeout=15) as response:repo=json.load(response)
        if repo.get('private') is not False:return 'Remote has not been verified Public'
    except Exception:return 'Cannot verify remote repository exists and is Public'
    return None

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--release',action='store_true');parser.add_argument('--scaffold-only',action='store_true');parser.add_argument('--expected-commit');parser.add_argument('--remote-url');parser.add_argument('--report',default='.build/publication-audit.json');args=parser.parse_args()
    rows=[];errors=[]
    if Path(git('rev-parse','--show-toplevel').decode().strip()).resolve()!=ROOT:raise SystemExit('Not an independent repository')
    entries=git('ls-files','--stage','-z').split(b'\0');paths=[]
    for raw in entries:
        if not raw:continue
        meta,name=raw.split(b'\t',1);mode,oid,stage=meta.decode().split();path=name.decode('utf-8');paths.append(path)
        reasons=[];parts=PurePosixPath(path).parts;p=PurePosixPath(path)
        if mode not in ['100644','100755'] or stage!='0':reasons.append('symlink/submodule/unmerged entry')
        if any(x.lower() in FORBIDDEN for x in parts):reasons.append('private/experimental path')
        if p.suffix.lower() in BLOCKED or p.name.startswith('.env'):reasons.append('blocked file type')
        if 'library/files' in path.lower():reasons.append('full-text attachment tree')
        data=blob(path);text=data.decode('utf-8',errors='replace')
        if len(data)>5*1024*1024:reasons.append('large staged file')
        if b'\0' not in data:
            for kind,pattern in SECRETS+PERSONAL:
                if re.search(pattern,text):reasons.append(kind)
        rows.append({'path':path,'mode':mode,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'result':'pass' if not reasons else 'blocked','reasons':reasons})
        errors.extend(path+': '+x for x in reasons)
    if not paths:errors.append('Git index is empty')
    allow=json.loads(blob('publication/allowlist.json'))
    if set(paths)!=set(allow['files']):errors.append('Full staged file set differs from reviewed technical allowlist')
    images=json.loads(blob('publication/image-rights.json'))
    allowed_images={x['path']:x for x in images['research_images']}
    for row in rows:
        path=row['path'];suffix=PurePosixPath(path).suffix.lower()
        if suffix in ['.png','.jpg','.jpeg','.tif','.tiff','.svg']:
            item=allowed_images.get(path)
            if not item or not item.get('owner_approved') or not item.get('license_evidence_url') or not item.get('attribution'):errors.append(path+': missing owner-approved image rights')
    release_status='not_requested'
    if args.scaffold_only:
        baseline=json.loads(blob('publication/scaffold-baseline.json'))['docs']
        docs={p:hashlib.sha256(blob(p)).hexdigest() for p in paths if p.startswith('docs/') and p.endswith(('.md','.json'))}
        if docs!=baseline:errors.append('Scaffold-only upload would contain modified or additional scientific documents')
        release_status='technical_scaffold_only_no_scientific_publication'
    if args.release:
        release_status='blocked'
        approval=json.loads(blob('publication/owner-approval.json'))
        if not approval.get('owner_approved') or not approval.get('approved_by'):errors.append('Scientific files have not been selected and approved by the owner')
        approved=approval.get('approved_files',{})
        science=[p for p in paths if p.startswith('docs/') and p.endswith(('.md','.json'))]
        for path in science:
            if approved.get(path)!=hashlib.sha256(blob(path)).hexdigest():errors.append(path+': owner approval missing or stale')
        for topic in TOPICS:
            path='docs/topics/'+topic+'.md'
            value=blob(path).decode('utf-8') if path in paths else ''
            if len(value)<800 or not re.search(r'SRC-\d{6}',value):errors.append(path+': reviewed scientific note not imported')
        head=git('rev-parse','--verify','HEAD',check=False).decode().strip()
        if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}',head):errors.append('No commit has been created')
        if args.expected_commit and args.expected_commit!=head:errors.append('Requested reviewed commit does not match HEAD')
        if head and subprocess.run(['git','-C',str(ROOT),'diff-index','--quiet','--cached','HEAD'],capture_output=True).returncode:errors.append('Staged tree differs from commit to be pushed')
        if not errors:release_status='owner_approval_and_commit_checks_passed'
    if args.scaffold_only:
        head=git('rev-parse','--verify','HEAD',check=False).decode().strip()
        if args.expected_commit and args.expected_commit!=head:errors.append('Scaffold commit does not match reviewed HEAD')
        if head and subprocess.run(['git','-C',str(ROOT),'diff-index','--quiet','--cached','HEAD'],capture_output=True).returncode:errors.append('Staged scaffold differs from commit')
    if args.remote_url:
        issue=verify_public_remote(args.remote_url)
        if issue:errors.append(issue)
    report={'files':rows,'errors':errors,'checked_files':len(rows),'scope':'complete Git index, not selected diff only','release':release_status,'owner_review_is_not_replaced_by_scanner':True}
    output=ROOT/args.report;output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checked_files':len(rows),'errors':errors,'release':release_status},ensure_ascii=False))
    raise SystemExit(1 if errors else 0)

if __name__=='__main__':main()
