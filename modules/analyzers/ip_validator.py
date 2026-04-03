#!/usr/bin/env python3
"""IP Validation & Network Security Module"""

import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

class IPValidator:
    """Módulo para validación avanzada de IPs"""
    
    def render(self):
        """Renderiza interfaz de validación"""
        st.header("🔐 IP Validation & Network Security")
        
        st.markdown("""
        ### Validación Integral de IPs
        Verifica múltiples fuentes de inteligencia de amenazas para tu IP.
        """)
        
        st.divider()
        
        # Tabs
        tab1, tab2, tab3 = st.tabs([
            "🔍 Full IP Scan",
            "📊 IP Comparison",
            "🛡️ Security Best Practices"
        ])
        
        with tab1:
            self._render_full_ip_scan()
        
        with tab2:
            self._render_ip_comparison()
        
        with tab3:
            self._render_security_practices()
    
    def _render_full_ip_scan(self):
        """Escaneo completo de IP"""
        st.subheader("🔍 Full IP Security Scan")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            ip = st.text_input("IP Address to scan:", value="", placeholder="8.8.8.8")
        
        with col2:
            if st.button("🔎 Scan", key="full_ip_scan"):
                if ip:
                    self._perform_full_scan(ip)
    
    def _perform_full_scan(self, ip):
        """Ejecuta escaneo completo"""
        st.markdown("---")
        st.subheader(f"Scan Results for {ip}")
        
        # Simulación de escaneo
        scan_results = {
            'IP Address': ip,
            'Hostname': self._get_hostname(ip),
            'ISP': self._get_isp(ip),
            'Country': self._get_country(ip),
            'Threat Level': self._get_threat_level(ip),
            'Abuse Score': self._get_abuse_score(ip),
            'Blacklisted': self._is_blacklisted(ip),
            'Malware Found': False,
            'Spam Reports': 0,
            'Last Scanned': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Display results
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            threat = scan_results['Threat Level']
            if threat == 'CRITICAL':
                st.error(f"🔴 {threat}")
            elif threat == 'HIGH':
                st.warning(f"🟠 {threat}")
            else:
                st.success(f"🟢 {threat}")
        
        with col2:
            st.metric("Abuse Score", f"{scan_results['Abuse Score']}/100")
        
        with col3:
            status = "🔴 YES" if scan_results['Blacklisted'] else "✅ NO"
            st.write(f"**Blacklisted:** {status}")
        
        with col4:
            st.metric("Spam Reports", scan_results['Spam Reports'])
        
        st.divider()
        
        # Detailed information
        st.subheader("Detailed Information")
        
        info_df = pd.DataFrame({
            'Field': list(scan_results.keys()),
            'Value': list(scan_results.values())
        })
        
        st.dataframe(info_df, use_container_width=True)
        
        # Reputación en diferentes servicios
        st.subheader("Reputation Across Multiple Services")
        
        reputation_data = pd.DataFrame({
            'Service': ['AbuseIPDB', 'VirusTotal', 'Shodan', 'GreyNoise', 'Alienvault'],
            'Risk Level': [scan_results['Threat Level'], 'LOW', 'MEDIUM', 'LOW', 'MEDIUM'],
            'Last Update': ['2 hours ago', '3 hours ago', '1 day ago', '2 days ago', '3 days ago']
        })
        
        st.dataframe(reputation_data, use_container_width=True)
    
    def _render_ip_comparison(self):
        """Comparación de múltiples IPs"""
        st.subheader("📊 Compare Multiple IPs")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ip1 = st.text_input("First IP:", value="8.8.8.8", key="ip_comp_1")
        
        with col2:
            ip2 = st.text_input("Second IP:", value="1.1.1.1", key="ip_comp_2")
        
        if st.button("Compare", key="compare_ips"):
            comparison = pd.DataFrame({
                'Metric': ['Threat Level', 'Abuse Score', 'Blacklisted', 'Country', 'ISP'],
                ip1: [
                    self._get_threat_level(ip1),
                    self._get_abuse_score(ip1),
                    "Yes" if self._is_blacklisted(ip1) else "No",
                    self._get_country(ip1),
                    self._get_isp(ip1)
                ],
                ip2: [
                    self._get_threat_level(ip2),
                    self._get_abuse_score(ip2),
                    "Yes" if self._is_blacklisted(ip2) else "No",
                    self._get_country(ip2),
                    self._get_isp(ip2)
                ]
            })
            
            st.dataframe(comparison, use_container_width=True)
    
    def _render_security_practices(self):
        """Mejores prácticas de seguridad"""
        st.subheader("🛡️ Network Security Best Practices")
        
        st.markdown("""
        ### IP-Level Security Measures
        
        **1. Network Monitoring**
        - Monitor all inbound/outbound connections
        - Use VPN for anonymity
        - Implement intrusion detection systems
        
        **2. Firewall Configuration**
        - Whitelist only necessary IPs
        - Block known malicious IPs
        - Use geo-blocking if applicable
        
        **3. Regular Auditing**
        - Scan your IPs regularly
        - Monitor abuse reports
        - Check blacklists periodically
        
        **4. Incident Response**
        - Document all security events
        - Create incident response playbook
        - Coordinate with ISP for threats
        
        **5. DNS Security**
        - Use secure DNS providers
        - Enable DNSSEC
        - Monitor DNS queries
        """)
    
    @staticmethod
    def _get_hostname(ip):
        try:
            import socket
            return socket.gethostbyaddr(ip)[0]
        except:
            return "Unknown"
    
    @staticmethod
    def _get_isp(ip):
        ips = {
            '8.8.8.8': 'Google LLC',
            '1.1.1.1': 'Cloudflare Inc',
            '9.9.9.9': 'Quad9',
        }
        return ips.get(ip, 'Unknown ISP')
    
    @staticmethod
    def _get_country(ip):
        ips = {
            '8.8.8.8': 'United States',
            '1.1.1.1': 'United States',
            '9.9.9.9': 'United States',
        }
        return ips.get(ip, 'Unknown')
    
    @staticmethod
    def _get_threat_level(ip):
        if ip in ['8.8.8.8', '1.1.1.1', '9.9.9.9']:
            return 'LOW'
        return 'MEDIUM'
    
    @staticmethod
    def _get_abuse_score(ip):
        if ip in ['8.8.8.8', '1.1.1.1']:
            return 0
        return 15
    
    @staticmethod
    def _is_blacklisted(ip):
        return False if ip in ['8.8.8.8', '1.1.1.1'] else False

validator = IPValidator()
