import gdown
class getSongFromDrive:
    URL = ""
    def __init__(self, URL):
        self.URL = URL

    def __init__(self):
        pass
    
    def setURL(self, URL):
        self.URL = URL
    
    def getURL(self):
        return self.URL

    def getSong(self):
        try:
            gdown.download_folder(self.getURL(), remaining_ok=False, use_cookies=False, quiet=True)
        except Exception as e:
            print(f"An error occurred: {e}")
            
            