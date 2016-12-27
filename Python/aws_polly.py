# *********************************************************************
# Version:     2016.12.27                                             #
# Author:      Archer Huang                                           #
# License:     MIT                                                    #
# Description: Amazon Polly Service (Text To Speech)                  #
# *********************************************************************

import boto3

client = boto3.client(
    'polly',
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY',
    aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY',
    region_name = 'us-west-2'
)

polly_response = client.synthesize_speech(
	Text = "Hello world",
	OutputFormat = "mp3",
	VoiceId = "Joanna")

print polly_response

with open('polly_stream.mp3', 'wb') as f:
    f.write(polly_response['AudioStream'].read())