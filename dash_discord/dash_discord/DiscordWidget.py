# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DiscordWidget(Component):
    """A DiscordWidget component.


Keyword arguments:

- id (string; optional)

- avatar (string; optional)

- channel (string; default '355719584830980096')

- className (string; optional)

- server (string; default '299881420891881473')

- style (dict; optional)

- username (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_discord'
    _type = 'DiscordWidget'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, server=Component.UNDEFINED, channel=Component.UNDEFINED, username=Component.UNDEFINED, avatar=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'avatar', 'channel', 'className', 'server', 'style', 'username']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'avatar', 'channel', 'className', 'server', 'style', 'username']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DiscordWidget, self).__init__(**args)
