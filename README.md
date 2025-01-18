# Mc-Kali
Hack Interface for Kali Linux - Multi-Tool for Network Scanning,  Payload Creation and other !

This project is an interactive Python interface designed for Kali Linux users or any compatible system. It features tools for network scanning, payload generation using Metasploit, and input validation for IPs and ports. Perfect for cybersecurity enthusiasts looking to automate common tasks in a user-friendly environment.

Key Features:

  Custom ASCII Art Display:
      A colorful ASCII art welcome message for users.

  Network Scanning:
      Validate and scan IP ranges using nmap.
      Search for vulnerabilities in scanned systems.

  Metasploit Payload Generation:
      Generate payloads for Android, Windows, Linux, and macOS.
      Seamless integration with msfvenom and automatic launch of msfconsole.

  Input Validation:
      IP and port validation to prevent execution errors.

  Intuitive Interface:
      Navigate through an interactive menu.
      Clear messages and color-coded outputs with colorama for an enhanced user experience.

  Command Availability Check:
      Notify users if required tools like nmap or msfvenom are not installed.

Prerequisites:

  Python 3.12.7 (This project was created with this version),
  Python Modules: in requirements.txt,
  Required third-party tools:
      nmap for network scanning.
      msfvenom and msfconsole for payload generation.

Installation:

  Clone the repository:

    git clone https://github.com/username/hack-interface-kali.git
    cd hack-interface-kali

Install Python dependencies:

    pip install requirements.txt

Ensure nmap and Metasploit are installed:

    sudo apt-get install nmap
    sudo apt-get install metasploit-framework

Usage:

Run the main script with Python:

    python3 main.py

Navigate the menu to choose options like scanning a network or generating a payload.
