# Bob - Server

from socket import *

y = 687169

def caesar(data, key, ecrypyt=True):
    if ecrypyt == False : key = -key
    result = []
    for char in data:
        if char.isalpha():
            shift_char = 65 if char.isupper() else 97
            encrypted = chr((ord(char) - shift_char + key) % 26 + shift_char)
        else:
            encrypted = char  # Non-alphabetic characters remain unchanged
        result.append(encrypted)
    return ''.join(result)

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5)

print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

data =  connectionSocket.recv(1024).decode()
split_data = data.split(";")

G = (int)(split_data [0])
N = (int)(split_data [1])
R1 = (int)(split_data [2])

y = int(input("Escolha um numero privado para Diffie-Hellman: "))
R2 = pow(G, y, N)

connectionSocket.send(str(R2).encode())

K2 = pow(R1, y, N) % 26

encrypted_sentence = connectionSocket.recv(65000).decode()
decrypted_sentence = caesar(encrypted_sentence, K2, False)

capitalizedSentence = decrypted_sentence.upper()

capitalized_sentence_encrypted = caesar(capitalizedSentence, K2, True)

connectionSocket.send(capitalized_sentence_encrypted.encode())

print ("Sent back to Client: ", capitalized_sentence_encrypted)

connectionSocket.close()