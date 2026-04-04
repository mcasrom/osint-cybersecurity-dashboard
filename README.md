# SIGE OSINT - Privacy Tools

Enterprise‑grade OSINT and cybersecurity dashboard for real‑time threat intelligence, CVE monitoring, attack surface analysis, and reputation‑based threat detection.

## 🎯 Overview

**SIGE OSINT - Privacy Tools** is an open‑source, enterprise‑grade OSINT and cybersecurity dashboard built with Python and Streamlit. It helps SOC analysts, penetration testers, and OSINT researchers monitor:

- CVEs in real time
- Attack surface exposure
- Reputation‑based threats
- Botnet / malicious activity
- Public IP analysis (from the browser, not the server)

Designed for **local execution** on your own hardware (e.g., an Odroid or Linux server), but deployable on Streamlit Cloud for remote access.

---

## 📸 Screenshots

To keep the repo light, we avoid storing large screenshots directly here.  
If you want visual references, see the project in action in the Streamlit deployment:

👉 [https://share.streamlit.io/mcasrom/osint-cybersecurity-dashboard](https://share.streamlit.io/mcasrom/osint-cybersecurity-dashboard)

---

## 🧩 Features

### Home / Dashboard
- General KPIs: CVEs today, critical CVEs, exploitable vulnerabilities, threat level, and system health.
- `About` box that explains the purpose and target audience.

### Monitor
- **Dashboard**: Real‑time overview of detected threats and anomalies.
- **CVE Monitoring**: Watch for new CVEs relevant to your environment.
- **Attack Surface**: Analyze exposed systems and services.
- **Reputation**: Check IP/domain reputation and malicious history.
- **Botnets**: Botnet‑related IP checks and alerts.
- **IP Validator**: Basic IP validation and sanity checks.

### Analyze
- **Methodology**: Documentation of the OSINT methodology used.
- **Technical Docs**: API and internal module references.
- **Benchmarks**: Performance and usage benchmarks.

### Learn
- **Help Guide**: User‑oriented instructions and troubleshooting.
- **API Reference**: Documentation of internal API structures.

### Business
- **Use Cases**: Example scenarios and workflows for different roles.

### Configure
- **API Keys**: Centralized configuration for external services.
- **Settings**: General app settings and UI preferences.

---

## 🚀 Quick Start (Local)

Run this app on your own machine (e.g., Linux, Odroid, or Raspberry Pi):

```bash
# Clona el repositorio
git clone https://github.com/mcasrom/osint-cybersecurity-dashboard.git
cd osint-cybersecurity-dashboard

# Crea y activa el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la app
python app.py
```

Then open in your browser:

```text
http://localhost:8501
```

---

## ☁ Deployment on Streamlit Cloud

To deploy this app publicly, use Streamlit Cloud:

1. Fork or push this repo to your GitHub account.
2. Go to [https://share.streamlit.io](https://share.streamlit.io) and connect your GitHub repository.
3. Configure the main file as `app.py` and let it build.

The app will run in the cloud, but **for real client IP detection**, you must use the local‑hosted version or inject your IP manually into the Botnet module.

---

## 💡 Best Practices

- For **real IP / botnet checks**, run this app **locally** (not on Streamlit Cloud), where it can see your network IP directly.
- Use the **“Get Your Public IP (for Botnet Check)”** button in the `Home` tab to retrieve your IP from the browser when using the cloud version.
- Copy that IP and paste it into the **Botnets** tab for detailed analysis.

---

## 📦 Requirements

- Python 3.8+
- Streamlit
- `requests` (for public IP checks)
- Other dependencies listed in `requirements.txt`

---

## 📄 License

This project is licensed under the terms specified in the `LICENSE` file.

---

## 👤 Attribution

Author: **M. Castillo**  
Contact: <mailto:mybloggingnotes@gmail.com>
