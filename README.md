# 🌐 Domain Expiry Checker

A simple and efficient Python script to check the expiration status of domains listed in `domains.txt`. The results are saved in `done.txt`, with a 4-second delay between each check. ⏳

## 🚀 Made by
[🔗 emailnightmare.com](https://emailnightmare.com)

## ✨ Features
✅ Checks domain expiration date
✅ Outputs results to `done.txt`
✅ Waits 4 seconds between each check to avoid rate limits

## 🛠️ Installation

### 📌 Prerequisites
Ensure you have Python installed. You also need the `whois` module, which you can install using:

```sh
pip install python-whois
```

## 🎯 Usage
1️⃣ Place your domains in `domains.txt` (one per line). 📄
2️⃣ Run the script: 🏃‍♂️

```sh
python check_domain_expiry.py
```

3️⃣ The results will be printed in the terminal and saved in `done.txt`. 📜

## 📌 Example Output
```
🌐 Made by https://emailnightmare.com
✅ example.com - Expires on: 2025-06-15
❌ anotherdomain.com - Error: No whois data found
```

## 📜 License
This script is provided as-is with no warranty. Feel free to modify and use it. 🛠️

