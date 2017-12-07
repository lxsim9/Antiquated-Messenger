class FileWrite: 
    def __init__(self, message):
        self.message = str(message)
        f=open("Message.txt", "a+")
        f.write(message)
        f.write("\n")
        f.close()
        