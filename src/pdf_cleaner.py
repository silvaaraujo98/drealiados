import pandas as pd
import numpy as np
import pdfplumber


def read_all_pages(path):
    pdf = pdfplumber.open(path)
    num_pages = len(pdf.pages)
    return pdf,num_pages


def open_extract_pdf(pdf,i):
    page = pdf.pages[i]
    table = page.extract_table()
    return table

def create_dataframe(table):
   df = pd.DataFrame(table)
   return df

def cleaning_df(df):
    df.dropna(axis=1,inplace=True,thresh=len(df)/2)
    df_cleaned = df.iloc[:,[1,2,3]]
    df_cleaned.dropna(inplace=True)
    df_cleaned.columns = [1,2,3]
    return df_cleaned

def extract_all_pages(pdf,num_pages):
    df_final = pd.DataFrame([])
    for page in range(num_pages):
        table = open_extract_pdf(pdf,page)
        df = create_dataframe(table)
        df_limpo = cleaning_df(df)
        df_final = pd.concat([df_final,df_limpo])
    return df_final
def main(path):
    month = path[path.find("-")+1:path.find("-")+7]
    pdf,num_pages = read_all_pages(path)
    df_final = extract_all_pages(pdf,num_pages)
    df_final['Mes'] = month
    return df_final
