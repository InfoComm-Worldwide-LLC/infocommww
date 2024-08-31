import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';
import logo from '../../assets/updatedlogo.png'; // Adjust path based on actual location

const HomePage = () => {
  return (
    <div className="homepage">
      <header className="hero">
        <nav className="navbar">
          <img src={logo} alt="InfoComm Logo" className="logo" />
          <ul className="nav-links">
            <li><Link to="/services">Services</Link></li>
            <li><Link to="/features">Features</Link></li>
            <li><Link to="/about">About Us</Link></li>
            <li><Link to="/contact">Contact</Link></li>
            <li><button className="join-now">Join Now</button></li>
          </ul>
        </nav>
        <div className="hero-content">
          <h1>Welcome to InfoComm Worldwide</h1>
          <p>Your Favorite IT Playground</p>
          <button className="cta-button">Explore Our Features</button>
        </div>
      </header>
      <section id="features" className="features">
        <h2>Explore Our Features</h2>
        <div className="feature-grid">
          <div className="feature-item">
            <h3>Cybersecurity</h3>
            <p>Learn the latest in cybersecurity techniques and best practices.</p>
          </div>
          <div className="feature-item">
            <h3>Networking</h3>
            <p>Master networking skills with our comprehensive resources.</p>
          </div>
          <div className="feature-item">
            <h4>Data Analysis</h4>
            <p>Practice the art of managing information.</p>
          </div>
          <div className="feature-item">
            <h4>Software Development</h4>
            <p>Acquire the ability to create and deploy software.</p>
          </div>
          {/* Add more feature items as needed */}
        </div>
      </section>
    </div>
  );
};

export default HomePage;
