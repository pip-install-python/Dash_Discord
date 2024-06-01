# AUTO GENERATED FILE - DO NOT EDIT

export discordwidget

"""
    discordwidget(;kwargs...)

A DiscordWidget component.

Keyword arguments:
- `id` (String; optional)
- `avatar` (String; optional)
- `channel` (String; optional)
- `className` (String; optional)
- `height` (String; optional)
- `server` (String; optional)
- `username` (String; optional)
- `width` (String; optional)
"""
function discordwidget(; kwargs...)
        available_props = Symbol[:id, :avatar, :channel, :className, :height, :server, :username, :width]
        wild_props = Symbol[]
        return Component("discordwidget", "DiscordWidget", "dash_discord", available_props, wild_props; kwargs...)
end

