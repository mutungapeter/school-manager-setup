
import os
import subprocess
import sys
import time

# Set the path to your hidden project folder
PROJECT_PATH = r"C:\Users\san\Desktop\Peter\Electron"

# Ensure paths are correct
BACKEND_PATH = os.path.join(PROJECT_PATH, "School-ERP-APIs-Backend")
FRONTEND_PATH = os.path.join(PROJECT_PATH, "school-Erp-frontend")

# Function to kill existing Django and Next.js processes
def kill_processes():
    print("❌ Stopping Django Backend...")
    os.system("taskkill /F /IM python.exe /T >nul 2>&1")

    print("❌ Stopping Next.js Frontend...")
    os.system("taskkill /F /IM node.exe /T >nul 2>&1")

# Function to start Django backend
def start_django_backend():
    if not os.path.exists(BACKEND_PATH):
        print(f"❌ Error: Backend path {BACKEND_PATH} not found!")
        sys.exit(1)

    os.chdir(BACKEND_PATH)
    subprocess.Popen(
        ["cmd.exe", "/c", "env\\Scripts\\activate && waitress-serve --host=0.0.0.0 --port=8000 School.wsgi:application"],
        creationflags=subprocess.CREATE_NO_WINDOW  # Runs without opening a console
    )
    print("✅ Django Backend started on http://127.0.0.1:8000")

# Function to start Next.js frontend
def start_nextjs_frontend():
    if not os.path.exists(FRONTEND_PATH):
        print(f"❌ Error: Frontend path {FRONTEND_PATH} not found!")
        sys.exit(1)

    os.chdir(FRONTEND_PATH)
    subprocess.Popen(
        ["cmd.exe", "/c", "npm start"],
        creationflags=subprocess.CREATE_NO_WINDOW  # Runs without opening a console
    )
    print("✅ Next.js Frontend started on http://localhost:3000")

# Function to open browser automatically
def open_browser():
    time.sleep(8)  # Give Next.js time to start
    os.system('start "" "http://localhost:3000"')

# Run functions in order
kill_processes()
start_django_backend()
start_nextjs_frontend()
open_browser()
