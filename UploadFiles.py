import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):

            for filesname in files:
                filePath = os.path.join(root,filesname)
                relativePath = os.path.relpath(filePath, file_from)
                dropboxPath = os.path.join(file_to, relativePath)
                with open(filePath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BDh4zFq9YTdF-On8f7Xhz16CLkVxWERDjhteYF66TNqEn2J5p-OtsPe-sRPCuYsKDzg6UVdVrCY-Z5okR7sZ9EpEBbn8HSyPFTJYKj4ANfZxE4_6QeqCxWxPhdrkn3TSrulW2NI'
    transfer_data = TransferData(access_token)
    '''file_from = input("Enter the file path to transfer")
    file_to = input("Enter the full path to upload to dropbox")'''
    file_from = "C:\\Users\\Arya Inamdar\\Desktop\\Python\\Test.txt"
    file_to = "C:\\Users\\Arya Inamdar\\Dropbox\\Documents"
    transfer_data.upload_file(file_from,file_to)
    print("File has been uploaded")

main()