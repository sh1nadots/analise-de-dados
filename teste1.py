from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel file://C:/Users/victo/Downloads/vendas-metasjunho.xlsx,
print(df) 

#fig = px.bar 

#app.layout = html.Div(children=[
#    html.H1(children='Teste'),
#
#    html.Div(children= '''
#    teste da bagaça
#    '''),

#    dcc.Graph(
#       id = 'example-graph',
#        figure = fig
#    ),
#])

#if __name__ == "__main__":
#  app.run_server(debug=True)