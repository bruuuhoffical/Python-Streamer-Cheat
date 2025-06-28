from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os
import subprocess
from pymem.process import inject_dll
from pymem.exception import ProcessNotFound

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
    #print("Command Received")

    try:
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        print("Process not found")
        #return "Process not found"

    try:
        if proc:
            print("Scanning Players...")
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
                print(f"Scan Complete")
                #return f"Scan Complete"
            else:
                print("Scan Failed")
                #return "Scan Failed"

    except Exception as e:
        print(f"[ERROR] {e}")
        #return "Scan failed due to error"
    finally:
        if proc:
            proc.close_process()






def HEADLOADV2():
    #print("Command Received")

    try:
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        print("Process not found")
        #return "Process not found"

    try:
        if proc:
            print("Scanning Players...")
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
                print(f"Scan Complete")
                #return f"Scan Complete"
            else:
                print("Scan Failed")
                #return "Scan Failed"

    except Exception as e:
        print(f"[ERROR] {e}")
        #return "Scan failed due to error"
    finally:
        if proc:
            proc.close_process()

    


def HEADON():
    #print("Command Received")
    global original_value, aimbot_addresses
    original_value = []

    try:
        proc = Pymem("HD-Player")

        # Final deduplication and memory validation
        unique_addrs = list(set(aimbot_addresses))
        verified = []
        for addr in unique_addrs:
            try:
                read_bytes(proc.process_handle, addr, 4)
                verified.append(addr)
            except:
                continue
        aimbot_addresses = verified

        for current_entity in aimbot_addresses:
            original_AA = read_bytes(proc.process_handle, current_entity + 0xAA, 4)
            original_A6 = read_bytes(proc.process_handle, current_entity + 0xA6, 4)
            original_value.append((current_entity, original_AA, original_A6))
            ##print(f"[HEADON] Backing up entity {hex(current_entity)} AA={original_AA.hex()} A6={original_A6.hex()}")
            print("Aim Position >> Neck")

            write_bytes(proc.process_handle, current_entity + 0xA6, original_AA, len(original_AA))

    except ProcessNotFound:
        print("Process not found")
        #return "Process not found"
    finally:
        try: proc.close_process()
        except: pass

    #return f"Aimbot Enabled on {len(aimbot_addresses)} players"


def HEADONV2():
    #print("Command Received")
    global original_value, aimbot_addresses
    original_value = []

    try:
        proc = Pymem("HD-Player")

        # Final deduplication and memory validation
        unique_addrs = list(set(aimbot_addresses))
        verified = []
        for addr in unique_addrs:
            try:
                read_bytes(proc.process_handle, addr, 4)
                verified.append(addr)
            except:
                continue
        aimbot_addresses = verified

        for current_entity in aimbot_addresses:
            original_AA = read_bytes(proc.process_handle, current_entity + 0xAA, 4)
            original_A6 = read_bytes(proc.process_handle, current_entity + 0xA6, 4)
            original_value.append((current_entity, original_AA, original_A6))
            ##print(f"[HEADON] Backing up entity {hex(current_entity)} AA={original_AA.hex()} A6={original_A6.hex()}")
            print("Aim Position >> Neck")

            write_bytes(proc.process_handle, current_entity + 0xA6, original_AA, len(original_AA))

    except ProcessNotFound:
        print("Process not found")
        #return "Process not found"
    finally:
        try: proc.close_process()
        except: pass

    #return f"Aim Position >> Neck {len(aimbot_addresses)} Players"





def HEADOFF():
    #print("Command Received")
    global original_value

    try:
        proc = Pymem("HD-Player")

        if not original_value:
            print("Unable to Disable")
            #return "Unable to Disable"

        for entity, AA, A6 in original_value:
            try:
                write_bytes(proc.process_handle, entity + 0xAA, AA, len(AA))
                write_bytes(proc.process_handle, entity + 0xA6, A6, len(A6))
                #print(f"[HEADOFF] Restored entity {hex(entity)}")
            except Exception as e:
                #print(f"[ERROR] Failed to restore {hex(entity)}: {e}")
                print(f"Unale to Restore")

        print(f"Aim Position >> Default")

    except ProcessNotFound:
        print("Process not found")
        #return "Process not found"
    except Exception as e:
        print(f"[ERROR] {e}")
        # return f"Error: {e}"
    finally:
        try: proc.close_process()
        except: pass

    # return f"Aimbot disabled on {len(original_value)} players"


def HEADOFFV2():
    #print("Command Received")
    global original_value

    try:
        proc = Pymem("HD-Player")

        if not original_value:
            print("Unable to Disable")
            #return "Unable to Disable"

        for entity, AA, A6 in original_value:
            try:
                write_bytes(proc.process_handle, entity + 0xAA, AA, len(AA))
                write_bytes(proc.process_handle, entity + 0xA6, A6, len(A6))
                #print(f"[HEADOFF] Restored entity {hex(entity)}")
            except Exception as e:
                #print(f"[ERROR] Failed to restore {hex(entity)}: {e}")
                print(f"Unale to Restore")

        print(f"Aim Position >> Default")

    except ProcessNotFound:
        print("Process not found")
        #return "Process not found"
    except Exception as e:
        print(f"[ERROR] {e}")
        # return f"Error: {e}"
    finally:
        try: proc.close_process()
        except: pass

    # return f"Aimbot disabled on {len(original_value)} players"


def SniperScopeon():
    # print("SniperScopeon started")
    try:
       proc = Pymem("HD-Player")
    except:
       print("Emulator Not Running")

    try:
       if proc:
        #print("Enabling Sniper Scope")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    print("Sniper Scope Enabled")

def SniperScopeoff():
    #print("SniperScopeoff started")
    try:
       proc = Pymem("HD-Player")
    except:
       print("Emulator Not Running")

    try:
       if proc:
        #print("Disabling Sniper Scope")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    print("Sniper Scope Disabled")


def SniperAimon():
    #print("SniperAimon started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling Sniper Aim")
            value = pattern_scan_all(proc.process_handle, mkp("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Aim Enabled")

def SniperAimoff():
    #print("SniperAimoff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling Sniper Aim")
            value = pattern_scan_all(proc.process_handle, mkp("00"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Aim Disabled")


def SniperSwitchon():
    #print("SniperSwitchon started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling Sniper Switch")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Switch Enabled")

def SniperSwitchoff():
    #print("SniperSwitchoff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling Sniper Switch")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Switch Disabled")

def SniperSwitchfixOn():
    #print("SniperSwitchfixOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling Sniper Delay Fix")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 60"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 59")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Delay Fix Enabled")

def SniperSwitchfixOff():
    #print("SniperSwitchfixOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling Sniper Delay Fix")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 59"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 60")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Delay Fix Disabled")



def NoRecoilOn():
    #rint("NoRecoilOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling No Recoil")
            value = pattern_scan_all(proc.process_handle, mkp("7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("7A FF F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("No Recoil Enabled")

def NoRecoilOff():
    
    #print("NoRecoilOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling No Recoil")
            value = pattern_scan_all(proc.process_handle, mkp("7A FF F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED 08 D0")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("No Recoil Disabled")

def ScopeTracking2XOn():
    # print("ScopeTracking2XOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling Scope Tracking 2X")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 2X Enabled")

def ScopeTracking2XOff():
    #("ScopeTracking2XOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling Scope Tracking 2X")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 2X Disabled")

def ScopeTracking4XOn():
    #print("ScopeTracking4XOn started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Enabling Scope Tracking 4X")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 4X Enabled")

def ScopeTracking4XOff():
    #print("ScopeTracking4XOff started")
    try:
        proc = Pymem("HD-Player")
    except:
        print("Emulator Not Running")
        return

    try:
        if proc:
            #print("Disabling Scope Tracking 4X")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00"), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 4X Disabled")



    try:
       proc = Pymem("HD-Player")
    except:
       print("Emulator Not Running")

    try:
       if proc:
        #print("Disabling Head Tracking")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
  

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Scope Tracking 4X Disabled")


def ResetGuest():
    #print("ResetGuest started")
    try:
       proc = Pymem("HD-Player")
    except:
       print("Emulator Not Running")

    try:
       if proc:
        #print("Enabling Reset Guest")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Guest Reset Successfully")

    try:
       proc = Pymem("HD-Player")
    except:
       print("Emulator Not Running")

    try:
       if proc:
        #print("Disabling Reset Guest")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("Error Encountered (AOB)")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Guest Reset Successfully")




def taskmanager():
    try:
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')
        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))
        open_process = Pymem("Taskmgr.exe")
        inject_dll(open_process.process_handle, dll_path_bytes)
    except:
        pass
    #print("Streamer is Online")
    process_name = "Taskmgr.exe"

    try:
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        #print("Task Manager Injected DLL Successfully") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found")
    except Exception as e:
        print(f"Error: {e}")

def StartChams():
    #print("StartChams started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'glew32.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Loaded") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")

def ChamsMenuV1():
    #print("ChamsMenuV1 started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormal.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Menu V1 Enabled") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")

def ChamsMenuV2():
    #print("ChamsMenuV2 started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormalv2.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Menu Enabled") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")

def ChamsGlow():
    #print("ChamsGlow started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'GLOW.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Glow Enabled") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")

def ChamsBlue():
    #print("ChamsBlue started")
    process_name = "HD-Player"

    try:
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Blue.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Blue Enabled") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")

def HDRMap():
    #print("HDRMap started")
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MapHdr.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        inject_dll(open_process.process_handle, dll_path_bytes)
        print("HDR Map Enabled") 

    except pymem.exception.ProcessNotFound:
        print("Emulator Not Running")
    except Exception as e:
        print(f"Error: {e}")