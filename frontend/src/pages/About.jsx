import React from 'react';
import { Shield, Camera, Activity, BarChart3, Video, Users, Award, Globe, Heart, Code, BookOpen, Target, Building, Wrench, AlertTriangle } from 'lucide-react';

const About = () => {
  const team = [
    {
      name: "AI Infrastructure Engineering Team",
      role: "Developers & Civil Engineers",
      description: "A multidisciplinary team of AI engineers, computer vision experts, and civil engineering specialists working together to ensure infrastructure safety through advanced technology."
    }
  ];

  const technologies = [
    { name: "YOLOv8", description: "Advanced object detection for crack and structural damage identification", icon: Camera },
    { name: "OpenCV", description: "Computer vision library for image processing and structural analysis", icon: Activity },
    { name: "TensorFlow/PyTorch", description: "Deep learning frameworks for material classification and predictive analytics", icon: BarChart3 },
    { name: "React", description: "Modern web interface for real-time infrastructure monitoring", icon: Code },
    { name: "Flask", description: "Python web framework for AI model deployment and data analytics", icon: Globe }
  ];

  const features = [
    {
      icon: Shield,
      title: "AI-Powered Analysis",
      description: "Advanced machine learning models automatically detect structural damage, material degradation, and safety risks in civil infrastructure."
    },
    {
      icon: Activity,
      title: "Real-time Monitoring",
      description: "Continuous surveillance systems provide instant alerts and enable proactive maintenance measures for critical infrastructure."
    },
    {
      icon: Target,
      title: "Precision Assessment",
      description: "Accurate measurements and severity classifications help prioritize maintenance efforts and allocate resources effectively."
    },
    {
      icon: Building,
      title: "Infrastructure Safety",
      description: "Bridging technology and civil engineering to ensure safe, reliable infrastructure for communities and economic development."
    }
  ];

  const impact = [
    { number: "10K+", label: "Infrastructure Elements Analyzed" },
    { number: "1M+", label: "Images Processed" },
    { number: "95%", label: "Detection Accuracy" },
    { number: "24/7", label: "Monitoring Capability" }
  ];

  return (
    <div className="content-area">
      <div className="page-header">
        <h1>
          <Shield className="inline-icon" size={32} />
          About InfraVision AI
        </h1>
        <p>Revolutionizing infrastructure monitoring with advanced artificial intelligence and computer vision technology</p>
      </div>

      {/* Mission Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Target size={24} />
            Our Mission
          </h2>
        </div>
        <div className="card-body">
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <h3 style={{ color: 'var(--dark)', marginBottom: '1rem' }}>
              Transforming Infrastructure Safety Through Intelligent Technology
            </h3>
            <p style={{ fontSize: '1.1rem', lineHeight: '1.6', color: 'var(--secondary)' }}>
              InfraVision AI represents a revolutionary leap in infrastructure safety and monitoring.
              By seamlessly integrating cutting-edge artificial intelligence with civil engineering expertise,
              we empower infrastructure managers to monitor, assess, and maintain critical structures
              with unprecedented accuracy, efficiency, and predictive capabilities.
            </p>
          </div>

          {/* Impact Numbers */}
          <div className="impact-grid" style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
            gap: '1.5rem',
            marginTop: '2rem'
          }}>
            {impact.map((item, index) => (
              <div key={index} style={{
                textAlign: 'center',
                padding: '1.5rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)'
              }}>
                <div style={{
                  fontSize: '2rem',
                  fontWeight: 'bold',
                  color: 'var(--primary)',
                  marginBottom: '0.5rem'
                }}>
                  {item.number}
                </div>
                <div style={{
                  fontSize: '0.9rem',
                  color: 'var(--secondary)',
                  fontWeight: '500'
                }}>
                  {item.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Shield size={24} />
            Key Features
          </h2>
        </div>
        <div className="card-body">
          <div className="features-grid" style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '1.5rem'
          }}>
            {features.map((feature, index) => (
              <div key={index} className="feature-card" style={{
                padding: '1.5rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)',
                transition: 'transform 0.2s ease'
              }}>
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  marginBottom: '1rem',
                  gap: '0.75rem'
                }}>
                  <div style={{
                    width: '48px',
                    height: '48px',
                    borderRadius: '50%',
                    background: 'var(--primary)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: 'white'
                  }}>
                    <feature.icon size={24} />
                  </div>
                  <h3 style={{
                    margin: 0,
                    color: 'var(--dark)',
                    fontSize: '1.1rem'
                  }}>
                    {feature.title}
                  </h3>
                </div>
                <p style={{
                  margin: 0,
                  color: 'var(--secondary)',
                  lineHeight: '1.5'
                }}>
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Technology Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Code size={24} />
            Technology Stack
          </h2>
        </div>
        <div className="card-body">
          <div className="tech-grid" style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '1rem'
          }}>
            {technologies.map((tech, index) => (
              <div key={index} style={{
                padding: '1rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)',
                display: 'flex',
                alignItems: 'center',
                gap: '0.75rem'
              }}>
                <div style={{
                  width: '40px',
                  height: '40px',
                  borderRadius: '8px',
                  background: 'var(--primary)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: 'white',
                  flexShrink: 0
                }}>
                  <tech.icon size={20} />
                </div>
                <div>
                  <h4 style={{
                    margin: '0 0 0.25rem 0',
                    color: 'var(--dark)',
                    fontSize: '1rem'
                  }}>
                    {tech.name}
                  </h4>
                  <p style={{
                    margin: 0,
                    color: 'var(--secondary)',
                    fontSize: '0.875rem',
                    lineHeight: '1.4'
                  }}>
                    {tech.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Team Section */}
      <div className="card" style={{ marginBottom: '2rem' }}>
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Users size={24} />
            Our Team
          </h2>
        </div>
        <div className="card-body">
          {team.map((member, index) => (
            <div key={index} style={{
              padding: '1.5rem',
              background: 'var(--light)',
              borderRadius: 'var(--border-radius)',
              border: '1px solid var(--glass-border)',
              marginBottom: index < team.length - 1 ? '1rem' : 0
            }}>
              <h3 style={{
                margin: '0 0 0.5rem 0',
                color: 'var(--dark)',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem'
              }}>
                <Users size={20} />
                {member.name}
              </h3>
              <p style={{
                margin: '0 0 1rem 0',
                color: 'var(--primary)',
                fontWeight: '500'
              }}>
                {member.role}
              </p>
              <p style={{
                margin: 0,
                color: 'var(--secondary)',
                lineHeight: '1.5'
              }}>
                {member.description}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Vision Section */}
      <div className="card">
        <div className="card-header">
          <h2 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
            <Globe size={24} />
            Our Vision
          </h2>
        </div>
        <div className="card-body">
          <div style={{ textAlign: 'center' }}>
            <h3 style={{ color: 'var(--dark)', marginBottom: '1rem' }}>
              A Future Where Technology Protects Our Infrastructure
            </h3>
            <p style={{
              fontSize: '1.1rem',
              lineHeight: '1.6',
              color: 'var(--secondary)',
              marginBottom: '2rem'
            }}>
              We envision a world where every critical infrastructure element is equipped with intelligent monitoring systems
              that can predict deterioration, prevent catastrophic failures, and guide maintenance efforts. By making
              advanced AI technology accessible to civil engineers and infrastructure professionals worldwide, we aim to ensure
              that our infrastructure remains safe, reliable, and resilient for future generations.
            </p>

            <div style={{
              display: 'flex',
              justifyContent: 'center',
              gap: '2rem',
              flexWrap: 'wrap'
            }}>
              <div style={{
                textAlign: 'center',
                padding: '1rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)',
                minWidth: '150px'
              }}>
                <Award size={32} style={{ color: 'var(--primary)', marginBottom: '0.5rem' }} />
                <h4 style={{ margin: '0 0 0.5rem 0', color: 'var(--dark)' }}>Innovation</h4>
                <p style={{ margin: 0, fontSize: '0.9rem', color: 'var(--secondary)' }}>
                  Pushing the boundaries of AI in infrastructure safety
                </p>
              </div>

              <div style={{
                textAlign: 'center',
                padding: '1rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)',
                minWidth: '150px'
              }}>
                <Globe size={32} style={{ color: 'var(--primary)', marginBottom: '0.5rem' }} />
                <h4 style={{ margin: '0 0 0.5rem 0', color: 'var(--dark)' }}>Global Impact</h4>
                <p style={{ margin: 0, fontSize: '0.9rem', color: 'var(--secondary)' }}>
                  Protecting infrastructure worldwide
                </p>
              </div>

              <div style={{
                textAlign: 'center',
                padding: '1rem',
                background: 'var(--light)',
                borderRadius: 'var(--border-radius)',
                border: '1px solid var(--glass-border)',
                minWidth: '150px'
              }}>
                <Wrench size={32} style={{ color: 'var(--primary)', marginBottom: '0.5rem' }} />
                <h4 style={{ margin: '0 0 0.5rem 0', color: 'var(--dark)' }}>Safety First</h4>
                <p style={{ margin: 0, fontSize: '0.9rem', color: 'var(--secondary)' }}>
                  Safeguarding our critical infrastructure
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;