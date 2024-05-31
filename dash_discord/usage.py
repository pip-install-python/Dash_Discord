from dash import Dash, html
import dash_discord

app = Dash(__name__)

app.layout = html.Div([
    dash_discord.DiscordCrate(
        id='crate',
        server='1246197743307980940',
        channel='1246197743781810332',
    ),
], style={'height': '100%'})

if __name__ == '__main__':
    app.run_server(debug=True, port='2122')
