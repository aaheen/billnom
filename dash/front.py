from dash import Dash, html, dcc, Input, Output

import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Bill Nom"),
    html.Div("The Legalese Summarizer"),
    html.Br(),

    html.Div([
        "MN bill URL: ",
        dcc.Input(value="Input URL", id="bill-url-in"),
        html.Br(),
        "URL should be from the MN Revisor's Office (www.revisor.mn.gov)"
    ]),
    html.Br(),

    html.Div(id="bill-summary")
])

@app.callback(
    Output(component_id="bill-summary", component_property="children"),
    Input(component_id="bill-url-in", component_property="value")
)
def getBillSummary(billURL):
    return f'Output: {billURL}' # ANDREW PUT STUFF HERE

if __name__ == '__main__':
    app.run_server(debug=True)