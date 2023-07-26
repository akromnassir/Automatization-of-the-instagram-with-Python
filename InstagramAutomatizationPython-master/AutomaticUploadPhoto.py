from InstagramAPI import InstagramAPI
from datetime import *

class New_Upload:
    def __init__(self, upload_date, type):
        self.date = upload_date
        self.type = type
        getData()
    
    def getData():
        #Type 1 is to upload a single photo
        if(type == 1):
            print("Please enter the path to the photo you want to upload")
            self.dir = str(input())
            print("The path is "+ dir)
            print("Please enter the caption for your instagram post")
            self.caption = str(input())
            print("The caption is " + caption)
        #Type 2 is for uploading an album of photos
        elif (type == 2):
            print("Please enter the path for the file where you only have the photos you want to upload")

        elif (type == 3):

        








