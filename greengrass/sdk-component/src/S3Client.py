import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, EndpointConnectionError

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class S3Client:
    def __init__(self, bucket_name):
        """Initialize the S3 client and the target S3 bucket."""
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload(self, file_path) -> None:
        """Uploads a file to the specified S3 bucket."""
        try:

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")

            object_name = os.path.basename(file_path)

            # Upload the file
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            logging.info(f"File {file_path} successfully uploaded to s3://{self.bucket_name}/{object_name}")

        except FileNotFoundError as fnf_error:
            logging.error(f"The file {file_path} was not found: {fnf_error}")
            raise fnf_error

        except NoCredentialsError as nce_error:
            logging.error(f"Credentials not available: {nce_error}")
            raise nce_error

        except PartialCredentialsError as pce_error:
            logging.error(f"Incomplete AWS credentials: {pce_error}")
            raise pce_error

        except EndpointConnectionError as ec_error:
            logging.error(f"Failed to connect to AWS S3 endpoint: {ec_error}")
            raise ec_error

        except Exception as e:
            logging.error(f"An unexpected error occurred while uploading {file_name}: {e}")
            raise e
