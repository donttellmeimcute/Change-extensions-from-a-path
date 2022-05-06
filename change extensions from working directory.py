from pathlib import Path
path = Path('WORKING DIRECTORY')
for f in path.iterdir():
    if f.is_file() and f.suffix in ['.*']:
        f.rename(f.with_suffix('.jpg'))