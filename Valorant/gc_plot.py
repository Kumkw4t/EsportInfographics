import plotly.graph_objects as go
import pandas as pd

gc_emea_df = pd.read_csv("gc_emea.csv")

# Create dimensions
name_dim = go.parcats.Dimension(
    values=gc_emea_df.Name,
    label="Name"
)

kickoff_dim = go.parcats.Dimension(values=gc_emea_df.kickoff_2024, label="Kickoff '24")

S12024_dim = go.parcats.Dimension(
    values=gc_emea_df.S1_2024, label="Stage 1 '24"
)
S22024_dim = go.parcats.Dimension(
    values=gc_emea_df.S2_2024, label="Stage 2 '24"
)
S32024_dim = go.parcats.Dimension(
    values=gc_emea_df.S3_2024, label="Stage 3 '24"
)

gc_emea_df['S3_2024_numeric'] = gc_emea_df['S3_2024'].astype('category').cat.codes

# Create parcats trace
colorscale = [[0.0, 'rgb(245, 90, 66)'],
            [0.16666666666666666, 'rgb(245, 158, 66)'],
            [0.3333333333333333, 'rgb(245, 245, 66)'],
            [0.5, 'rgb(66, 245, 132)'],
            [0.6666666666666666, 'rgb(66, 194, 245)'],
            [0.8333333333333334, 'rgb(191, 66, 245)'],
            [1.0, 'rgb(245, 66, 164)']]

color = [num for num in range(10) for _ in range(5)]
            
                        
fig = go.Figure(data = [go.Parcats(dimensions=[name_dim, kickoff_dim, S12024_dim, S22024_dim, S32024_dim],
        line={'color': color, 'colorscale': colorscale, 'shape': 'hspline'},
        hoveron='color',
        labelfont={'size': 18, 'family': 'Times'},
        tickfont={'size': 16, 'family': 'Times'},
        arrangement='freeform',
        hoverinfo='none'
        )],
        layout= {'bargap': 0})

# print(gc_emea_df['S3_2024_numeric'])
fig.show()
