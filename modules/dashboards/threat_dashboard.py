#!/usr/bin/env python3
"""Threat Intelligence Dashboard Module"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class ThreatDashboard:
    """Módulo independiente para dashboard de amenazas"""
    
    def __init__(self):
        self.title = "📊 Threat Intelligence Dashboard"
        self.update_time = datetime.now()
    
    def render(self):
        """Renderiza el dashboard completo"""
        st.header(self.title)
        
        # Alerts
        st.subheader("🚨 Critical Alerts")
        self._render_alerts()
        
        st.divider()
        
        # Charts
        col1, col2 = st.columns(2)
        with col1:
            self._render_cve_trends()
        with col2:
            self._render_severity_distribution()
        
        st.divider()
        
        # KPIs
        self._render_kpis()
        
        st.divider()
        
        # Geographic distribution
        self._render_geographic_analysis()
    
    def _render_alerts(self):
        """Renderiza alertas críticas"""
        st.markdown("""
        <div style='background: #fef2f2; border-left: 4px solid #dc2626; padding: 15px; border-radius: 5px; margin-bottom: 10px;'>
            <strong>⚠️ CVE-2024-1234 Actively Exploited</strong><br>
            Apache vulnerability with 3 vulnerable hosts. Immediate patching required.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; border-radius: 5px;'>
            <strong>⚡ Zero-Day in Chromium</strong><br>
            Security researchers discovered an unpatched vulnerability.
        </div>
        """, unsafe_allow_html=True)
    
    def _render_cve_trends(self):
        """Gráfico de tendencia de CVEs"""
        st.subheader("📈 CVE Discoveries (30 Days)")
        
        cve_data = pd.DataFrame({
            'Day': list(range(1, 31)),
            'Critical': [2, 3, 2, 4, 5, 4, 5, 6, 5, 4, 3, 4, 5, 6, 7, 5, 4, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1],
            'High': [5, 6, 7, 6, 8, 8, 8, 9, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2],
            'Medium': [4, 5, 5, 6, 7, 7, 7, 8, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        })
        
        fig = px.line(cve_data, x='Day', y=['Critical', 'High', 'Medium'],
                     title='CVE Trend Analysis',
                     color_discrete_map={'Critical': '#dc2626', 'High': '#ea580c', 'Medium': '#f59e0b'})
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_severity_distribution(self):
        """Gráfico de distribución de severidad"""
        st.subheader("📊 Severity Distribution")
        
        severity_data = pd.DataFrame({
            'Severity': ['Critical', 'High', 'Medium', 'Low'],
            'Count': [5, 8, 7, 4]
        })
        
        fig = px.pie(severity_data, values='Count', names='Severity',
                    color_discrete_map={'Critical': '#dc2626', 'High': '#ea580c', 
                                       'Medium': '#f59e0b', 'Low': '#10b981'})
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_kpis(self):
        """Renderiza KPIs principales"""
        st.subheader("📊 Key Performance Indicators")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Response Time", "23h 45m", "↓ 4h faster")
        with col2:
            st.metric("Patch Rate", "87.3%", "↑ 5.2%")
        with col3:
            st.metric("Exposed Assets", "15.2k", "↑ 3.1%")
        with col4:
            st.metric("CVSS Avg", "8.7", "↑ 0.4")
        with col5:
            st.metric("Detection Rate", "94.2%", "↑ 2.1%")
    
    def _render_geographic_analysis(self):
        """Análisis geográfico de amenazas"""
        st.subheader("🌍 Geographic Threat Distribution")
        
        geo_data = pd.DataFrame({
            'Region': ['Asia', 'Europe', 'Americas', 'Middle East', 'Africa'],
            'Attacks': [1250, 750, 580, 240, 120]
        })
        
        fig = px.bar(geo_data, x='Region', y='Attacks', color='Attacks',
                    color_continuous_scale='Reds')
        st.plotly_chart(fig, use_container_width=True)

# Export
dashboard = ThreatDashboard()
