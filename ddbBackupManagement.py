#!/usr/bin/env python3
""" 20180730 rescamil Deployment script for DDB2 Backup functions.
"""
__version__ = '0.1.1'

import ddbDropBU
import ddbBackup
drop = ddbDropBU.TableDropBU()
save = ddbBackup.TableBackup()
def main():
  drop()
  save()
