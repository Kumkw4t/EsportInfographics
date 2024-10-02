import plotly.graph_objects as go
import pandas as pd

gc_emea_df = pd.read_csv("gc_emea.csv")

# Create dimensions
name_dim = go.parcats.Dimension(
    values=gc_emea_df.Name,
    label="Name"
)

kickoff_dim = go.parcats.Dimension(values=gc_emea_df.kickoff_2024, label="Kickoff '24")

S32024_dim = go.parcats.Dimension(
    values=gc_emea_df.S3_2024, label="Stage 3 '24"
)

gc_emea_df['S3_2024_numeric'] = gc_emea_df['S3_2024'].astype('category').cat.codes
colorscale = [[0, 'lightsteelblue'], [1, 'mediumseagreen']]

# Create parcats trace

fig = go.Figure(data = [go.Parcats(dimensions=[name_dim, kickoff_dim, S32024_dim],
        line={'color': gc_emea_df['S3_2024_numeric'], 'colorscale': 'teal', 'shape': 'hspline'},
        hoveron='color',
        hoverinfo='none',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        arrangement='freeform',
        hovertemplate='<b>Test</b>: %{points[0]}<br>'
        )],
        layout= {'bargap': 0})

fig.show()
