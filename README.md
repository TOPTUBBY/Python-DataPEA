# Python-DataPEA

> Browser-based engineering CSV plotting, evaluation, annotation, cycle analysis, and report-generation tool built with Python, FastAPI, Plotly, and Matplotlib.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-WebServer-009688?logo=fastapi&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?logo=plotly&logoColor=white)
![Version](https://img.shields.io/badge/version-V4.4.5-blue)
![Default Port](https://img.shields.io/badge/LAN%20Port-8800-6f42c1)

## Overview

**Python-DataPEA** is a portable WebServer-based engineering data-analysis tool for CSV log files.

It is designed for test, validation, qualification, and laboratory workflows where users need to:

- load and visualize CSV data in a browser;
- combine multiple sequential CSV log files;
- configure Primary / Secondary Y axes;
- inspect signals interactively with Cursor A/B;
- calculate Min / Max / Average values over a selected range;
- add engineering reference lines, tolerance bands, and comments;
- analyze temperature-cycling and thermal-shock profiles;
- save reusable plotting presets;
- export plots and reports to PNG, PDF, Word, and CSV;
- run locally or as a LAN WebServer without a cloud dependency.

The current release is **V4.4.5.2026** and uses TCP port **8800** by default.

## Key Features

### Interactive plotting

- Offline Plotly-based browser graph
- Mouse-wheel zoom and drag zoom
- Pan / autoscale / reset view
- Hover signal inspection
- Legend show/hide and isolate
- Up to 8 independent plot pages
- Primary and Secondary Y axes
- Automatic or manual trace colors

### Multi-file CSV binding

V4.4.5 supports selecting multiple CSV files at once.

1. Choose one or more CSV files.
2. Review the selected-file list.
3. Files are initially ordered by browser-visible **Last Modified** time.
4. Drag and drop to manually correct the file sequence.
5. Click **Bind Data** for 2+ files.
6. GraphPlot removes repeated metadata/header sections from subsequent files.
7. Load the bound dataset directly or download the generated Bound CSV.

GraphPlot validates that the column names and column order match before binding.

> Browser File APIs do not expose the Windows filesystem Creation Time. The initial sequence therefore uses Last Modified, with drag-and-drop available for user-controlled ordering.

### Smart CSV header detection

The application can automatically locate logger headers using first-column markers such as:

- `Timestamp`
- `Date&Time`
- `Date`
- `Time`

Ordinary CSV files fall back to row 1 when no supported marker is detected.

### Cursor A/B and statistics

- Cursor A / Cursor B
- Delta Time / Delta X
- Per-signal A and B values
- Delta Value
- Min
- Max
- Average
- Sample count
- Statistics over the A↔B interval or current zoom range

### Engineering annotations

- Reference / limit lines
- Tolerance / acceptance range bands
- Graph comments
- Primary / Secondary axis targeting
- Configurable colors, line styles, opacity, and labels
- Drag editing directly on the Plotly graph
- Comment arrow / border / size / position controls

### Cycle analysis

Supports **Auto**, **Temperature Cycling**, and **Thermal Shock** profiles.

Calculated results include complete cycle count, Tmin/Tmax, average Tmin/Tmax soak, average cycle time, detailed per-cycle table, and CSV result export.

### Reports and export

- PNG plot export
- Custom-wide multi-page PDF
- A4 landscape PDF
- A4 landscape Word report
- Selectable report pages
- Cycle Analysis CSV
- Bound CSV
- `.preset` import/export
- Browser Save As support where permitted

### Appearance

The Web UI uses a compact **Light / Dark toggle**.

On a fresh browser session, the initial theme follows the Windows/browser system preference automatically. Manual Light/Dark selection is retained for the current browser session.

## Technology

| Component | Technology |
|---|---|
| Language | Python 3 |
| Web framework | FastAPI |
| ASGI server | Uvicorn |
| Interactive graph | Plotly |
| Static/report plotting | Matplotlib |
| Data processing | pandas / NumPy |
| Word report | python-docx |
| Browser UI | Embedded HTML / CSS / JavaScript |
| Default port | 8800 |
| Cloud dependency | None |
| LAN support | Yes |

## Repository Structure

```text
Python-DataPEA/
├── Graphplot_webserv_v4_4_5.py
├── launcher_helper.py
├── lib_install.bat
├── requirements.txt
├── README.md
├── VERSION_HISTORY.md
├── PRESET_FORMAT_V1.md
├── VALIDATION_V4_4_5.txt
├── .gitignore
├── .gitattributes
└── Launcher/
    ├── Stable/
    ├── Hidden/
    ├── Debug/
    ├── Server/
    └── LAN_Setup/
```

## Installation

### Windows automatic installer

Install Python 3, then run:

```bat
lib_install.bat
```

### pip

```bash
python -m pip install -r requirements.txt
```

## Quick Start

### Local mode

```text
Launcher\Stable\Start_Local.bat
```

Open:

```text
http://127.0.0.1:8800
```

### LAN mode

```text
Launcher\Stable\Start_LAN.bat
```

Other PCs on the LAN open:

```text
http://<SERVER-IP>:8800
```

If Windows Firewall blocks access, run once as Administrator:

```text
Launcher\LAN_Setup\Allow_GraphPlot_Port_8800_Firewall.bat
```

### Dedicated server PC

```text
Launcher\Server\Start_Server_LAN.bat
```

## Direct Python Commands

```bash
python Graphplot_webserv_v4_4_5.py --port 8800
python Graphplot_webserv_v4_4_5.py --lan --port 8800
python Graphplot_webserv_v4_4_5.py --lan --port 8800 --no-browser --no-auto-shutdown
```

## Preset Files

GraphPlot supports portable `.preset` files containing signal selection, axis assignments, colors, reference lines, and range bands.

See `PRESET_FORMAT_V1.md` for details.

## Troubleshooting

Check port usage:

```text
Launcher\Debug\Check_Port_8800.bat
```

LAN diagnostics:

```text
Launcher\Debug\LAN_Diagnostics.bat
```

## Version History

- **V4.0** — WebServer architecture
- **V4.1** — Interactive Plotly graph
- **V4.2** — Professional UI, Cursor A/B, statistics, presets, launcher lifecycle
- **V4.3** — Smart Header Detection, Cycle Analysis, appearance themes
- **V4.4.0–V4.4.3** — Engineering annotations and report workflow
- **V4.4.4** — Thermal Shock-aware plateau analysis
- **V4.4.5** — Multi-file CSV binding and Bound CSV workflow

See `VERSION_HISTORY.md` for detailed changes.

## Author

**Patiphan Phakdeeburti**

Project development: DET DQT EVSBG / Patiphan.Phak

## License

A public software license has not been declared for Python-DataPEA yet.
