# z3r0sec WordPress Paths Checker

![z3r0sec](https://img.shields.io/badge/made%20by-z3r0sec-red?style=for-the-badge)

A simple Python tool to enumerate common sensitive WordPress paths that may expose important files or directories.

---

## 🚀 Features

- Check common WordPress sensitive paths like `wp-login.php`, `wp-config.php`, `.htaccess`, `backup.zip`, and more.
- Detect if the paths are accessible (`200 OK`), forbidden (`403 Forbidden`), or redirected (`301/302 Redirect`).
- Easy to use and lightweight.

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

You can install the requirements using:

```bash
pip install -r requirements.txt
```
## Usage 

```bash 
python wp_paths_checker.py -u <target-url>
```

