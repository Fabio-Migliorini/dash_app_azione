import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


# assigns colors
colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}



# first chart only
data = pd.read_csv("graduates_unemp.csv")
country_list=['Italy','Euro area - 19 countries  (from 2015)','Germany (until 1990 former territory of the FRG)','France']



data = data.query("paese == @country_list and genere =='Totale'")
data["Date"] = pd.to_datetime(data["year"], format="%Y")
data.sort_values("Date", inplace=True)

fig_gender_total = px.line(data, x="Date", y="tasso di occupazione", color="paese",
              line_group="paese", hover_name="paese",title="Tasso di occupazione di laureati 20-34 in Italia")


fig_gender_total.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# second chart only
data_gender_compared =pd.read_csv("graduates_unemp.csv")
data_gender_compared = data_gender_compared.query("paese == 'Italy'")
data_gender_compared["Date"] = pd.to_datetime(data_gender_compared["year"], format="%Y")
fig_gender_compared = px.line(data_gender_compared, x="Date", y="tasso di occupazione", color="genere",
              line_group="genere", hover_name="genere",title="Tasso di occupazione dei laureati italiani per genere")

fig_gender_compared.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


# third chart only

# data = data.query("paese == @country_list & genere =='Totale' & year = 2019")
data_country_compared = data.query("paese == @country_list & genere =='Totale' & year == 2019")

#pd.read_csv("graduates_unemp.csv")
#  Fix the filter data_country_compared = data_country_compared.query(" year == '2019'  and genere =='Totale'")
fig_country_compared =  px.bar(data_country_compared, x="paese", y="tasso di occupazione", color="paese",hover_name="paese",title="Tasso di occupazione laureati per paese")

fig_country_compared.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Dati in Azione: in god we trust tutti gli altri portano dati !"



app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="", className="header-emoji"),
                html.H1(
                    children="Dati in Azione: Tasso di occupazione dei laureati in eta' 20-34", className="header-title"
                ),
                html.P(
                    children="Mostra andamento della percentuale di occupati in EU",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="gender_total",
                        config={"displayModeBar": False},
                        figure=fig_gender_total,
                    ),
                    className="card",
                ),
        html.Div(
            children=dcc.Graph(
                id="fig_gender_compared",
                config={"displayModeBar": False},
                figure=fig_gender_compared,
            ),
            className="card",
        ),
            html.Div(
                children=dcc.Graph(
                    id="fig_country_compared",
                    config={"displayModeBar": False},
                    figure=fig_country_compared,
                ),
                className="card",
            ),
            ],
            className="wrapper",
        ),

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
