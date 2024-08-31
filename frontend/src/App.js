import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import HomePage from './pages/HomePage/HomePage';
import SubscriptionAPI from './pages/HomePage/Services/SubscriptionAPI.js';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/services/subscriptionapi" element={<SubscriptionAPI />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
}

export default App;
