####18-04-2023
# Authors:Alican Dogan

# %%
# Title: Alarm Info Modülü
# Description: Günün belli saatlerinde alarm bilgilerini mail olarak gönderir.



import json, logging, requests
from pymongo import MongoClient
from datetime import datetime
import pandas as pd


# %%

# @TODO: connString'i .env dosyası
connString = ""

## logger

logger = logging.getLogger()
logger.setLevel(logging.INFO)

##
# Lambda handler
# @param event: Event
# @param context: Context
# @return: İşlem sonucu
##

def lambda_handler(event, context):


    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully.')
    }
