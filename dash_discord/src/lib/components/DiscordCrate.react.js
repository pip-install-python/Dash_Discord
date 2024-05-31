import React, { useEffect } from 'react';
import PropTypes from 'prop-types';

const DiscordCrate = (props) => {
    const {id, server, channel} = props;

    useEffect(() => {
        const script = document.createElement('script');

        script.src = "https://cdn.jsdelivr.net/npm/@widgetbot/crate@3";
        script.async = true;

        script.onload = () => {
            window.Crate = new window.Crate({
                server: server,
                channel: channel,
            });
        };

        document.body.appendChild(script);

        return () => {
            document.body.removeChild(script);
        };
    }, [server, channel]);

    return <div id={id} />;
}

DiscordCrate.defaultProps = {
    server: '1246197743307980940',
    channel: '1246197743781810332',
};

DiscordCrate.propTypes = {
    id: PropTypes.string,
    server: PropTypes.string.isRequired,
    channel: PropTypes.string.isRequired,
};

export default DiscordCrate;