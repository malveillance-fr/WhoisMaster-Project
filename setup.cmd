:: ========================================================================
::                            LICENCE D'UTILISATION
:: ========================================================================
:: Nom du programme : WhoisMaster
:: Développeur : Malveillance
:: Version : 1.0
:: Année : 2025
:: Droits d'auteur : © 2025 Malveillance. Tous droits réservés.
:: ========================================================================

:: FRANÇAIS :

:: 1. Ce programme est destiné uniquement à un usage légal et éducatif. 
:: L'utilisateur doit respecter les lois en vigueur sur la cybersécurité 
:: et la protection des données. Toute utilisation illégale est interdite.

:: 2. Il est interdit d'utiliser ce programme pour récupérer des informations 
:: sans l'autorisation du propriétaire du domaine. Toute tentative d'accès 
:: non autorisé est une infraction.

:: 3. L'utilisateur est entièrement responsable de son utilisation. 
:: Le développeur ne pourra être tenu responsable des conséquences d'un 
:: usage inapproprié.

:: 4. Ce programme est protégé par le droit d'auteur. Toute modification, 
:: revente ou redistribution sans autorisation est interdite.

:: 5. Ce programme est fourni sans garantie. Le développeur ne peut être 
:: tenu responsable des dysfonctionnements ou dommages éventuels.

:: ========================================================================

:: ENGLISH :

:: 1. This program is for legal and educational use only. The user must 
:: comply with cybersecurity and data protection laws. Any illegal use is 
:: prohibited.

:: 2. It is forbidden to use this program to retrieve information without 
:: the domain owner's consent. Any unauthorized access attempt is illegal.

:: 3. The user is fully responsible for its use. The developer is not liable 
:: for any consequences of improper use.

:: 4. This program is copyrighted. Any modification, resale, or redistribution 
:: without permission is prohibited.

:: 5. This program is provided without warranty. The developer is not 
:: responsible for any malfunctions or damages.

:: ========================================================================


color 5
cls

@echo off
title WhoisMaster - Setup
echo ==========================================
echo        Installing Dependencies...
echo ==========================================
python -m pip install --upgrade pip
python -m pip install whois pystyle

pip install whois 
pip install pystyle

pip3 install whois 
pip3 install pystyle

echo ==========================================
echo        Installation Complete!
echo ==========================================
cls

echo ==========================================
echo        Launching WhoisMaster...
echo ==========================================
python 	WhoisMaster.py

exit
