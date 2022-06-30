import boto3
s3 = boto3.client('s3',)
listObjSummary = s3.list_buckets()

for objSum in listObjSummary["Buckets"]
  print(objSum)




ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = ''

s3 = boto3.resource{
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret__access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version0='s3v4')
}

listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for objSum in listObjSummary:
  print('Item:')
  print(objSum.key)
print("Done")




BUCKET_NAME = 'Ejemplo'

session = boto3.session.Session(profile_name='miguel')
s3 = session.resource('s3')

listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for objSum in listObjSummary:
  print('Item:')
  print(objSum.key)
print("Done")