import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ----------------------------------------------------------------------------------------------------------------------
# Data Prep
df = pd.read_csv("./_modified_data/state_yearly_avg_growth_rate_2009-21.csv", index_col=0)

# Get years (column headers)
years = []
for x in range(2001, 2022):
    years.append(x)
years = list(map(str, years))

# Change column headers to str format
df.reset_index(inplace=True)
df.columns = df.columns.astype(str)

# Melt
df = df.melt(id_vars=['StateName'], value_vars=years,
             var_name='Year', value_name='GrowthRate')

# Calculate AAGR for 1, 2, 3, 4, and 5 years from present

df1 = df[df['Year'].isin(['2020', '2021'])]
df1 = df1.groupby('StateName', as_index=False).mean()
df1['Years'] = 1

df2 = df[df['Year'].isin(['2019', '2020', '2021'])]
df2 = df2.groupby('StateName', as_index=False).mean()
df2['Years'] = 2

df3 = df[df['Year'].isin(['2018', '2019', '2020', '2021'])]
df3 = df3.groupby('StateName', as_index=False).mean()
df3['Years'] = 3

df4 = df[df['Year'].isin(['2017', '2018', '2019', '2020', '2021'])]
df4 = df4.groupby('StateName', as_index=False).mean()
df4['Years'] = 4

df5 = df[df['Year'].isin(['2016', '2017', '2018', '2019', '2020', '2021'])]
df5 = df5.groupby('StateName', as_index=False).mean()
df5['Years'] = 5

df = pd.concat([df1, df2, df3, df4, df5]).reset_index(drop=True)

df['GrowthRate'] = (df['GrowthRate'] * 100).round(2)


# ----------------------------------------------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Zillow Housing Data Analysis", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "1 year (2021-2020)", "value": 1},
                     {"label": "2 years (2021-2019)", "value": 2},
                     {"label": "3 years (2021-2018)", "value": 3},
                     {"label": "4 years (2021-2017)", "value": 4},
                     {"label": "5 years (2021-2016)", "value": 5}],
                 multi=False,
                 value=1,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='aagr_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='aagr_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "\nLookback period: {} year(s)".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Years"] == option_slctd]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='StateName',
        scope="usa",
        color='GrowthRate',
        hover_data=['StateName', 'GrowthRate'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'GrowthRate': 'Average Annual Growth Rate'},
        template='plotly_dark'
    )

    # Plotly Graph Objects (GO)
    fig = go.Figure(
        data=[go.Choropleth(
            locationmode='USA-states',
            locations=dff['StateName'],
            z=dff["GrowthRate"].astype(float),
            colorscale='Reds',
        )]
    )

    fig.update_layout(
        title_text="Average Annual Growth Rate in the USA",
        title_xanchor="center",
        title_font=dict(size=24),
        title_x=0.5,
        geo=dict(scope='usa'),
    )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)