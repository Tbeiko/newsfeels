from azure.storage.blob import BlobService
import os

blob_service = BlobService(account_name='newsfeels', account_key=os.environ['AZUREKEY'])
blob_service.put_block_blob_from_path(
    'songs',
    '06_3005',       # number before the song emotion corresponds to 'sentValue' from songdictionary.py. 10 = 1.0, 08 = 0.8, etc.
    '06_3005.mp3',
    x_ms_blob_content_type='mp3'
)