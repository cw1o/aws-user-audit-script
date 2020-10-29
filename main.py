# Imports 
import boto3, csv, os, datetime

iam = boto3.client("iam")

userList = []
userAccountInfo = [['User', 'Date Created', 'Password Last Used']] 
accessKeyInfo = [['User', 'Access Key ID', 'Status', 'Date Created', 'Last Used']]
consoleAuditFileName = "console-access-audit.csv"
programAuditFIleName = "programmatic-access-audit.csv"

# Get list of users
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    for user in response['Users']:
        userList.append(user['UserName'])
        newRow = []
        newRow.append(user['UserName'])
        newRow.append(user['CreateDate'].strftime("%d/%m/%Y"))
        if 'PasswordLastUsed' in user:
            newRow.append(user['PasswordLastUsed'].strftime("%d/%m/%Y"))
        else:
            newRow.append("Password Never Used")
        userAccountInfo.append(newRow)

# Get Access Keys from list of users
for item in userList:
    paginator = iam.get_paginator('list_access_keys')
    for response in paginator.paginate(UserName=item):
        for element in response['AccessKeyMetadata']:
            lastUsedInfo = iam.get_access_key_last_used(AccessKeyId=element['AccessKeyId'])
            newEntry = []
            newEntry.append(element['UserName'])
            newEntry.append(element['AccessKeyId'])
            newEntry.append(element['Status'])
            newEntry.append(element['CreateDate'].strftime("%d/%m/%Y"))
            if 'LastUsedDate' in lastUsedInfo['AccessKeyLastUsed']:
                newEntry.append(lastUsedInfo['AccessKeyLastUsed']['LastUsedDate'].strftime("%d/%m/%Y"))
            else:
                newEntry.append("Key Never Used")
            accessKeyInfo.append(newEntry)

# Create CSV's
if os.path.exists(consoleAuditFileName):
    os.remove(consoleAuditFileName)

if os.path.exists(programAuditFIleName):
    os.remove(programAuditFIleName)

# Console Access CSV
with open(consoleAuditFileName, 'w', newline='') as consoleFile:
    writer = csv.writer(consoleFile)
    writer.writerows(userAccountInfo)

# CLI / Programmatic Access CSV
with open(programAuditFIleName, 'w', newline='') as accessKeyFile:
    writer = csv.writer(accessKeyFile)
    writer.writerows(accessKeyInfo)
