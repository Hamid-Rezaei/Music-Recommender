import boto3
from botocore.exceptions import ClientError

from project.configuration.config import Config


class SimpleStorageService:
    def __init__(self):
        self.bucket = self._initial_s3_bucket()

    def _initial_s3_bucket(self):
        try:
            s3_resource = boto3.resource(
                's3',
                endpoint_url=Config.ENDPOINT_URL,
                aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
            )

        except Exception:
            raise
        else:
            bucket = s3_resource.Bucket(Config.AWS_STORAGE_BUCKET_NAME)
            return bucket

    def upload_object(self, file, object_uri: str):
        try:
            self.bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_uri
            )
        except ClientError:
            raise

    def download_object(self, object_uri: str):
        try:
            object_name = object_uri.rsplit('/')[-1]
            self.bucket.download_file(
                object_name,
                object_uri
            )
        except ClientError:
            raise
