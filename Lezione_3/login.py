user_lower = "beppe"
user_upper = "Beppe"
password = "12345"
tentativi_rimasti = 3

user_inserita = input("inserisci l'utente\n")
password_inserita = int(input("inserisci la password\n"))

if user_inserita == user_lower or user_upper:
    if int(password_inserita) == password:
        print("Benvenuto")
    else:
        tentativi_rimasti - 1
        print("Accesso non consentito!")

        user_inserita = input("inserisci l'utente\n")
        password_inserita = int(input("inserisci la password\n"))

        if user_inserita == user_lower or user_upper:
            if int(password_inserita) == password:
                print("Benvenuto")
            else:
                tentativi_rimasti - 1
                print("Accesso non consentito!")

                user_inserita = input("inserisci l'utente\n")
                password_inserita = int(input("inserisci la password\n"))

                if user_inserita == user_lower or user_upper:
                    if int(password_inserita) == password:
                        print("Benvenuto")
                    else:
                        tentativi_rimasti - 1
                    print("Accesso non consentito!")
                    print("Terminale Bloccato")