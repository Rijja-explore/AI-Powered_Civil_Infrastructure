import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import {
  Camera,
  Video,
  Leaf,
  Activity,
  BarChart,
  User
} from 'lucide-react';

const Navbar = () => {
  const [open, setOpen] = useState(false);

  const navItems = [
    { to: '/', icon: Camera, label: 'Image Analysis' },
    { to: '/video-analysis', icon: Video, label: 'Video Analysis' },
    { to: '/environmental', icon: Leaf, label: 'Environmental' },
    { to: '/realtime', icon: Activity, label: 'Real-time' },
    { to: '/analytics', icon: BarChart, label: 'Analytics' }
  ];

  return (
    <header className="header" role="banner">
      <div className="header-content">
        <div className="brand" aria-hidden>
          <h1>Heritage Health Monitor</h1>
          <p className="sr-only">Navigation for Heritage Health Monitor application</p>
        </div>

        <button
          className="nav-toggle btn"
          aria-expanded={open}
          aria-label="Toggle navigation"
          onClick={() => setOpen((s) => !s)}
        >
          ☰
        </button>

        <nav className={`nav-tabs ${open ? 'open' : ''}`} role="navigation" aria-label="Main">
          {navItems.map(({ to, icon: Icon, label }) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
              onClick={() => setOpen(false)}
            >
              <Icon size={18} />
              <span className="nav-label">{label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="header-actions">
          <button className="btn btn-secondary" title="Account">
            <User size={16} />
          </button>
        </div>
      </div>
    </header>
  );
};

export default Navbar;