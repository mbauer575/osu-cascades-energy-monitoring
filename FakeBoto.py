class boto3:
    def __init__(self):
        #allow access to self.meta.client.download_file -> self.download_file
        self.meta = self
        self.client = self
        pass

    def download_file(self, bucket, key, filename):
        #ddoesnt ownload file from bucket/key to filename
        pass

    def Session(aws_access_key_id, aws_secret_access_key):
        #accepts any keys and returns self
        return boto3()

    def resource(self, s):
        #returns self
        return self
    
    #here is a fake appkeys.json file
    #{
    #"aws_access_key_id": "FAKE_AWS_ACCESS_KEY_ID",
    #"aws_secret_access_key": "FAKE_AWS_SECRET_ACCESS_KEY"
    #}