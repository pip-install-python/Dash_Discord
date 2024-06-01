from dash import Dash, html
import dash_discord

app = Dash(__name__)

app.layout = html.Div([
    dash_discord.DiscordCrate(
        id='crate',
        server='1246197743307980940',
        channel='1246197743781810332',
        username='Pip Install Python',
        avatar='https://avatars.githubusercontent.com/u/83238564',
        location=['top', 'left'],
        color='red',
        glyph=['https://geomapindex.com/media/blog_qr/2024/05/28/qr-http___dashgeomapindexcom_AihBuSf.gif', '75px'],
        notifications=True,
        indicator=True,
        timeout=5000,
        allChannelNotifications=True,
        embedNotificationTimeout=5000,
        defer=True,
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, port='2122')
