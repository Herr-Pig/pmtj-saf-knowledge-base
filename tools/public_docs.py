"""Only expose the standalone public policy; never access a sibling project."""
from pathlib import Path
from mkdocs.structure.files import File,InclusionLevel

def on_files(files,config):
    root=Path(config.config_file_path).parent
    files.append(File.generated(config,'publication-policy.md',abs_src_path=str(root/'PUBLICATION_POLICY.md'),inclusion=InclusionLevel.INCLUDED))
    return files
