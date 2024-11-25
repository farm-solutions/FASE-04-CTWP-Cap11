import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
import utils
import importlib

## Configs

importlib.reload(utils)
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
pd.set_option('display.max_rows', 100)      # Mostra até 100 linhas
pd.set_option('display.max_colwidth', 100)  # Máxima largura da coluna
pd.set_option('display.float_format', '{:.2f}'.format)  # Formato dos números flutuantes
pd.set_option('display.expand_frame_repr', False)  # Não quebra o DataFrame em múltiplas linhas
pd.set_option('display.max_rows', None)  # Mostra todas as linhas no output
warnings.filterwarnings('ignore')

# Colors
colors = ['#705557', '#b27b77', '#ddcac6', '#af9294', '#8c9a5b', '#708090', '#c5a880', '#a0522d']

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=colors)
sns.set_palette(sns.color_palette(colors))  
sns.set_theme(style="whitegrid")

# Params


# Bases
pasta_raw = '../data/raw/'
pasta_stage = '../data/stage/'
pasta_analitics = '../data/analitics/'

# Metadados
metadados = {
    "INDEX": {
        "index": 0,
        "descricao": "IDENTIFICADOR",
        "tipo": "IDENTIFICADOR",
        "relevancia": "NENHUMA",
        "dados_de": "NENHUM",
        "one_hot_encoding": 0,
        "analise": 0
    }
}

