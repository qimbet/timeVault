#Timevault
#Jacob Mattie, May 13, 2024

# This is code to encrypt a file for an indeterminate (user-set) amount of time; most typically in weeks scale. 
# Security should be considered -- this is not a robust file encryption scheme, since all keys are visible within keyChain.
# Keychain could be encrypted elsehow (consider private data center & API calls, should this be expanded for business use). 
# For a user-end simple encryption, generating a large enough set of random data to obfuscate the true term (vulnerable to automated attacks)

#Future improvements:
	# Write a .bat script to parse timevault cells on computer startup (so files are decrypted when appropriate)
	# On TimeVault startup, check jail times. If none are due for release, exit the program to save computer power.
    # Develop a GUI to select files to be encrypted

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

fileName = "LeagueofLegends.exe"

conn = sqlite3.connect("timeVault.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE if NOT EXISTS jail(
            identifier INT, 
            convict BLOB, 
            PRIMARY KEY(identifier))""")

cursor.execute("""CREATE TABLE if NOT EXISTS wardenRecords(
            identifier INT, 
            originalFileLocation TEXT, 
            originalFilename TEXT, 
            releaseDate DATETIME, 
            PRIMARY KEY(identifier))""")

conn.commit()   #use this line whenever the table is updated

# --------------------------------------------------------------------------------------------------------------------------

#                                        Function Definitions 

# --------------------------------------------------------------------------------------------------------------------------

def encryptFile(identifier, key, originalFileDirectory, fileName, jailTimeWeeks, conn, cursor):  #copies and encrypts target file; 
    #record calculateRelease alongside information on: key, originalFileDirectory
    #timeVaultInventory: Encrypted files are stored here. This is the 'prison'
    encryptionMethod = Fernet(key)

    os.chdir(originalFileDirectory)
    encryptedData = encryptionMethod.encrypt(fileData)

    os.chdir(timeVaultInventory)

    cursor.execute("""
        INSERT INTO jail (identifier, convict)
        VALUES (?, ?)
    """(identifierInput, encryptedData))

    cursor.execute("""
        INSERT INTO wardenRecords (identifier, originalFileLocation, originalFileName, releaseDate)
        VALUES (?, ?, ?, ?)
    """(identifierInput, originalFileDirectory, fileName, calculateRelease(jailTimeWeeks)))    

    conn.commit()   #use this line whenever the table is updated

    os.chdir(originalFileDirectory)
    os.remove(fileName)           
    os.chdir(timeVaultDirectory)

def decryptFile(identifierInput, key, conn, cursor):
    encryptionMethod = Fernet(key)

    cursor.execute("""
        SELECT convict
        FROM jail
        WHERE identifier = ?;    
    """, (identifierInput,))
    fileData = cursor.fetchone()

    cursor.execute("""
        SELECT *
        FROM wardenRecords
        WHERE identifier = ?;    
    """, (identifierInput,))

    fileInfo = cursor.fetchall() #(identifier, originalDirectory, filename, releasedate)

    originalDirectory = fileInfo[1]
    fileName = fileInfo[2]

    decryptedFile = encryptionMethod.decrypt(fileData) 
    os.chdir(originalDirectory)

    with open((fileName), "wb") as decryptedFile:       #to be edited if we want to differentiate files based on type (e.g. .exe)
        decryptedFile.write(decryptedData)

        cursor.execute("DELETE FROM jail WHERE identifier = ?", (identifier,))
        cursor.execute("DELETE FROM wardenRecords WHERE identifier = ?", (identifier,))
        conn.commit()   #use this line whenever the table is updated

    os.chdir(timeVaultInventory)

def checkRelease(cursor):
    cursor.execute("""
        SELECT key, identifier
        FROM jail
        WHERE releaseDate < DATE('now');    
    """)
    #date('now') function returns the date as text in this format: YYYY-MM-DD
    results = cursor.fetchall()
    return results

def calculateRelease(jailTimeWeeks): #returns date in YYYY-MM-DD
    releaseDate = datetime.datetime.now() + datetime.timedelta(weeks=jailTimeWeeks)
    return releaseDate

def generateKey():
    return Fernet.generate_key()
        
def newIdentifier(cursor)
    while(true):
        testIdentifier = random.randint(1,maxNumberOfEncryptions) #this allows up to 1000 programs to be encrypted at a time
        cursor.execute("""
                       SELECT 1
                       FROM jail
                       WHERE identifier = ?
                    """, (testIdentifier,))
        result = cursor.fetchone()
        if result != 1: 
            return testIdentifier

# --------------------------------------------------------------------------------------------------------------------------

#                                        Main 

# --------------------------------------------------------------------------------------------------------------------------

if not os.path.exists(timeVaultInventory): #create database tables during the initial setup
    os.mkdir("Inventory")
    print("Folder 'Inventory' created!")
    os.chdir(timeVaultDirectory)

toRelease = checkRelease(conn, cursor) #checkRelease returns a list of tuples; (identifier, key)
for element in toRelease:
    decryptFile(element[0], element[1], conn, cursor)

startupMessage = f"""Welcome to Timevault. \nCurrent timelock settings are for: {jailTimeWeeks} weeks\n
                    Current target file directory is: {targetFileDirectory} \n
                    You are looking to encrypt: {fileName} \n\n
                    Press 'enter' to begin.\n\n
                    Enter 'edit' to change settings.\n
                    Enter 'help' for more information."""

promptIterationMessage = "Continue.\nPress 'enter' to begin program, using values as defined previously"
helpString = "help"
editString = "edit"

userChoice = input(startupMessage)
while True:
    if(upper.helpstring == upper.userChoice)
        print("Actually I haven't filled in the help section yet. Good luck.")
        input(userChoice)
    if(upper.editstring == upper.userChoice)
        print("Here's where you will be able to edit variables. But later. Once I build that feature in. :P")
        input(userChoice)
    if(len.userChoice == 0)
        break


key = generateKey()
identifier = newIdentifier()
os.chdir(timeVaultInventory)

encryptFile(key, identifier, targetFileDirectory, fileName, conn, cursor)

conn.close()