# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DiscordWidget(Component):
    """A DiscordWidget component.


Keyword arguments:

- id (string; optional)

- avatar (string; optional)

- channel (string; default '1246197743781810332')

- className (string; optional)

- height (string; default '100%')

- server (string; default '1246197743307980940')

- username (string; optional)

- width (string; default '100%')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_discord'
    _type = 'DiscordWidget'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, server=Component.UNDEFINED, channel=Component.UNDEFINED, username=Component.UNDEFINED, avatar=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'avatar', 'channel', 'className', 'height', 'server', 'username', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'avatar', 'channel', 'className', 'height', 'server', 'username', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DiscordWidget, self).__init__(**args)
