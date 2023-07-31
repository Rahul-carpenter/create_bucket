import boto3

# Replace 'your_bucket_name' with the desired bucket name
bucket_name = 'rahulcarpenter'
region = 'ap-south-1'

s3 = boto3.client('s3', region_name=region)

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print("Error creating bucket:", e)
