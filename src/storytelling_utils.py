"""
Módulo com funções utilitárias para storytelling com dados
Adaptado do curso DSA - Data Science Academy
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Função para formatar os eixos de um gráfico (ax) com opção para borda direita
def covid_format_spines(ax, right_border = True):

    # Define a cor da borda inferior
    ax.spines['bottom'].set_color('#000000')

    # Define a cor da borda esquerda
    ax.spines['left'].set_color('#000000')

    # Torna a borda superior invisível
    ax.spines['top'].set_visible(False)

    # Verifica se a borda direita deve ser visível
    if right_border:

        # Se sim, define a cor da borda direita como branco
        ax.spines['right'].set_color('#FFFFFF')

    else:

        # Se não, também define a cor da borda direita como branco
        ax.spines['right'].set_color('#FFFFFF')

    # Define a cor de fundo do gráfico como branco
    ax.patch.set_facecolor('#FFFFFF')
    
# Define uma função para criar um gráfico de contagem (count plot)
def covid_count_plot(feature, df, colors = 'Reds', hue = False, ax = None, title = ''):

    # Inicializa uma variável com o número total de entradas no dataframe
    ncount = len(df)

    # Cria um gráfico de contagem com ou sem uma variável de agrupamento (hue)
    if hue != False:
        ax = sns.countplot(x = feature, data = df, palette = colors, hue = hue, ax = ax)
    else:
        ax = sns.countplot(x = feature, data = df, palette = colors, ax = ax)

    # Chama a função para formatar as bordas do gráfico
    covid_format_spines(ax)

    # Calcula e anota (imprime no gráfico) a porcentagem de cada barra no gráfico
    for p in ax.patches:

        # Obtém as coordenadas x do retângulo da barra
        x = p.get_bbox().get_points()[:,0]

        # Obtém a coordenada y do topo do retângulo da barra
        y = p.get_bbox().get_points()[1,1]

        # Anota a porcentagem acima da barra
        ax.annotate('{:.1f}%'.format(100. * y / ncount), (x.mean(), y), ha = 'center', va = 'bottom')

    # Define o título do gráfico com base na presença ou ausência da variável de agrupamento (hue)
    if not hue:

        # Sem variável de agrupamento
        ax.set_title(df[feature].describe().name + ' Análise', size = 13, pad = 15)

    else:

        # Com variável de agrupamento
        ax.set_title(df[feature].describe().name + ' Analisado Por ' + hue, size = 13, pad = 15)

    # Se um título personalizado foi fornecido, ele é definido aqui
    if title != '':
        ax.set_title(title)

    # Ajusta o layout do gráfico para evitar sobreposições de elementos gráficos
    plt.tight_layout()
    
# Define uma função para criar um gráfico de barras
def covid_bar_plot(x, y, df, colors = 'YlOrBr', hue = False, ax = None, value = False, title = ''):

    # Tenta calcular o total da variável y, se falhar, calcula o total da variável x
    try:

        # Calcula o total dos valores da coluna y
        ncount = sum(df[y])

    except:

        # Calcula o total dos valores da coluna x em caso de erro com y
        ncount = sum(df[x])

    # Cria um gráfico de barras com ou sem uma variável de agrupamento (hue)
    if hue != False:

        # Com variável de agrupamento
        ax = sns.barplot(x = x, y = y, data = df, palette = colors, hue = hue, ax = ax, ci = None)

    else:

        # Sem variável de agrupamento
        ax = sns.barplot(x = x, y = y, data = df, palette = colors, ax = ax, ci = None)

    # Chama a função para formatar as bordas do gráfico
    covid_format_spines(ax)

    # Anota o valor ou a porcentagem sobre cada barra no gráfico
    for p in ax.patches:

        # Obtém as coordenadas x do retângulo da barra
        xp = p.get_bbox().get_points()[:,0]

        # Obtém a coordenada y do topo do retângulo da barra
        yp = p.get_bbox().get_points()[1,1]

        # Se verdadeiro
        if value:

            # Anota o valor em milhares se value=True
            ax.annotate('{:.2f}k'.format(yp / 1000), (xp.mean(), yp), ha = 'center', va = 'bottom')

        else:

            # Anota a porcentagem se value=False
            ax.annotate('{:.1f}%'.format(100. * yp / ncount), (xp.mean(), yp), ha = 'center', va = 'bottom')

    # Define o título do gráfico com base na presença ou ausência da variável de agrupamento (hue)
    if not hue:

        # Sem variável de agrupamento
        ax.set_title(df[x].describe().name + ' Análise', size = 12, pad = 15)

    else:

        # Com variável de agrupamento
        ax.set_title(df[x].describe().name + ' Analisado Por ' + hue, size = 12, pad = 15)

    # Se um título personalizado foi fornecido, ele é definido aqui
    if title != '':

        # Define o título personalizado
        ax.set_title(title)

    # Ajusta o layout do gráfico para evitar sobreposições de elementos gráficos
    plt.tight_layout()
    
if __name__ == "__main__":
    print("Módulo de utilitários para storytelling COVID carregado com sucesso!")
