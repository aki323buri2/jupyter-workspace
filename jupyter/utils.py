# %%
import pandas as pd 
from pathlib import Path 
from functools import reduce 
import csv

# %%
def fullpath(*path):
  root = Path(".")
  full = reduce(lambda a, b: Path(a) / Path(b), path, root)
  return full.resolve().absolute()
  
def ensure_dir(*path):
  dirname = fullpath(*path) 
  dirname.mkdir(parents=True, exist_ok=True)
  return dirname 

# fullpath("..", "path/to/dsit")

# %%
class dotdict(dict):
  def __setattr__(self, name, value):
    self[name] = value 
  def __getattr__(self, name):
    return self[name]

# dd = dotdict(dict(id=1000, name="shokuryu"))
# dd.title = "タイトル"
# dd 

# %%
def load_csv(filename, dtype=str, **kargs):
  return pd.read_csv(filename, dtype=dtype, **kargs)

def save_csv(df, filename, index=False, quoting=csv.QUOTE_ALL, encoding="utf-8_sig", **kargs):
  filename = fullpath(filename)
  df.to_csv(filename, index=index, quoting=quoting, encoding=encoding, **kargs)
  return filename 

# df = pd.DataFrame([dict(id=x, name=f"name of {x}") for x in range(10)])
# filename = fullpath(ensure_dir("_test"), "test.csv")
# save_csv(df, filename)
# load_csv(filename)

# %%



