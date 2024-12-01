// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { ModalProvider } from './components/ModalContext'; // Импортируем ModalProvider
import App from './components/App'; // Импортируем главный компонент приложения


ReactDOM.render(
    <ModalProvider>
        <App />
    </ModalProvider>,
    document.getElementById('root')
);
