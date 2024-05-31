# AUTO GENERATED FILE - DO NOT EDIT

#' @export
discordCrate <- function(id=NULL, channel=NULL, server=NULL) {
    
    props <- list(id=id, channel=channel, server=server)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DiscordCrate',
        namespace = 'dash_discord',
        propNames = c('id', 'channel', 'server'),
        package = 'dashDiscord'
        )

    structure(component, class = c('dash_component', 'list'))
}
