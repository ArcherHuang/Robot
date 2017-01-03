import boto3

client = boto3.client(
    'rekognition',
    aws_access_key_id = 'YOUR_AWS_ACCESS_KEY',
    aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY',
    region_name = 'us-west-2'
)


p = open("/Users/Archer/Desktop/ngrok/test.jpg", 'rb')
reko_response = client.detect_faces(Image={
                                            'Bytes':bytearray(p.read())
                                          },
                                    Attributes=[
                                        'ALL'
                                    ])
p.close()

print reko_response