# Patient Chatbot

A small Flask application with a browser-based chat interface.

## Requirements

- Python 3.10 or newer
- Windows PowerShell (commands below use PowerShell syntax)

## Run the project

Open PowerShell in the project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell does not allow environment activation, run the app directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe .\app.py
```

Open **http://127.0.0.1:5000/** in your browser. Keep the terminal open while
using the app. Press `Ctrl+C` in the terminal to stop the server.

## Chat API

The chat endpoint accepts a JSON `POST` request at `/chat`:

```json
{"message": "fever"}
```

Example PowerShell request:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"message":"fever"}'
```

## Project files

- `app.py` — Flask server, page/static file routes, and chat endpoint
- `index.html` — chat page
- `style.css` — page styling and background image
- `script.js` — browser chat behavior
- `Whats1.jpg` — page background
- `Whats.jpg` — chat avatar
- `requirements.txt` — Python dependencies

This is a development server; use a production WSGI server for deployment.
