import boto3
from botocore.exceptions import ClientError

from main.utils.singleton import Singleton
from project.configuration.config import Config
from project.configuration.configuration import Configuration


class SimpleStorageService(metaclass=Singleton):
    def __init__(self):
        self.bucket = self._initiate_s3_bucket()

    def _initiate_s3_bucket(self):
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
                Key=object_uri,
                Filename=f'/home/h.rezaei@asax.local/MyWorkspace/cloud/music-recommender-system/{object_name}'
            )

        except ClientError:
            raise


if __name__ == '__main__':
    Configuration.configure(Config)

    sss = SimpleStorageService()
    sss.download_object('2024/audio/0453f14e-4bc5-475c-8ad1-32dbfa7233c8.mp3')
