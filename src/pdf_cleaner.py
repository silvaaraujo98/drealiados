import pandas as pd
import numpy as np
import pdfplumber


def open_extract_pdf(path):
    pdf = pdfplumber.open(path)
    page0 = pdf.pages[0]
    table = page0.extract_table()

    return table

def create_dataframe(table):
   df = pd.DataFrame(table)
   return df

def cleaning_df(df):
    df_cleaned = df.iloc[:,[0,1,2,3]]
    df_cleaned.dropna(inplace=True)
    return df_cleaned


path  = "data/raw/DRE-Abr-24.pdf"
table = open_extract_pdf(path)
df = create_dataframe(table)
df_cleaned = cleaning_df(df)