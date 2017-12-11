class FileWrite: 
    def __init__(self, message):
        self.message = str(message)
        
        
    def file(self)  
        f=open("Message.txt", "a+")
        f.write(self.message)
        f.write("\n")
        f.close()
        