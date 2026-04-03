#!/usr/bin/env python3
"""Reputation Analysis Module"""

import streamlit as st
import pandas as pd
from scripts.data_collection.reputation_checker import ReputationChecker

class ReputationAnalyzer:
    """Módulo para análisis de reputación"""
    
    def __init__(self):
        self.checker = ReputationChecker()
    
    def render(self):
        """Renderiza interfaz de verificación"""
        st.header("🔍 IP/Domain Reputation Check")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            target = st.text_input("Enter IP or Domain:", value="8.8.8.8")
        with col2:
            if st.button("📊 Check", key="check_reputation"):
                self._check_reputation(target)
        
        st.divider()
        
        # Reputation Summary
        self._display_reputation_summary()
    
    def _check_reputation(self, target):
        """Verifica reputación"""
        try:
            report = self.checker.comprehensive_report(target)
            st.success("✅ Check completed!")
            st.json(report)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    def _display_reputation_summary(self):
        """Muestra resumen de reputaciones"""
        st.subheader("Recent Reputation Checks")
        
        rep_data = pd.DataFrame({
            'Target': ['8.8.8.8', '1.1.1.1', 'google.com', 'cloudflare.com', 'malicious-site.xyz'],
            'Type': ['IP', 'IP', 'Domain', 'Domain', 'Domain'],
            'Reputation': ['CLEAN', 'CLEAN', 'TRUSTED', 'TRUSTED', 'MALICIOUS'],
            'Score': [0, 0, 100, 95, -50],
            'Threats': [0, 0, 0, 0, 12],
            'Last Checked': ['2 hours ago', '5 hours ago', '1 day ago', '2 days ago', '3 days ago']
        })
        
        st.dataframe(rep_data, use_container_width=True)

# Export
analyzer = ReputationAnalyzer()
