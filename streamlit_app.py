import pandas as pd
import streamlit as st

dados = pd.read_csv('tarefas-teste.csv')
print(dados.head()) # Exibe as primeiras 5 linhas do DataFrame