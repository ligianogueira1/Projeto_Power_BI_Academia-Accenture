# Passo 1: criação do arquivo filmes.csv para armazenar os dados
# Passo 2: importação da biblioteca pandas para leitura dos arquivos

import pandas as pd
filmes_df = pd.read_csv("filmes.csv")

# Passo 3: convertendo dados armazenados como texto para números
filmes_df["ID"] = pd.to_numeric(filmes_df["ID"])

# Passo 4: removendo espaços desnecessários
filmes_df["Streaming"] = filmes_df["Streaming"].str.strip()

# Passo 5: convertendo dados INT para Float

filmes_df["Quantidade_de_Visualizações"] = filmes_df["Quantidade_de_Visualizações"].astype(float)

# Passo 6: exibindo os dados na tela
print(filmes_df)
