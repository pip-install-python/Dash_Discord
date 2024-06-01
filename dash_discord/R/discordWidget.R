# AUTO GENERATED FILE - DO NOT EDIT

#' @export
discordWidget <- function(id=NULL, avatar=NULL, channel=NULL, className=NULL, height=NULL, server=NULL, username=NULL, width=NULL) {
    
    props <- list(id=id, avatar=avatar, channel=channel, className=className, height=height, server=server, username=username, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DiscordWidget',
        namespace = 'dash_discord',
        propNames = c('id', 'avatar', 'channel', 'className', 'height', 'server', 'username', 'width'),
        package = 'dashDiscord'
        )

    structure(component, class = c('dash_component', 'list'))
}
