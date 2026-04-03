#!/usr/bin/env python3
"""External Attack Surface Scanner"""

import socket
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExternalAttackSurface:
    """Escanea la superficie de ataque externa"""
    
    def __init__(self, domain):
        self.domain = domain
        self.results = {}
        
    def resolve_domain(self):
        """Resuelve IPs del dominio"""
        try:
            ips = socket.getaddrinfo(self.domain, None)
            return list(set([ip[4][0] for ip in ips]))
        except Exception as e:
            logger.error(f"Error resolving domain: {e}")
            return []
    
    def scan_subdomains(self):
        """Enumera subdominios usando CT Logs"""
        url = f"https://crt.sh/?q=%.{self.domain}&output=json"
        try:
            response = requests.get(url, timeout=10)
            certs = response.json()
            subdomains = set()
            for cert in certs:
                names = cert.get("name_value", "").split("\n")
                subdomains.update(names)
            logger.info(f"Found {len(subdomains)} subdomains")
            return list(subdomains)
        except Exception as e:
            logger.error(f"Error scanning subdomains: {e}")
            return []
    
    def scan_ports(self, ip, ports=[80, 443, 22, 3306, 5432, 8080]):
        """Escanea puertos comunes"""
        open_ports = []
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                pass
        return open_ports
    
    def full_scan(self):
        """Ejecuta analisis completo"""
        logger.info(f"Starting scan for {self.domain}")
        
        ips = self.resolve_domain()
        logger.info(f"IPs found: {ips}")
        
        subdomains = self.scan_subdomains()
        logger.info(f"Subdomains found: {len(subdomains)}")
        
        results = {
            "domain": self.domain,
            "ips": ips,
            "subdomains": subdomains[:50],
            "infrastructure": {}
        }
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {}
            for ip in ips[:5]:
                futures[executor.submit(self.scan_ports, ip)] = ip
            
            for future in as_completed(futures):
                ip = futures[future]
                open_ports = future.result()
                results["infrastructure"][ip] = {
                    "open_ports": open_ports
                }
        
        return results

if __name__ == "__main__":
    scanner = ExternalAttackSurface("example.com")
    results = scanner.full_scan()
    print(json.dumps(results, indent=2))
