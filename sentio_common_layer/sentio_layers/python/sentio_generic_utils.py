from datetime import datetime

import sys
sys.path.append("/opt/python/python_libs")

# Getting Current timestamp
def get_current_timestamp():
    dateTimeObj = datetime.now()
    return dateTimeObj.strftime("%d-%m-%YT%H:%M:%SZ")

# Creating a guid of specified length
import secrets
import string

def generate_random_string(length: int) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

# JSON Decimal decoder
# Helper class to convert a DynamoDB item to JSON.
import json, decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def decimal_encoded_json_dump(data):
    return json.dumps(data, cls=DecimalEncoder)

# Converting values to Decimal from float
def convert_float_to_decimal(data):
    if isinstance(data, dict):
        return {k: decimal.Decimal(str(v)) if isinstance(v, float) else v for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_float_to_decimal(d) for d in data]
    else:
        return data

# Upload local file to S3 bucket
from boto3 import resource
s3 = resource('s3')
def send_file_to_s3(bucket_name, local_file_path, s3_file_path):
    # Sending file to s3
    print(f"Sending file {local_file_path} to S3: {s3_file_path}")
    try:
        s3.Bucket(bucket_name).upload_file(local_file_path, s3_file_path)
        return True
    except Exception as e:
        print("Error: Failed to send file to S3")
        print(e)
        return False

# Creating Thumbnail of an image
from PIL import Image

def create_thumbnail(original_file_path, thumbnail_file_path, size=(512, 512)):
    try:
        image = Image.open(original_file_path)
        image.thumbnail(size)
        image.save(thumbnail_file_path)
        return True
    except IOError as e:
        print(f"Error creating thumbnail: {e}")
        return False

# Creating image from a byte array
import io
def create_image_from_byte_array(byte_array, image_path):
    try:
        byte_string = bytes(byte_array)
        img = Image.open(io.BytesIO(byte_string))
        img.save(image_path)
    except IOError as e:
        print(f"Error creating image from byte array: {e}")
        return False
    return True
