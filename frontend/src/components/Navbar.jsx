import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import {
  Camera,
  Video,
  Leaf,
  Activity,
  BarChart,
  User,
  Shield
} from 'lucide-react';

const Navbar = () => {
  const [open, setOpen] = useState(false);

  const navItems = [
    { to: '/', icon: Camera, label: 'Image Analysis' },
    { to: '/image-insights', icon: Activity, label: 'Image Insights' },
    { to: '/video-analysis', icon: Video, label: 'Video Analysis' },
    { to: '/environmental', icon: Leaf, label: 'Environmental' },
    { to: '/analytics', icon: BarChart, label: 'Analytics' },
    { to: '/about', icon: Shield, label: 'About' }
  ];

  return (
    <header className="header" role="banner">
      <div className="header-content">
        <div className="brand" aria-hidden>
          <div style={{ 
            display: 'flex', 
            alignItems: 'center', 
            gap: '0.75rem'
          }}>
            <Shield 
              size={28} 
              style={{ 
                color: 'var(--accent-blue)',
                filter: 'drop-shadow(0 2px 4px rgba(59, 130, 246, 0.3))'
              }} 
            />
            <h1 style={{ 
              color: '#ffffff !important',
              margin: 0,
              fontSize: '1.5rem',
              fontWeight: '700',
              textShadow: '0 2px 4px rgba(0, 0, 0, 0.3)'
            }}>
              InfraVision AI
            </h1>
          </div>
          <p className="sr-only">Navigation for InfraVision AI application</p>
        </div>

        <button
          className="nav-toggle btn"
          aria-expanded={open}
          aria-label="Toggle navigation"
          onClick={() => setOpen((s) => !s)}
          style={{
            background: 'var(--surface-secondary)',
            border: '1px solid var(--border-color)',
            color: 'var(--text-primary)',
            borderRadius: 'var(--border-radius)',
            padding: '0.5rem',
            transition: 'all 0.3s ease'
          }}
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
              style={{
                transition: 'all 0.3s ease'
              }}
            >
              <Icon 
                size={18} 
                style={{ 
                  transition: 'all 0.3s ease'
                }} 
              />
              <span className="nav-label">{label}</span>
            </NavLink>
          ))}
        </nav>

        <div className="header-actions">
          <button 
            className="btn btn-secondary" 
            title="Account"
            style={{
              background: 'var(--surface-secondary)',
              border: '1px solid var(--border-color)',
              color: 'var(--text-secondary)',
              borderRadius: 'var(--border-radius)',
              padding: '0.5rem',
              transition: 'all 0.3s ease'
            }}
          >
            <User size={16} />
          </button>
        </div>

        <div className="header-status">
          <span style={{ 
            color: 'var(--text-secondary)', 
            fontSize: '0.875rem',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem'
          }}>
            <span style={{ 
              color: 'var(--success-color)'
            }}>
              🟢
            </span>
            System Online
          </span>
        </div>
      </div>
    </header>
  );
};

export default Navbar;