#!/usr/bin/env python3
""" 20180613 rescamil   development module to backup current DDB tables
    Reference doc: https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.list_backups
    script output provides a commandline prompt of all DDB tables for specified account
"""
__version__ = '0.0.1'
import boto3
import datetime

client = boto3.client('dynamodb')
now = datetime.datetime.now()
timeStamp = now.strftime("%Y%m%d%H%M")
NoBackup = []

def TableBackup():
    response = client.list_tables(
      Limit=100
    )

    tableCnt = 1
    for key, val in response.items():
        if key == 'TableNames':
           for tname in val:
               tnameLower = tname.lower()
               if tnameLower.find('test') == -1:
                  if tnameLower.find('beta') == -1:
                     if tnameLower.find('gamma') == -1:
                        tableCnt += 1
                        print("aws dynamodb create-backup --table-name " + tname + " --backup-name " + tname + "-" + timeStamp)
                     else:
                      NoBackup.append(tname)
                  else:
                    NoBackup.append(tname)
               else:
                 NoBackup.append(tname)
        else:
           print("\n")
    print("# " + str(tableCnt) + " tables")
    
    for NoBU in NoBackup:
        print("# No Backup for Table:" + NoBU)

def main():
    TableBackup()

if __name__ == "__main__":
   main()
