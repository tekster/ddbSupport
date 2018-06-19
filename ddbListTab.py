#!/usr/bin/env python3
""" 12-Jun-2018 rescamil	attempting to created python scripts for automating backups for DDB tables
    				this is a copy from the aws ddb manual https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html
"""
__version__ = '0.0.1'
import boto3

client = boto3.client('dynamodb')

def TableList():
    response = client.list_tables(
        Limit=100
    )

    tableCnt = 1
    NoBackup = []
    for key, val in response.items():
        if key == 'TableNames':
           for tname in val:

               tnameLower = tname.lower()
               if tnameLower.find('test') == -1:
                  if tnameLower.find('beta') == -1:
                     if tnameLower.find('gamma') == -1:
                        tableCnt += 1
                        print("Prod: " + tname)
                     else:
                        NoBackup.append(tname)
                  else:
                    NoBackup.append(tname)
               else:
                 NoBackup.append(tname)
        else:
           print("\n")
    print(str(tableCnt) + " tables")
    for NoBU in NoBackup:
        print("Non-Prod: " + NoBU)

def main():
    TableList()

if __name__ == "__main__":
   main()
