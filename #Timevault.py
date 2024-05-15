#Timevault
#Jacob Mattie, May 13, 2024



# ------------------------------------------------------------
# Tasklist: 
#
# Update functions to use database features: encryptFile, DecryptFile, mostRecentIdentifier
# For public release: require that encrypted files have the extension '.exe' (to lock out casual ransomware uses)
# Develop a GUI to select files to be encrypted
# 
# ------------------------------------------------------------



# This is code to encrypt a file for an indeterminate (user-set) amount of time; most typically in weeks scale. 
# Security should be considered -- this is not a robust file encryption scheme, since all keys are visible within keyChain.
# Keychain could be encrypted elsehow (consider private data center & API calls, should this be expanded for business use). 
# For a user-end simple encryption, generating a large enough set of random data to obfuscate the true term (vulnerable to automated attacks)

#Future improvements:
	# Write a .bat script to parse timevault cells on computer startup (so files are decrypted when appropriate)
	# On TimeVault startup, check jail times. If none are due for release, exit the program to save computer power.

import os
from cryptography.fernet import Fernet
import datetime
import sqlite3

# class cell: 
#     def __init__(inputKey, inputReleaseDate, inputOriginalDirectory, inputFileName, inputContents, inputIdentifier):
#         self.key = inputKey
#         self.releaseDate = inputReleaseDate
#         self.originalDirectory = inputOriginalDirectory
#         self.fileName = inputFileName
#         self.contents = inputContents       #human-readable
#         self.identifier = inputIdentifier   #numerical
#         self.encryptionMethod = Fernet(self.key)
#
    # def __str__(self):
    #     if (self.contents == ""):
    #         return(f"File release date is: day: {releaseDate.day}, month: {releaseDate.month}, of {releaseDate.year}\n")     
    #     else:
    #         return (f"Recorded file summary is: {self.Contents}\n\nFile release date is:  day: {releaseDate.day}, month: {releaseDate.month}, of {releaseDate.year}\n\n")     
    
    # def encryptFile(self):  #note that the "self" argument allows access to all class parameters
    #     #record calculateRelease alongside information on: key, originalDirectory
    #     os.chdir(originalDirectory)
    #     with open(fileName, "rb") as file:
    #         saveStatus = False
    #         fileData = file.read()
    #         encryptedData = encryptionMethod.encrypt(fileData)
    #         os.chdir(timeVaultInventory)
    #         with open(fileName + ".encrypted", "wb") as encrypted_file:
    #             encrypted_file.write(encryptedData)
    #             saveStatus = True
    #         os.chdir(originalDirectory)
    #         if (encryptSaveStatus == True):
    #             os.remove(fileName)           #only removes the unencrypted file once the duplicate has been successfully saved
    #         os.chdir(timeVaultDirectory)

    # def decryptFile(self):
    #     print(f"{self.contents} has finished its jail time! Now decrypting...\n")
    #     os.chdir("./Inventory")
    #     with open(fileName + ".encrypted", "rb") as file:
    #         saveStatus = False
    #         fileData = file.read()
    #         decryptedData = encryptionMethod.decrypt(fileData)
    #         os.chdir(originalDirectory)
    #         with open(fileName, "wb") as decryptedFile:
    #             decryptedFile.write(decryptedData)
    #             saveStatus = True
    #         os.chdir(timeVaultInventory)
    #         if (encryptSaveStatus == True):
    #             os.remove(fileName + ".encrypted")           #only removes the encrypted file once the duplicate has been successfully restored
    #             os.chdir(timeVaultDirectory)

    # def checkSentenceDone(self): #boolean return
    #     if ((self.releaseDate) <= datetime.datetime.today()):
    #         return False
    #     else:
    #         return True


class warden:
    def __init__(inputKey, inputIdentifier, inputConnection, inputCursor):
        self.key = inputKey
        self.identifier = inputIdentifier
        self.connection = inputConnection
        self.cursor = inputCursor
        self.encryptionMethod = Fernet(self.key)

        def releaseFile(self.key, self.identifier):


def calculateRelease(timeIn, jailTimeWeeks): #returns date in YYYY-MM-DD. Can call for calculateRelease(timeIn, jailTimeWeeks).year
    releaseDate = timeIn + datetime.timedelta(weeks=jailTimeWeeks)
    return releaseDate

def generateKey():
    return Fernet.generate_key()

def mostRecentIdentifier(): #generates the next available identifier number with which to associate a cell. Should be replaced with SQL someday
    os.chdir(timeVaultInventory)

    with open("Identifiers.txt", "r") as file:
        identifier = int(file.readline().strip())

    with open("Identifiers.txt", "w") as file:
        file.write(identifier + 1)

    os.chdir(timeVaultDirectory)
    return identifier

def encryptFile(connection, cursor, key, identifier, releaseDate, originalDirectory, fileName):

def releaseFile(connection, cursor, key, identifier):
    

# ------------------------------------------------------------
# Main 
# ------------------------------------------------------------


global targetFileDirectory = "/targetFileDirectory"
global timeVaultDirectory = os.path.dirname(__file__)
global inventoryString = "/Inventory"
global inventory = f".{inventoryString}"
global timeVaultInventory = timeVaultDirectory + inventoryString
targetFile = "LeagueofLegends.exe"
global jailTimeWeeks = 6 #default value; should be amenable to user-directed changes

startupMessage = f"Welcome to Timevault. \nCurrent timelock settings are for: {jailTimeWeeks} weeks\nCurrent target file directory is: " + targetFileDirectory + "\n" + f"You are looking to encrypt: {targetFile}" + "\n\nPress 'enter' to begin.\n\nEnter 'edit' to change settings.\nEnter 'help' for more information."
promptIterationMessage = "Continue.\nPress 'enter' to begin program, using values as defined previously"
helpString = "help"
editString = "edit"

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

userComments = input("Would you like to associate comments with the file?\n")

key = generateKey()
identifier = mostRecentIdentifier()
os.chdir(timeVaultInventory)

convict = cell(key, calculateRelease(), targetFileDirectory, targetFile, userComments, identifier)

# with open("Inventory.txt", "a") as file:
#     file.write(identifier + ", ")  # Writing a numerical value, followed by a comma delimiter
#     keyStr = key.decode('utf-8')  # Decoding bytes to string
#     file.write(keyStr)

#     currentDate = datetime.datetime.today() # returns date in format: YYYY-MM-DD
#     releaseDate = calculateRelease(currentDate, jailTimeWeeks)

convict.encryptFile() #################################################################################

conn = sqlite3.connect("Program Files.db")
cursor = conn.cursor()

if not os.inventory.exists(inventory): #create database tables during the initial setup
    os.mkdir(inventory)
    print("Folder {inventory} created!")
    os.chdir(timeVaultInventory)
    # with open("Inventory.txt", "w") as file:
    # with open("Identifiers.txt", "w") as file:
    create_cellTable = '''
    CREATE TABLE IF NOT EXISTS prisonerList (
        identifier INTEGER PRIMARY KEY,
        fileName TEXT,
        originalDirectory TEXT,
        encryptedFile BLOB,     #Binary Large Object (i.e. encrypted .exe file)
        cell_number INTEGER
    )
    '''
    create_keychainTable = '''
    CREATE TABLE IF NOT EXISTS guardKeychain (
        identifier INTEGER PRIMARY KEY,
        key BLOB,
        releaseDate DATE
    )
    '''
    os.chdir(timeVaultDirectory)

    cursor.execute(create_cellTable)
    cursor.execute(create_keychainTable)
    conn.commit()








