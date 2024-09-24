#pip install dash
#pip install pandas
#pip install openpyxl


#Estrutura dentro de um dashboard
#Layout -> tudo que vi ser visualizado
#Callbacks -> Funcionalidades que voce tera no dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Vendas.xlsx")
#Esta linha lê o arquivo Excel e armazena os dados em uma variavel chamada df

fig = px.bar(df, x="Produto",y="Quantidade", color= "ID Loja", barmode="group")
#Esta linha cria uma linha contendo os valores unicos da coluna
opcoes = list(df['ID Loja'].unique())
# esta linha adiciona a string "Todas as logjas ao final da lista de opções"
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com faturamento de todos os produtos separados por loja'),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )

])
# utilizado para mudar a interface cada vez que o usuário selecionar algo diferente
@app.callback(
    Output('grafico_quantidade_produto','figure'), #é uma função para atualização do gráfico
    Input('lista_lojas','value')
)

def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja",barmode="group")
    else: 
        tabela_filtrada= df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja",barmode="group")

    return fig

if __name__ == '__main__':
    app.run(debug=True)
