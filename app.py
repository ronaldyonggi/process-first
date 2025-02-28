import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

# Sample data using pandas DataFrame
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emily",
        "Frank",
        "Grace",
        "Henry",
        "Isabella",
        "Jack",
    ],
    "Age": [25, 30, 28, 22, 35, 29, 27, 31, 26, 33],
    "City": [
        "New York",
        "London",
        "Paris",
        "Tokyo",
        "Sydney",
        "Berlin",
        "Rome",
        "Madrid",
        "Toronto",
        "Dubai",
    ],
}
df = pd.DataFrame(data)

# Column definitions
columnDefs = [{"field": "Name"}, {"field": "Age"}, {"field": "City"}]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dag.AgGrid(
            id="my-table",
            rowData=df.to_dict("records"),  # Convert DataFrame to list of dicts
            columnDefs=columnDefs,
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
