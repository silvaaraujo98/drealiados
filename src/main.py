import os
from pdf_cleaner import *




def iterate_over_files_and_call_function():
    df_final = pd.DataFrame([])
    directory_in_str = "data/raw"
    directory = os.fsencode(directory_in_str)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("DRE"):
            df_inter = main(os.path.join(directory_in_str, filename))
            df_final = pd.concat([df_inter,df_final])
        else:
            pass
    return df_final

def excel_exporter(df):
    df[4] = df[3].str.replace(".","_").str.replace(",",".").str.replace("_",",")
    df.to_excel("data/processed/dres.xlsx",index=False)
excel_exporter(iterate_over_files_and_call_function())
