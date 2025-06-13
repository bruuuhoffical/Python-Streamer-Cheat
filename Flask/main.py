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
import keyboard # type: ignore





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
    name = "STREAMER", # App name 
    ownerid = "JOqGMbH9vP",
    secret= "31bc402275867bf1bf36fe9a2bf7c459d0b96b431e89685419527de9d38ba6ec", # Account ID
    version = "2.4", 
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


def taskmanagerloop():
    while True:
        taskmanager()
        print("Taskmanager is running...")
        time.sleep(2)  # Wait for 2 seconds

def run_taskmanager():
    # Running taskmanagerloop in a separate thread
    task_thread = threading.Thread(target=taskmanagerloop)
    task_thread.daemon = True  # Allows thread to exit when the main program exits
    task_thread.start()



app = Flask("Streamer") # type: ignore # type: ignore

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
            alert_message = "Command : Load Aimbot"
            alert_type = "primary"
        elif 'aimbotEnabled' in request.form: # type: ignore
            HEADON()
            alert_message = "Command : Enable Aimbot"
            alert_type = "primary"

        elif 'aimbotdisable' in request.form: # type: ignore # type: ignore
            HEADOFF()
            alert_message = "Command : Disable Aimbot"
            alert_type = "primary"

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
        }

        .emulator-buttons button {
            padding: 8px 14px;
            background-color: transparent;
            color: #5C6BC0;
            border: 1px solid #5C6BC0;
            cursor: pointer;
            font-size: 14px;
            border-radius: 4px;
            font-weight: 500;
        }

        .emulator-buttons button:hover {
            background-color: rgba(92,107,192,0.1);
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
            border-bottom: 2px solid #5C6BC0;
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
            padding: 8px 12px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 6px;
        }

        .panel p {
            margin: 0;
            font-size: 15px;
            color: #ccc;
            font-weight: 500;
        }

        .panel .buttons-row {
            display: flex;
            gap: 10px;
        }

        button {
            padding: 8px 14px;
            background-color: transparent;
            color: #5C6BC0;
            border: 1px solid #5C6BC0;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            border-radius: 4px;
        }

        button:hover {
            background-color: rgba(92,107,192,0.1);
        }

        /* Console style */
        .console-wrapper {
            padding: 12px;
        }

        .console {
            background-color: black;
            border: 1px solid #00ff00;
            border-radius: 4px;
            color: #00ff00;
            padding: 10px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            height: 120px;
            overflow-y: auto;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>BRUUUH CHEATS</h2>
    <h3>Streamer Panel 2.5</h3>

    <div class="status-panel">
        Status: <span>Online</span> • v2.5 - -- ms<br>
        Connected to: BRUUUH CHEATS
    </div>

    <div class="emulator-row">
        <label>Emulator</label>
        <div class="emulator-buttons">
            <button>32-bit</button>
            <button>64-bit</button>
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
            <p>Load Headshot</p>
            <button name="aimbotscan">Load</button>
        </div>

        <div class="panel">
            <p>Headshot Legit</p>
            <button name="aimbotEnabled">Enable</button>
        </div>

        <div class="panel">
            <p>Headshot Legit</p>
            <button name="aimbotdisable">Disable</button>
        </div>

        <div class="panel">
            <p>No Recoil</p>
            <div class="buttons-row">
                <button name="noRecoilOn">Enable</button>
                <button name="noRecoilOff">Disable</button>
            </div>
        </div>
    </div>

    <!-- MISC TAB -->
    <div id="misc" class="tab-content">
        <div class="panel">
            <p>Scope Tracking 2X</p>
            <div class="buttons-row">
                <button name="scopeTracking2xOn">Enable</button>
                <button name="scopeTracking2xOff">Disable</button>
            </div>
        </div>

        <div class="panel">
            <p>Scope Tracking 4X</p>
            <div class="buttons-row">
                <button name="scopeTracking4xOn">Enable</button>
                <button name="scopeTracking4xOff">Disable</button>
            </div>
        </div>
    </div>

    <!-- VISUALS TAB -->
    <div id="visuals" class="tab-content">
        <div class="panel">
            <p>Start Chams</p>
            <button name="startchams">Start</button>
        </div>
        <div class="panel">
            <p>Chams Menu V1</p>
            <button name="chamsmenuv1">Inject</button>
        </div>
        <div class="panel">
            <p>Chams Menu V2</p>
            <button name="chamsmenuv2">Inject</button>
        </div>
        <div class="panel">
            <p>Chams Glow</p>
            <button name="chamsglow">Inject</button>
        </div>
        <div class="panel">
            <p>HDR Map</p>
            <button name="maphdr">Inject</button>
        </div>
    </div>

    <!-- SETTINGS TAB -->
    <div id="settings" class="tab-content">
        <div class="panel">
            <p>Clear Console</p>
            <button type="button" onclick="clearConsole()">Clear</button>
        </div>
    </div>
    </form>
    </div>

    <!-- CONSOLE ALWAYS FIXED -->
    <div class="console-wrapper">
        <div class="console" id="console-log"></div>
    </div>
</div>

<!-- JS -->
<script>
    // Tabs logic
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

    // Console functions
    function logToConsole(message) {
        const consoleLog = document.getElementById('console-log');
        const newLine = document.createElement('div');
        const time = new Date().toLocaleTimeString();
        newLine.textContent = `[${time}] ${message}`;
        consoleLog.appendChild(newLine);
        consoleLog.scrollTop = consoleLog.scrollHeight;
    }

    function clearConsole() {
        const consoleLog = document.getElementById('console-log');
        consoleLog.innerHTML = '';
        logToConsole('Console cleared');
    }

    // Example logging
    const enabledButtons = document.querySelectorAll('button[name$="On"], button[name$="on"]');
    const disableButtons = document.querySelectorAll('button[name$="Off"], button[name$="off"], button[name="aimbotdisable"], button[name="chamsmenu"], button[name="aimbotEnabled"]');

    enabledButtons.forEach(button => {
        button.addEventListener('click', () => {
            logToConsole(`${button.name} Enable clicked`);
        });
    });

    disableButtons.forEach(button => {
        button.addEventListener('click', () => {
            logToConsole(`${button.name} Disable clicked`);
        });
    });

    document.querySelector('button[name="aimbotscan"]').addEventListener('click', () => {
        logToConsole('Command: Load Headshot');
    });
</script>

</body>
</html>


'''
    return render_template_string(html, alert_message=alert_message , alert_type=alert_type) 


if __name__ == '__main__':
    run_taskmanager()
    app.run(host='0.0.0.0', port=2099, debug=False)
  
