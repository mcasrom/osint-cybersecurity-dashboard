#!/usr/bin/env python3
"""
OSINT Cybersecurity Dashboard - Enterprise Edition
Author: M. Castillo
Copyright: © 2026 M. Castillo
Contact: mailto:mybloggingnotes@gmail.com
"""

import streamlit as st
import os
from dotenv import load_dotenv

# --- CONFIGURACIÓN DE SEGURIDAD (BRIDGE) ---
# Intentamos cargar .env en local, pero en la nube usamos st.secrets
load_dotenv()

def sync_secrets():
    """Sincroniza secretos de Streamlit Cloud con variables de entorno del sistema"""
    try:
        for key in st.secrets:
            os.environ[key] = str(st.secrets[key])
    except:
        # Si estamos en local y no hay secrets.toml, no pasa nada
        pass

sync_secrets()

# --- CONFIGURACIÓN DE PÁGINA ---
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

# --- IMPORTACIÓN DE MÓDULOS (Post-Configuración) ---
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

# --- ESTILOS CSS (Mejora de Contraste y Tamaños) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    * { font-family: 'Inter', sans-serif; }

    /* Título Principal: Más grande y brillante */
    .main-header { 
        font-size: 3.5rem !important; 
        font-weight: 800; 
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    /* Subtítulo: Color adaptativo con opacidad para contraste */
    .main-subtitle {
        font-size: 1.4rem;
        color: var(--text-color);
        opacity: 0.7;
        margin-bottom: 2rem;
    }

    /* Ajuste de métricas para mejor visibilidad */
    [data-testid="stMetricValue"] {
        color: #00ffa2 !important;
        font-weight: 700;
    }
    
    /* Banner de marca en footer */
    .footer-banner {
        text-align: center; 
        padding: 30px; 
        margin-top: 50px;
        border-top: 1px solid rgba(128, 128, 128, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<p class="main-header">🔒 M. Castillo - Privacy Tools</p>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Enterprise-Grade Threat Intelligence & OSINT Dashboard</p>', unsafe_allow_html=True)

# --- INDICADORES KPI ---
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("CVEs Today", 24, "+5")
with col2:
    st.metric("Critical", 5, "⚠️")
with col3:
    st.metric("Exploitable", 3, "🔴")
with col4:
    st.metric("Threat Level", "MEDIUM", "68%")
with col5:
    st.metric("Sys Health", "87.3%", "+5.2%")

st.divider()

# --- NAVEGACIÓN PRINCIPAL ---
main_tabs = st.tabs([
    "🏠 Home", "📊 Monitor", "🔍 Analyze", "📚 Learn", "💼 Business", "🛠️ Configure"
])

# Tab: HOME
with main_tabs[0]:
    col_a, col_b = st.columns([2, 1])
    with col_a:
        preview_page.render()
    with col_b:
        st.markdown("### 📊 Recent Activity")
        st.info("CVEs: +5 this week\nIncidents: 0\nSystems: 1.2K monitored")

# Tab: MONITOR
with main_tabs[1]:
    sub_tabs = st.tabs(["Dashboard", "CVE Monitoring", "Attack Surface", "Reputation", "Botnets", "IP Validator"])
    with sub_tabs[0]: threat_dashboard.render()
    with sub_tabs[1]: cve_analyzer.render()
    with sub_tabs[2]: attack_surface_analyzer.render()
    with sub_tabs[3]: reputation_analyzer.render()
    with sub_tabs[4]: botnet_analyzer.render()
    with sub_tabs[5]: ip_validator.render()

# Tab: ANALYZE
with main_tabs[2]:
    sub_tabs = st.tabs(["Methodology", "Technical Docs", "Benchmarks"])
    with sub_tabs[0]: methodology_module.render()
    with sub_tabs[1]: technical_docs.render()
    with sub_tabs[2]: benchmarks_page.render()

# Tab: LEARN
with main_tabs[3]:
    sub_tabs = st.tabs(["Help Guide", "API Reference"])
    with sub_tabs[0]: help_guide_module.render()
    with sub_tabs[1]: technical_docs.render()

# Tab: BUSINESS
with main_tabs[4]:
    use_cases_page.render()

# Tab: CONFIGURE
with main_tabs[5]:
    sub_tabs = st.tabs(["API Keys", "Settings"])
    with sub_tabs[0]: api_manager.render()
    with sub_tabs[1]: settings_page.render()

# --- FOOTER PROFESIONAL ---
st.markdown("""
<div class="footer-banner">
    <p><strong>M. Castillo - Privacy Tools</strong></p>
    <p>OSINT Cybersecurity Dashboard v3.2.0</p>
    <p>© 2024-2026 M. Castillo | <a href='mailto:mybloggingnotes@gmail.com'>Support</a></p>
    <p style='font-size: 0.8em; color: gray;'>Security • Privacy • Intelligence</p>
</div>
""", unsafe_allow_html=True)
