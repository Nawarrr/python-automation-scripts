import subprocess
import re

# netsh wlan show profiles : gets all profiles
# netsh wlan show profile <name> : gets profile info 
# netsh wlan show profile <name> key=clear : gets profile info and shows the password
 
def wifi_passwords_getter():
    wifi_networks = subprocess.run(["netsh" , "wlan" , "show" , "profiles"] ,
                                    capture_output=True).stdout.decode()


    profile_names = re.findall("    All User Profile     : (.*)\r" , wifi_networks)

    wifis = []

    # if there is wifi networks
    if profile_names:
        for name in profile_names:
            wifi = {}

            wifi_info = subprocess.run(["netsh" , "wlan" , "show" , "profile" , name] ,
                                        capture_output=True).stdout.decode()
            # Checking if the Security key exist and not hidden 
            if re.search("    Security key           : Present" , wifi_info):
                wifi["ssid"] = name
                profile_info_with_password = subprocess.run(["netsh" , "wlan" , "show" , "profile" , name , "key=clear"] ,
                                                            capture_output=True).stdout.decode()

                password = re.search("    Key Content            :(.*)\r" , profile_info_with_password)


                if password :
                    wifi['password'] = password[1]
                else:
                    wifi['password'] = None
                
                wifis.append(wifi)

    return wifis


def main():
    wifis = wifi_passwords_getter()
    for i in wifis :
        print(i)


main()