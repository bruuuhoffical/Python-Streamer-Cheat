from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os
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
    try:
        # Open the process
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        return

    try:
        if proc:
            print("\033[31m[>]\033[0m Searching Entity...")
            # Scan for entities
            global aimbot_addresses
            entity_pattern = mkp("01 00 00 00 00 00 00 00 ?? ?? ?? ?? 00 00 00 00 ?? ?? ?? ?? 01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 01")
            aimbot_addresses = pattern_scan_all(proc.process_handle, entity_pattern, return_multiple=True)

            if aimbot_addresses:
                print("Aimbot Loaded")
                
            else:
                print("\033[31m[!]\033[0m Aimbot Not Found")
    
    except:
        print("")
    finally:
        if proc:
            proc.close_process()
    return "Fitur Berhasil Di Load"
    


def HEADON():
    try:
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            original_value = []

            for current_entity in aimbot_addresses:
                # Save original values before overwriting
                original_2A = read_bytes(proc.process_handle, current_entity + 0x2A, 4)
                original_AA = read_bytes(proc.process_handle, current_entity + 0x158, 4)

                original_value.append((current_entity, original_2A, original_AA))

                # Read values from source offsets
                value_2A = read_bytes(proc.process_handle, current_entity + 0x2A, 4)
                value_AA = read_bytes(proc.process_handle, current_entity + 0x158, 4)

                # Write those values to destination offsets
                write_bytes(proc.process_handle, current_entity + 0x26, value_2A, len(value_2A))    
                write_bytes(proc.process_handle, current_entity + 0x154, value_AA, len(value_AA))    

    except pymem.exception.ProcessNotFound:
        print("Process not found")
        return
    finally:
        if proc:
            proc.close_process()

    return "AIMBOT HEAD ON"

# def HEADOFF():
    try:
        proc = Pymem("HD-Player")
        
        if original_value:
            for i in original_value:
                entity_address = i[0]
                original_2A = i[1]
                original_AA = i[2]

                # Restore original values to source offsets
                write_bytes(proc.process_handle, entity_address + 0x2A, original_2A, len(original_2A))
                write_bytes(proc.process_handle, entity_address + 0xAA, original_AA, len(original_AA))

    except pymem.exception.ProcessNotFound:
        print("Process not found")
        return
    finally:
        if proc:
            proc.close_process()

    return "AIMBOT HEAD OFF"

def HEADOFF():
    try:
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            original_value = []

            for current_entity in aimbot_addresses:
                # Save original values before overwriting
                original_2A = read_bytes(proc.process_handle, current_entity + 0x2A, 4)
                original_AA = read_bytes(proc.process_handle, current_entity + 0x154, 4)

                original_value.append((current_entity, original_2A, original_AA))

                # Read values from source offsets
                value_2A = read_bytes(proc.process_handle, current_entity + 0x2A, 4)
                value_AA = read_bytes(proc.process_handle, current_entity + 0x154, 4)

                # Write those values to destination offsets
                write_bytes(proc.process_handle, current_entity + 0x26, value_2A, len(value_2A))    
                write_bytes(proc.process_handle, current_entity + 0x158, value_AA, len(value_AA))    

    except pymem.exception.ProcessNotFound:
        print("Process not found")
        return
    finally:
        if proc:
            proc.close_process()

    return "AIMBOT HEAD OFF"


def SniperScopeon():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.")

    try:
       if proc:
        print("Enabling Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    print("Sniper Scope Enabled!")

def SniperScopeoff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.")

    try:
       if proc:
        print("Disabling Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),34)
    print("Sniper Scope Disabled!")


def SniperAimon():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling Sniper Aim", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Aim Enabled!")

def SniperAimoff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling Sniper Aim", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("01 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 CB 00 00 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Aim Disabled!")


def SniperSwitchon():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling Sniper Switch", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Switch Enabled!")

def SniperSwitchoff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling Sniper Switch", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 3c 00 00 80 00 00 00 00 00 04 00 00 00 00 00 80 3F"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 ?? 00 00 80 ?? 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 8F C2 35 3F 9A 99 99 3F 00 00 80 3F 00 00 00 00 00 00 80 3F 00 00 80 3F 00 00 80 3F 00 00 00 00 00 00 00 00 00 00 00 3F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Switch Disabled!")

def SniperSwitchfixOn():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling Sniper Delay Fix", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 60"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 59")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Delay Fix Enabled!")

def SniperSwitchfixOff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling Sniper Delay Fix", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("49 86 00 EB 00 00 00 EA 00 59"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("49 86 00 EB 00 00 00 EA 00 60")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Sniper Delay Fix Disabled!")



def NoRecoilOn():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling No Recoil", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("03 0A 9F ED 10 0A 01 EE 00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 7A 44 F0"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("03 0A 9F ED 10 0A 01 EE 00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 00 00 F0")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("No Recoil Enabled!")

def NoRecoilOff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling No Recoil", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("03 0A 9F ED 10 0A 01 EE 00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 00 00 F0"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("03 0A 9F ED 10 0A 01 EE 00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 7A 44 F0")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("No Recoil Disabled")

def ScopeTracking2XOn():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling Scope Tracking 2X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 2X Enabled!")

def ScopeTracking2XOff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling Scope Tracking 2X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 29 5C"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("A0 42 00 00 C0 3F 33 33 13 40 00 00 F0 3F 00 00 80 3F")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 2X Disabled")

def ScopeTracking4XOn():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Enabling Scope Tracking 4X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 4X Enabled!")

def ScopeTracking4XOff():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.")
        return

    try:
        if proc:
            print("Disabling Scope Tracking 4X", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 5C 01 00"), return_multiple=True)
    except:
        print("aob not found")
        return

    if value:
        for addr in value:
            b = bytes.fromhex("00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 D0 3F 00 00 80 3F 01 00")
            write_bytes(proc.process_handle, addr, b, len(b))
    print("Scope Tracking 4X Disabled")



    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.")

    try:
       if proc:
        print("Disabling Head Tracking", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Head Tracking Disabled")


def ResetGuest():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.")

    try:
       if proc:
        print("Enabling Reset Guest", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Reset Guest Enabled!")

    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.")

    try:
       if proc:
        print("Disabling Reset Guest", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp(""), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex(""),16)
    print("Reset Guest Disabled!")




def taskmanager():
    process_name = "Taskmgr.exe"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Task Manager Injected DLL Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found!")
    except Exception as e:
        print(f"Error: {e}")

def StartChams():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'glew32.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Start Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")

def ChamsMenuV1():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormal.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Menu V1 Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")

def ChamsMenuV2():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cnormalv2.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Menu V2 Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")

def ChamsGlow():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'GLOW.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Chams Glow Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")

def HDRMap():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MapHdr.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("HDR Map Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")

