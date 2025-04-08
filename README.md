# Async IP Lookup Tool

An asynchronous Python utility to perform IP lookups using the `ip-api.com` service. This tool reads IP addresses from an Excel file, queries the API concurrently using `aiohttp`, and saves enriched data (ASN, ISP, Country, State) into a new Excel file.

---

## 🚀 Features

- 🔄 Asynchronous IP lookup with retry mechanism
- 📊 Excel (.xlsx) input/output support
- 🔍 Enriches IPs with ASN, ISP, Country, State
- 📁 Modular and extensible project structure
- 🧾 Configurable settings via `config.py`
- 🪵 Structured logging with timestamps and module-level granularity

---

## 🧱 Project Structure

