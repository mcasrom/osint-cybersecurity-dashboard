#!/usr/bin/env python3
"""
OSINT Cybersecurity Dashboard - Enterprise Edition
Author: M. Castillo
Copyright: © 2024-2026 M. Castillo
Contact: mailto:mybloggingnotes@gmail.com
"""

# --- 1. SEGURIDAD Y BRIDGE DE SECRETOS (CABECERA LIMPIA) ---
import streamlit as st
import os
from dotenv import load_dotenv

from dotenv import load_dotenv
import os

# 1. Cargar .env siempre (local / Odroid)
load_dotenv()

# 2. Intentar cargar st.secrets solo si el fichero existe (Streamlit Cloud / entornos con secrets.toml)
try:
    # Iterar sobre st.secrets si está disponible
    for key in st.secrets:
        os.environ[key] = str(st.secrets[key])
except Exception as e:
    st.warning(f"Secrets not loaded (running local or without secrets.toml): {e}")




# --- AHORA YA PUEDES IMPORTAR TUS MÓDULOS ---
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


# --- 2. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="OSINT Cybersecurity Dashboard – Enterprise Threat Intelligence",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/mcasrom/osint-dashboard",
        "Report a bug": "mailto:mybloggingnotes@gmail.com",
        "About": "OSINT Cybersecurity Dashboard v3.2.0 - Enterprise Edition"
    }
)

# --- 3. SEO META TAGS (texto visible para indexación) ---
st.markdown("""
<meta name="description" content="OSINT Cybersecurity Dashboard - Enterprise threat intelligence platform for CVEs, attack surface, reputation and botnet monitoring.">
<meta name="author" content="M. Castillo">
<meta property="og:title" content="OSINT Cybersecurity Dashboard – Enterprise Threat Intelligence">
<meta property="og:type" content="website">
<meta property="og:description" content="Enterprise-grade OSINT cybersecurity dashboard for real-time threat intelligence and vulnerability management.">
""", unsafe_allow_html=True)

# --- 4. MOTOR DE ESTILOS (CSS ADAPTATIVO DARK/LIGHT) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    * { font-family: 'Inter', sans-serif; }

    /* Título Principal con Gradiente Profesional */
    .main-header { 
        font-size: 3.5rem !important; 
        font-weight: 800; 
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* FIX DEFINITIVO PARA TEXTO INVISIBLE EN MODO OSCURO */
    /* Forzamos a que párrafos, spans y markdowns usen la variable nativa de Streamlit */
    p, span, label, li, .stMarkdown {
        color: var(--text-color) !important;
    }

    /* Caja especial para el "About" que garantiza lectura */
    .about-box {
        background-color: rgba(128, 128, 128, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #3b82f6;
        margin-bottom: 2rem;
    }

    /* Métricas en Verde Ciber */
    [data-testid="stMetricValue"] {
        color: #00ffa2 !important;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# --- 5. CABECERA ---
st.markdown('<p class="main-header">🔒 M. Castillo - Privacy Tools</p>', unsafe_allow_html=True)
st.markdown("### Enterprise‑Grade Threat Intelligence & Vulnerability Management")

# --- 6. PANEL DE MÉTRICAS (KPIs) ---
# Recuerda: reemplaza estos valores por datos reales o de demo bien etiquetados
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("CVEs Today", 24, "+5")
with col2:
    st.metric("Critical", 5, "⚠")
with col3:
    st.metric("Exploitable", 3, "🔴")
with col4:
    st.metric("Threat Level", "MEDIUM", "68%")
with col5:
    st.metric("Sys Health", "87.3%", "+5.2%")

st.divider()

# --- 7. NAVEGACIÓN PRINCIPAL ---
main_tabs = st.tabs([
    "🏠 Home", "📊 Monitor", "🔍 Analyze", "📚 Learn", "💼 Business", "🛠 Configure"
])

# --- PESTAÑA HOME ---
with main_tabs[0]:
    # About section con branding claro
    st.markdown("""
    <div class="about-box">
        <h3 style="color: #3b82f6; margin-top:0;">About This Platform</h3>
        <p><strong>OSINT Cybersecurity Dashboard</strong></p>
        <p>Comprehensive threat intelligence and vulnerability management platform.</p>
        <p>This dashboard is designed for:
            <ul style="font-size: 0.9em;">
                <li>SOC analysts who need a centralized view of threats.</li>
                <li>Security consultants and OSINT researchers.</li>
            </ul>
        </p>
        <p style="font-size: 0.8em; opacity: 0.8;">© 2024–2026 M. Castillo | mailto:mybloggingnotes@gmail.com</p>
        <p style="font-size: 0.8em; font-weight: bold;">Version 3.2.0 | Enterprise Features Enabled</p>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns([2, 1])
    with col_a:
        preview_page.render()
    with col_b:
        st.markdown("### 📊 Recent Activity")
        st.info("CVEs: +5 this week\\nIncidents: 0\\nSystems: 1.2K monitored")

# --- PESTAÑA MONITOR ---
with main_tabs[1]:
    sub_tabs = st.tabs([
        "Dashboard", "CVE Monitoring", "Attack Surface", "Reputation", "Botnets", "IP Validator"
    ])
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

# --- PESTAÑA ANALYZE ---
with main_tabs[2]:
    sub_tabs = st.tabs([
        "Methodology", "Technical Docs", "Benchmarks"
    ])
    with sub_tabs[0]:
        methodology_module.render()
    with sub_tabs[1]:
        technical_docs.render()
    with sub_tabs[2]:
        benchmarks_page.render()

# --- PESTAÑA LEARN ---
with main_tabs[3]:
    sub_tabs = st.tabs([
        "Help Guide", "API Reference"
    ])
    with sub_tabs[0]:
        help_guide_module.render()
    with sub_tabs[1]:
        technical_docs.render()

# --- PESTAÑA BUSINESS ---
with main_tabs[4]:
    use_cases_page.render()

# --- PESTAÑA CONFIGURE ---
with main_tabs[5]:
    sub_tabs = st.tabs([
        "API Keys", "Settings"
    ])
    with sub_tabs[0]:
        api_manager.render()
    with sub_tabs[1]:
        settings_page.render()

# --- 8. FOOTER PROFESIONAL ---
st.divider()
st.markdown("""
<div style='text-align: center; padding: 20px; opacity: 0.7;'>
    <p><strong>M. Castillo - Privacy Tools</strong> | OSINT Cybersecurity Dashboard v3.2.0</p>
    <p>© 2024–2026 M. Castillo | <a href='mailto:mybloggingnotes@gmail.com'>Contact Support</a></p>
    <p style='font-size: 0.8em;'>Enterprise Threat Intelligence • Real‑time Monitoring • Advanced Analytics</p>
</div>
""", unsafe_allow_html=True)
