# AUTO GENERATED FILE - DO NOT EDIT

#' @export
discordCrate <- function(id=NULL, allChannelNotifications=NULL, avatar=NULL, channel=NULL, color=NULL, defer=NULL, embedNotificationTimeout=NULL, glyph=NULL, indicator=NULL, location=NULL, notifications=NULL, server=NULL, shard=NULL, timeout=NULL, username=NULL) {
    
    props <- list(id=id, allChannelNotifications=allChannelNotifications, avatar=avatar, channel=channel, color=color, defer=defer, embedNotificationTimeout=embedNotificationTimeout, glyph=glyph, indicator=indicator, location=location, notifications=notifications, server=server, shard=shard, timeout=timeout, username=username)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DiscordCrate',
        namespace = 'dash_discord',
        propNames = c('id', 'allChannelNotifications', 'avatar', 'channel', 'color', 'defer', 'embedNotificationTimeout', 'glyph', 'indicator', 'location', 'notifications', 'server', 'shard', 'timeout', 'username'),
        package = 'dashDiscord'
        )

    structure(component, class = c('dash_component', 'list'))
}
