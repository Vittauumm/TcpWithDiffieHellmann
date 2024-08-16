# Alice - Client

from socket import *
import random

def caesar(data, key, ecrypyt = True):
    if ecrypyt is False : key = -key
    result = []
    for char in data:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted = chr((ord(char) - shift_amount + key) % 26 + shift_amount)
        else:
            encrypted = char
        result.append(encrypted)
    return ''.join(result)

def generate_prime_number(bits):
    while True:
        number = random.getrandbits(bits)
        number |= (1 << bits - 1) | 1
        
        if prime_number_check(number):
            return number

def prime_number_check(number):
    i = 2
    while i < number:
        R = number % i
        if R == 0:
            return False
            
        i += 1
        
    return True

G = generate_prime_number(16)
N = generate_prime_number(16)

x = int(input("Escolha seu numero privado para o Diffie-Hellmann: "))
    
serverName = "10.1.70.37"
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

R1 = pow(G, x, N)
data = str(G) + ";" + str(N) + ";" + str(R1)

clientSocket.send(data.encode())

R2 = int(clientSocket.recv(1024).decode())

K1 = pow(R2, x, N) % 26

sentence = input("Input lowercase sentence: ")
encrypted_sentence = caesar(sentence, K1)

clientSocket.send(encrypted_sentence.encode())
print("Sent to server: ", encrypted_sentence)

encrypted_response = clientSocket.recv(65000).decode()

decrypted_response = caesar(encrypted_response, K1, False)

print ("Received from Make Upper Case Server: ", decrypted_response)

clientSocket.close()
