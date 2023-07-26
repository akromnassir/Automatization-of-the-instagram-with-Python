from InstagramAPI import InstagramAPI


class InstaLogin:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password
        
    def upload_photo(self, path, caption):
        Insta = InstagramAPI(self.user_name, self.user_password)
        Insta.login()
        Insta.uploadPhoto(path, caption)
        print("Your photo has been uploaded")   
