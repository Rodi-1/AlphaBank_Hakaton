// src/components/ModalContext.js
import React, { createContext, useState, useContext } from 'react';

// Создаем контекст
const ModalContext = createContext();

// Компонент Provider, который будет оборачивать все приложение
export const ModalProvider = ({ children }) => {
    const [hasHeader, setHasHeader] = useState(false);

    return (
        <ModalContext.Provider value={{ hasHeader, setHasHeader }}>
            {children}
        </ModalContext.Provider>
    );
};

// Хук для использования контекста
export const useModalContext = () => useContext(ModalContext);
