#!/usr/bin/env python3
"""Methodology Documentation Module"""

import streamlit as st
import pandas as pd

class MethodologyModule:
    """Módulo de documentación y metodología"""
    
    def render(self):
        """Renderiza documentación completa"""
        st.header("📖 Methodology & Technical Approach")
        
        st.subheader("🎯 Our OSINT Strategy")
        st.markdown("""
        ### 1. **Data Collection Layer**
        - **CVE Monitoring**: Real-time collection from NVD
        - **Asset Discovery**: DNS enumeration, subdomain scanning
        - **Reputation Analysis**: Cross-checking against threat intel sources
        
        ### 2. **Processing & Analysis**
        - **Threat Scoring**: CVSS metrics calculation
        - **Pattern Recognition**: Exploit trend identification
        - **Risk Assessment**: Exposure quantification
        
        ### 3. **Visualization & Reporting**
        - **Interactive Dashboards**: Real-time KPI tracking
        - **Geospatial Analysis**: Threat actor mapping
        - **Trend Forecasting**: Predictive analysis
        
        ### 4. **Automation & Response**
        - **Alert Generation**: Critical vulnerability notifications
        - **Remediation Tracking**: Patch deployment monitoring
        - **Compliance Reporting**: Automated audit trails
        """)
        
        st.divider()
        
        st.subheader("🔬 Technical Stack")
        tech_stack = pd.DataFrame({
            'Component': ['Data Collection', 'Processing', 'Visualization', 'Backend', 'Deployment'],
            'Technology': ['Python + Requests', 'Pandas + NumPy', 'Plotly + Streamlit', 'FastAPI', 'Docker'],
            'Purpose': ['API queries', 'Data transformation', 'Interactive charts', 'API serving', 'Containerization']
        })
        st.dataframe(tech_stack, use_container_width=True)

module = MethodologyModule()
