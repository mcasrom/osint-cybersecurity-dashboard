#!/usr/bin/env python3
"""IP/Domain Reputation Checker"""

import requests
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReputationChecker:
    """Verifica reputacion de IPs y dominios"""
    
    def __init__(self, abuseipdb_key=None, virustotal_key=None):
        self.abuseipdb_key = abuseipdb_key
        self.virustotal_key = virustotal_key
        
    def check_abuseipdb(self, ip):
        """Consulta reputacion en AbuseIPDB"""
        if not self.abuseipdb_key:
            logger.warning("AbuseIPDB key not configured")
            return {"error": "No API key"}
            
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": self.abuseipdb_key,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 90,
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            data = response.json()["data"]
            return {
                "abuse_score": data["abuseConfidenceScore"],
                "total_reports": data["totalReports"],
                "last_reported": data["lastReportedAt"],
                "is_malicious": data["abuseConfidenceScore"] > 25
            }
        except Exception as e:
            logger.error(f"Error checking AbuseIPDB: {e}")
            return {"error": str(e)}
    
    def comprehensive_report(self, ip_or_domain):
        """Genera reporte completo"""
        report = {
            "target": ip_or_domain,
            "timestamp": datetime.now().isoformat(),
            "is_ip": self._is_ip(ip_or_domain),
            "reputation": {}
        }
        
        if report["is_ip"]:
            report["reputation"] = self.check_abuseipdb(ip_or_domain)
        
        return report
    
    @staticmethod
    def _is_ip(value):
        parts = value.split(".")
        return len(parts) == 4 and all(
            part.isdigit() and 0 <= int(part) <= 255 for part in parts
        )

if __name__ == "__main__":
    checker = ReputationChecker()
    report = checker.comprehensive_report("8.8.8.8")
    print(json.dumps(report, indent=2, default=str))
