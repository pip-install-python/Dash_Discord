# AUTO GENERATED FILE - DO NOT EDIT

export discordcrate

"""
    discordcrate(;kwargs...)

A DiscordCrate component.

Keyword arguments:
- `id` (String; optional)
- `allChannelNotifications` (Bool; optional)
- `avatar` (String; optional)
- `channel` (String; optional)
- `color` (String; optional)
- `defer` (Bool; optional)
- `embedNotificationTimeout` (Real; optional)
- `glyph` (Array; optional)
- `indicator` (Bool; optional)
- `location` (Array; optional)
- `notifications` (Bool; optional)
- `server` (String; optional)
- `shard` (String; optional)
- `timeout` (Real; optional)
- `username` (String; optional)
"""
function discordcrate(; kwargs...)
        available_props = Symbol[:id, :allChannelNotifications, :avatar, :channel, :color, :defer, :embedNotificationTimeout, :glyph, :indicator, :location, :notifications, :server, :shard, :timeout, :username]
        wild_props = Symbol[]
        return Component("discordcrate", "DiscordCrate", "dash_discord", available_props, wild_props; kwargs...)
end

