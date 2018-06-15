#!/usr/bin/env python3
""" 20180613 rescamil   development module to backup current DDB tables
    Reference doc: https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.list_backups
    attempt to remove test/beta/gamma from dictionary list
"""
__version__ = '0.0.1'
import boto3
import datetime

client = boto3.client('dynamodb')
now = datetime.datetime.now()
timeStamp = now.strftime("%Y%m%d%H%M")

def TableBackup():
    response = client.list_tables(
      Limit=100
    )

    tableCnt = 1
    for key, val in response.items():
           for tname in val:
               if tname.index('beta'):
                 print(index)
                 if tname.lower() not in ('beta', 'gamma', 'test'):
                    tableCnt += 1
                    # print("aws dynamodb create-backup --table-name " + tname + " --backup-name " + tname + "-" + timeStamp + "\n")
                    print(tname + " | " + tname.lower() + " not in list\n")
               else:
                    print(tname + " | " + tname.lower() + " found!\n")
        else:
           print("\n")
    print(str(tableCnt) + " tables")

def main():
    TableBackup()

if __name__ == "__main__":
   main()
