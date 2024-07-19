password = int(input("inserire la password\n"))
if password == 123456:
    print("password accettata")
    
else:
    print("la password non è corretta, tentativi rimasti: 3")

    password = int(input("inserire la password\n"))    
    if password == 123456:
        print("password accettata")
    
    else:
        print("la password non è corretta, tentativi rimasti: 2")

        password = int(input("inserire la password\n"))
        if password == 123456:
            print("password accettata")
    
        else:
            print("la password non è corretta, tentativi rimasti: 1")
    
            password = int(input("inserire la password\n"))
            if password == 123456:
                print("password accettata")
    
            else:
                print("terminale bloccato")

    
