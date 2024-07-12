prima_lettera = "a"
ultima_lettera = "z"

tentativi = [chr(i) for i in range(ord(prima_lettera), ord(ultima_lettera) + 1)]
print("".join(tentativi))