#!/usr/bin/env python3
"""OSINT Cybersecurity Dashboard - SEO & Professional Edition"""

import streamlit as st
from modules.dashboards.threat_dashboard import dashboard as threat_dashboard
from modules.analyzers.cve_analyzer import analyzer as cve_analyzer
from modules.analyzers.attack_surface_analyzer import analyzer as attack_surface_analyzer
from modules.analyzers.reputation_analyzer import analyzer as reputation_analyzer
from modules.analyzers.botnet_analyzer import analyzer as botnet_analyzer
from modules.analyzers.ip_validator import validator as ip_validator
from modules.documentation.methodology import module as methodology_module
from modules.documentation.help_guide import module as help_guide_module
from modules.documentation.technical_docs import tech_docs as technical_docs
from modules.config.api_manager import manager as api_manager
from modules.pages.preview import preview as preview_page
from modules.pages.settings import settings as settings_page
from modules.pages.use_cases import use_cases as use_cases_page
from modules.pages.benchmarks import benchmarks as benchmarks_page

st.set_page_config(
    page_title="OSINT Cybersecurity Dashboard - Enterprise Threat Intelligence",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/mcasrom/osint-dashboard",
        "Report a bug": "mailto:mybloggingnotes@gmail.com",
        "About": "OSINT Cybersecurity Dashboard v3.2.0 - Enterprise Edition"
    }
)

# Meta tags for SEO
st.markdown("""
<head>
    <meta name="description" content="OSINT Cybersecurity Dashboard - Enterprise threat intelligence platform for real-time CVE monitoring, botnet detection, and vulnerability management.">
    <meta name="keywords" content="OSINT, cybersecurity, threat intelligence, CVE monitoring, vulnerability management, botnet detection">
    <meta name="author" content="M. Castillo">
    <meta property="og:title" content="OSINT Cybersecurity Dashboard">
    <meta property="og:description" content="Professional threat intelligence platform for security teams">
    <meta property="og:type" content="website">
</head>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .main-header { 
        font-size: 2.5em; 
        font-weight: bold; 
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .main-subtitle {
        font-size: 1.2em;
        color: #64748b;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🔒 OSINT Cybersecurity Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Enterprise-Grade Threat Intelligence & Vulnerability Management Platform</p>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("CVEs", 24, "+5")
with col2:
    st.metric("Critical", 5, "⚠️")
with col3:
    st.metric("Exploitable", 3, "🔴")
with col4:
    st.metric("Threat Level", "MEDIUM", "68%")
with col5:
    st.metric("System Health", "87.3%", "+5.2%")

st.divider()

# Main Navigation Tabs
main_tabs = st.tabs([
    "🏠 Home",
    "📊 Monitor",
    "🔍 Analyze",
    "📚 Learn",
    "💼 Business",
    "🛠️ Configure"
])

# Home Tab
with main_tabs[0]:
    col1, col2 = st.columns([2, 1])
    with col1:
        preview_page.render()
    with col2:
        st.markdown("### 📊 Recent Activity")
        st.info("CVEs: +5 this week\nIncidents: 0\nSystems: 1.2K monitored")

# Monitor Tab
with main_tabs[1]:
    sub_tabs = st.tabs(["Dashboard", "CVE Monitoring", "Attack Surface", "Reputation", "Botnets", "IP Validator"])
    
    with sub_tabs[0]:
        threat_dashboard.render()
    with sub_tabs[1]:
        cve_analyzer.render()
    with sub_tabs[2]:
        attack_surface_analyzer.render()
    with sub_tabs[3]:
        reputation_analyzer.render()
    with sub_tabs[4]:
        botnet_analyzer.render()
    with sub_tabs[5]:
        ip_validator.render()

# Analyze Tab
with main_tabs[2]:
    sub_tabs = st.tabs(["Methodology", "Technical Docs", "Benchmarks"])
    
    with sub_tabs[0]:
        methodology_module.render()
    with sub_tabs[1]:
        technical_docs.render()
    with sub_tabs[2]:
        benchmarks_page.render()

# Learn Tab
with main_tabs[3]:
    sub_tabs = st.tabs(["Help Guide", "API Reference"])
    
    with sub_tabs[0]:
        help_guide_module.render()
    with sub_tabs[1]:
        technical_docs.render()

# Business Tab
with main_tabs[4]:
    use_cases_page.render()

# Configure Tab
with main_tabs[5]:
    sub_tabs = st.tabs(["API Keys", "Settings"])
    
    with sub_tabs[0]:
        api_manager.render()
    with sub_tabs[1]:
        settings_page.render()

st.divider()

st.markdown("""
<div style='text-align: center; padding: 20px; margin-top: 40px;'>
    <p><strong>OSINT Cybersecurity Dashboard v3.2.0</strong></p>
    <p>© 2024-2026 M. Castillo | <a href='mailto:mybloggingnotes@gmail.com'>Contact Support</a></p>
    <p style='font-size: 0.85em; color: #64748b;'>Enterprise Threat Intelligence • Real-time Monitoring • Advanced Analytics</p>
</div>
""", unsafe_allow_html=True)
