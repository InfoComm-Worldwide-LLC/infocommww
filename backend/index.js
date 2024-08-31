const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const path = require('path');
const { auth } = require('express-openid-connect');

dotenv.config(); // Load environment variables from .env file

const app = express();
const port = process.env.PORT || 5000;

// Auth0 Configuration
const config = {
  authRequired: false,
  auth0Logout: true,
  secret: process.env.AUTH0_SECRET, // Use the secret stored in .env file
  baseURL: process.env.BASE_URL || 'http://localhost:3000', // Use baseURL from .env or default
  clientID: process.env.AUTH0_CLIENT_ID, // Use clientID from .env
  issuerBaseURL: process.env.AUTH0_ISSUER_BASE_URL, // Use issuerBaseURL from .env
};

// Middleware
app.use(express.json());

// Auth0 middleware
app.use(auth(config));

// Sample route to check authentication
app.get('/status', (req, res) => {
  res.send(req.oidc.isAuthenticated() ? 'Logged in' : 'Logged out');
});

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('Failed to connect to MongoDB', err);
});

// Serve static files from the React frontend app
app.use(express.static(path.join(__dirname, '../frontend/build')));

// Anything that doesn't match the above, send back index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/build/index.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
