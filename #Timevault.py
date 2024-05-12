#Timevault

# This is code to encrypt a file for an indeterminate (user-set) amount of time; most typically in months/weeks scale. 
# 
# Startup: Greet user, present information manual, output prompt text to start: 
# "Welcome to Timevault. 
# Current timelock settings are for: n weeks
# Current file directory is: /fileDirectory

# Press 'enter' to begin.


# Enter 'edit' to change settings.
# Enter 'help' for more information.

# >_
# "
# 
# On choosing a file directory (for now*, hardcode to League), use pyOS to create a folder "Encrypted Files" internal to the TimeVault directory.
# Create folder: "Program Files"
# Create class object within TimeVault code: define as 'encryptedFile'
#   parameters: timeIn, jailTime, fileSize, encryptionKey, originalDirectory, fileName, fileNumber
# Create class object within "Program Files": define as 'keyChain'
#   parameters: fileNumber, keyNumber, [clutter dummyNumber series? To make it harder to decrypt]
#
# Move files from selected directory to a container within /TimeVault.
# Create a class instance of encryptedFile
# Initalize it according to the file to be encrypted
# Run an encryption method on the file to be encrypted, and store relevant data in both the encryptedFile variable, as well as on the keyring
# Every new day, have TimeVault check its inmates -- if Jailtime exceeds the distance to timeIn, decrypt the file with the relevant keyRing entry.
# Return the decrypted file to its original file directory.
#
#
# * This would be best meshed with a GUI, wherein locations could be selected through a traditinal file-window manager.
# Security should be considered -- this is not a robust file encryption scheme, since all keys are visible within keyChain.
# Keychain could be encrypted elsehow (consider private data center & API calls for business use). 
# For user-end simple encryption, generating a large enough set of random data to obfuscate the true term (vulnerable to automation)

import os
from cryptography.fernet import Fernet
import datetime
import sqlite3

class cell: 
    def __init__(inputKey, inputTimeIn, inputJailTime, inputOriginalDirectory, inputFileName, inputContents, inputIdentifier):
        self.key = inputKey
        self.timeIn = inputTimeIn
        self.jailTime = inputJailTime
        self.originalDirectory = inputOriginalDirectory
        self.fileName = inputFileName
        self.contents = inputContents
        self.identifier = inputIdentifier   

    def __str__(self):
        return(f"Recorded file contents are: {self.Contents}\nFile release date is: {calculateRelease(self.timeIn, self.jailTime)} (YYYY-MM-DD)\n")     
    
    def encryptFile(self):  #note that the "self" argument allows access to all class parameters
        currentDate = datetime.datetime.today() # returns date in format: YYYY-MM-DD
        calculateRelease(currentDate, jailTime)


        #record calculateRelease alongside information on: key, originalDirectory
        #file management/jailing is addressed here

        encryptionMethod = Fernet(self.key)

        with open(fileName, "rb") as file:
            fileData = file.read()
        encryptedData = encryptionMethod.encrypt(fileData)

        with open(fileName + ".encrypted", "wb") as encrypted_file:
            encrypted_file.write(encrypteData)
            #write a copy of encrypted data to timeVault inventory

        #delete original .exe file

# Example usage

write_key_to_file(key, "encryption_key.key")  # Save the key to a file (keep it secure)
file_to_encrypt = "file_to_encrypt.txt"  # Replace with the path to your file
encrypt_file(file_to_encrypt, key)




    def decryptFile(self):
        print(f"{self.contents} has finished its jail time! Now decrypting...\n")
        #this also returns the incarcerated file to its home

        

def calculateRelease(timeIn, jailTimeWeeks):
    #expect timeIn to be of the format: YYYY-MM-DD
    releaseDate = timeIn + datetime.timedelta(weeks=jailTimeWeeks)
    return releaseDate

def checkSentence(file, currentDate):
    if (file.timeIn + file.jailTime) <= (datetime.datetime.today()):
        return True
    else:
        return False

def generateKey():
    return Fernet.generate_key()

def makeInventory():
    inventory = "./Inventory" #could be iterated in a loop -- for files in [], if not os.[x] exists ...
    if not os.inventory.exists(inventory):
        os.mkdir(inventory)
        print("Folder {inventory} created!")
    else:
        continue

# ------------------------------------------------------------
# Main 
# ------------------------------------------------------------


defaultFileDirectory = "/defaultFileDirectory"
targetFile = "LeagueofLegends.exe"
startupMessage = "Welcome to Timevault. \nCurrent timelock settings are for: n weeks\nCurrent file directory is: " + defaultFileDirectory + "\n" + f"You are looking to encrypt: {targetFile}" + "\n\nPress 'enter' to begin.\n\nEnter 'edit' to change settings.\nEnter 'help' for more information."
promptIterationMessage = "Continue.\nPress 'enter' to begin program, using values as defined previously"
helpString = "help"
editString = "edit"

global timeVaultInventory = "./Inventory"

input(startupMessage) = userChoice
while True:
    if(upper.helpstring == upper.userChoice)
        print("Actually I haven't filled in the help section yet. Good luck.")
        input(userChoice)
    if(upper.editstring == upper.userChoice)
        print("Here's where you will be able to edit variables, later")
        input(userChoice)
    if(len.userChoice == 0)
        break

key = generateKey()
# ------------------------------------------------------------
# Reference 
# ------------------------------------------------------------


# ------------------------------
# DECRYPT
# ------------------------------

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename.replace(".encrypted", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Example usage
key = load_key_from_file("encryption_key.key")  # Load the key from the file
file_to_decrypt = "file_to_encrypt.txt.encrypted"  # Replace with the path to your encrypted file
decrypt_file(file_to_decrypt, key)
