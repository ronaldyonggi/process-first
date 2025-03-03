# Process Flow Visualization App

This Dash application allows users to visualize and interact with process flows in a tabular and graphical format. It's designed for users in the chemical industry to model and troubleshoot process inefficiencies.

## Features

*   **Node Table:** Displays a table of process nodes with their names and types.  Supports filtering and sorting.
*   **Edge Table:** Displays a table of connections (edges) between nodes, defining the flow direction. Supports filtering and sorting.  Allows selection of upstream and downstream nodes via dropdown menus (populated from the Node table).
*   **Dynamic Dropdowns:** The dropdown options in the Edge table are dynamically updated based on the nodes defined in the Node table.
*   **Modular Design:** The code is organized into modules for better maintainability and reusability (`components`, `data`, `utils`).
*   **Reusable Table Component:** A `PaginatedTable` component is implemented for displaying tabular data with pagination, filtering, and sorting.
*   **Data Storage:** Uses `dcc.Store` to manage node and edge data, enabling data updates to propagate between components.

## Installation and Setup

1.  **Prerequisites:**
    *   Python 3.8 or later
    *   pip

2.  **Clone the Repository:**

    ```bash
    git clone <your_repository_url>  # Replace with your repository URL
    cd process_flow_app
    ```

3.  **Create and Activate a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Navigate to the project directory:**

    ```bash
    cd process_flow_app
    ```

2.  **Activate the virtual environment (if you created one):**

    ```bash
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

3.  **Run the app:**

    ```bash
    python app.py
    ```

4.  **Open your web browser and go to:** `http://127.0.0.1:8050/` (or the address shown in your terminal).

## Usage

1.  **Node Table:** View and filter/sort the list of nodes.
2.  **Edge Table:**
    *   View the connections between nodes.
    *   Double-click on the "Upstream Node" or "Downstream Node" cells to select nodes from a dropdown menu. The dropdown options are populated from the Node table.

## Incomplete Features / Future Work

This section clearly outlines the parts of the application that are not yet implemented or require further development. 

1.  **Node and Edge Table Editing:**
    *   **Adding Nodes:**  Currently, there is no UI for adding new nodes to the Node table.  This would require adding a button, a form (likely using `dbc.Modal` from Dash Bootstrap Components) to input the node name and type, and a callback to update the `node-store` and the Node table's `rowData`.
    *   **Adding Edges:** Similarly, there's no UI for adding new edges.  This would involve a button, a form, and a callback to update the `edge-store` and the Edge table.
    *   **Deleting Nodes/Edges:**  No functionality exists to delete nodes or edges.  This could be implemented using AG Grid's row selection feature and a callback to remove the selected rows from the appropriate `dcc.Store` and table.
    *   **Modifying Nodes/Edges:** While the Edge table dropdowns *appear* to allow editing, the changes are *not* currently saved back to the `dcc.Store`.  A callback using the `cellValueChanged` event of AG Grid is needed to capture these edits and update the `edge-store`.  Similar functionality would be needed for modifying node names and types in the Node table.

2.  **Canvas Visualization:**
    *   The "Canvas" section is currently a placeholder.  The intended functionality is to visually represent the nodes and edges as a graph.
    *   **Graph Library:** A suitable graph visualization library would need to be chosen.  Options include:
        *   **Dash Cytoscape:**  A Dash component specifically designed for visualizing graphs.  
        *   **NetworkX (with a custom rendering solution):** NetworkX is a powerful Python library for graph manipulation.  
        *   **Plotly Graph Objects:**  Plotly itself can create network graphs.  
    *   **Callback for Canvas Update:** A callback would be required to listen for changes in the `node-store` and `edge-store` and update the canvas visualization accordingly.  This would involve:
        *   Reading the node and edge data.
        *   Constructing the graph representation (using the chosen library).
        *   Rendering the graph on the canvas.
    * **Interactive Canvas:** Ideally, the canvas would be interactive, allowing users to:
        *   Drag and move nodes.
        *   Click on nodes/edges to view details (perhaps in a modal or a separate panel).
        *   Potentially even edit the graph directly on the canvas (which would then update the tables).

3.  **Error Handling:**
    *   The application currently lacks robust error handling.  For example:
        *   What happens if the user tries to create an edge with a non-existent node?
        *   What happens if there are data validation errors (e.g., an empty node name)?
        *   What if there are issues connecting to the server?
    *   Appropriate error messages and handling mechanisms should be implemented to provide a better user experience and prevent unexpected crashes.

4.  **Typing:**
    *   The code could benefit from adding type hints (using Python's typing module) to improve code clarity and maintainability. This would also help catch potential errors during development.

5. **Testing:**
    * Unit tests and integration tests should be added.