import msvcrt
import os

# Dizionario per la conversione delle lettere e dei numeri in codice Morse
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('?')  # Per caratteri non riconosciuti
    return ' '.join(morse_code)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Inserisci il testo da convertire in codice Morse. Premi Esc per uscire.")
    full_text = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\x1b':  # Codice ASCII per 'Esc'
            break
        if char.isalnum() or char == ' ':
            full_text += char
            morse_output = text_to_morse(full_text)
            clear_screen()
            print(f"Testo: {full_text}")
            print(f"Codice Morse: {morse_output}")
        elif char == '\b':  # Gestione del backspace
            full_text = full_text[:-1]
            morse_output = text_to_morse(full_text)
            clear_screen()
            print(f"Testo: {full_text}")
            print(f"Codice Morse: {morse_output}")

if __name__ == "__main__":
    main()