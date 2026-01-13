import sys
import pandas as pd

def main():
    print(sys.argv)    
    month = int(sys.argv[1])
    
    df = pd.DataFrame({"numbers": [1, 2, 3], "letters": ['a', 'b', 'c']})
    df['month'] = month
    print(df.head())    
    
    df.to_csv(f"output_month_{month}.csv", index=False)

    #more optimized file format
    df.to_parquet(f"output_month_{month}.parquet", index=False)
    
    print(f"Hello, World! It is the {month} month.")
    
    
if __name__ == "__main__":
    main()