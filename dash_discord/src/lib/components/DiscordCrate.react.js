import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

const DiscordCrate = (props) => {
    const {
        id, server, channel, username, avatar, location, color, glyph, notifications, indicator, timeout, allChannelNotifications, embedNotificationTimeout, defer, shard
    } = props;

    console.log(props);

    useEffect(() => {
        const script = document.createElement('script');

        script.src = "https://cdn.jsdelivr.net/npm/@widgetbot/crate@3";
        script.async = true;

        script.onload = () => {
            window.Crate = new window.Crate({
                server: server,
                channel: channel,
                username: username,
                avatar: avatar,
                location: location,
                color: color,
                glyph: glyph,
                notifications: notifications,
                indicator: indicator,
                timeout: timeout,
                allChannelNotifications: allChannelNotifications,
                embedNotificationTimeout: embedNotificationTimeout,
                defer: defer,
                shard: shard
            });
        };

        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        };
    }, [server, channel, username, avatar, location]);

    return <div id={id} />;
}

DiscordCrate.defaultProps = {
    server: '1246197743307980940',
    channel: '1246197743781810332',
};

DiscordCrate.propTypes = {
    id: PropTypes.string,
    server: PropTypes.string.isRequired,
    channel: PropTypes.string,
    username: PropTypes.string,
    avatar: PropTypes.string,
    location: PropTypes.array,
    color: PropTypes.string,
    glyph: PropTypes.array,
    notifications: PropTypes.bool,
    indicator: PropTypes.bool,
    timeout: PropTypes.number,
    allChannelNotifications: PropTypes.bool,
    embedNotificationTimeout: PropTypes.number,
    defer: PropTypes.bool,
    shard: PropTypes.string
};

export default DiscordCrate;