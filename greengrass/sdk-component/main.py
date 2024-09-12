import sys
from src.S3Client import S3Client

BUCKET_NAME = "dev-przemo-device-storage"

def main():
    args = sys.argv[1:]

    print("Create S3 Client")

    s3_client = S3Client(BUCKET_NAME)

    s3_client.upload("test.jpg")

if __name__ == "__main__":
    main()
