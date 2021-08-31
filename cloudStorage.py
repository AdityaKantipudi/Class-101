import dropbox  
 
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "FSkMJADFSSMAAAAAAAAAARC7eVT4M_CLK_ZArTJ5V6wN4zB8hww8wQQh4ck-vJq1"
    transferData= TransferData(access_token)

    file_from = input("Enter The File Path To Transfer")
    file_to = input("Enter The Full Path To Upload To Dropbox")

    transferData.upload_file(file_from,file_to)
    print("File Has Been Moved")

main()
