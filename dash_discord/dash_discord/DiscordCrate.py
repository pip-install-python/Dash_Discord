# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DiscordCrate(Component):
    """A DiscordCrate component.


Keyword arguments:

- id (string; optional)

- channel (string; default '355719584830980096')

- server (string; default '299881420891881473')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_discord'
    _type = 'DiscordCrate'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, server=Component.UNDEFINED, channel=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'channel', 'server']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'channel', 'server']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DiscordCrate, self).__init__(**args)
