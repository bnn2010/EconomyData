import pandas as pd

def  readURLs(url):
    data =pd.read_html(url)[0]

