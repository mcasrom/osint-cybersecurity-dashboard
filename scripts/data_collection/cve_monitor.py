#!/usr/bin/env python3
"""CVE Real-time Threat Monitor"""

import requests
import json
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CVEMonitor:
    """Monitorea vulnerabilidades CVE en tiempo real"""
    
    def __init__(self, api_key=None):
        self.nvd_url = "https://services.nvacenter.org/rest/json/cves/2.0"
        self.shodan_url = "https://api.shodan.io"
        self.shodan_key = api_key
        
    def fetch_trending_cves(self, days=7):
        """Obtiene CVEs de los ultimos N dias"""
        start_date = (datetime.now() - timedelta(days=days)).isoformat()
        params = {
            "pubStartDate": start_date,
            "resultsPerPage": 100,
            "startIndex": 0
        }
        
        try:
            response = requests.get(self.nvd_url, params=params, timeout=10)
            cves = response.json().get("vulnerabilities", [])
            logger.info(f"Fetched {len(cves)} CVEs from NVD")
            return sorted(cves, 
                         key=lambda x: x["cve"]["metrics"].get("cvssV3", {}).get("baseSeverity", "UNKNOWN"),
                         reverse=True)
        except Exception as e:
            logger.error(f"Error fetching CVEs: {e}")
            return []
    
    def filter_by_severity(self, cves, min_score=7.0):
        """Filtra solo CVEs criticos/altos"""
        critical = []
        for cve in cves:
            try:
                severity = cve["cve"]["metrics"]["cvssV3"]["baseSeverity"]
                score = cve["cve"]["metrics"]["cvssV3"]["baseScore"]
                if score >= min_score:
                    critical.append({
                        "id": cve["cve"]["id"],
                        "description": cve["cve"]["descriptions"][0]["value"][:100],
                        "score": score,
                        "severity": severity,
                        "date": cve["cve"]["published"]
                    })
            except:
                continue
        return critical
    
    def dashboard_data(self):
        """Retorna datos formateados para dashboard"""
        cves = self.fetch_trending_cves(days=7)
        critical = self.filter_by_severity(cves, min_score=7.0)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_new_cves": len(cves),
            "critical_count": len(critical),
            "critical_cves": critical[:20],
            "top_severity": critical[0] if critical else None
        }

if __name__ == "__main__":
    monitor = CVEMonitor()
    data = monitor.dashboard_data()
    print(json.dumps(data, indent=2, default=str))
