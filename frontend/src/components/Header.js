// src/components/Header.js
import React, { useEffect } from 'react';
import { useModalContext } from './ModalContext';

const Header = () => {
    const { setHasHeader } = useModalContext(); // Используем хук для контекста

    useEffect(() => {
        setHasHeader(true);
    }, [setHasHeader]);

    const commonStyles = {
        backgroundColor: 'rgba(55, 120, 251, 0.1)',
        border: '1px dashed rgb(55, 120, 251)',
        boxSizing: 'border-box',
        borderRadius: '8px',
        height: '48px',
    };

    const addonsStyles = {
        ...commonStyles,
        width: '48px',
    };

    const innerAddonsStyles = {
        ...addonsStyles,
        backgroundColor: 'rgba(207, 112, 255, 0.1)',
    };

    const bottomAddonsStyles = {
        ...commonStyles,
        width: '100%',
    };

    const wrapperStyles = {
        display: 'flex',
        justifyContent: 'center',
    };

    const titleStyles = {
        ...commonStyles,
        flexGrow: 1,
    };

    return (
        <div style={{ margin: 'var(--modal-s-header-paddings)' }}>
            <div style={wrapperStyles}>
                <div style={innerAddonsStyles} />
                <div style={addonsStyles} />
                <div style={titleStyles} />
                <div style={addonsStyles} />
                <div style={innerAddonsStyles} />
            </div>
            <div style={bottomAddonsStyles} />
        </div>
    );
};

export default Header;
