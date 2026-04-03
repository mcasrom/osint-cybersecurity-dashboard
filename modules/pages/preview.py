#!/usr/bin/env python3
"""Dashboard Preview & Splash Screen"""

import streamlit as st

class PreviewPage:
    """Página de inicio/preview del dashboard"""
    
    @staticmethod
    def render():
        """Renderiza página de bienvenida"""
        
        st.markdown("""
        <style>
            .preview-title {
                font-size: 3.5em;
                font-weight: bold;
                background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 20px;
                text-align: center;
            }
            .preview-subtitle {
                font-size: 1.5em;
                color: #64748b;
                margin-bottom: 30px;
                text-align: center;
            }
            .feature-card {
                background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
                padding: 20px;
                border-radius: 10px;
                border-left: 4px solid #1e40af;
                margin-bottom: 15px;
            }
            .feature-icon {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .feature-title {
                font-weight: bold;
                color: #1e40af;
                margin-bottom: 8px;
                font-size: 1.2em;
            }
            .feature-desc {
                color: #64748b;
                font-size: 0.9em;
            }
            .stat-box {
                background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 4px 12px rgba(30, 64, 175, 0.15);
            }
            .stat-number {
                font-size: 2em;
                font-weight: bold;
            }
            .stat-label {
                font-size: 0.9em;
                opacity: 0.9;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Header
        st.markdown('<div class="preview-title">🔒 OSINT Cybersecurity Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="preview-subtitle">Real-time Threat Intelligence & Vulnerability Monitoring Platform</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Quick Stats
        st.markdown("### 📊 Quick Statistics")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">24</div>
                <div class="stat-label">CVEs/Week</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">5</div>
                <div class="stat-label">Critical</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">87.3%</div>
                <div class="stat-label">Patched</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">15.2k</div>
                <div class="stat-label">Assets</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col5:
            st.markdown("""
            <div class="stat-box">
                <div class="stat-number">94.2%</div>
                <div class="stat-label">Detection</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        # Features
        st.markdown("### 🚀 Core Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Real-time Dashboard</div>
                <div class="feature-desc">Live monitoring of threats, vulnerabilities, and attack surface metrics</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔴</div>
                <div class="feature-title">CVE Monitoring</div>
                <div class="feature-desc">Track vulnerabilities from NVD in real-time with severity scoring</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🗺️</div>
                <div class="feature-title">Attack Surface</div>
                <div class="feature-desc">Scan external infrastructure, discover exposed assets and subdomains</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">Reputation Check</div>
                <div class="feature-desc">Validate IPs and domains against threat intelligence feeds</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <div class="feature-title">Botnet Detection</div>
                <div class="feature-desc">Detect botnets, map infrastructure, validate IP security</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔐</div>
                <div class="feature-title">IP Validator</div>
                <div class="feature-desc">Comprehensive IP security scanning and comparison</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        # Technology Stack
        st.markdown("### 🔬 Technology Stack")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            **Backend**
            - Python 3.13
            - FastAPI
            - Streamlit
            """)
        
        with col2:
            st.markdown("""
            **Data Sources**
            - NVD (NIST)
            - AbuseIPDB
            - VirusTotal
            - Shodan
            """)
        
        with col3:
            st.markdown("""
            **Deployment**
            - Docker
            - Linux (DietPi)
            - Odroid Compatible
            """)
        
        st.divider()
        
        # Getting Started
        st.markdown("### 🚀 Getting Started")
        
        st.markdown("""
        1. **Configure API Keys** → Go to 🔐 API Configuration
        2. **View Dashboard** → Check 📊 Dashboard for real-time metrics
        3. **Monitor CVEs** → Visit 🔴 CVE Monitoring
        4. **Scan Infrastructure** → Use 🗺️ Attack Surface Scanner
        5. **Validate Security** → Check 🔍 Reputation and 🤖 Botnets
        
        ### 📚 Documentation
        - 📖 **Methodology**: Learn about our OSINT approach
        - ℹ️ **Help**: Get detailed guidance on each feature
        """)
        
        st.divider()
        
        # Contact & Info
        st.markdown("""
        <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 10px; margin-top: 30px;'>
            <h3>About This Platform</h3>
            <p><strong>OSINT Cybersecurity Dashboard</strong></p>
            <p>Comprehensive threat intelligence and vulnerability management platform</p>
            <p>© 2024-2026 M. Castillo | <a href='mailto:mybloggingnotes@gmail.com'>mybloggingnotes@gmail.com</a></p>
            <p style='color: #64748b; font-size: 0.9em;'>Version 3.1.0 | Advanced Features Enabled</p>
        </div>
        """, unsafe_allow_html=True)

preview = PreviewPage()
