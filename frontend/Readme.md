
# Alpha Bank Hackathon - Front-End Task ![Alpha Bank Logo](https://github.com/Sh1iba/Sh1iba/blob/main/alfa.png)

This project is part of the front-end challenge for the Alpha Bank Hackathon. The task involves creating a React application that interacts with an API by sending data via POST requests and displaying the responses in the UI.

## Overview

The goal of this task was to build a React application that sends data to a server via a POST request and displays the server's response. The app uses `fetch` to handle HTTP requests and `useState`/`useEffect` to manage state and lifecycle methods.

### What’s Included

- **React-based front-end**: The application is built using React to create a dynamic and responsive user interface.
- **POST request functionality**: The app sends data to the server and displays the response, with error handling in place.
- **UI components**: A modal and buttons are used to show the data and send a request.

## Getting Started

This project was bootstrapped with [Create React App](https://reactjs.org/docs/create-a-new-react-app.html).

### Available Scripts

In the project directory, you can run the following commands:

#### `npm start`

Runs the app in development mode.  
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.  
The page will reload if you make changes. You may also see any lint errors in the console.


### Project Structure

. ├── public/ 
│ └── index.html # The main HTML page 
├── src/ 
│ ├── components/ 
│ │ ├── App.jsx # Main component handling state and rendering UI 
│ │ ├── Header.js # Header component 
│ │ └── ModalContext.js # Context for managing modal state 
│ ├── data.js # Data to be sent via POST request 
│ ├── index.js # Entry point for React app 
│ └── style.css # Styles for the application 
├── package.json # npm configuration and dependencies 
└── README.md # This file


### How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_project.git
   cd your_project
Install dependencies:


npm install
Run the app:


#### `npm start`
This will start the local development server and open the app in the browser at
 http://localhost:3000.

Technologies
React: For building the user interface.
Fetch API: For making HTTP requests.
useState and useEffect: For managing state and performing side effects in React.
About the Hackathon
This project is part of the Alpha Bank Hackathon. The objective of the front-end challenge was to create a functional web application that interacts with a remote server, performs data submission using POST requests, and displays responses in a user-friendly interface.

