import datetime
import pandas as pd

# Get the current date
now = datetime.datetime.now()

# Convert the current date to ddmm format
dd_mm = now.strftime("%d%m")

print(dd_mm)  # Output: e.g. 0303 (for March 3rd)

file = pd.read_excel("check.xlsx")

file['kid'] = 'yes'


file.to_excel(f"{dd_mm}_barred.xlsx", index=False)


