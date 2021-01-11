def translate(message):
    encrypt =  {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                '?': '..--..','/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/', '!': '-.-.--',
                '@': '.--.-.', '&': '.-...'} # dictionary of letters and morse code for each
    
    decrypt = {v: k for k, v in encrypt.items()} # creates a dictionary of morse code and letter for each
                                                 # since the key and values is a reverse of the encrypt dictionary, I used this method :)

    if len([i for i in message if i != '-' and i != '.' and i != ' ' and i != '/']) != 0: # checks if the message isn't a morse code
        return ' '.join(encrypt[i] for i in message.upper()) # if message isn't a morse code, it encrypts it to a morse code
    else:
        return ''.join(decrypt[i] for i in message.split()) # if message is a morse code, it decrypts it to a normal message

print(translate('Hello. This is a sample test.')) # this will translate the normal message to morse code
print(translate('.... . .-.. .-.. --- .-.-.- / - .... .. ... / .. ... / .- / ... .- -- .--. .-.. . / - . ... - .-.-.-')) # this will translate the normal message to morse code
# print(translate(input('The message you want to translate: ')))
