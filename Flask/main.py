import threading
from flask import * # type: ignore
from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime
from aob import *
from aob import taskmanager
import keyboard 
from flask import render_template_string
import threading
import io
import sys





def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()    
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest




keyauthapp = api(
    name = "STREAMER",
    ownerid = "JOqGMbH9vP",
    secret= "31bc402275867bf1bf36fe9a2bf7c459d0b96b431e89685419527de9d38ba6ec",
    version = "2.7", 
    hash_to_check = getchecksum()
)


auth_path = r'C:\Windows\key.json'
try:
    if os.path.isfile(auth_path): # Checking if the auth file exists
        with open(auth_path, 'r') as file:
            authfile = json.load(file) # type: ignore
        if authfile.get("authusername") == "": # Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans = input("Select Option: ")  # Skipping auto-login because auth file is empty
            if ans == "1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user, password)
                authfile["authusername"] = user
                authfile["authpassword"] = password
                with open(auth_path, 'w') as file:
                    json.dump(authfile, file, sort_keys=False, indent=4) # type: ignore
            elif ans == "2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user, password, license)
                authfile["authusername"] = user
                authfile["authpassword"] = password
                with open(auth_path, 'w') as file:
                    json.dump(authfile, file, sort_keys=False, indent=4) # type: ignore # type: ignore
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: # Auto login
                authuser = authfile.get('authusername')
                authpass = authfile.get('authpassword')
                keyauthapp.login(authuser, authpass)
            except Exception as e: # Error handling
                print(e)
    else: # Creating auth file because it is missing
        try:
            with open(auth_path, "w") as file: # Writing content
                file.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            print ("""
1. Login
2. Register
            """) # Skipping auto-login because the file is empty/missing
            ans = input("Select Option: ") 
            if ans == "1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user, password)
                with open(auth_path, 'r') as file:
                    authfile = json.load(file) # type: ignore
                authfile["authusername"] = user
                authfile["authpassword"] = password
                with open(auth_path, 'w') as file:
                    json.dump(authfile, file, sort_keys=False, indent=4) # type: ignore
            elif ans == "2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user, password, license)
                with open(auth_path, 'r') as file:
                    authfile = json.load(file) # type: ignore # type: ignore
                authfile["authusername"] = user
                authfile["authpassword"] = password
                with open(auth_path, 'w') as file:
                    json.dump(authfile, file, sort_keys=False, indent=4) # type: ignore
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: # Error handling
            print(e)
            os._exit(1) 
except Exception as e: # Error handling
    print(e)
    os._exit(1)





if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) # type: ignore # type: ignore


# def taskmanagerloop():
#     try:
#         taskmanager()
#         print("Taskmanager executed once.")
#     except Exception as e:
#         print(f"Taskmanager error: {e}")
def taskmanagerloop():
    try:
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        taskmanager() 

        sys.stdout = original_stdout 
    except Exception:
        sys.stdout = original_stdout


def run_taskmanager():
    task_thread = threading.Thread(target=taskmanagerloop)
    task_thread.daemon = True
    task_thread.start()




app = Flask("Streamer")

is_executing = False 


def handle_F4():
    global is_executing
    if not is_executing:
        is_executing = True 
        HEADLOAD()  
        is_executing = False 

def listen_for_f4():
    
    keyboard.add_hotkey('F4', handle_F4) 

threading.Thread(target=listen_for_f4, daemon=True).start()

def handle_F5():
    global is_executing
    if not is_executing:
        is_executing = True 
        HEADON()  
        is_executing = False 

def listen_for_f5():
    
    keyboard.add_hotkey('F5', handle_F5) 

threading.Thread(target=listen_for_f5, daemon=True).start()

def handle_F6():
    global is_executing
    if not is_executing:
        is_executing = True 
        HEADOFF()  
        is_executing = False 

def listen_for_f6():
    
    keyboard.add_hotkey('F6', handle_F6) 

threading.Thread(target=listen_for_f6, daemon=True).start()


@app.route('/', methods=['GET', 'POST'])
def home():
    alert_message = ""
    alert_type = ""

    image_path = "disocrd.png"

    if request.method == 'POST': # type: ignore
        if 'aimbotscan' in request.form: # type: ignore
            HEADLOAD()
            alert_message = "Command : Load HeadShot"
            alert_type = "primary"

        elif 'aimbotEnabled' in request.form: # type: ignore
            HEADON()
            alert_message = "Command : Enable HeadShot"
            alert_type = "primary"

        elif 'aimbotdisable' in request.form: # type: ignore # type: ignore
            HEADOFF()
            alert_message = "Command : Disable HeadShot"
            alert_type = "primary"

        elif 'aimbotscanv2' in request.form: # type: ignore
            HEADLOADV2()
            alert_message = "Command : Load HeadShot V2"
            alert_type = "primary"

        elif 'aimbotenablev2' in request.form: # type: ignore # type: ignore
            HEADONV2()
            alert_message = "Command : Enable HeadShot V2"
            alert_type = "primary"

        elif 'aimbotdisablev2' in request.form: # type: ignore # type: ignore
            HEADOFFV2()
            alert_message = "Command : Disable HeadShot V2"
            alert_type = "primary"
#======================= MISC ==============================
        elif 'noRecoilOn' in request.form: # type: ignore
            NoRecoilOn()
            alert_message = "Command : Enable No Recoil"
            alert_type = "primary"
        
        elif 'noRecoilOff' in request.form: # type: ignore
            NoRecoilOff()
            alert_message = "Command : Disable No Recoil"
            alert_type = "primary"

        elif 'scopeTracking2xOn' in request.form: # type: ignore
            ScopeTracking2XOn()
            alert_message = "Command : Enable Scope Tracking 2x"
            alert_type = "primary"
        
        elif 'scopeTracking2xOff' in request.form: # type: ignore
            ScopeTracking2XOff()
            alert_message = "Command : Disable Scope Tracking 2x"
            alert_type = "primary"
        
        elif 'scopeTracking4xOn' in request.form: # type: ignore
            ScopeTracking4XOn()
            alert_message = "Command : Enable Scope Tracking 4x"
            alert_type = "primary"
        
        elif 'scopeTracking4xOff' in request.form: # type: ignore
            ScopeTracking4XOff()
            alert_message = "Command : Disable Scope Tracking 4x"
            alert_type = "primary"

        elif 'sniperscopeon' in request.form: # type: ignore # type: ignore
            SniperScopeon()
            alert_message = "Command : Enable Sniper Scope"
            alert_type = "primary"
        elif 'sniperscopeoff' in request.form: # type: ignore # type: ignore
            SniperScopeoff()
            alert_message = "Command : Disable Sniper Scope"
            alert_type = "primary"

        elif 'sniperaimon' in request.form: # type: ignore # type: ignore
            SniperAimon()
            alert_message = "Command : Enable Sniper Aim"
            alert_type = "primary"
        elif 'sniperaimoff' in request.form: # type: ignore # type: ignore
            SniperAimoff()
            alert_message = "Command : Disable Sniper Aim"
            alert_type = "primary"
     
        elif 'sniperswitchon' in request.form: # type: ignore # type: ignore
            SniperSwitchon()
            alert_message = "Command : Enable Sniper Switch"
            alert_type = "primary"

        elif 'sniperswitchoff' in request.form: # type: ignore
            SniperSwitchoff()
            alert_message = "Command : Disable Sniper Switch"
            alert_type = "primary"

        elif 'SniperFixON' in request.form: # type: ignore
            SniperSwitchfixOn()
            alert_message = "Command : Enable Sniper Delay Fix"
            alert_type = "primary"

        elif 'SniperFixOFF' in request.form: # type: ignore
            SniperSwitchfixOff()
            alert_message = "Command : Disable Sniper Delay Fix"
            alert_type = "primary"

        elif 'startchams' in request.form: # type: ignore
            StartChams()
            alert_message = "Command : Enable Chams"
            alert_type = "primary"

        elif 'chamsmenuv1' in request.form: # type: ignore
            ChamsMenuV1()
            alert_message = "Command : Enable Chams Menu V2"
            alert_type = "primary"

        elif 'chamsmenuv2' in request.form: # type: ignore
            ChamsMenuV2()
            alert_message = "Command : Enable Chams Menu V2"
            alert_type = "primary"

        elif 'chamsglow' in request.form: # type: ignore
            ChamsGlow()
            alert_message = "Command : Enable Chams Glow"
            alert_type = "primary"
        
        elif 'chamsblue' in request.form: # type: ignore
            ChamsBlue()
            alert_message = "Command : Enable Chams Blue"
            alert_type = "primary"

        elif 'maphdr' in request.form: # type: ignore
            HDRMap()
            alert_message = "Command : Enable HDR Map"
            alert_type = "primary"


        




    html = ''' 
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>BRUUUH CHEATS</title>
    <style>
        body {
            font-family: 'Roboto', 'Arial', sans-serif;
            background-color: #0d0d0d;
            color: #f1f1f1;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 400px;
            margin: 20px auto;
            background-color: #1a1a1a;
            border: 1px solid #333;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            min-height: 700px;
        }

        h2 {
            text-align: center;
            padding: 10px 0 0;
            margin: 0;
        }

        h3 {
            text-align: center;
            margin: 0;
            padding-bottom: 10px;
            color: #aaa;
            font-size: 14px;
        }

        .status-panel {
            background-color: #111;
            padding: 8px 12px 4px 12px;
            font-size: 13px;
            border-top: 1px solid #333;
            border-bottom: 1px solid #333;
            line-height: 1.4;
        }

        .status-panel span {
            color: #00ff00;
            font-weight: bold;
        }

        .emulator-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 12px;
            border-bottom: 1px solid #333;
            background-color: #1a1a1a;
        }

        .emulator-row label {
            font-size: 14px;
        }

        .emulator-buttons {
            display: flex;
            gap: 6px;
            border: 1px solid rgb(75, 99, 206);
            border-radius: 4px;
            overflow: hidden;
        }

        .emulator-buttons button {
            padding: 8px 14px;
            background-color: transparent;
            color: rgb(75, 99, 206);
            border: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            flex: 1;
        }

        .emulator-buttons button.active {
            background-color: rgb(75, 99, 206);
            color: #fff;
        }

        .aimbot-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 12px;
            border-bottom: 1px solid #333;
            background-color: #1a1a1a;
        }

        .aimbot-row label {
            font-size: 14px;
        }

        .aimbots-buttons {
            display: flex;
            gap: 6px;
            border: 1px solid rgb(75, 99, 206);
            border-radius: 4px;
            overflow: hidden;
        }

        .aimbots-buttons button {
            padding: 8px 0; 
            min-width: 65px;
            background-color: transparent;
            color: rgb(75, 99, 206);
            border: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            flex: 1;
        }

        .aimbots-buttons button.active {
            background-color: rgb(75, 99, 206);
            color: #fff;
        }
        .tabs {
            display: flex;
            background-color: #2c2c2c;
        }

        .tabs button {
            flex: 1;
            padding: 12px;
            background: none;
            border: none;
            color: #ccc;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            font-size: 14px;
            font-weight: 500;
        }

        .tabs button.active {
            border-bottom: 2px solid rgb(75, 99, 206);
            color: #fff;
        }

        .tab-area {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            padding: 0;
        }

        .tab-content {
            display: none;
            padding: 15px 12px;
            flex-grow: 1;
            overflow-y: auto;
        }

        .tab-content.active {
            display: block;
        }

        .panel {
            border: 1px solid #333;
            background-color: #222;
            padding: 12px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 6px;
        }

        .panel-left {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .panel-left p {
            margin: 0;
            font-size: 15px;
            color: #ccc;
            font-weight: 500;
        }

        .function-label {
            font-size: 11px;
            color: #888;
            margin-top: 4px;
        }

        .panel button {
            padding: 8px 14px;
            background-color: transparent;
            color: rgb(75, 99, 206);
            border: 1px solid rgb(75, 99, 206);
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            border-radius: 4px;
        }

        .panel button:hover {
            background-color: rgba(75, 99, 206, 0.1);
        }

        /* Filled buttons */
        .panel button[name$="On"], 
        .panel button[name$="Enabled"], 
        .panel button[name$="enable"], 
        .panel button[name="startchams"], 
        .panel button[name^="scopeTracking"][name$="On"], 
        .panel button[name="aimbotscan"], 
        .panel button[name="aimbotscanv2"], 
        .panel button[name="aimbotenablev2"], 
        .panel button[name="chamsmenuv1"], 
        .panel button[name="chamsblue"],
        .panel button[name="chamsmenuv2"], 
        .panel button[name="chamsglow"], 
        .panel button[name="maphdr"] {
            background-color: rgb(75, 99, 206);
            color: #fff;
        }

        .panel button[name$="On"]:hover, 
        .panel button[name$="Enabled"]:hover, 
        .panel button[name$="enable"]:hover, 
        .panel button[name="startchams"]:hover, 
        .panel button[name^="scopeTracking"][name$="On"]:hover, 
        .panel button[name="aimbotscan"]:hover, 
        .panel button[name="aimbotscanv2"]:hover, 
        .panel button[name="aimbotenablev2"]:hover, 
        .panel button[name="chamsblue"]:hover,
        .panel button[name="chamsmenuv1"]:hover, 
        .panel button[name="chamsmenuv2"]:hover, 
        .panel button[name="chamsglow"]:hover, 
        .panel button[name="maphdr"]:hover {
            background-color: rgb(65, 85, 180);
        }

        .select-wrapper {
            position: relative;
            display: inline-block;
        }

        .styled-select {
            background-color: transparent;
            color: rgb(75, 99, 206);
            border: 1px solid rgb(75, 99, 206);
            border-radius: 4px;
            padding: 8px 24px 8px 14px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            appearance: none;
            outline: none;
            width: auto;
            min-width: 120px;
            max-width: 100%;
            white-space: nowrap;
        }

        .select-wrapper::after {
            /* content: "▼"; */
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            pointer-events: none;
            color: rgb(75, 99, 206);
            font-size: 11px;
            transition: transform 0.2s ease;
        }

        /* .select-wrapper:focus-within::after {
            content: "▲";
        } */
        .styled-select option {
            background-color: #1a1a1a;
            color: #f1f1f1;
        }

        .styled-select:focus {
            background-color: #1a1a1a;
            color: rgb(75, 99, 206);
        }



    .console-wrapper {
        padding: 12px;
        position: relative;
    }

    .console-header {
        background-color: #222;
        color: white;
        font-size: 14px;
        font-weight: bold;
        padding: 6px 12px;
        border: 1px solid #087428;
        border-bottom: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
    }

    .console {
        background-color: black;
        border: 1px solid #087428;
        border-top: none;
        border-bottom-left-radius: 4px;
        border-bottom-right-radius: 4px;
        color: #026930;
        padding: 8px 12px;
        font-family: 'Courier New', monospace;
        font-size: 13px;
        height: 140px;
        overflow-y: auto;
        line-height: 1.4;

        scrollbar-width: auto;
        scrollbar-color: rgba(255,255,255,0.15) transparent;
    }

    .console::-webkit-scrollbar {
        width: 12px;
    }
    .console::-webkit-scrollbar-track {
        background: transparent;
    }
    .console::-webkit-scrollbar-thumb {
        background-color: rgba(255,255,255,0.15);
        border-radius: 4px;
    }
    .console::-webkit-scrollbar-button {
        display: initial;
        height: 10px;
    }

    .console > div {
        padding: 2px 0;
        border-bottom: 1px solid rgb(38, 39, 38);
    }



    </style>
</head>
<body>

<div class="container">
    <h2>BRUUUH CHEATS</h2>
    <h3>Streamer Panel 2.6</h3>

    <div class="status-panel">
        Status: <span>Online</span> • v2.6 - -- ms<br>
        Connected to: BRUUUH CHEATS
    </div>

    <div class="emulator-row">
        <label>Emulator</label>
        <div class="emulator-buttons" id="emulator-toggle">
            <button class="active">32-bit</button>
            <button>64-bit</button>
        </div>
    </div>
    <div class="aimbot-row">
        <label>Headshot Mode</label>
        <div class="aimbots-buttons" id="aimbot-toggle">
            <button class="active">V1-Old</button>
            <button>V2-New</button>
        </div>
    </div>

    <div class="tabs">
        <button class="tab-button active" data-tab="aimbot">Headshot</button>
        <button class="tab-button" data-tab="misc">Misc</button>
        <button class="tab-button" data-tab="visuals">Visuals</button>
        <button class="tab-button" data-tab="settings">Settings</button>
    </div>

    <div class="tab-area">
    <form method="post">
    <!-- AIMBOT TAB -->
    <div id="aimbot" class="tab-content active">
        <div class="panel">
            <div class="panel-left">
                <p>Scan Enemies</p>
                <div class="function-label">Hotkey: F7</div>
            </div>
            <button name="aimbotscan">Scan</button>
        </div>

        <div class="panel">
            <div class="panel-left">
                <p>Aim Position</p>
                <div class="function-label">Activates headshot aimbot</div>
            </div>
            <div class="buttons-row">
                <button name="aimbotEnabled">Neck</button>
                <button name="aimbotdisable">Default Aim</button>
            </div>
        </div>

        <div class="panel">
            <div class="panel-left">
                <p>Other Aim Position</p>
                <div class="function-label">Select your default target bone</div>
            </div>
            <div class="select-wrapper">
                <select name="aimtarget" id="aimtarget" class="styled-select">
                <option value="neck">Neck</option>
                <option value="neckleft">Neck Left</option>
                <option value="neckright">Neck Right</option>
                <option value="leftshoulder">Left Shoulder</option>
                <option value="rightshoulder">Right Shoulder</option>
                </select>
            </div>
        </div>




    </div>

    <!-- MISC TAB -->
    <div id="misc" class="tab-content">
        <div class="panel">
            <div class="panel-left">
                <p>No Recoil</p>
                <div class="function-label">Removes weapon recoil</div>
            </div>
            <div class="buttons-row">
                <button name="noRecoilOn">Enable</button>
                <button name="noRecoilOff">Disable</button>
            </div>
        </div>

        <div class="panel">
            <div class="panel-left">
                <p>Scope Tracking 2X</p>
                <div class="function-label">Improves 2x scope tracking</div>
            </div>
            <div class="buttons-row">
                <button name="scopeTracking2xOn">Enable</button>
                <button name="scopeTracking2xOff">Disable</button>
            </div>
        </div>

        <div class="panel">
            <div class="panel-left">
                <p>Scope Tracking 4X</p>
                <div class="function-label">Improves 4x scope tracking</div>
            </div>
            <div class="buttons-row">
                <button name="scopeTracking4xOn">Enable</button>
                <button name="scopeTracking4xOff">Disable</button>
            </div>
        </div>

        
    </div>

    <!-- VISUALS TAB -->
    <div id="visuals" class="tab-content">
        <div class="panel">
            <div class="panel-left">
                <p>Start Chams</p>
                <div class="function-label">Starts Chams visual effect</div>
            </div>
            <button name="startchams">Start</button>
        </div>
        <div class="panel">
            <div class="panel-left">
                <p>Chams Menu V1</p>
                <div class="function-label">Open Location Menu</div>
            </div>
            <button name="chamsmenuv1">Inject</button>
        </div>
        <div class="panel">
            <div class="panel-left">
                <p>Chams Menu V2</p>
                <div class="function-label">Open Location Menu V2</div>
            </div>
            <button name="chamsmenuv2">Inject</button>
        </div>
        <div class="panel">
            <div class="panel-left">
                <p>Glow Hack</p>
                <div class="function-label">Make Enemies Glow</div>
            </div>
            <button name="chamsglow">Inject</button>
        </div>
        <div class="panel">
            <div class="panel-left">
                <p>Blue Hack</p>
                <div class="function-label">Make Enemies Blue</div>
            </div>
            <button name="chamsblue">Inject</button>
        </div>
        <div class="panel">
            <div class="panel-left">
                <p>HDR Map</p>
                <div class="function-label">Make Enemies Glow</div>
            </div>
            <button name="maphdr">Inject</button>
        </div>
        
    </div>

    <!-- SETTINGS TAB -->
    <div id="settings" class="tab-content">
        <div class="panel">
            <div class="panel-left">
                <p>Clear Console</p>
                <div class="function-label">Clears the console log</div>
            </div>
            <button type="button" onclick="clearConsole()">Clear</button>
        </div>
    </div>
    </form>
    </div>

    <!-- CONSOLE ALWAYS FIXED -->
    <div class="console-wrapper">
        <div class="console-header">Console</div>
        <div class="console" id="console-log"></div>
    </div>



</div>

<!-- JS -->
<script>
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const tabContents = document.querySelectorAll('.tab-content');
            tabContents.forEach(content => content.classList.remove('active'));

            const activeTab = document.getElementById(button.dataset.tab);
            activeTab.classList.add('active');
        });
    });

    const emulatorButtons = document.querySelectorAll('#emulator-toggle button');
    emulatorButtons.forEach(button => {
        button.addEventListener('click', () => {
            emulatorButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });
    const aimbotButtons = document.querySelectorAll('#aimbot-toggle button');
    aimbotButtons.forEach(button => {
        button.addEventListener('click', () => {
            aimbotButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
        });
    });

    function clearConsole() {
        const consoleLog = document.getElementById('console-log');
        consoleLog.innerHTML = '';
        const time = new Date().toLocaleTimeString();
        const newLine = document.createElement('div');
        newLine.textContent = `${time} Console cleared`;
        consoleLog.appendChild(newLine);
    }
    document.querySelectorAll("form button[name]").forEach(button => {
    button.addEventListener("click", function (e) {
        e.preventDefault();
        let actionName = this.name;

        if (["aimbotscan", "aimbotEnabled", "aimbotdisable"].includes(actionName)) {
            const isV2 = document.querySelector('#aimbot-toggle button.active')?.textContent.includes("V2");
            if (isV2) {
                if (actionName === "aimbotscan") actionName = "aimbotscanv2";
                if (actionName === "aimbotEnabled") actionName = "aimbotenablev2";
                if (actionName === "aimbotdisable") actionName = "aimbotdisablev2";
            }
        }

        fetch("/execute", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({ action: actionName })
        })
        .then(res => res.text())
        .then(data => {
            const log = document.getElementById("console-log");
            const time = new Date().toLocaleTimeString(undefined, { hour12: false });

            const line = document.createElement("div");
            line.textContent = `${time} : ${data}`;
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;

            function checkScanResultUntilReady() {
                fetch("/result")
                    .then(res => res.text())
                    .then(data => {
                        if (data && data.trim() !== "") {
                            const delayedLine = document.createElement("div");
                            const newTime = new Date().toLocaleTimeString(undefined, { hour12: false });
                            delayedLine.textContent = `${newTime} : ${data}`;
                            log.appendChild(delayedLine);
                            log.scrollTop = log.scrollHeight;
                        } else {
                            setTimeout(checkScanResultUntilReady, 300);
                        }
                        if (log.children.length > 100) {
                            log.removeChild(log.firstChild);  // Remove oldest line
                        }

                    });
            }

            checkScanResultUntilReady();
        })
        .catch(error => {
            const log = document.getElementById("console-log");
            const time = new Date().toLocaleTimeString(undefined, { hour12: false });
            const line = document.createElement("div");
            line.textContent = `${time} : ${error}`;
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;
        });
    });
});

const aimSelect = document.getElementById("aimtarget");

function resizeSelectWidth() {
    const temp = document.createElement("span");
    temp.style.position = "absolute";
    temp.style.visibility = "hidden";
    temp.style.font = getComputedStyle(aimSelect).font;
    temp.textContent = aimSelect.options[aimSelect.selectedIndex].text;
    document.body.appendChild(temp);
    aimSelect.style.width = (temp.offsetWidth + 40) + "px";
    document.body.removeChild(temp);
}

    function logAimSelectionChange() {
        const selectedText = aimSelect.options[aimSelect.selectedIndex].text;
        const time = new Date().toLocaleTimeString(undefined, { hour12: false });
        const line = document.createElement("div");
        line.textContent = `${time} : Aim Position set to ${selectedText}`;
        const consoleLog = document.getElementById("console-log");
        consoleLog.appendChild(line);
        consoleLog.scrollTop = consoleLog.scrollHeight;
    }

    aimSelect.addEventListener("change", () => {
        resizeSelectWidth();
        logAimSelectionChange();
    });

    resizeSelectWidth();

function scrollConsoleTop() {
    const log = document.getElementById("console-log");
    log.scrollTop = 0;
}

function scrollConsoleBottom() {
    const log = document.getElementById("console-log");
    log.scrollTop = log.scrollHeight;
}


</script>

</body>
</html>`


    '''
    return render_template_string(html, alert_message=alert_message , alert_type=alert_type) 



  
import threading
import io
import sys

last_result = None  # stores output for /result polling

def run_command_capture_output(func):
    global last_result
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer  # redirect all print() to string

    try:
        result = func()
        if result:
            print(result)  # include returned message too
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        sys.stdout = old_stdout
        last_result = buffer.getvalue()
        buffer.close()


@app.route('/execute', methods=['POST'])
def execute():
    action = request.form.get('action')

    commands = {
        "aimbotscan": HEADLOAD,
        "aimbotEnabled": HEADON,
        "aimbotdisable": HEADOFF,
        "aimbotscanv2": HEADLOADV2,
        "aimbotenablev2": HEADONV2,
        "aimbotdisablev2": HEADOFFV2,
        "sniperscopeon": SniperScopeon,
        "sniperscopeoff": SniperScopeoff,
        "sniperaimon": SniperAimon,
        "sniperaimoff": SniperAimoff,
        "sniperswitchon": SniperSwitchon,
        "sniperswitchoff": SniperSwitchoff,
        "SniperFixON": SniperSwitchfixOn,
        "SniperFixOFF": SniperSwitchfixOff,
        "noRecoilOn": NoRecoilOn,
        "noRecoilOff": NoRecoilOff,
        "scopeTracking2xOn": ScopeTracking2XOn,
        "scopeTracking2xOff": ScopeTracking2XOff,
        "scopeTracking4xOn": ScopeTracking4XOn,
        "scopeTracking4xOff": ScopeTracking4XOff,
        "startchams": StartChams,
        "chamsmenuv1": ChamsMenuV1,
        "chamsmenuv2": ChamsMenuV2,
        "chamsglow": ChamsGlow,
        "chamsblue": ChamsBlue,
        "maphdr": HDRMap,
    }

    if action in commands:
        try:
            threading.Thread(target=run_command_capture_output, args=(commands[action],), daemon=True).start()
            return "Command Received"
            #return "Please Wait..."
        except Exception as e:
            return f"Error: {e}", 500

    return "Unknown action", 400


@app.route('/result')
def get_last_result():
    global last_result
    if last_result:
        response = last_result
        last_result = None 
        return response
    return ""


if __name__ == '__main__':
    run_taskmanager()
    app.run(host='0.0.0.0', port=2099, debug=False)