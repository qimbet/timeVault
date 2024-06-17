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

#SQL tables: 
#1 table contains in each row:
# BLOBFile, Identifier

#2nd table contains, in each row: 
#identifier, original file location, original filename, original file extension, releaseDate

import os
from cryptography.fernet import Fernet
import datetime
import sqlite3
import random

global targetFileDirectory = "/targetFileDirectory"

global timeVaultDirectory = os.path.dirname(os.path.realpath(__file__))     #this needs verification imo
global inventoryString = "/Inventory"
global timeVaultInventory = timeVaultDirectory + inventoryString

global jailTimeWeeks = 6 #default value; should be amenable to user-directed changes
global maxNumberOfEncryptions = 1000

targetFile = "LeagueofLegends.exe"

# --------------------------------------------------------------------------------------------------------------------------

#                                        Function Definitions 

# --------------------------------------------------------------------------------------------------------------------------

def encryptFile(key, identifier, originalFileDirectory, fileName, connection, cursor):  #copies and encrypts target file; 
    #record calculateRelease alongside information on: key, originalFileDirectory
    #timeVaultInventory: Encrypted files are stored here. This is the 'prison'
    encryptionMethod = Fernet(key)
    saveStatus = False

    os.chdir(originalFileDirectory)
    encryptedData = encryptionMethod.encrypt(fileData)

    os.chdir(timeVaultInventory)
    SQLOPERATION1 := add_to_table: encryptedData      #-------------------------------------------------- add to "BLOB-prisoner" colum
    SQLOPERATION1 := add_to_table: identifier     #-------------------------------------------------
    conn.commit()   #use this line whenever the table is updated

    os.chdir(originalFileDirectory)
    os.remove(fileName)           #only removes the unencrypted files once the duplicate has been successfully saved
    os.chdir(timeVaultDirectory)

def decryptFile(key, identifier, connection, cursor):
    encryptionMethod = Fernet(key)
    saveStatus = False

    SQLOPERATION1 := search_by_identifier #-------------------------------------------------- identify row to decrypt
    SQLOPERATION1 := fileData = lookup_BLOB-prisoner_file  #--------------------------------------------------

    SQLOPERATION2 := lookup(fileName)
    SQLOPERATION2 := lookup(fileExtension)
    SQLOPERATION2 := lookup(originalDirectory)
    conn.commit()   #use this line whenever the table is updated


    decryptedFile = encryptionMethod.decrypt(fileData) 
    os.chdir(originalDirectory)
    with open((fileName+fileExtension), "wb") as decryptedFile:
        decryptedFile.write(decryptedData)
        saveStatus = True

    os.chdir(timeVaultInventory)
    if (encryptSaveStatus == True):
        os.remove(fileName + ".encrypted")           #only removes the encrypted file once the duplicate has been successfully restored
        os.chdir(timeVaultDirectory)
        SQLOPERATION1 remove rows
        SQLOPERATION2 remove rows
        conn.commit()   #use this line whenever the table is updated

def checkRelease(conn, cursor):
    

def calculateRelease(timeIn, jailTimeWeeks): #returns date in YYYY-MM-DD. Can call for calculateRelease(timeIn, jailTimeWeeks).year
    releaseDate = timeIn + datetime.timedelta(weeks=jailTimeWeeks)
    return releaseDate

def checkSentenceDone(): #boolean return
    if ((releaseDate) <= datetime.datetime.today()):
        return False
    else:
        return True

def generateKey():
    return Fernet.generate_key()
        
def newIdentifier(connection, cursor)
    while(true):
        testIdentifier = random.randint(1,maxNumberOfEncryptions) #this allows up to 1000 programs to be encrypted at a time
        if(SQLOPERATION2 does not contain testIdentifier):
            return identifier

# --------------------------------------------------------------------------------------------------------------------------

#                                        Main 

# --------------------------------------------------------------------------------------------------------------------------

if not os.path.exists(timeVaultInventory): #create database tables during the initial setup
    os.mkdir("Inventory")
    print("Folder 'Inventory' created!")
    os.chdir(timeVaultDirectory)

startupMessage = f"Welcome to Timevault. \nCurrent timelock settings are for: {jailTimeWeeks} weeks\nCurrent target file directory is: {targetFileDirectory} \nYou are looking to encrypt: {targetFile}" + "\n\nPress 'enter' to begin.\n\nEnter 'edit' to change settings.\nEnter 'help' for more information."
promptIterationMessage = "Continue.\nPress 'enter' to begin program, using values as defined previously"
helpString = "help"
editString = "edit"

input(startupMessage) = userChoice
while True:
    if(upper.helpstring == upper.userChoice)
        print("Actually I haven't filled in the help section yet. Good luck.")
        input(userChoice)
    if(upper.editstring == upper.userChoice)
        print("Here's where you will be able to edit variables. But later. Once I build that feature in. :P")
        input(userChoice)
    if(len.userChoice == 0)
        break

conn = sqlite3.connect("timeVault.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE if NOT EXISTS jail(identifier INT, jailFile BLOB, PRIMARY KEY(identifier))")
cursor.execute("CREATE TABLE if NOT EXISTS wardenRecords(identifier INT, originalFileLocation TEXT, originalFilename TEXT, originalFileExtension TEXT, releaseDate DATETIME, PRIMARY KEY(identifier))")
conn.commit()   #use this line whenever the table is updated

key = generateKey()
identifier = newIdentifier()
os.chdir(timeVaultInventory)


encryptFile(key, identifier, targetFileDirectory, fileName, conn, cursor)

decryptFile(key, identifier, conn, cursor)