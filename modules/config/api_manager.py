#!/usr/bin/env python3
"""API Keys Configuration Manager"""

import streamlit as st
import os

class APIManager:
    """Gestiona configuración de API keys de forma segura"""
    
    def __init__(self):
        self.env_file = ".env"
    
    def render(self):
        """Renderiza interfaz de configuración de API keys"""
        st.header("🔐 API Keys Configuration")
        
        st.markdown("""
        ### Agrega tus API Keys aquí
        Las API keys se guardan de forma segura en tu archivo `.env` local.
        Nunca se compartirán ni se subirán a internet.
        """)
        
        st.divider()
        
        # Tabs para cada API
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🔴 AbuseIPDB",
            "🟢 VirusTotal",
            "🟡 Shodan",
            "🟣 Recorded Future",
            "🔵 Censys"
        ])
        
        with tab1:
            self._render_abuseipdb_config()
        
        with tab2:
            self._render_virustotal_config()
        
        with tab3:
            self._render_shodan_config()
        
        with tab4:
            self._render_recorded_future_config()
        
        with tab5:
            self._render_censys_config()
        
        st.divider()
        st.subheader("✅ API Status")
        self._render_api_status()
    
    def _render_abuseipdb_config(self):
        """Configurar AbuseIPDB"""
        st.subheader("AbuseIPDB API Configuration")
        
        st.info("""
        **¿Qué es AbuseIPDB?**
        - Verifica reputación de direcciones IP
        - Identifica IPs maliciosas
        
        **¿Dónde obtenerla?**
        1. Visita: https://www.abuseipdb.com/register
        2. Crea una cuenta gratuita
        3. Ve a Dashboard → API
        4. Copia tu API Key
        """)
        
        api_key = st.text_input("AbuseIPDB API Key", type="password", key="abuseipdb_key")
        
        if api_key:
            if st.button("💾 Save AbuseIPDB Key", key="save_abuseipdb"):
                self._save_api_key('ABUSEIPDB_API_KEY', api_key)
                st.success("✅ AbuseIPDB key guardada")
        
        if self._api_is_configured('ABUSEIPDB_API_KEY'):
            st.success("✅ AbuseIPDB configurado")
        else:
            st.warning("⚠️ AbuseIPDB no configurado")
    
    def _render_virustotal_config(self):
        """Configurar VirusTotal"""
        st.subheader("VirusTotal API Configuration")
        
        st.info("""
        **¿Qué es VirusTotal?**
        - Analiza archivos y dominios
        - Detección de malware
        
        **¿Dónde obtenerla?**
        1. Visita: https://www.virustotal.com/gui/home/upload
        2. Crea cuenta gratuita
        3. Ve a Settings → API Key
        4. Copia tu API key
        """)
        
        api_key = st.text_input("VirusTotal API Key", type="password", key="virustotal_key")
        
        if api_key:
            if st.button("💾 Save VirusTotal Key", key="save_virustotal"):
                self._save_api_key('VIRUSTOTAL_API_KEY', api_key)
                st.success("✅ VirusTotal key guardada")
        
        if self._api_is_configured('VIRUSTOTAL_API_KEY'):
            st.success("✅ VirusTotal configurado")
        else:
            st.warning("⚠️ VirusTotal no configurado")
    
    def _render_shodan_config(self):
        """Configurar Shodan"""
        st.subheader("Shodan API Configuration")
        
        st.info("""
        **¿Qué es Shodan?**
        - Buscador de dispositivos en Internet
        - Descubre servicios expuestos
        
        **¿Dónde obtenerla?**
        1. Visita: https://www.shodan.io/
        2. Crea cuenta (plan free disponible)
        3. Ve a Dashboard → API Key
        4. Copia tu API key
        """)
        
        api_key = st.text_input("Shodan API Key", type="password", key="shodan_key")
        
        if api_key:
            if st.button("💾 Save Shodan Key", key="save_shodan"):
                self._save_api_key('SHODAN_API_KEY', api_key)
                st.success("✅ Shodan key guardada")
        
        if self._api_is_configured('SHODAN_API_KEY'):
            st.success("✅ Shodan configurado")
        else:
            st.warning("⚠️ Shodan no configurado")
    
    def _render_recorded_future_config(self):
        """Configurar Recorded Future"""
        st.subheader("Recorded Future API Configuration")
        
        st.info("""
        **¿Qué es Recorded Future?**
        - Inteligencia de amenazas avanzada
        
        **¿Dónde obtenerla?**
        1. Visita: https://www.recordedfuture.com/
        2. Solicita acceso
        3. Dashboard → API Configuration
        """)
        
        api_key = st.text_input("Recorded Future API Key", type="password", key="recorded_future_key")
        
        if api_key:
            if st.button("💾 Save Recorded Future Key", key="save_recorded_future"):
                self._save_api_key('RECORDED_FUTURE_API_KEY', api_key)
                st.success("✅ Recorded Future key guardada")
        
        if self._api_is_configured('RECORDED_FUTURE_API_KEY'):
            st.success("✅ Recorded Future configurado")
        else:
            st.warning("⚠️ Recorded Future no configurado")
    
    def _render_censys_config(self):
        """Configurar Censys"""
        st.subheader("Censys API Configuration")
        
        st.info("""
        **¿Qué es Censys?**
        - Búsqueda de certificados SSL
        
        **¿Dónde obtenerla?**
        1. Visita: https://censys.io/
        2. Crea cuenta (plan free disponible)
        3. Ve a Account → API
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            api_id = st.text_input("Censys API ID", type="password", key="censys_id")
        
        with col2:
            api_secret = st.text_input("Censys API Secret", type="password", key="censys_secret")
        
        if api_id and api_secret:
            if st.button("💾 Save Censys Keys", key="save_censys"):
                self._save_api_key('CENSYS_API_ID', api_id)
                self._save_api_key('CENSYS_API_SECRET', api_secret)
                st.success("✅ Censys keys guardadas")
        
        if self._api_is_configured('CENSYS_API_ID'):
            st.success("✅ Censys configurado")
        else:
            st.warning("⚠️ Censys no configurado")
    
    def _save_api_key(self, key_name, api_key):
        """Guarda API key en archivo .env"""
        try:
            env_content = ""
            if os.path.exists(self.env_file):
                with open(self.env_file, 'r') as f:
                    env_content = f.read()
            
            lines = env_content.split('\n')
            lines = [l for l in lines if not l.startswith(f"{key_name}=")]
            lines.append(f"{key_name}={api_key}")
            
            with open(self.env_file, 'w') as f:
                f.write('\n'.join(lines))
            
            st.session_state[f"api_{key_name}"] = api_key
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    def _api_is_configured(self, key_name):
        """Verifica si una API está configurada"""
        try:
            if os.path.exists(self.env_file):
                with open(self.env_file, 'r') as f:
                    content = f.read()
                    return f"{key_name}=" in content
            return False
        except:
            return False
    
    def _render_api_status(self):
        """Muestra estado de todas las APIs"""
        import pandas as pd
        
        status_data = {
            'API': ['AbuseIPDB', 'VirusTotal', 'Shodan', 'Recorded Future', 'Censys'],
            'Configured': [
                "✅" if self._api_is_configured('ABUSEIPDB_API_KEY') else "❌",
                "✅" if self._api_is_configured('VIRUSTOTAL_API_KEY') else "❌",
                "✅" if self._api_is_configured('SHODAN_API_KEY') else "❌",
                "✅" if self._api_is_configured('RECORDED_FUTURE_API_KEY') else "❌",
                "✅" if self._api_is_configured('CENSYS_API_ID') else "❌",
            ]
        }
        
        df = pd.DataFrame(status_data)
        st.dataframe(df, use_container_width=True)
        
        st.success("""
        ✅ **Notas de Seguridad:**
        - Las API keys se guardan localmente en `.env`
        - Nunca compartas tu archivo `.env`
        - Agrega `.env` a `.gitignore`
        - Las keys nunca se envían a servidores
        """)

manager = APIManager()
