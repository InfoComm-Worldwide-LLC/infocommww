require('dotenv').config();
const express = require('express');
const app = express();
const port = process.env.PORT || 3001;

app.use(express.json());

// Example route
app.get('/api/subscription', (req, res) => {
  res.json({ message: "Welcome to the Subscription API" });
});

// Add more routes as needed

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
