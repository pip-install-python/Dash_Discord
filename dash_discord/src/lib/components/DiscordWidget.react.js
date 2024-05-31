import React from 'react';
import PropTypes from 'prop-types';
import WidgetBot from '@widgetbot/react-embed'

const DiscordWidget = (props) => {
    const {id, server, channel, avatar, username, className, style} = props;

    return (
        <div id={id} className={className} style={{...style, height: '50vh', width: '50vw'}}>
            <WidgetBot
                server={server}
                channel={channel}
                username={username}
                avatar={avatar}
              />
        </div>
    );
}

DiscordWidget.defaultProps = {
    server: '1246197743307980940',
    channel: '1246197743781810332',
    username: null,
    avatar: null,
    className: null,
    style: {}
};

DiscordWidget.propTypes = {
    id: PropTypes.string,
    server: PropTypes.string.isRequired,
    channel: PropTypes.string.isRequired,
    username: PropTypes.string,
    avatar: PropTypes.string,
    className: PropTypes.string,
    style: PropTypes.object
};

export default DiscordWidget;
