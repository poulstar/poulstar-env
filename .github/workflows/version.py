import toml
import os

def get_version():
  data=toml.load("./poulstar/pyproject.toml")
  version = data["tool"]["poetry"]["version"]
  return version

if __name__ == '__main__':
  version = get_version()
  with open(os.environ['GITHUB_OUTPUT'], 'at') as f:
    f.write(f"version={version}")
  
