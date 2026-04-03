#!/usr/bin/env python3
"""CVE Analysis Module"""

import streamlit as st
import pandas as pd
from scripts.data_collection.cve_monitor import CVEMonitor

class CVEAnalyzer:
    """Módulo independiente para análisis de CVEs"""
    
    def __init__(self):
        self.monitor = CVEMonitor()
    
    def render(self):
        """Renderiza la interfaz de análisis de CVEs"""
        st.header("🔴 CVE Monitoring & Threat Intelligence")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            days = st.slider("Days to monitor:", 1, 30, 7)
        with col2:
            if st.button("🔄 Fetch CVEs", key="fetch_cves"):
                self._fetch_and_display(days)
        
        st.divider()
        
        # Sample CVE Table
        self._display_sample_cves()
    
    def _fetch_and_display(self, days):
        """Fetch y muestra CVEs"""
        st.info("Fetching CVEs from NVD...")
        try:
            data = self.monitor.dashboard_data()
            st.success(f"✅ Found {data['total_new_cves']} new CVEs")
            st.metric("Critical CVEs", data['critical_count'])
            
            if data['critical_cves']:
                st.subheader("Top Critical CVEs")
                for i, cve in enumerate(data['critical_cves'][:5], 1):
                    with st.expander(f"{i}. {cve['id']} - Score: {cve['score']}"):
                        st.write(f"**Severity:** {cve['severity']}")
                        st.write(f"**Published:** {cve['date']}")
                        st.write(f"**Description:** {cve['description']}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    def _display_sample_cves(self):
        """Muestra tabla de CVEs de ejemplo"""
        st.subheader("📋 Sample Critical CVEs")
        
        cve_table = pd.DataFrame({
            'CVE ID': ['CVE-2024-1234', 'CVE-2024-5678', 'CVE-2024-9012', 'CVE-2024-3456', 'CVE-2024-7890'],
            'CVSS Score': [9.8, 9.1, 8.6, 8.2, 6.8],
            'Severity': ['CRITICAL', 'CRITICAL', 'HIGH', 'HIGH', 'MEDIUM'],
            'Product': ['Apache HTTP', 'PostgreSQL', 'OpenSSL', 'Node.js', 'Django'],
            'Exploitable': ['Yes', 'Yes', 'Yes', 'Possible', 'Possible'],
            'Hosts at Risk': [7, 3, 12, 5, 2],
            'Action': ['PATCH NOW', 'PATCH NOW', 'REVIEW', 'REVIEW', 'MONITOR']
        })
        
        st.dataframe(cve_table, use_container_width=True)

# Export
analyzer = CVEAnalyzer()
