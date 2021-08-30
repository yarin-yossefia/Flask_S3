import boto3,botocore
from errors import *
import s3transfer

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIA2H2TIE6SUH7K3HPP',
    aws_secret_access_key='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'

)
file = "dog.jpg"
# select bucket
my_bucket = s3.Bucket('dcdevopstask')
# download file into current directory
for s3_object in my_bucket.objects.all():
    filename = s3_object.key
    #print(filename)
    if file in filename:
        full_path = str(filename)
print(full_path)
file = "dog.jpg"
try:
    s3.Bucket('dcdevopstask').download_file("dogs/dog.jpg", file)
    print("{} downloaded".format(full_path))
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        raise FileNotExist("the file not exist")

