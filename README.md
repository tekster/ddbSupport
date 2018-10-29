19-Jun-2018 {rescamil}  DynamoDB python scripts for creating/replacing all DDB tables per AWS account
Requirements:  scripts require Python3 (3.4.7 and above)  Boto3 and AWS client installed on local/remote host
  Script will apply changes to AWS_PROFILE or ~/.aws/credentials location

ddbDropBU.py will drop all existing backups
ddbBackup.py will backup all prod tables and list non-prod tables based on table names
    ignores tables that contain: (%test%, %beta%, %gamma%)
ddbListTab.py will list tables in prod/non-prod categories
ddbBackupManagement.py will execute drop/backup, and must live in same directory and executes backup/drop

sample crontab:
06 19 * * * PATH=$PATH:/usr/local/bin/AmazonAwsCli/bin ; /home/rescamil/ddb/ddbBackupManagement.py
