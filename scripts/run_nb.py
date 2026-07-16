import sys
import nbformat
from nbclient import NotebookClient

path = sys.argv[1]
nb = nbformat.read(path, as_version=4)
client = NotebookClient(nb, timeout=300, kernel_name='python3',
                        resources={'metadata': {'path': 'notebooks'}})
client.execute()
nbformat.write(nb, path)
print(f'OK: {path}')
