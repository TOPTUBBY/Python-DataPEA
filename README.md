# 📊 Python-DataPEA

<p align="center">
  <strong>Engineering CSV Plotting · Evaluation · Analysis</strong><br>
  <strong>เครื่องมือวิเคราะห์และพล็อตข้อมูล CSV สำหรับงาน Engineering / Test / Validation</strong>
</p>

<p align="center">
  <a href="http://127.0.0.1:8800"><img alt="Open DataPEA" src="https://img.shields.io/badge/🌐_OPEN-DataPEA-0A7EA4?style=for-the-badge"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://fastapi.tiangolo.com/"><img alt="FastAPI" src="https://img.shields.io/badge/FRAMEWORK-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"></a>
  <a href="https://plotly.com/python/"><img alt="Plotly" src="https://img.shields.io/badge/PLOT-Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"></a>
</p>

<p align="center">
  <a href="./VERSION_HISTORY.md"><img alt="Version" src="https://img.shields.io/badge/VERSION-V4.4.5-2F80ED?style=flat-square"></a>
  <a href="http://127.0.0.1:8800"><img alt="LAN Port" src="https://img.shields.io/badge/WEB_PORT-8800-7B61FF?style=flat-square"></a>
  <img alt="Status" src="https://img.shields.io/badge/STATUS-ACTIVE-2EA043?style=flat-square">
  <img alt="Cloud" src="https://img.shields.io/badge/CLOUD-NOT_REQUIRED-555?style=flat-square">
  <a href="./LICENSE"><img alt="License" src="https://img.shields.io/badge/LICENSE-MIT-2EA043?style=flat-square"></a>
</p>

<p align="center">
  <a href="#-english">🇬🇧 English</a> ·
  <a href="#-ภาษาไทย">🇹🇭 ภาษาไทย</a> ·
  <a href="#-quick-start--เริ่มต้นใช้งาน">🚀 Quick Start</a> ·
  <a href="./PRESET_FORMAT_V1.md">🧩 Preset Format</a> ·
  <a href="./VERSION_HISTORY.md">🕘 Version History</a>
</p>

---

> [!TIP]
> **🌐 The “OPEN DataPEA” badge is a real link to the Web UI at `http://127.0.0.1:8800`.**  
> It works after DataPEA has been started on the **same PC**. For another PC on the LAN, use `http://<SERVER-IP>:8800`.
>
> **ปุ่ม “OPEN DataPEA” ด้านบนลิงก์ไปยัง Web UI จริงที่ `http://127.0.0.1:8800`**  
> โดยต้องเปิด DataPEA Server บนเครื่องนั้นก่อน ส่วนเครื่องอื่นใน LAN ให้ใช้ `http://<SERVER-IP>:8800`

---

## 🇬🇧 English

### What is Python-DataPEA?

**Python-DataPEA** is a portable, browser-based engineering data analysis tool designed for **CSV log files** from testing, validation, qualification, laboratory, environmental, automotive, and general engineering workflows.

Instead of manually preparing graphs in spreadsheet software every time, DataPEA provides a repeatable workflow for loading CSV files, selecting signals, configuring axes, inspecting data, adding engineering limits and comments, analyzing temperature cycles, and exporting professional reports.

The current baseline is **V4.4.5.2026**, using **TCP port 8800** by default.

### ✨ Why DataPEA?

- 🌐 **Browser-based UI** — no desktop GUI framework required.
- 🔒 **Local / LAN operation** — no cloud dependency for normal use.
- 📈 **Interactive plotting** — zoom, pan, autoscale, hover and legend controls.
- 📂 **Multi-file CSV binding** — combine sequential logger files into one dataset.
- 🧠 **Smart CSV header detection** — automatically finds common timestamp/header rows.
- ↔️ **Dual Y axes** — Primary / Secondary axis assignment per signal.
- 🎯 **Cursor A/B analysis** — Delta Time, Delta Value, Min, Max, Average and sample count.
- 🚧 **Engineering annotations** — reference lines, tolerance bands and graph comments.
- 🌡️ **Cycle Analysis** — Temperature Cycling and Thermal Shock workflows.
- 💾 **Reusable presets** — save and reuse signal/axis/limit configuration.
- 📄 **Professional export** — PNG, PDF, Word and CSV outputs.
- 🖥️ **Local, LAN and dedicated-server launchers** included.

---

## 🇹🇭 ภาษาไทย

### Python-DataPEA คืออะไร?

**Python-DataPEA** คือเครื่องมือสำหรับ **พล็อต วิเคราะห์ และประเมินข้อมูล CSV ผ่าน Web Browser** โดยออกแบบมาให้เหมาะกับงาน Engineering เช่นงาน **Test, Validation, Qualification, Laboratory, Environmental Test และ Automotive Test**

จุดประสงค์หลักคือช่วยลดขั้นตอนการนำข้อมูลจาก Logger ไปสร้างกราฟด้วยโปรแกรม Spreadsheet ซ้ำ ๆ ทุกครั้ง ผู้ใช้สามารถโหลดไฟล์ CSV เลือก Signal จัดแกนกราฟ วิเคราะห์ช่วงข้อมูล ใส่ Limit/Comment วิเคราะห์ Cycle และ Export Report ได้ภายในเครื่องมือเดียว

Baseline ปัจจุบันคือ **V4.4.5.2026** และใช้ **TCP Port 8800** เป็นค่าเริ่มต้น

### ✨ จุดเด่นของ DataPEA

- 🌐 **ใช้งานผ่าน Web Browser** — ไม่ต้องพึ่ง Desktop GUI
- 🔒 **ทำงานแบบ Local / LAN** — การใช้งานปกติไม่จำเป็นต้องส่งข้อมูลขึ้น Cloud
- 📈 **กราฟ Interactive** — Zoom, Pan, Autoscale, Hover และควบคุม Legend ได้
- 📂 **รวม CSV หลายไฟล์** — เหมาะกับ Logger ที่แบ่งข้อมูลออกเป็นหลายไฟล์ต่อเนื่อง
- 🧠 **Smart Header Detection** — ตรวจหาบรรทัด Header/Timestamp ให้อัตโนมัติ
- ↔️ **รองรับแกน Y สองฝั่ง** — Primary / Secondary แยกตาม Signal
- 🎯 **Cursor A/B** — วิเคราะห์ Delta Time, Delta Value, Min, Max, Average และจำนวน Sample
- 🚧 **Annotation สำหรับงาน Engineering** — Limit Line, Tolerance Band และ Comment
- 🌡️ **Cycle Analysis** — รองรับ Temperature Cycling และ Thermal Shock
- 💾 **Preset** — บันทึกการเลือก Signal, Axis, สี และ Limit ไว้ใช้ซ้ำ
- 📄 **Export Report** — PNG, PDF, Word และ CSV
- 🖥️ มี **Launcher สำหรับ Local, LAN และ Dedicated Server** พร้อมใช้งาน

---

## 🧭 Feature Overview / ภาพรวมฟังก์ชัน

| Feature | English | ภาษาไทย |
|---|---|---|
| 📈 Interactive Plot | Zoom, pan, hover, autoscale, legend control | ซูม เลื่อนกราฟ ดูค่าด้วยเมาส์ และควบคุม Signal จาก Legend |
| 📂 Multi-file Bind | Merge sequential CSV logs into one dataset | รวมไฟล์ CSV ต่อเนื่องหลายไฟล์เป็นข้อมูลชุดเดียว |
| 🧠 Smart Header | Detect common CSV timestamp/header markers | ตรวจหา Header และ Timestamp อัตโนมัติ |
| ↔️ Dual Y Axis | Primary / Secondary Y axis per signal | กำหนด Signal ไปยังแกน Y ซ้าย/ขวา |
| 🎯 Cursor A/B | A/B values, ΔTime, ΔValue, statistics | เปรียบเทียบค่า A/B, ΔTime, ΔValue และ Statistics |
| 📊 Statistics | Min, Max, Average, sample count | Min, Max, Average และจำนวน Sample |
| 🚧 Annotation | Reference line, limit band, comments | เส้น Limit, ช่วง Tolerance และ Comment |
| 🌡️ Cycle Analysis | Temp Cycling / Thermal Shock | วิเคราะห์รอบ Temperature Cycling / Thermal Shock |
| 💾 Preset | Reusable plotting configuration | บันทึก Configuration เพื่อนำกลับมาใช้ซ้ำ |
| 📄 Report Export | PNG, Wide PDF, A4 PDF, Word, CSV | Export PNG, PDF, Word และ CSV |
| 🌗 Theme | Light / Dark toggle | สลับ Light / Dark Theme |
| 🖥️ Deployment | Local, LAN, dedicated server | ใช้งานเครื่องเดียว, ผ่าน LAN หรือ Dedicated Server |

---

## 📈 Interactive Plotting / การใช้งานกราฟ

DataPEA uses an **offline Plotly-based interactive graph** served by the Python WebServer.

DataPEA ใช้กราฟ Interactive จาก Plotly ซึ่งให้บริการโดย Python WebServer และสามารถทำงานในระบบ Local/LAN ได้

Supported interactions include:

- 🖱️ Mouse-wheel zoom
- 🔍 Drag zoom
- ✋ Pan
- ♻️ Autoscale / Reset View
- 🧭 Hover inspection
- 👁️ Show / hide individual traces
- 🎨 Automatic or manual trace colors
- 🗂️ Up to **8 independent plot pages**
- ↔️ Primary and Secondary Y axes

---

## 📂 Multi-file CSV Binding / การรวม CSV หลายไฟล์

V4.4.5 supports selecting multiple CSV files and binding them before plotting.

V4.4.5 รองรับการเลือก CSV หลายไฟล์และรวมข้อมูลก่อนนำไป Plot

### Workflow

```text
Choose CSV files
      │
      ▼
Confirm selected files
      │
      ▼
Initial order by Last Modified
      │
      ├── Drag & Drop to reorder if required
      │
      ▼
Bind Data
      │
      ▼
Validate columns / headers
      │
      ▼
Load Bound CSV ─────► Plot / Analyze / Export
      │
      └──────────────► Download Bound CSV
```

DataPEA keeps the first file's header/metadata and appends only data rows from subsequent compatible files.

DataPEA จะเก็บ Header/Metadata จากไฟล์แรก และนำเฉพาะ Data Row ของไฟล์ถัดไปมาต่อกัน โดยตรวจสอบชื่อและลำดับ Column ก่อน Bind

> [!NOTE]
> Web browsers do not expose Windows **Creation Time** through the normal File API. Initial ordering therefore uses **Last Modified**, and the user can correct the sequence with drag-and-drop.
>
> Browser ไม่สามารถอ่าน Windows **Creation Time** ผ่าน File API ปกติได้ จึงใช้ **Last Modified** สำหรับเรียงลำดับเริ่มต้น และผู้ใช้สามารถ Drag & Drop เพื่อจัดลำดับใหม่ได้

---

## 🧠 Smart CSV Header Detection

DataPEA can automatically locate a CSV header using common first-column markers:

- `Timestamp`
- `Date&Time`
- `Date`
- `Time`

If no supported marker is found, a normal CSV can fall back to the first row.

ระบบสามารถตรวจหา Header จากคำที่ใช้บ่อยใน Logger โดยอัตโนมัติ หากไม่พบ Marker ที่รองรับ จะใช้แถวแรกเป็น Header ตามรูปแบบ CSV ทั่วไป

---

## 🎯 Cursor A/B & Statistics

Cursor A/B is intended for quick engineering comparison of two points or a selected time interval.

Cursor A/B เหมาะสำหรับวิเคราะห์ความแตกต่างของข้อมูลสองจุด หรือวิเคราะห์ข้อมูลภายในช่วงเวลาที่เลือก

Available results include:

- Cursor A value
- Cursor B value
- **ΔTime / ΔX**
- **ΔValue**
- **Min**
- **Max**
- **Average**
- Sample count

Statistics can follow the Cursor A↔B interval or the current zoom range.

---

## 🚧 Engineering Annotation & Limits

DataPEA supports engineering markup directly on the graph:

- 🔴 Reference / Limit lines
- 🟢 Acceptance / Tolerance range bands
- 💬 Graph comments
- 🎨 Configurable colors
- ┄ Line styles and widths
- 👁️ Show / hide controls
- ↔️ Primary / Secondary Y-axis targeting
- 🖱️ Drag editing on the Plotly graph

ช่วยให้ผู้ใช้สามารถใส่ Requirement, Limit, Tolerance และ Comment ลงบนกราฟเพื่อใช้ Review หรือจัดทำ Report ได้โดยตรง

---

## 🌡️ Cycle Analysis

Cycle Analysis supports three profile modes:

| Mode | Use case / การใช้งาน |
|---|---|
| 🤖 **Auto** | Automatically selects the most suitable profile logic / เลือกวิธีวิเคราะห์ให้อัตโนมัติ |
| 🌡️ **Temperature Cycling** | Slow-ramp chamber profiles / งาน Chamber ที่มีการ Ramp อุณหภูมิ |
| ⚡ **Thermal Shock** | Fast transitions between hot/cold plateaus / งาน Thermal Shock ที่เปลี่ยนอุณหภูมิรวดเร็ว |

Calculated results include:

- Complete cycle count
- Tmin / Tmax
- Average Tmin soak
- Average Tmax soak
- Average cycle duration
- Per-cycle result table
- Cycle Analysis CSV export

Thermal Shock mode uses dominant plateau detection so short overshoot peaks do not automatically become the soak temperature reference.

---

## 📄 Export & Reporting / การ Export Report

DataPEA can export:

- 🖼️ **PNG** plot image
- 📑 **Custom Wide PDF** — 1200 × 650 pt per report page
- 📄 **A4 Landscape PDF**
- 📝 **A4 Landscape Word**
- 📊 **Cycle Analysis CSV**
- 📂 **Bound CSV**
- 🧩 **`.preset`** plotting configuration

Report pages can be selected before export.

สามารถเลือกหน้า Plot ที่ต้องการก่อน Export เพื่อลด Report ที่ไม่จำเป็น

---

## 🧩 Preset System

A DataPEA `.preset` file can store reusable plotting configuration such as:

- Selected signals
- Primary / Secondary axis assignment
- Axis labels and ranges
- Manual trace colors
- Reference lines
- Range bands

ไฟล์ `.preset` เหมาะสำหรับ Test Setup ที่ต้องใช้ Signal และ Limit เดิมซ้ำหลายครั้ง ช่วยลดเวลาการตั้งค่ากราฟใหม่

📘 See / อ่านเพิ่มเติม: **[PRESET_FORMAT_V1.md](./PRESET_FORMAT_V1.md)**

---

## 🌗 Theme

The Web UI provides a compact **Light / Dark toggle**.

When a new browser session opens, DataPEA automatically starts from the Windows/browser preferred theme. If the user changes Light/Dark manually, that choice is kept for the current browser session.

เมื่อเปิด Browser Session ใหม่ ระบบจะเริ่มต้นตาม Theme ของ Windows/Browser อัตโนมัติ จากนั้นผู้ใช้สามารถสลับ Light/Dark ได้จาก Toggle

---

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3 |
| ⚡ Web Framework | FastAPI |
| 🚀 ASGI Server | Uvicorn |
| 📈 Interactive Plot | Plotly |
| 🖼️ Static / Report Plot | Matplotlib |
| 🧮 Data Processing | pandas + NumPy |
| 📝 Word Report | python-docx |
| 🌐 Frontend | Embedded HTML + CSS + JavaScript |
| 🔌 Default Port | **8800** |
| ☁️ Cloud Required | **No** |
| 🖥️ LAN Support | **Yes** |

---

## 🚀 Quick Start / เริ่มต้นใช้งาน

### 1. Requirements / สิ่งที่ต้องมี

- Windows PC
- Python 3
- Web browser
- Internet connection is needed only when installing Python libraries for the first time

หลังติดตั้ง Library แล้ว การใช้งาน DataPEA ปกติสามารถทำงานแบบ Local/LAN ได้โดยไม่ต้องพึ่ง Cloud

### 2. Install Python libraries / ติดตั้ง Library

#### Recommended for Windows

Double-click / เปิดไฟล์:

```text
lib_install.bat
```

or use pip:

```bash
python -m pip install -r requirements.txt
```

### 3. Start Local mode / ใช้งานเครื่องเดียว

Run:

```text
Launcher\Stable\Start_Local.bat
```

Then click / เปิด:

**[🌐 http://127.0.0.1:8800](http://127.0.0.1:8800)**

### 4. Start LAN mode / ใช้งานผ่าน LAN

Run:

```text
Launcher\Stable\Start_LAN.bat
```

Client PCs open:

```text
http://<SERVER-IP>:8800
```

Example:

```text
http://192.168.1.100:8800
```

If Windows Firewall blocks the connection, run once as Administrator:

```text
Launcher\LAN_Setup\Allow_GraphPlot_Port_8800_Firewall.bat
```

### 5. Dedicated Server mode

For a PC that should keep DataPEA running without opening a browser on the server:

```text
Launcher\Server\Start_Server_LAN.bat
```

---

## 💻 Direct Python Commands

### Local

```bash
python Graphplot_webserv_v4_4_5.py --port 8800
```

### LAN

```bash
python Graphplot_webserv_v4_4_5.py --lan --port 8800
```

### Dedicated LAN Server

```bash
python Graphplot_webserv_v4_4_5.py --lan --port 8800 --no-browser --no-auto-shutdown
```

---

## 🗂️ Repository Structure

```text
Python-DataPEA/
│
├── Graphplot_webserv_v4_4_5.py       # Main application / โปรแกรมหลัก
├── launcher_helper.py                 # Windows launcher helper
├── lib_install.bat                    # Library installer
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
├── LICENSE                            # MIT License
├── VERSION_HISTORY.md                 # Detailed version history
├── PRESET_FORMAT_V1.md                # Preset specification
├── VALIDATION_V4_4_5.txt              # Baseline validation
├── .gitignore
├── .gitattributes
│
└── Launcher/
    ├── Stable/                        # Normal Local / LAN launch
    ├── Hidden/                        # Launch without console window
    ├── Debug/                         # Diagnostics / troubleshooting
    ├── Server/                        # Dedicated LAN server
    └── LAN_Setup/                     # Windows Firewall helper
```

---

## 🛠️ Troubleshooting / การแก้ปัญหาเบื้องต้น

### Port 8800 is already in use / Port 8800 ถูกใช้งานอยู่

Run:

```text
Launcher\Debug\Check_Port_8800.bat
```

### LAN client cannot connect / เครื่อง Client เข้าไม่ได้

Run:

```text
Launcher\Debug\LAN_Diagnostics.bat
```

Check:

- Server and client are on reachable networks
- Windows network profile is **Private** or **Domain**
- TCP port **8800** is allowed
- Company VLAN / Firewall policy permits the connection

### Need detailed console output / ต้องการดู Error แบบละเอียด

Use:

```text
Launcher\Debug\Debug_Local.bat
```

or

```text
Launcher\Debug\Debug_LAN.bat
```

---

## 🔗 About the Web Link / เรื่องลิงก์ไปยังเว็บจริง

DataPEA is a **FastAPI server application**, not a static HTML-only website. Therefore the complete application cannot be hosted directly by GitHub Pages without a running Python backend.

DataPEA เป็น Web Application ที่ต้องมี Python/FastAPI Server ทำงานอยู่ จึงไม่สามารถนำตัวโปรแกรมทั้งหมดไปเปิดบน GitHub Pages แบบ Static Website ได้โดยตรง

### Current links

| Link | Purpose |
|---|---|
| [🌐 Open DataPEA Local](http://127.0.0.1:8800) | Opens DataPEA running on the same PC |
| `http://<SERVER-IP>:8800` | Opens a DataPEA server on your LAN |
| [📦 GitHub Repository](https://github.com/TOPTUBBY/Python-DataPEA) | Source code and documentation |

If a public Internet demo is added in the future, the **OPEN DataPEA** badge can be changed to that public URL without changing the application itself.

หากภายหลังมี Public Server หรือ Domain จริง สามารถเปลี่ยนปลายทางของปุ่ม **OPEN DataPEA** ให้ชี้ไปยัง URL นั้นได้ทันที

---

## 🕘 Version History

| Version | Highlight |
|---|---|
| **V4.0** | WebServer architecture |
| **V4.1** | Interactive Plotly graph |
| **V4.2** | Cursor A/B, statistics, presets, launcher lifecycle |
| **V4.3** | Smart Header Detection and Cycle Analysis |
| **V4.4.0–V4.4.3** | Annotation and professional report workflow |
| **V4.4.4** | Thermal Shock-aware plateau analysis |
| **V4.4.5** | Multi-file CSV binding and Bound CSV workflow |

📘 Full history / ประวัติทั้งหมด: **[VERSION_HISTORY.md](./VERSION_HISTORY.md)**

---

## ✅ Current Baseline

```text
Repository  : Python-DataPEA
Application : Graphplot_webserv_v4_4_5.py
Version     : V4.4.5.2026
Default Port: 8800
Mode        : Local / LAN / Dedicated Server
```

---

## 👨‍💻 Author

**Patiphan Phakdeeburti**

Project development: **DET DQT EVSBG / Patiphan.Phak**

---

## ⚖️ License

Python-DataPEA is released under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the terms of the license.

Python-DataPEA เผยแพร่ภายใต้ **MIT License** ซึ่งอนุญาตให้นำซอฟต์แวร์ไปใช้ คัดลอก แก้ไข รวม เผยแพร่ แจกจ่าย หรือพัฒนาต่อยอดได้ ภายใต้เงื่อนไขของ License

📄 **[Read the full MIT License](./LICENSE)**

---

<p align="center">
  <strong>📊 Python-DataPEA</strong><br>
  Plot · Evaluate · Analyze · Report<br>
  พล็อต · ประเมิน · วิเคราะห์ · สร้างรายงาน
</p>
