#!/usr/bin/env python3
"""Settings & Preferences Page"""

import streamlit as st

class SettingsPage:
    """Página de configuración y preferencias"""
    
    @staticmethod
    def render():
        """Renderiza página de configuración"""
        st.header("⚙️ Settings & Preferences")
        
        st.divider()
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎨 Appearance",
            "📊 Dashboard",
            "🔔 Notifications",
            "📈 Advanced"
        ])
        
        with tab1:
            SettingsPage._render_appearance()
        
        with tab2:
            SettingsPage._render_dashboard_settings()
        
        with tab3:
            SettingsPage._render_notification_settings()
        
        with tab4:
            SettingsPage._render_advanced_settings()
    
    @staticmethod
    def _render_appearance():
        """Configuración de apariencia"""
        st.subheader("🎨 Appearance Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            theme = st.selectbox("Theme", ["Light", "Dark", "Auto"], index=1)
        
        with col2:
            primary_color = st.color_picker("Primary Color", value="#1e40af")
        
        st.divider()
        
        font_size = st.slider("Font Size", min_value=10, max_value=20, value=14, step=1)
        
        st.divider()
        
        st.subheader("Chart Settings")
        chart_theme = st.selectbox("Chart Theme", ["Plotly", "Plotly Dark", "ggplot2"], index=0)
        animation = st.checkbox("Enable Animations", value=True)
        
        if st.button("💾 Save Appearance Settings"):
            st.success("✅ Settings saved!")
    
    @staticmethod
    def _render_dashboard_settings():
        """Configuración del dashboard"""
        st.subheader("📊 Dashboard Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            refresh = st.selectbox("Auto-refresh", ["Disabled", "30s", "1m", "5m"], index=3)
        
        with col2:
            default_view = st.selectbox("Default View", ["Dashboard", "CVE Monitoring"], index=0)
        
        st.divider()
        
        show_minimap = st.checkbox("Show Minimap", value=True)
        show_grid = st.checkbox("Show Grid", value=False)
        
        if st.button("💾 Save Dashboard Settings"):
            st.success("✅ Saved!")
    
    @staticmethod
    def _render_notification_settings():
        """Configuración de notificaciones"""
        st.subheader("🔔 Notification Settings")
        
        critical = st.checkbox("Critical Alerts", value=True)
        high = st.checkbox("High Alerts", value=True)
        
        st.divider()
        
        email = st.checkbox("Email Notifications", value=True)
        if email:
            st.text_input("Email Address", placeholder="your@email.com")
        
        if st.button("💾 Save Notification Settings"):
            st.success("✅ Saved!")
    
    @staticmethod
    def _render_advanced_settings():
        """Configuración avanzada"""
        st.subheader("📈 Advanced Settings")
        
        cache_size = st.slider("Cache Size (MB)", min_value=10, max_value=500, value=100)
        max_workers = st.slider("Max Workers", min_value=1, max_value=8, value=4)
        
        st.divider()
        
        debug_mode = st.checkbox("Debug Mode", value=False)
        
        if st.button("💾 Save Advanced Settings"):
            st.success("✅ Saved!")

settings = SettingsPage()
