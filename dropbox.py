import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BK9XlAvHfdeNTjaFbs4iIwDmdMtWRUULYogQVHEsgoB9Dtphry1-hGmvP-iALfnIaXNqzhm2aOrgUp8pNdS5W1-tt-qyVqYtBYid7eNqG67bfpubD7TEIRJXOSerwt-V6ofDiRs'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()