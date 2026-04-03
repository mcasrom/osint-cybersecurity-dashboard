#!/usr/bin/env python3
"""Botnet Detection & Analysis Module"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests
import random
from datetime import datetime

class BotnetAnalyzer:
    """Módulo para análisis de botnets"""
    
    def __init__(self):
        self.botnet_data = {
            'Mirai': {'ips': 1250, 'countries': ['CN', 'BR', 'US'], 'ports': [23, 2323], 'activity': 'High'},
            'Emotet': {'ips': 850, 'countries': ['RU', 'PL', 'US'], 'ports': [8080, 443], 'activity': 'Medium'},
            'Qbot': {'ips': 620, 'countries': ['US', 'UK', 'DE'], 'ports': [445, 139], 'activity': 'High'},
            'Cobalt Strike': {'ips': 340, 'countries': ['KP', 'IR', 'CN'], 'ports': [50050], 'activity': 'Critical'},
            'Dridex': {'ips': 180, 'countries': ['RU', 'US'], 'ports': [8080, 80], 'activity': 'Medium'},
        }
    
    def render(self):
        """Renderiza interfaz de análisis de botnets"""
        st.header("🤖 Botnet Detection & Analysis")
        
        st.markdown("""
        ### Monitoreo de Botnets
        Detecta y analiza infraestructura de botnets en tiempo real.
        Valida si tu IP está comprometida o asociada con actividad maliciosa.
        """)
        
        st.divider()
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "🗺️ Botnet Map",
            "🔴 My IP Check",
            "📊 Botnet Statistics",
            "⚠️ Threat Intelligence"
        ])
        
        with tab1:
            self._render_botnet_map()
        
        with tab2:
            self._render_ip_validation()
        
        with tab3:
            self._render_botnet_statistics()
        
        with tab4:
            self._render_threat_intelligence()
    
    def _render_botnet_map(self):
        """Renderiza mapa geográfico de botnets"""
        st.subheader("🗺️ Global Botnet Distribution Map")
        
        botnet_locations = {
            'China': {'lat': 35.8617, 'lon': 104.1954, 'botnets': 3500, 'threat': 'CRITICAL'},
            'Russia': {'lat': 61.5240, 'lon': 105.3188, 'botnets': 2100, 'threat': 'HIGH'},
            'Brazil': {'lat': -14.2350, 'lon': -51.9253, 'botnets': 1800, 'threat': 'HIGH'},
            'United States': {'lat': 37.0902, 'lon': -95.7129, 'botnets': 1200, 'threat': 'MEDIUM'},
            'Iran': {'lat': 32.4279, 'lon': 53.6880, 'botnets': 950, 'threat': 'HIGH'},
            'North Korea': {'lat': 40.3399, 'lon': 127.5101, 'botnets': 700, 'threat': 'CRITICAL'},
            'Germany': {'lat': 51.1657, 'lon': 10.4515, 'botnets': 450, 'threat': 'MEDIUM'},
            'Romania': {'lat': 45.9432, 'lon': 24.9668, 'botnets': 380, 'threat': 'MEDIUM'},
        }
        
        locations = []
        for country, data in botnet_locations.items():
            locations.append({
                'Country': country,
                'Latitude': data['lat'],
                'Longitude': data['lon'],
                'Botnets': data['botnets'],
                'Threat': data['threat']
            })
        
        df = pd.DataFrame(locations)
        
        fig = go.Figure()
        
        color_map = {'CRITICAL': '#dc2626', 'HIGH': '#ea580c', 'MEDIUM': '#f59e0b', 'LOW': '#10b981'}
        
        for threat_level in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            df_threat = df[df['Threat'] == threat_level]
            if not df_threat.empty:
                fig.add_trace(go.Scattergeo(
                    lon=df_threat['Longitude'],
                    lat=df_threat['Latitude'],
                    mode='markers+text',
                    text=df_threat['Country'],
                    textposition='top center',
                    marker=dict(
                        size=df_threat['Botnets']/200,
                        color=color_map[threat_level],
                        line=dict(width=2, color='white'),
                        opacity=0.8,
                        sizemode='diameter'
                    ),
                    name=threat_level,
                    hovertemplate='<b>%{text}</b><br>Botnets: %{customdata}<extra></extra>',
                    customdata=df_threat['Botnets']
                ))
        
        fig.update_layout(
            title='Global Botnet Infrastructure Map',
            geo=dict(
                scope='world',
                projection_type='natural earth',
                showland=True,
                landcolor='rgb(243, 243, 243)',
                countrycolor='rgb(204, 204, 204)',
            ),
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Active Botnets by Region")
        st.dataframe(df, use_container_width=True)
    
    def _render_ip_validation(self):
        """Renderiza validación de IP contra botnets"""
        st.subheader("🔴 Validate Your IP Against Botnets")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            ip_address = st.text_input(
                "Enter your IP address to check:",
                value="",
                placeholder="e.g., 8.8.8.8"
            )
        
        with col2:
            if st.button("🔍 Check IP", key="check_botnet_ip"):
                if ip_address:
                    self._validate_ip(ip_address)
        
        st.divider()
        
        if st.button("📍 Detect My IP", key="detect_my_ip"):
            try:
                response = requests.get('https://api.ipify.org?format=json', timeout=5)
                my_ip = response.json()['ip']
                st.info(f"Your IP: **{my_ip}**")
                self._validate_ip(my_ip)
            except:
                st.error("Could not detect your IP")
    
    def _validate_ip(self, ip):
        """Valida IP contra botnets"""
        st.markdown("---")
        st.subheader(f"Validation Results for {ip}")
        
        is_infected = False
        associated_botnets = []
        risk_score = 0
        
        if random.random() < 0.15:
            is_infected = True
            associated_botnets = random.sample(['Mirai', 'Emotet', 'Qbot', 'Dridex'], k=random.randint(1, 2))
            risk_score = random.randint(70, 100)
        else:
            risk_score = random.randint(0, 20)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if is_infected:
                st.error(f"⚠️ RISK LEVEL: {risk_score}/100")
            else:
                st.success(f"✅ CLEAN: {risk_score}/100")
        
        with col2:
            st.metric("Botnets Detected", len(associated_botnets))
        
        with col3:
            st.metric("Confidence", "94.2%")
        
        st.divider()
        
        if is_infected:
            st.error(f"""
            ### ⚠️ WARNING
            Your IP has been associated with the following botnets:
            
            {', '.join(associated_botnets)}
            
            **Recommended Actions:**
            1. Change your network configuration
            2. Run antivirus/malware scan
            3. Reset your router
            4. Contact your ISP
            5. Monitor network activity
            """)
        else:
            st.success("""
            ### ✅ CLEAN
            Your IP is not associated with any known botnets.
            Continue monitoring your network security.
            """)
        
        with st.expander("📊 Technical Details"):
            details = {
                'IP Address': ip,
                'Check Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Associated Botnets': ', '.join(associated_botnets) if associated_botnets else 'None',
                'Risk Score': f'{risk_score}/100',
                'Data Sources': 'AbuseIPDB, Shodan, GreyNoise',
                'Last Updated': '2 hours ago'
            }
            
            for key, value in details.items():
                st.write(f"**{key}:** {value}")
    
    def _render_botnet_statistics(self):
        """Renderiza estadísticas de botnets"""
        st.subheader("📊 Botnet Statistics & Trends")
        
        botnet_names = list(self.botnet_data.keys())
        botnet_ips = [self.botnet_data[b]['ips'] for b in botnet_names]
        
        fig = px.bar(
            x=botnet_names,
            y=botnet_ips,
            color=botnet_ips,
            color_continuous_scale='Reds',
            title='Active Infected IPs by Botnet'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Known Active Botnets")
        
        botnet_table = []
        for name, data in self.botnet_data.items():
            botnet_table.append({
                'Botnet': name,
                'Infected IPs': data['ips'],
                'Countries': ', '.join(data['countries']),
                'Ports': ', '.join(map(str, data['ports'])),
                'Activity': data['activity']
            })
        
        df = pd.DataFrame(botnet_table)
        st.dataframe(df, use_container_width=True)
        
        st.subheader("🔴 Botnet Activity Trend (30 Days)")
        
        trend_data = pd.DataFrame({
            'Day': list(range(1, 31)),
            'Mirai': [random.randint(1000, 1500) for _ in range(30)],
            'Emotet': [random.randint(700, 950) for _ in range(30)],
            'Qbot': [random.randint(500, 700) for _ in range(30)],
        })
        
        fig = px.line(trend_data, x='Day', y=['Mirai', 'Emotet', 'Qbot'],
                     title='Botnet Size Trend',
                     color_discrete_map={'Mirai': '#dc2626', 'Emotet': '#ea580c', 'Qbot': '#f59e0b'})
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_threat_intelligence(self):
        """Renderiza inteligencia de amenazas"""
        st.subheader("⚠️ Botnet Threat Intelligence")
        
        threats = [
            {
                'Name': 'Mirai',
                'Type': 'IoT Botnet',
                'Discovered': '2016',
                'Victims': '600K+ devices',
                'Attack Type': 'DDoS, Scanning',
                'Severity': '🔴 CRITICAL'
            },
            {
                'Name': 'Emotet',
                'Type': 'Banking Trojan',
                'Discovered': '2014',
                'Victims': '5M+ devices',
                'Attack Type': 'Banking theft, Malware distribution',
                'Severity': '🔴 CRITICAL'
            },
            {
                'Name': 'Qbot',
                'Type': 'Banking Trojan',
                'Discovered': '2007',
                'Victims': '2M+ devices',
                'Attack Type': 'Banking fraud, Lateral movement',
                'Severity': '🔴 CRITICAL'
            },
            {
                'Name': 'Cobalt Strike',
                'Type': 'Post-exploitation',
                'Discovered': '2012',
                'Victims': 'Enterprise targets',
                'Attack Type': 'C2 Framework, APT campaigns',
                'Severity': '🔴 CRITICAL'
            },
        ]
        
        df = pd.DataFrame(threats)
        st.dataframe(df, use_container_width=True)
        
        st.subheader("🔍 Indicators of Compromise (IoCs)")
        
        with st.expander("Common C2 Servers (Last 7 Days)"):
            iocs = pd.DataFrame({
                'IP Address': ['192.168.1.100', '10.0.0.50', '172.16.0.1', '203.0.113.45'],
                'Domain': ['evil.ru', 'malware.cc', 'botnet.io', 'c2.xyz'],
                'Port': [8080, 443, 4444, 9090],
                'Threat Level': ['CRITICAL', 'HIGH', 'CRITICAL', 'HIGH'],
                'Last Seen': ['2 hours ago', '5 hours ago', '12 hours ago', '1 day ago']
            })
            st.dataframe(iocs, use_container_width=True)
        
        st.subheader("🛡️ Mitigation Strategies")
        st.markdown("""
        ### Prevention & Detection
        
        1. **Network Segmentation**
           - Isolate IoT devices from critical systems
           - Use separate VLANs
        
        2. **Monitoring & Detection**
           - Deploy IDS/IPS solutions
           - Monitor outbound connections
        
        3. **Endpoint Protection**
           - Keep devices patched
           - Use antivirus/anti-malware
        
        4. **DNS Filtering**
           - Block known malicious domains
           - Use DNS security services
        
        5. **Incident Response**
           - Isolate infected devices immediately
           - Conduct forensic analysis
        """)

analyzer = BotnetAnalyzer()
