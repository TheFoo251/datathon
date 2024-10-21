import pandas as pd
from pathlib import Path 
frame = pd.read_csv(Path("data.csv"))
print(frame[0:10])