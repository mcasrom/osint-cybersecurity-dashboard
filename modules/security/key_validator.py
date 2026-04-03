#!/usr/bin/env python3
"""API Key Security and Validation"""

import streamlit as st
import re

class KeyValidator:
    """Validador de seguridad para API keys"""
    
    @staticmethod
    def validate_key_format(api_name, api_key):
        """Valida formato de API key"""
        
        patterns = {
            'abuseipdb': r'^[a-f0-9]{64}$',
            'virustotal': r'^[a-f0-9]{64}$',
            'shodan': r'^[a-zA-Z0-9]{32,}$',
            'censys_id': r'^[a-zA-Z0-9]{32,}$',
            'censys_secret': r'^[a-zA-Z0-9]{64,}$'
        }
        
        if api_name.lower() not in patterns:
            return False, "Unknown API service"
        
        pattern = patterns[api_name.lower()]
        
        if not re.match(pattern, api_key):
            return False, f"Invalid key format for {api_name}"
        
        if len(api_key) > 512:
            return False, "API key too long"
        
        suspicious = [';', '|', '&', '`', '$', '(', ')']
        if any(char in api_key for char in suspicious):
            return False, "Suspicious characters detected"
        
        return True, "Valid key format"
    
    @staticmethod
    def sanitize_key(api_key):
        """Sanitiza API key"""
        api_key = api_key.strip()
        api_key = api_key.replace('\n', '')
        api_key = api_key.replace('\r', '')
        return api_key
    
    @staticmethod
    def is_key_safe(api_key):
        """Verifica si la key es segura"""
        
        dangerous_chars = [';', '|', '&', '`', '$', '(', ')', 
                          '{', '}', '[', ']', '<', '>', '\\']
        
        for char in dangerous_chars:
            if char in api_key:
                return False
        
        if len(api_key) < 20 or len(api_key) > 512:
            return False
        
        return True

validator = KeyValidator()
