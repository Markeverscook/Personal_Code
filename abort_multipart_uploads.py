import boto3
import csv

#This python script is going to use the local AWS CLI credentials configured on your local machine. If you do not have those configured you will need to configure those first.
def abort_multipart_uploads():
    #Setting up the client using your local AWS CLI creds
    s3api_client = boto3.client(
        's3', #Service
        region_name="us-east-1" #Region
    )
    #Opening the csv file with the list of keys and uploadids
    with open('c:/Users/path/to/file/vault2.csv', newline='') as read_obj:
        csv_reader = csv.DictReader(read_obj)
        #for loop to go through each row and value.
        for row in csv_reader:
            #Output what you are deleting
            print('Deleting the following:\nKey =',row['key_id'],'\nUpload ID =', row['upload_id'],'\n')
            #Store the output of the boto3 function into response to output later
            response = s3api_client.abort_multipart_upload(
                Bucket='bucket_name',
                Key=row['key_id'],
                UploadId=row['upload_id']
            )
            #Print response
            print(response)

abort_multipart_uploads()