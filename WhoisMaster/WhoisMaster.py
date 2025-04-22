# ========================================================================
#                            LICENCE D'UTILISATION
# ========================================================================
# Nom du programme : WhoisMaster
# Développeur : Kazam
# Version : 3.6
# Année : 2025
# Droits d'auteur : © 2025 Malveillance. Tous droits réservés.
# ========================================================================
#
# FRANÇAIS :
#
# 1. Ce programme est destiné uniquement à un usage légal et éducatif. 
# L'utilisateur doit respecter les lois en vigueur sur la cybersécurité 
# et la protection des données. Toute utilisation illégale est interdite.
#
# 2. Il est interdit d'utiliser ce programme pour récupérer des informations 
# sans l'autorisation du propriétaire du domaine. Toute tentative d'accès 
# non autorisé est une infraction.
#
# 3. L'utilisateur est entièrement responsable de son utilisation. 
# Le développeur ne pourra être tenu responsable des conséquences d'un 
# usage inapproprié.
#
# 4. Ce programme est protégé par le droit d'auteur. Toute modification, 
# revente ou redistribution sans autorisation est interdite.
#
# 5. Ce programme est fourni sans garantie. Le développeur ne peut être 
# tenu responsable des dysfonctionnements ou dommages éventuels.
#
# ========================================================================
#
# ENGLISH :
#
# 1. This program is for legal and educational use only. The user must 
# comply with cybersecurity and data protection laws. Any illegal use is 
# prohibited.
#
# 2. It is forbidden to use this program to retrieve information without 
# the domain owner's consent. Any unauthorized access attempt is illegal.
#
# 3. The user is fully responsible for its use. The developer is not liable 
# for any consequences of improper use.
#
# 4. This program is copyrighted. Any modification, resale, or redistribution 
# without permission is prohibited.
#
# 5. This program is provided without warranty. The developer is not 
# responsible for any malfunctions or damages.
#
# ========================================================================


import whois
import pystyle
import sys
import getopt

def get_whois_info(query):
    try:
        w = whois.whois(query)
        whois_info = {key: value for key, value in w.items()}
        
        if not whois_info:
            return "No information available for this query."
        
        return whois_info
    except Exception as e:
        return f"Error: {str(e)}"

def display_whois_info(info):
    if isinstance(info, dict):
        print(pystyle.Colors.yellow + "\nWHOIS Information for the Domain/IP:")
        print(pystyle.Colors.blue + "-"*50)
        
        labels = {
            "domain_name": "Domain Name",
            "registrar": "Registrar",
            "creation_date": "Creation Date",
            "expiration_date": "Expiration Date",
            "updated_date": "Updated Date",
            "status": "Status",
            "name_servers": "Name Servers",
            "emails": "Emails",
            "org": "Organization",
            "country": "Country",
            "city": "City",
            "address": "Address",
            "phone": "Phone",
            "abuse_email": "Abuse Contact Email",
            "dnssec": "DNSSEC Status",
            "referral_url": "Referral URL",
            "created_date": "Creation Date",
            "changed_date": "Changed Date",
            "last_updated": "Last Updated"
        }
        
        for key, label in labels.items():
            if key in info:
                value = str(info[key])

                if "REDACTED FOR PRIVACY" in value:
                    if key == "city":
                        value = pystyle.Colors.red + "HIDE FOR PRIVACY"
                    elif key == "address":
                        value = pystyle.Colors.red + "HIDE FOR PRIVACY"
                    else:
                        value = pystyle.Colors.red + "HIDE FOR PRIVACY" 
                
                print(pystyle.Colors.cyan + f"[+] {label}: " + pystyle.Colors.green + value)
        
        print(pystyle.Colors.blue + "-"*50)
    else:
        print(pystyle.Colors.red + str(info))

def print_help():
    print(pystyle.Colors.green + "\nAvailable Commands:")
    print(pystyle.Colors.cyan + "wm -i {IP/Domain} : Get WHOIS information for an IP or Domain")
    print(pystyle.Colors.cyan + "help : Display available commands")

def main():
    if len(sys.argv) == 1:
        
        ascii_art = r"""
__        ___           _       __  __           _            
\ \      / / |__   ___ (_)___  |  \/  | __ _ ___| |_ ___ _ __ 
 \ \ /\ / /| '_ \ / _ \| / __| | |\/| |/ _` / __| __/ _ \ '__|
  \ V  V / | | | | (_) | \__ \ | |  | | (_| \__ \ ||  __/ |   
   \_/\_/  |_| |_|\___/|_|___/ |_|  |_|\__,_|___/\__\___|_|   
        
    """
    
        print(pystyle.Colors.green + ascii_art)  
        print("----------------------------------------")
        title = pystyle.Colors.yellow + "| WhoisMaster" + pystyle.Colors.blue + " - Investigation and Scan |"
        print(pystyle.Colors.green + title)
        print("----------------------------------------")
        query = input(pystyle.Colors.cyan + "\nEnter a domain or IP: " + pystyle.Colors.white)

        info = get_whois_info(query)
        display_whois_info(info)
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == "wm" and sys.argv[2] == "help":
            print_help()
        elif sys.argv[1] == "wm" and sys.argv[2].startswith("-i"):
            ip_or_domain = sys.argv[2][3:]
            info = get_whois_info(ip_or_domain)
            display_whois_info(info)
        else:
            print(pystyle.Colors.red + "Invalid command. Use 'wm help' to see available commands.")
    else:
        print(pystyle.Colors.red + "Invalid usage. Use 'wm help' to see available commands.")

if __name__ == "__main__":
    main()

input("")  
