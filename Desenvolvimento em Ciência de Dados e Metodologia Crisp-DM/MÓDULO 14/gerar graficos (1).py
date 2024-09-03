import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys


sns.set_theme()

meses = {
    "JAN":"01",
    "FER":"02",
    "MAR":"03",
    "ABR":"04",
    "MAI":"05",
    "JUN":"06",
    "JUL":"07",
    "AGO":"08",
    "SET":"09",
    "OUT":"10",
    "NOV":"11",
    "DEZ":"12"
}

print("O nome do nosso script é", sys.argv[0])

mes = sys.argv[1]

print("O mês de referência é", mes)

def plota_graficos(mes):
    
    
    mes = str(mes)
    
    base = pd.read_csv("./"+mes+".csv")          

    os.makedirs("./output/figs/", exist_ok=True) 

    fig, ax = plt.subplots(7, 1, figsize=[18, 42])

    pd.pivot_table(base, values='IDADEMAE', index='DTNASC',
                   aggfunc='mean').plot(ax = ax[0])
    pd.pivot_table(base, values='IDADEMAE', index='DTNASC',
                   aggfunc='count').plot(ax = ax[1])
    pd.pivot_table(base, values='IDADEMAE', index=['DTNASC', 'SEXO'],
                   aggfunc='count').unstack().plot(ax = ax[2])
    pd.pivot_table(base, values='PESO', index=['DTNASC', 'SEXO'],
                   aggfunc='count').unstack().plot(ax = ax[3])
    pd.pivot_table(base, values='PESO', index=['ESCMAE'],
                   aggfunc='median').sort_values('PESO').plot(ax = ax[4])
    pd.pivot_table(base, values='APGAR1', index=['GESTACAO'],
                   aggfunc='mean').sort_values('APGAR1').plot(ax = ax[5])
    pd.pivot_table(base, values='APGAR5', index=['GESTACAO'],
                   aggfunc='mean').sort_values('APGAR5').plot(ax = ax[6])

    ax[0].set_ylabel('média idade mãe');
    ax[1].set_ylabel('quantidade de nascimentos')
    ax[5].set_ylabel('apgar1 medio')
    ax[5].set_xlabel('gestacao')
    ax[6].set_ylabel('apgar5 medio')
    ax[6].set_xlabel('gestacao')
    
    mes_num = meses[mes]
    
    print("2019_"+mes_num+"") 
    
    return plt.savefig("./output/figs/2019_"+mes_num+".png")

plota_graficos(mes)

