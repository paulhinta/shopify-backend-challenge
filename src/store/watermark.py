
#to add watermark
import boto3
from gallery.settings import AWS_STORAGE_BUCKET_NAME, AWS_SECRET_ACCESS_KEY
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from base64 import b64encode
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

s3 = boto3.client('s3')
bucket = AWS_STORAGE_BUCKET_NAME

def watermark(name):
    file_byte_string = s3.get_object(Bucket=bucket, Key=name)['Body'].read()

    tw = Image.open(BytesIO(file_byte_string))

    tw.thumbnail((300,300))
    w, h = tw.size

    dr = ImageDraw.Draw(tw)

    font = ImageFont.load_default()
    text = "This is a sample photo."

    text_w, text_h = dr.textsize(text, font)
    pos = w - text_w, (h - text_h) - 30
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')

    dr = ImageDraw.Draw(c_text)
        
    dr.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
    
    tw.paste(c_text, pos, c_text)

    buffer = BytesIO()
    tw.save(buffer, 'JPEG', quality=75)

    watermarked_image = buffer.getvalue()

    return watermarked_image