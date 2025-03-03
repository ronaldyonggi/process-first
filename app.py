import dash
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
from dash import html, dcc

# Import the PaginatedTable class
from components.paginated_table import PaginatedTable

# Import data functions
from data.process_data import get_initial_edges, get_initial_nodes


# Create Dash app instance and use Bootstrap's CSS styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --- Node Table ---
node_table = PaginatedTable(id="node-table", dataframe=get_initial_nodes())

# --- Edge Table ---
# Initial column definitions for the Edge table (will be updated by callback)
initial_edge_column_defs = [
    {
        "field": "Upstream node",
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {"values": []},
        "editable": True
    },
    {
        "field": "Downstream node",
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {"values": []},
        "editable": True
    },
]
edge_table = PaginatedTable(
    id="edge-table",
    dataframe=get_initial_edges(),
    columnDefs=initial_edge_column_defs,  # Use custom column definitions
)

# --- Layout ---
app.layout = dbc.Container(
    [
        html.H1("Process Flow Visualization"),
        html.H2("Nodes"),
        node_table.layout(),
        html.H2("Edges"),
        edge_table.layout(),
        html.H2("Canvas"),  # Placeholder for canvas
        html.Div(id="canvas-container"),  # Placeholder
    ],
    fluid=True, # Take up the full width of the page
)


if __name__ == "__main__":
    app.run(debug=True)
