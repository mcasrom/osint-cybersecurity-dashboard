"""
Utils para obtener la IP real del cliente (navegador) en Streamlit,
sin depender de la IP del servidor.
"""

import streamlit as st
from streamlit_javascript import st_javascript
import json

def get_client_ip() -> str:
    """
    Obtiene la IP real del cliente a través de una API pública (ipify.org).
    Retorna:
        - la IP como string (ej. "192.168.1.47"),
        - o "unknown" si falla.
    """
    url = "https://api.ipify.org?format=json"
    script = (
        f"await fetch('{url}').then(r => r.json()).then(r => JSON.stringify(r));"
    )
    try:
        result = st_javascript(script)
        if isinstance(result, str):
            try:
                data = json.loads(result)
                return data.get("ip", "unknown")
            except json.JSONDecodeError:
                pass
    except Exception:
        pass
    return "unknown"


def render_client_ip_widget():
    client_ip = get_client_ip()
    st.markdown("### 📡 Your IP (Real Client IP)")
    if client_ip == "unknown":
        st.warning("Could not detect your real IP.")
    else:
        st.code(f"Your IP: {client_ip}")
import requests

def get_public_ip_python() -> str:
    try:
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            return response.text.strip()
    except Exception:
        pass
    return "unknown"
