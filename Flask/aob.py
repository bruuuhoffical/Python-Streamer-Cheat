from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os
import subprocess
from pymem.process import inject_dll
from pymem.exception import ProcessNotFound
from datetime import datetime

def log(msg):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"{msg}")
    #print(f"{time} : {msg}")

def mkp(aob: str):
    if '??' in aob:
        if aob.startswith("??"):
            aob = f" {aob}"
            n = aob.replace(" ??", ".").replace(" ", "\\x")
            b = bytes(n.encode())
        else:
            n = aob.replace(" ??", ".").replace(" ", "\\x") 
            b = bytes(f"\\x{n}".encode())
        del n
        return b
    else:
        m = aob.replace(" ", "\\x")
        c = bytes(f"\\x{m}".encode())
        del m
        return c
    


def HEADLOAD():
    #log("Command Received!")

    try:
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        log("Process not found")
        # return "Process not found"

    try:
        if proc:
            #log("Scanning Players...")
            global aimbot_addresses
            entity_pattern = mkp("FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 A5 43")
            
            raw_addresses = pattern_scan_all(proc.process_handle, entity_pattern, return_multiple=True)

            unique_addresses = set([addr for addr in raw_addresses if addr != 0])
            valid_addresses = []
            for addr in unique_addresses:
                try:
                    test = read_bytes(proc.process_handle, addr, 4)
                    valid_addresses.append(addr)
                except:
                    continue

            aimbot_addresses = valid_addresses

            if aimbot_addresses:
                count = len(aimbot_addresses)
                log(f"Scan Complete")
                #return f"Scan Complete - {count}/{count}"
            else:
                log("Scan Failed")
                #return "Scan Failed - No Players found"

    except Exception as e:
        log(f"Error : {e}")
        #return "Scan failed due to error"
    finally:
        if proc:
            proc.close_process()






def HEADLOADV2():
    #log("Command Received!")

    try:
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        log("Process not found")
        #return "Process not found"

    try:
        if proc:
            #log("Scanning Players...")
            global aimbot_addresses
            entity_pattern = mkp("FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 A5 43")
            
            raw_addresses = pattern_scan_all(proc.process_handle, entity_pattern, return_multiple=True)

            unique_addresses = set([addr for addr in raw_addresses if addr != 0])
            valid_addresses = []
            for addr in unique_addresses:
                try:
                    test = read_bytes(proc.process_handle, addr, 4)
                    valid_addresses.append(addr)
                except:
                    continue

            aimbot_addresses = valid_addresses

            if aimbot_addresses:
                count = len(aimbot_addresses)
                log(f"Scan Complete")
                # return f"Scan Complete - {count}/{count}"
            else:
                # log("Scan Failed - No Players found")
                return "Scan Failed"

    except Exception as e:
        log(f"Error : {e}")
        return "Scan failed due to error"
    finally:
        if proc:
            proc.close_process()

    


def HEADON():
    #log("Command Recieved!")
    global original_value, aimbot_addresses
    original_value = []

    try:
        proc = Pymem("HD-Player")

        unique_addrs = list(set(aimbot_addresses))
        verified = []
        for addr in unique_addrs:
            try:
                read_bytes(proc.process_handle, addr, 4)
                verified.append(addr)
            except:
                continue
        aimbot_addresses = verified

        if not aimbot_addresses:
            log("No Players Found")
            return

        for current_entity in aimbot_addresses:
            original_AA = read_bytes(proc.process_handle, current_entity + 0xAA, 4)
            original_A6 = read_bytes(proc.process_handle, current_entity + 0xA6, 4)
            original_value.append((current_entity, original_AA, original_A6))
            # log(f"[HEADON] Backing up entity {hex(current_entity)} AA={original_AA.hex()} A6={original_A6.hex()}")
            write_bytes(proc.process_handle, current_entity + 0xA6, original_AA, len(original_AA))

        log("Aim Position >> Neck")

    except ProcessNotFound:
        log("Process not found")
    finally:
        try:
            proc.close_process()
        except:
            pass



def HEADONV2():
    #log("Command Recieved!")
    global original_value, aimbot_addresses
    original_value = []

    try:
        proc = Pymem("HD-Player")

        unique_addrs = list(set(aimbot_addresses))
        verified = []
        for addr in unique_addrs:
            try:
                read_bytes(proc.process_handle, addr, 4)
                verified.append(addr)
            except:
                continue
        aimbot_addresses = verified

        if not aimbot_addresses:
            log("No Players Found")
            return

        for current_entity in aimbot_addresses:
            original_AA = read_bytes(proc.process_handle, current_entity + 0xAA, 4)
            original_A6 = read_bytes(proc.process_handle, current_entity + 0xA6, 4)
            original_value.append((current_entity, original_AA, original_A6))
            # log(f"[HEADON] Backing up entity {hex(current_entity)} AA={original_AA.hex()} A6={original_A6.hex()}")
            write_bytes(proc.process_handle, current_entity + 0xA6, original_AA, len(original_AA))

        log("Aim Position >> Neck")

    except ProcessNotFound:
        log("Process not found")
    finally:
        try:
            proc.close_process()
        except:
            pass






def HEADOFF():
    #log("Command Recieved!")
    global original_value

    try:
        proc = Pymem("HD-Player")

        if not original_value:
            log("No Players Found")
            return

        restored = set()
        for entity, AA, A6 in original_value:
            if entity in restored:
                continue
            restored.add(entity)
            try:
                write_bytes(proc.process_handle, entity + 0xAA, AA, len(AA))
                write_bytes(proc.process_handle, entity + 0xA6, A6, len(A6))
            except:
                log(f"Failed to restore entity {hex(entity)}")

        #log(f"Aimbot disabled on {len(restored)} players")
        log("Aim Position >> Default")

    except ProcessNotFound:
        log("Process not found")
    except Exception as e:
        log(f"Error : {e}")
    finally:
        try:
            proc.close_process()
        except:
            pass



def HEADOFFV2():
    #log("Command Recieved!")
    global original_value

    try:
        proc = Pymem("HD-Player")

        if not original_value:
            log("No Players Found")
            return

        restored = set()
        for entity, AA, A6 in original_value:
            if entity in restored:
                continue
            restored.add(entity)
            try:
                write_bytes(proc.process_handle, entity + 0xAA, AA, len(AA))
                write_bytes(proc.process_handle, entity + 0xA6, A6, len(A6))
            except:
                log(f"Failed to restore entity {hex(entity)}")

        #log(f"Aimbot V2 disabled on {len(restored)} players")
        log("Aim Position >> Default")

    except ProcessNotFound:
        log("Process not found")
    except Exception as e:
        log(f"Error : {e}")
    finally:
        try:
            proc.close_process()
        except:
            pass



def SniperScopeon():
    log("SniperScopeon started")
    try:
       proc = Pymem("HD-Player")
    except:
       log("Bluestacks is not running.")

    try:
       if proc:
        log("Enabling Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        log("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    log("Sniper Scope Enabled!")

def SniperScopeoff():
    log("SniperScopeoff started")
    try:
       proc = Pymem("HD-Player")
    except:
       log("Bluestacks is not running.")

    try:
       if proc:
        log("Disabling Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        log("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    log("Sniper Scope Disabled!")


def SniperAimon():
    log("SniperAimon started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling Sniper Aim", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Aim Enabled!")

def SniperAimoff():
    log("SniperAimoff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling Sniper Aim", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Aim Disabled!")


def SniperSwitchon():
    log("SniperSwitchon started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling Sniper Switch", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Switch Enabled!")

def SniperSwitchoff():
    log("SniperSwitchoff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling Sniper Switch", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Switch Disabled!")

def SniperSwitchfixOn():
    log("SniperSwitchfixOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling Sniper Delay Fix", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 60"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 59")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Delay Fix Enabled!")

def SniperSwitchfixOff():
    log("SniperSwitchfixOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling Sniper Delay Fix", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 59"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 60")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Sniper Delay Fix Disabled!")



def NoRecoilOn():
    log("NoRecoilOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling No Recoil", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("7A FF F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("No Recoil Enabled!")

def NoRecoilOff():
    log("NoRecoilOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling No Recoil", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("7A FF F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("No Recoil Disabled")

def ScopeTracking2XOn():
    log("ScopeTracking2XOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling Scope Tracking 2X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Scope Tracking 2X Enabled!")

def ScopeTracking2XOff():
    log("ScopeTracking2XOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling Scope Tracking 2X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Scope Tracking 2X Disabled")

def ScopeTracking4XOn():
    log("ScopeTracking4XOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Enabling Scope Tracking 4X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Scope Tracking 4X Enabled!")

def ScopeTracking4XOff():
    log("ScopeTracking4XOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        log("Bluestacks is not running.")
        return

    try:
        if proc:
            log("Disabling Scope Tracking 4X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00"), return_multiple=True)
    except:
        log("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    log("Scope Tracking 4X Disabled")



    try:
       proc = Pymem("HD-Player")
    except:
       log("Bluestacks is not running.")

    try:
       if proc:
        log("Disabling Head Tracking", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        log("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    log("Head Tracking Disabled")


def ResetGuest():
    log("ResetGuest started")
    try:
       proc = Pymem("HD-Player")
    except:
       log("Bluestacks is not running.")

    try:
       if proc:
        log("Enabling Reset Guest", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        log("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    log("Reset Guest Enabled!")

    try:
       proc = Pymem("HD-Player")
    except:
       log("Bluestacks is not running.")

    try:
       if proc:
        log("Disabling Reset Guest", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        log("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    log("Reset Guest Disabled!")


def taskmanager():
    try:
        dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')
        open_process = Pymem("Taskmgr.exe")
        inject_dll(open_process.process_handle, dll_path.encode('UTF-8'))
        log("Streamer is Online!")
    except:
        pass 
    # Comment these:
    # log("Streamer is Online!")
    # log("Task Manager Injected DLL Successfully!")



def StartChams():
    log("StartChams started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'glew32.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("Chams Start Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Bluestacks Not Found!")
    except Exception as e:
        log(f"Error: {e}")

def ChamsMenuV1():
    log("ChamsMenuV1 started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormal.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("Chams Menu V1 Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Bluestacks Not Found!")
    except Exception as e:
        log(f"Error: {e}")

def ChamsMenuV2():
    log("ChamsMenuV2 started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormalv2.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("Chams Menu V2 Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Bluestacks Not Found!")
    except Exception as e:
        log(f"Error: {e}")

def ChamsGlow():
    log("ChamsGlow started")
    process_name = "HD-Player"

    try:
        # Open the process
        #log("Command Received!")
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'GLOW.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("Chams Glow Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Process Not Found!")
    except Exception as e:
        log(f"Error: {e}")

def ChamsBlue():
    log("ChamsBlue started")
    process_name = "HD-Player"

    try:
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Blue.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("Chams Blue Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Bluestacks Not Found!")
    except Exception as e:
        log(f"Error: {e}")

def HDRMap():
    log("HDRMap started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MapHdr.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        log("HDR Map Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        log("Bluestacks Not Found!")
    except Exception as e:
        log(f"Error: {e}")



