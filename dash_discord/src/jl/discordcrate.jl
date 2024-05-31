# AUTO GENERATED FILE - DO NOT EDIT

export discordcrate

"""
    discordcrate(;kwargs...)

A DiscordCrate component.

Keyword arguments:
- `id` (String; optional)
- `channel` (String; optional)
- `server` (String; optional)
"""
function discordcrate(; kwargs...)
        available_props = Symbol[:id, :channel, :server]
        wild_props = Symbol[]
        return Component("discordcrate", "DiscordCrate", "dash_discord", available_props, wild_props; kwargs...)
end

