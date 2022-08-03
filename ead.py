#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Versão Python utilizada
from platform import python_version
print('Versão da Linguagem Python utilizada neste Jupyter Notebook:', python_version())


# In[2]:


# Instalando pacotes

# !pip install -q -U watermark


# ## _Imports_

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[4]:


# Parâmetros de configuração dos gráficos
from matplotlib import rcParams

rcParams['figure.figsize'] = 12, 4
rcParams['lines.linewidth'] = 3
rcParams['xtick.labelsize'] = 'x-large'
rcParams['ytick.labelsize'] = 'x-large'


# In[5]:


# Versões dos pacotes usados
get_ipython().run_line_magic('reload_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-a "Sandro Luiz Mazzolla Junior" --iversions')


# ## Instalando às versões utilizadas neste pacote
# 
# !pip install nome_pacote = versão_pacote
# 
# __Exemplo__
# 
# !pip install pandas = 1.4.2

# ## _Carregando Dataset_

# In[6]:


df = pd.read_csv('dados/dataset.csv')


# In[7]:


# Formato do Dataset em linhas , colunas
df.shape


# In[8]:


# Informações sobre colunas do Dataset
df.info()


# In[9]:


# Mostrando os cinco primeiros itens do Dataset
df.head(5)


# In[10]:


# Amostra(5) do Dataset
df.sample(5)


# In[11]:


# Mostrando os cinco últimos itens do Dataset
df.tail(5)


# ### Separando Variáveis Categóricas e Numéricas

# In[12]:


df.columns


# In[13]:


df.dtypes


# In[14]:


# Lista de colunas categóricas
categoricas = ['corredor_armazem',
               'modo_envio',
               'prioridade_produto',
               'genero']


# In[15]:


# Lista de colunas numéricas
numericas = ['numero_chamadas_cliente',
             'avaliacao_cliente',
             'custo_produto',
             'compras_anteriores',
             'desconto',
             'peso_gramas']

# ID não possui nenhuma informação útil


# In[16]:


# Contando valores únicos (cada categoria) da variável alvo

# 1 classe positiva, entrega dentro do prazo
# 0 classe negativa, entrega fora do prazo
df['entregue_no_prazo'].value_counts()


# In[17]:


# Variável alvo, estudo será feito com base nesta variável
target = ['entregue_no_prazo']


# ### Explorando as Variáveis Numéricas

# In[18]:


# Resumo das Variáveis Numéricas
df[numericas].describe()


# Observações:
# 
# 1. As colunas `numero_chamadas_cliente`, `avaliacao_cliente` e `custo_produto` parecem ter uma distribuição bastante simétrica (média(mean) e mediana(50%) não são muito diferentes).
# 
# 2. As colunas `compras_anteriores` e `desconto` parecem estar inclinadas para a direita (Média(mean) maior do que a Mediana(50%)).
# 
# 3. A coluna `peso_gramas` parece estar mais inclinada para a esquerda (Média(mean) menor do que a Mediana(50%)).

# In[19]:


# Criando um histograma da variável custo_produto
df['custo_produto'].hist()


# In[20]:


# Criando um histograma da variável compras_anteriores
df['compras_anteriores'].hist()

