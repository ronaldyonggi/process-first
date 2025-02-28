import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div (
    "Hello, this is my first Dash app!"
)

if __name__ == '__main__':
    app.run(debug=True)