from time import strftime, gmtime
import pandas as pd
from tabulate import tabulate
import os
import pyarrow.parquet
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Error: please specify input file")
        return
    file_path = sys.argv[1]
    schema = pyarrow.parquet.read_schema(file_path, memory_map=True)
    df = pd.read_parquet(file_path, engine="pyarrow")
    profile_column = pd.DataFrame({'Columns Name': df.columns, 'Data Type': map(lambda x: str(x), schema.types),
                                   'Null Count': df.isna().sum(), 'Distinct Values': df.nunique(), 'Minimum': df.min(),
                                   'Maximum': df.max()}, )
    profile_column.index = range(len(profile_column))

    general_info = pd.DataFrame([[len(df),
                                  os.stat(file_path).st_size / (1024 * 1024),
                                  df['ingest_ts'].max(), '']],
                                columns=['Number Of Rows', 'Size MB', 'Last Data update', 'Last Schema Update'])
    print(tabulate(profile_column, headers='keys', tablefmt='psql'))
    print(tabulate(general_info, headers='keys', tablefmt='psql'))
    file_path_without_extension = os.path.splitext(file_path)[0]
    date = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    with open(f"{date}_{file_path_without_extension}_profile_column.csv", "w") as f:
        f.write(profile_column.to_csv())
    with open(f"{date}_{file_path_without_extension}general_info.csv", "w") as f:
        f.write(general_info.to_csv())


if __name__ == '__main__':
    main()
