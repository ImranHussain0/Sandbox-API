# AWS Lambda funtion for results of Crowdsrike API submissions
# Author: Imran Hussain

import json
from falconpy import FalconXSandbox
import botocore 
import botocore.session 
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig 

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache( config = cache_config, client = client)

api_client = cache.get_secret_string('falcon_client')
api_secret = cache.get_secret_string('falcon_secret')

#  ************* Important Note ***************
# !!! DO NOT HARDCODE YOUR API CREDENTIALS !!!
# ********************************************

falcon = FalconXSandbox(client_id='api_client',
                        client_secret='api_secret'
                        )

def lambda_handler(event, context):
    response = falcon.get_reports(event)
    return {
            'statusCode': 200,
            'body': json.dumps(response, indent=4)
    }

#print(lambda_handler())