#!/usr/bin/env python3
"""Secure API Key Storage"""

import os
import streamlit as st

class SecureStorage:
    """Almacenamiento seguro de API keys"""
    
    def __init__(self):
        self.env_file = ".env"
    
    def save_secure(self, api_name, api_key):
        """Guarda API key de forma segura"""
        
        from modules.security.key_validator import validator
        
        is_valid, msg = validator.validate_key_format(api_name, api_key)
        
        if not is_valid:
            return False, msg
        
        api_key = validator.sanitize_key(api_key)
        
        if not validator.is_key_safe(api_key):
            return False, "Key contains suspicious characters"
        
        try:
            env_content = ""
            if os.path.exists(self.env_file):
                with open(self.env_file, 'r') as f:
                    env_content = f.read()
            
            lines = env_content.split('\n')
            lines = [l for l in lines if not l.startswith(f"{api_name.upper()}=")]
            lines.append(f"{api_name.upper()}={api_key}")
            
            with open(self.env_file, 'w') as f:
                f.write('\n'.join(lines))
            
            os.chmod(self.env_file, 0o600)
            
            return True, "Key saved securely"
        
        except Exception as e:
            return False, f"Error saving key: {str(e)}"
    
    def get_key(self, api_name):
        """Obtiene API key de forma segura"""
        try:
            if os.path.exists(self.env_file):
                with open(self.env_file, 'r') as f:
                    for line in f:
                        if line.startswith(f"{api_name.upper()}="):
                            return line.split('=')[1].strip()
            return None
        except:
            return None
    
    def list_configured_keys(self):
        """Lista todas las keys configuradas"""
        configured = []
        
        if os.path.exists(self.env_file):
            with open(self.env_file, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key_name = line.split('=')[0]
                        configured.append(key_name)
        
        return configured

secure_storage = SecureStorage()
