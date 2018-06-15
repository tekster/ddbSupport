#!/usr/bin/env python3
""" 12-Jun-2018 rescamil	attempting to created python scripts for automating backups for DDB tables
    				this is a copy from the aws ddb manual https://boto3.readthedocs.io/en/latest/reference/services/dynamodb.html
"""

import boto3

client = boto3.client('dynamodb')

response = client.list_tables(
    ExclusiveStartTableName='string',
    Limit=100
)

print(response)
