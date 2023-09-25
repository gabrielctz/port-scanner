<h1 align="center" id="title">Ports Scanner 📶</h1><br>

[![python version](https://img.shields.io/badge/Python-3.10%2B-brightgreen)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/License-GNU-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.fr.html)


# **Python Port Scanner Informations**
Cet outil en **pytho**n vous permettra de voir les **ports ouverts** sur un **NDD/Adresse IP**, il fonctionne à l'aide de **threads** ce qui accélère l'énumération. 

**Features of script**
- threads
- nmap features (pas tous)

## **🛠️ Requirements / Launch**

- [Python 3](https://www.python.org/downloads/)

```
git clone https://github.com/gabrielctz/Ports-Scanner.git
cd Port-Scanner
pip3 install -r requirements.txt
```

### Then just run the script 🔧

`python3 script.py 127.0.0.1 `

**Example of result:**
```
Scanning target: 127.0.0.1
Time started: 2023-09-25 19:48:55.655441
--------------------------------------------------
Port 135 | MS RPC | 127.0.0.1 (TCP)
Port 445 | Microsoft-DS (SMB) | 127.0.0.1 (TCP)
Port 2869 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 5040 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 6463 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 9010 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 9080 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 9100 | Printer (JetDirect) | 127.0.0.1 (TCP)
Port 9180 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 45654 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49664 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49665 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49666 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49667 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49668 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49683 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 49718 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 64246 | Service inconnu/privé. | 127.0.0.1 (TCP)
Port 65001 | Service inconnu/privé. | 127.0.0.1 (TCP)
```
