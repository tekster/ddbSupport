#!/usr/bin/env python3
""" 20180613 rescamil	Development script to identify Python tables in this AWS account
    Reference: https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html#DynamoDB.Client.create_backup
    script output provides a commandline prompt of all DDB tables to back up
    script updated to call boto3 to drop table backups
"""
__version__ = '0.1.1'
import boto3

client = boto3.client('dynamodb')

def TableDropBU():
    response = client.list_backups(
    Limit=100
    )

    buCnt = 1
    for key, val in response.items():
        if key == 'BackupSummaries':
           for tname in val:
               buCnt += 1
               for key2, val2 in tname.items():
                   if key2 == 'BackupArn':
                      print("aws dynamodb delete-backup --backup-arn " + str(val2))
                      rmExec = client.delete_backup(
                        BackupArn=str(val2)
                        )
        else:
           print("\n")
    print("# " +str(buCnt) + " backups")

def main():
    TableDropBU()

if __name__ == "__main__":
   main()
