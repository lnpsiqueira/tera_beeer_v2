import pandas as pd
import numpy as np


### Dataframe from Untappd
def create_table():
    
    df_estilos = pd.read_csv('./data/lista_cervejas.csv', sep=';')
    
    return df_estilos


