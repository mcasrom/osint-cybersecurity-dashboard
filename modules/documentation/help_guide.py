#!/usr/bin/env python3
"""Help & User Guide Module"""

import streamlit as st

class HelpGuideModule:
    """Módulo de ayuda y guía de usuario"""
    
    def render(self):
        """Renderiza guía de usuario"""
        st.header("ℹ️ User Guide & Help")
        
        st.subheader("🚀 Getting Started")
        st.markdown("""
        ### Dashboard Tabs Overview
        
        **📊 Dashboard Tab**
        - Real-time threat metrics
        - CVE trends and severity analysis
        - Geographic threat distribution
        - KPI tracking
        
        **🔴 CVE Monitoring Tab**
        - Fetch latest CVEs from NVD
        - Filter by severity
        - Review vulnerability details
        - Export threat reports
        
        **🗺️ Attack Surface Tab**
        - Scan external infrastructure
        - Identify exposed assets
        - Map network topology
        - Discover subdomain exposure
        
        **🔍 Reputation Tab**
        - Check IP reputation
        - Verify domain trustworthiness
        - View abuse history
        - Track malicious activity
        """)
        
        st.divider()
        
        st.subheader("❓ Frequently Asked Questions")
        
        faqs = {
            "How do I scan a domain?": """
            1. Go to the **🗺️ Attack Surface** tab
            2. Enter your domain (e.g., example.com)
            3. Click **🔍 Run Scan**
            4. Wait for results (1-2 minutes)
            5. Review infrastructure breakdown
            """,
            
            "What does Threat Level mean?": """
            - 🟢 **LOW**: Minimal threat activity
            - 🟡 **MEDIUM**: Moderate threats
            - 🟠 **HIGH**: Significant threats
            - 🔴 **CRITICAL**: Severe threats
            """,
            
            "How often is data updated?": """
            - **CVE Data**: Real-time from NVD
            - **Reputation**: Real-time from feeds
            - **Attack Surface**: On-demand
            - **Dashboard KPIs**: Every 1 hour
            """,
            
            "What are the API keys for?": """
            Optional keys for enhanced features:
            - **AbuseIPDB**: IP reputation details
            - **VirusTotal**: File/domain analysis
            - **Shodan**: Device discovery
            
            Dashboard works without them!
            """,
            
            "How do I interpret CVSS scores?": """
            - **0.0**: No risk
            - **0.1-3.9**: Low
            - **4.0-6.9**: Medium
            - **7.0-8.9**: High
            - **9.0-10.0**: Critical
            """
        }
        
        for question, answer in faqs.items():
            with st.expander(question):
                st.markdown(answer)

module = HelpGuideModule()
