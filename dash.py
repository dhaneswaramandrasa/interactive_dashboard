import dash
import dash_core_components as dcc
import dash_html_components as html

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1("My Dashboard"),
    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Bar chart"},
                {"x": [1, 2, 3], "y": [2, 4, 5], "type": "line", "name": "Line chart"},
            ],
            "layout": {
                "title": "Sample Graphs",
            }
        }
    ),
    dcc.Graph(
        id="scatter-plot",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [10, 5, 8], "mode": "markers", "name": "Scatter plot"},
            ],
            "layout": {
                "title": "Sample Scatter Plot",
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
