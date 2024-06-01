# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DiscordCrate(Component):
    """A DiscordCrate component.


Keyword arguments:

- id (string; optional)

- allChannelNotifications (boolean; optional)

- avatar (string; optional)

- channel (string; default '1246197743781810332')

- color (string; optional)

- defer (boolean; optional)

- embedNotificationTimeout (number; optional)

- glyph (list; optional)

- indicator (boolean; optional)

- location (list; optional)

- notifications (boolean; optional)

- server (string; default '1246197743307980940')

- shard (string; optional)

- timeout (number; optional)

- username (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_discord'
    _type = 'DiscordCrate'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, server=Component.UNDEFINED, channel=Component.UNDEFINED, username=Component.UNDEFINED, avatar=Component.UNDEFINED, location=Component.UNDEFINED, color=Component.UNDEFINED, glyph=Component.UNDEFINED, notifications=Component.UNDEFINED, indicator=Component.UNDEFINED, timeout=Component.UNDEFINED, allChannelNotifications=Component.UNDEFINED, embedNotificationTimeout=Component.UNDEFINED, defer=Component.UNDEFINED, shard=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'allChannelNotifications', 'avatar', 'channel', 'color', 'defer', 'embedNotificationTimeout', 'glyph', 'indicator', 'location', 'notifications', 'server', 'shard', 'timeout', 'username']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allChannelNotifications', 'avatar', 'channel', 'color', 'defer', 'embedNotificationTimeout', 'glyph', 'indicator', 'location', 'notifications', 'server', 'shard', 'timeout', 'username']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DiscordCrate, self).__init__(**args)
