"""Build in a fresh directory. Preview can only serve a generated public site."""
from pathlib import Path
from datetime import datetime
import argparse,functools,http.server,json,logging,uuid

ROOT=Path(__file__).resolve().parent.parent

def build():
    from mkdocs.config import load_config
    from mkdocs.commands.build import build as mkbuild
    target=ROOT/'.build'/('site-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:6])
    if target.exists():raise RuntimeError('Refusing to clean or overwrite an existing build')
    c=load_config(config_file=str(ROOT/'mkdocs.yml'),site_dir=str(target),strict=True)
    c.plugins.on_startup(command='build',dirty=False)
    try:mkbuild(c)
    finally:c.plugins.on_shutdown()
    (ROOT/'.build/latest.json').write_text(json.dumps({'site_dir':str(target)},indent=2),encoding='utf-8')
    print('BUILT',target)

def main():
    logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')
    p=argparse.ArgumentParser();p.add_argument('command',choices=['build','path','preview']);p.add_argument('--port',type=int,default=8766);a=p.parse_args()
    if a.command=='build':build();return
    target=Path(json.loads((ROOT/'.build/latest.json').read_text())['site_dir']).resolve()
    if not target.is_relative_to((ROOT/'.build').resolve()):raise RuntimeError('Invalid preview root')
    if a.command=='path':print(target);return
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(target));server=http.server.ThreadingHTTPServer(('127.0.0.1',a.port),handler)
    print('LOCAL PREVIEW http://127.0.0.1:'+str(a.port)+'/',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()

if __name__=='__main__':main()
