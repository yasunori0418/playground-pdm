import toml
import os

basename: str = os.path.basename(__file__)
dirname: str = os.path.abspath(os.path.dirname(__file__))
print(basename)
print(dirname)
print(toml.load(os.path.join(dirname, 'config.toml')))
