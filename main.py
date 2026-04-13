import os
import webbrowser
import urllib.request
import subprocess
import requests  # لازم تعمل pip install requests

# رابط ملف الـ JSON المباشر على جيتهاب
# ملاحظة: استخدم رابط الـ "Raw" دايماً
DATA_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/data.json"

def get_remote_data():
    try:
        response = requests.get(DATA_URL)
        return response.json()
    except:
        print("Error: Could not connect to the server!")
        return {}

def show_menu(mouse_options):
    print("================================")
    print("    Evo Online Mouse Installer  ")
    print("================================")
    for key, data in mouse_options.items():
        print(f"{key}) {data['name']}")
    print("0) Exit")
    print("================================")

def start_process():
    # سحب البيانات من النت أول ما البرنامج يفتح
    mouse_options = get_remote_data()
    
    if not mouse_options:
        return

    while True:
        show_menu(mouse_options)
        choice = input("Choose an option: ")

        if choice == "0":
            break
        
        if choice in mouse_options:
            selected = mouse_options[choice]
            
            # نفس الخطوات السابقة (فتح الصورة، التحميل، التثبيت)
            webbrowser.open(selected['image'])
            confirm = input(f"Install {selected['name']}? (y/n): ").lower()
            
            if confirm == 'y':
                print("Downloading...")
                # ... باقي كود التحميل والتثبيت اللي كتبناه قبل كدة ...