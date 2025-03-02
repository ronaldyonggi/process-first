import pandas as pd

def get_initial_nodes():
    """
    Provides initial data for the Node table.

    Returns:
        pd.DataFrame: A DataFrame containing the initial node data.
    """
    data = {
        "Name": ['Node A', 'Node B', 'Node C'],
        "Type": ['type1', 'type2', 'type1']
    }

    return pd.DataFrame(data)

def get_initial_edges():
    """
    Provides initial data for the Edge table.

    Returns:
        pd.DataFrame: A DataFrame containing the initial edge data.
    """

    data = {
        'Upstram node': ['Node A', 'Node B'],
        'Downstream node': ['Node B', 'Node C'],
    }

    return pd.DataFrame(data)