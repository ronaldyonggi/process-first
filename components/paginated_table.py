import dash_ag_grid as dag
import pandas as pd

class PaginatedTable:
    """
    A reusable component for displaying paginated tables using Dash AG Grid.

    Args:
        id (str): The unique ID of the table component.
        dataframe (pd.DataFrame): The pandas DataFrame containing the table data.
        columnDefs (list, optional): Custom column definitions for AG Grid. Defaults to None.
        page_size (int, optional): The number of rows to display per page. Defaults to 5.
    """

    def __init__(self, id, dataframe, columnDefs = None, page_size=5):
        self.id = id
        self.dataframe = dataframe
        self.page_size = page_size

        # Use provided columnDefs or generate default ones
        if columnDefs is None:
            self.columnDefs = [
                {'field': col, 'filter': True, 'sortable': True} for col in dataframe.columns
            ]
        else:
            self.columnDefs = columnDefs


    def layout(self):
        """
        Generate Dash AG Grid component for the table

        Returns:
            dag.AgGrid: The generated Dash AG Grid component
        """
        return dag.AgGrid(
            id = self.id,
            # Convert dataframe to list of dictionaries
            rowData = self.dataframe.to_dict('records'), 
            columnDefs = self.columnDefs,

            # Make columns resizable
            defaultColDef = {'resizable': True},

            # Enable pagination
            dashGridOptions = {'pagination': True, 'paginationPageSize': self.page_size},
        )