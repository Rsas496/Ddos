import os
import sys
import time

os.system("clear")

print("\n\n\n")
ab= "\033[96m        System Loading..."
for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")

time.sleep(2)
os.system("clear")
print("\n\n")
ab= "\033[91m    Successfully \033[92mLoaded\n"
for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
name = input("\033[93m    Your Name: ")

ab= "\033[95m    Hey "+name+", \033[94m Be Ethical..."
for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n")
time.sleep(2)
os.system("clear")

print("""\033[92m

  _____       _       _        
 / ____|     | |     | |       
| (___  _   _| | __ _| |_ ___  
 \___ \| | | | |/ _` | __/ _ \ 
 ____) | |_| | | (_| | ||  __/ 
|_____/ \__,_|_|\__,_|\__\___

\033[94m================================
\033[95mOwner    : Splunk
Telegram : Upcoming 
Facebook : Cyberlearn - Hub
Page     : Cyberlearn - Hub
Gorup    : Cyberlearn - Hub
\033[94m================================
""")


def install_termux_packages():
    print("📦/033[94m Updating Termux... CreateBy Cyber \n Cyberlearn - Hub\033[0m")
    os.system("pkg update -y")
    os.system("pkg upgrade -y")

    print("🔧 Installing basic tools...")
    os.system("pkg install python -y")
    os.system("pkg install git -y")
    os.system("pkg install curl -y")
    os.system("pkg install wget -y")
    os.system("pkg install nano -y")
    os.system("pkg install openssl -y")
    os.system("pkg install clang -y")
    os.system("pkg install zip -y")
    os.system("pkg install unzip -y")

    print("\033[91m✅ All basic Termux packages installed successfully!/n/033[92m⚙️ File Create by: Cyber (Educational Purpose Only)")

install_termux_packages()