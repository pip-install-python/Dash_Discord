# AUTO GENERATED FILE - DO NOT EDIT

#' @export
discordWidget <- function(id=NULL, avatar=NULL, channel=NULL, className=NULL, server=NULL, style=NULL, username=NULL) {
    
    props <- list(id=id, avatar=avatar, channel=channel, className=className, server=server, style=style, username=username)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DiscordWidget',
        namespace = 'dash_discord',
        propNames = c('id', 'avatar', 'channel', 'className', 'server', 'style', 'username'),
        package = 'dashDiscord'
        )

    structure(component, class = c('dash_component', 'list'))
}
