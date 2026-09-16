# Meraki Config Manager

A browser-based management tool for Cisco Meraki MX networks. Run it locally or in Docker — no cloud account required.

---

## Features

| Feature | Description |
|---|---|
| **Dashboard** | Network count, total VPN exclusion rules, org overview |
| **Networks** | Browse and search all MX networks in your organization |
| **VPN Exclusions** | View, import (CSV/XLSX/JSON), dry-run, and deploy split-tunnel rules |
| **Copy Rules** | Copy VPN exclusion rules across multiple networks with a 5-step wizard |
| **Group Policies** | Copy group policies across multiple networks with preview and conflict detection |
| **Compare Networks** | Side-by-side diff of VPN rules, SSIDs, and appliance settings |
| **New Network Wizard** | Create a new network cloned from a template in 6 guided steps |
| **Activity Log** | Timestamped log of every action taken during your session |

---

## Requirements

- Python **3.10+**
- A [Cisco Meraki Dashboard API key](https://developer.cisco.com/meraki/api-v1/authorization/)

---

## Quick Start

### macOS / Linux

```bash
git clone https://github.com/shayiqbal/client-meraki-web.git
cd client-meraki-web
bash run_web.sh
```

The script will:
1. Create a Python virtual environment (`.web_venv/`)
2. Install all dependencies
3. Start the server and open `http://localhost:8000` in your browser automatically

---

### Windows

```
git clone https://github.com/shayiqbal/client-meraki-web.git
cd client-meraki-web
run_web.bat
```

Double-click `run_web.bat` or run it from Command Prompt. Same steps as above.

---

### Docker

```bash
git clone https://github.com/shayiqbal/client-meraki-web.git
cd client-meraki-web
docker build -t meraki-config-manager .
docker run -p 8000:8000 meraki-config-manager
```

Then open `http://localhost:8000` in your browser.

---

## Usage

1. Open `http://localhost:8000`
2. Paste your **Meraki Dashboard API key** and click **Connect**
3. Select your **organization** from the dropdown in the top bar
4. Use the sidebar to navigate between features

---

## Security

- Your API key is validated live against the Meraki API on login
- It is held **in memory only** for the duration of your session — never written to disk or logged
- Sessions expire automatically after **8 hours** of inactivity
