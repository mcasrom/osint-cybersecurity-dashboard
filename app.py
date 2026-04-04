#!/usr/bin/env python3
"""
OSINT Cybersecurity Dashboard - Enterprise Edition
Author: M. Castillo
Copyright: © 2024-2026 M. Castillo
Contact: mailto:mybloggingnotes@gmail.com
"""

# --- 1. SEGURIDAD Y BRIDGE DE SECRETOS (CABECERA LIMPIA) ---
from dotenv import load_dotenv
import os
import streamlit as st

# Cargar .env primero (local / Odroid)
load_dotenv()

# Intentar usar st.secrets solo si el fichero secrets.toml está en producción
# Si no existe, se ignora sin romper la app
try:
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
        "Get Help": "https://github.com/mcasrom/osint-cybersecurity-dashboard",
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

    /* FIX para texto en modo oscuro */
    p, span, label, li, .stMarkdown {
        color: var(--text-color) !important;
    }

    /* Caja especial para el "About" que garantiza lectura */
    .about-box {
        background-color: #f0f4f9;
        border: 1px solid #d1d5db;
        border-left: 6px solid #3b82f6;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        color: #111827 !important;
    }

    .about-box h3 {
        color: #3b82f6;
        margin-top: 0;
    }

    /* Fuerza que el contenido interno use el color de texto definido arriba */
    .about-box p,
    .about-box li,
    .about-box span,
    .about-box .stMarkdown p {
        color: inherit !important;
    }

    /* Métricas en Verde Ciber, más visibles */
    [data-testid="stMetricValue"] {
        color: #00c851 !important;
        font-weight: 700;
    }

    /* Énfasis en negritas dentro del about box */
    .about-box strong {
        color: #111827;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# --- 5. CABECERA ---
st.markdown('<p class="main-header">🔒 M. Castillo - Privacy Tools</p>', unsafe_allow_html=True)
st.markdown("### Enterprise‑Grade Threat Intelligence & Vulnerability Management")

# --- 6. SIMULACIÓN DE DATOS Y PANEL DE KPIs ---
# Aquí puedes reemplazar por st.cache_data y datos reales
from datetime import datetime
import random

def simulate_cve_count():
    base = 20
    return base + random.randint(-5, 15)

def simulate_exposed_systems():
    return 800 + random.randint(-50, 200)

def simulate_threat_level():
    index = random.random()
    if index < 0.3:
        return "LOW", 35
    else:
        return "MEDIUM", 68

def simulate_system_health():
    return 70 + random.randint(-5, 20)

cve_today = simulate_cve_count()
critical_cves = max(1, cve_today // 5)
exploitable = max(1, cve_today // 7)
threat_level, threat_pct = simulate_threat_level()
sys_health = simulate_system_health()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("CVEs Today", cve_today, delta="+5 this week")
with col2:
    st.metric("Critical CVEs", critical_cves, delta="+1 this week")
with col3:
    st.metric("Exploitable", exploitable, delta=None)
with col4:
    st.metric("Threat Level", threat_level, delta=f"{threat_pct}%")
with col5:
    st.metric("System Health", f"{sys_health}%", f"+{random.randint(0,10)}%")

st.divider()

# --- 7. NAVEGACIÓN PRINCIPAL ---
main_tabs = st.tabs([
    "🏠 Home", "📊 Monitor", "🔍 Analyze", "📚 Learn", "💼 Business", "🛠 Configure"
])

# --- PESTAÑA HOME ---
with main_tabs[0]:
    # About section con mejor contraste y HTML corregido
    st.markdown("""
    <div class="about-box">
        <h3>About This Platform</h3>

        <p><strong>OSINT Cybersecurity Dashboard</strong></p>
        <p>Enterprise‑grade OSINT and cybersecurity dashboard for real‑time threat intelligence, CVE monitoring, attack surface analysis, and reputation‑based threat detection.</p>

        <p>This dashboard is designed for:</p>
        <ul style="font-size: 0.9em; margin-bottom: 0;">
            <li>SOC analysts and incident responders.</li>
            <li>Security engineers and penetration testers.</li>
            <li>OSINT researchers and privacy consultants.</li>
        </ul>

        <p style="font-size: 0.9em; opacity: 0.8;">© 2024–2026 M. Castillo | <a href="mailto:mybloggingnotes@gmail.com">Contact</a></p>
        <p style="font-size: 0.8em; font-weight: bold;">Version 3.2.0 | Enterprise Threat Intelligence Features Enabled</p>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns([2, 1])
    with col_a:
        preview_page.render()
    with col_b:
        st.markdown("### 📊 Recent Activity")
        st.markdown("""
- **CVEs:** +5 this week  
- **Incidents:** 0  
- **Monitored systems:** 1.2K  
""", unsafe_allow_html=True)

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
