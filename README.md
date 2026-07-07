# Bomber
SMS-Bomber | Created By : IHOSI
# 💣 BOMBER - OTP Attack Tool

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Android-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/APIs-40%2B-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

<p align="center">
  <b>⚡ A powerful, multi-threaded OTP bombing tool for security testing ⚡</b>
</p>

---

## 📌 What is BOMBER?

**BOMBER** is a high-performance, multi-threaded OTP (One-Time Password) bombing tool designed specifically for **security testing and educational purposes**. It simultaneously sends OTP requests to **40+ Iranian services** including major platforms like Snapp, Digikala, Divar, Tapsi, and many more.

> ⚠️ **DISCLAIMER:** This tool is created for **educational and authorized security testing ONLY**. Use it exclusively on numbers you own or have explicit written permission to test. The author (ihosi) is not responsible for any misuse, illegal activities, or damages caused by this tool.

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| ⚡ **0.1s Loop** | Continuous attacks every 0.1 seconds |
| 🚀 **Multi-Threaded** | 20 concurrent threads for maximum speed |
| 📱 **40+ Services** | Supports all major Iranian platforms |
| 💻 **Cross-Platform** | Works on Windows, Linux, macOS, Android |
| 📊 **Real-time Stats** | Live sent/failed/error counters |
| 🛑 **CTRL+C Support** | Stop anytime with keyboard interrupt |
| 🎨 **Beautiful UI** | Colorful terminal with animations |

---

## 📱 Supported Services (40+)

<details>
<summary><b>🖱️ Click to expand full list</b></summary>

| # | Service | # | Service | # | Service |
|---|---------|---|---------|---|---------|
| 1 | Snapp V1 | 15 | Tap33 | 29 | Khodro45 |
| 2 | Snapp V2 | 16 | Tapsi | 30 | Delino |
| 3 | Achareh | 17 | GapFilm | 31 | DigikalaJet |
| 4 | Zigap | 18 | IToll | 32 | Miare |
| 5 | Jabama | 19 | Anargift | 33 | Dosma |
| 6 | Banimode | 20 | Nobat | 34 | Ostadkr |
| 7 | Classino | 21 | Lendo | 35 | Sibbazar |
| 8 | Digikala V1 | 22 | Hamrah-Mechanic | 36 | Namava |
| 9 | Digikala V2 | 23 | Abantether | 37 | Shab |
| 10 | Sms.ir | 24 | OKCS | 38 | Bitpin |
| 11 | Alibaba | 25 | Tebinja | 39 | Taaghche |
| 12 | Divar | 26 | Bit24 | 40 | Rojashop |
| 13 | Sheypoor | 27 | Paklean | | |
| 14 | Bikoplus | 28 | Mootanroo | | |

**Total: 40+ Iranian services**

</details>

---

## 🚀 Installation Guide

### Quick Install (All Platforms)
```
```bash
git clone https://github.com/ihosi/Bomber.git
cd Bomber
pip install -r requirements.txt
python Bomber.py
```

---

### 💻 Windows

1. Download and install Python from [python.org](https://python.org)
2. Open Command Prompt (CMD) as Administrator
3. Run these commands:
```

```batch
git clone https://github.com/ihosi/Bomber.git
cd Bomber
pip install -r requirements.txt
run.bat
```

---

### 🐧 Linux / macOS
```
1. Open Terminal
2. Run these commands:

```bash
git clone https://github.com/ihosi/Bomber.git
cd Bomber
pip3 install -r requirements.txt
chmod +x run.sh
./run.sh
```

---
### 📱 Android (Termux)

1. Install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/)
2. Open Termux and run:
```

```bash
pkg update && pkg upgrade -y
pkg install python python-pip git -y
git clone https://github.com/ihosi/Bomber.git
cd Bomber
pip install -r requirements.txt
chmod +x termux-setup.sh
./termux-setup.sh

```
##  How to Use
```
**Step 1:** Run the tool
```bash
python Bomber.py
```

**Step 2:** Enter a phone number
```
➜ 09123456789
```

**Step 3:** Watch the attack in real-time
```
[1] 📤 Sent: 35 ❌ Failed: 3 ⚠ Error: 2 📊 Total: 40
[2] 📤 Sent: 38 ❌ Failed: 1 ⚠ Error: 1 📊 Total: 40
```

**Step 4:** Stop anytime
```
Press CTRL+C to stop
```

---

## 📊 Example Output

```
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

         ✦ OTP BOMBER TOOL ✦

Created by: ihosi
Version: 4.0 (Custom Loop Delay)
GitHub: github.com/ihosi/Bomber

────────────────────────────────────────────────────────────
⚡ BOMBER - OTP Attack Tool
👑 Creator: ihosi
🔄 Version: 4.0 (Custom Loop Delay)
⏱  You choose the delay between attacks!
Press CTRL+C to stop
────────────────────────────────────────────────────────────

[1] 📤 Sent: 35 ❌ Failed: 3 ⚠ Error: 2 📊 Total: 40 ⏱ Delay: 0.5s
[2] 📤 Sent: 38 ❌ Failed: 1 ⚠ Error: 1 📊 Total: 40 ⏱ Delay: 0.5s
[3] 📤 Sent: 40 ❌ Failed: 0 ⚠ Error: 0 📊 Total: 40 ⏱ Delay: 0.5s
---
```
## 🛠️ Requirements
```
- Python 3.6 or higher
- pip (Python package manager)
- Internet connection
```
### Dependencies
```
requests>=2.31.0
colorama>=0.4.6


```
## ⚠️ Legal Disclaimer
```
> **IMPORTANT NOTICE:**
>
> This tool is provided for **educational and authorized security testing purposes only**.
>
> **✅ DO:**
> - Use on numbers you own
> - Use with explicit written permission
> - Use for security testing and research
>
> **❌ DON'T:**
> - Harass or annoy others
> - Spam phone numbers
> - Use for illegal activities
>
> **The author (ihosi) is not responsible for any misuse.**

---
```
## 📝 License
```

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
## 📊 Example Output

```
**ihosi**
- GitHub: [@ihosi](https://github.com/ihosi)
- Project: [Bomber](https://github.com/ihosi/Bomber)
```
## 🌟 Support

```
If you find this tool useful, please give it a ⭐ on GitHub!
|-------------------------|
**Made with ❤️ by ihosi**
|-------------------------|
