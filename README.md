# 🌐 Basic Port Scanner

A Python-based TCP port scanner designed for basic network security analysis and learning socket programming fundamentals.

---

## 📌 Project Overview

The Basic Port Scanner scans a target system (IP address or domain) for open TCP ports within a specified range.

It demonstrates:

- Socket programming
- Network communication basics
- Port scanning logic
- Exception handling
- Scan time calculation

This project is built for educational and cybersecurity learning purposes.

---

## 🚀 Features

- Scans ports from 1–100 (customizable)
- Accepts domain name or IP address
- Detects open ports
- Identifies closed ports
- Displays total scan duration
- Lightweight and fast execution
- Error handling for invalid hostnames

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Datetime Module
- Exception Handling
- Networking Fundamentals

---

## 📂 Project Structure

basic-port-scanner/
│
├── scanner.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/Jithendra1828/basic-port-scanner.git

### 2️⃣ Navigate to Project Folder

cd basic-port-scanner

### 3️⃣ Install Dependencies (if required)

pip install -r requirements.txt

### 4️⃣ Run the Scanner

python scanner.py

---

## 🧠 How It Works

1. The user enters a target IP address or domain name.
2. The program resolves the hostname to an IP address.
3. It attempts TCP connections on ports 1–100.
4. If the connection succeeds → Port is Open.
5. If the connection fails → Port is Closed.
6. Total scan time is calculated and displayed.

---

## 📌 Example Output

Enter target: scanme.nmap.org

Scanning Target: 45.33.xx.xx  
Scanning first 100 ports...

Port 22: Open  
Port 80: Open  
Port 443: Open  

Scan Completed Successfully  
Total Time: 2.35 seconds

---

## ⚠️ Disclaimer

This tool is developed strictly for educational purposes.  
Do not scan systems without proper authorization.

---

## 🎯 Learning Outcomes

- Understanding TCP connections
- Working with sockets in Python
- Implementing port scanning logic
- Basic network security concepts

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, feel free to star the repository!
