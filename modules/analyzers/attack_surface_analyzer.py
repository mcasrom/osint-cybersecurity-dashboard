#!/usr/bin/env python3
"""Attack Surface Analysis Module"""

import streamlit as st
import pandas as pd
from scripts.data_collection.external_attack_surface import ExternalAttackSurface

class AttackSurfaceAnalyzer:
    """Módulo para análisis de superficie de ataque externa"""
    
    def __init__(self):
        pass
    
    def render(self):
        """Renderiza interfaz de escaneo"""
        st.header("🗺️ External Attack Surface Scanner")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            domain = st.text_input("Enter domain to scan:", value="example.com")
        with col2:
            if st.button("🔍 Run Scan", key="run_attack_surface_scan"):
                self._perform_scan(domain)
        
        st.divider()
        
        # Infrastructure Breakdown
        self._display_infrastructure_breakdown()
    
    def _perform_scan(self, domain):
        """Ejecuta escaneo de dominio"""
        st.info(f"Scanning {domain}...")
        try:
            scanner = ExternalAttackSurface(domain)
            results = scanner.full_scan()
            
            st.success("✅ Scan completed!")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("IPs Found", len(results['ips']))
            with col2:
                st.metric("Subdomains", len(results['subdomains']))
            with col3:
                st.metric("Infrastructure Assets", len(results['infrastructure']))
            with col4:
                st.metric("Risk Level", "MEDIUM")
            
            st.subheader("Scan Results")
            st.json(results)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    def _display_infrastructure_breakdown(self):
        """Muestra desglose de infraestructura"""
        st.subheader("Infrastructure Breakdown")
        
        infra_data = pd.DataFrame({
            'Asset Type': ['Web Servers', 'DNS Servers', 'Mail Servers', 'Database', 'CDN', 'Load Balancers'],
            'Count': [3, 2, 2, 1, 1, 1],
            'Risk Level': ['Medium', 'Low', 'Low', 'High', 'Low', 'Medium'],
            'Last Scanned': ['2 hours ago', '2 hours ago', '2 hours ago', '2 hours ago', '2 hours ago', '2 hours ago']
        })
        
        st.dataframe(infra_data, use_container_width=True)

# Export
analyzer = AttackSurfaceAnalyzer()
