import React from 'react';
import PropTypes from 'prop-types';
import WidgetBot from '@widgetbot/react-embed'

const DiscordWidget = (props) => {
    const {id, server, channel, avatar, username, className, width, height} = props;

    return (
        <div id={id} className={className}>
            <WidgetBot
                server={server}
                channel={channel}
                username={username}
                avatar={avatar}
                width={width}
                height={height}
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
    width: '100%',
    height: '100%',
};

DiscordWidget.propTypes = {
    id: PropTypes.string,
    server: PropTypes.string.isRequired,
    channel: PropTypes.string.isRequired,
    username: PropTypes.string,
    avatar: PropTypes.string,
    className: PropTypes.string,
    width: PropTypes.string,
    height: PropTypes.string,
};

export default DiscordWidget;
