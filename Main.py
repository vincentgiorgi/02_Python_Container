import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("pandas:     " + pd.__version__)
print("numpy:      " + np.__version__ )
print("matplotlib: " + matplotlib.__version__)

# Path to your CSV (no headers)
csv_path = "TPU14-PEO21.csv"

# Read CSV with no header row
df = pd.read_csv(
    csv_path,
    sep=";",
    header=None,
    names=["Category", "Tag", "Timestamp", "Value"],
    decimal="."            # important for numeric parsing
)

# Parse timestamp format: DD.MM.YYYY HH:MM:SS.sss
df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    format="%d.%m.%Y %H:%M:%S.%f",
    errors="coerce"
)

# Clean
df = df.dropna(subset=["Timestamp"]).sort_values("Timestamp")
print(df["Tag"].unique())

tag = "FT617 Weir Water Flow"
df_tag = df[df["Tag"] == tag]

plt.figure(figsize=(12, 5))
plt.plot(df_tag["Timestamp"], df_tag["Value"], linewidth=1.5)
plt.title(tag)
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
plt.show()

