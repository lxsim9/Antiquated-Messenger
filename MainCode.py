while true:
    ans = str(input("What way would you like to communicate? (Pigeon, Morse, Encrypt, town crier)"))
    if ans.title == "Pigeon":
        a = "p"
        break
    elif ans.title == "Morse":
        a = "m"
        break
    elif ans.title == "Encrypt":
        a = "e"
        break
    elif ans.title == "town crier":
        a = "t"
        break
    else:
        print("Sorry, what does "+ans+" mean?")

ms = str(input("What would you like your message to be? "))

if a == "p":
    msg = Pigeon(ms)
elif a == "m":
    msg = Morse(ms)
elif a == "t":
    msg = towncrier(ms)
else:
    msg = Code(ms)
    
ans = FileWrite(msg)

ans.file()
    



        
