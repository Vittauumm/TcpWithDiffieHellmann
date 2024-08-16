# Alice - Client

from socket import *

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

def prime_number_check(number):
    i = 2
    while i < number:
        R = number % i
        if R == 0:
            return False
            
        i += 1
        
    return True

G = int(input("Digite um numero primo (G) para o algoritmo de Diffie-Hellmann\nNote: Quanto maior o numero primo melhor\nSugestão: 7877\n"))
while prime_number_check(G) == False :
    G =  int(input("O numero digitado não é primo. Por favor insira outro numero.\n"))
    prime_number_check(G)

N = int(input("Digite outro numero primo (N) para o algoritmo de Diffie-Hellmann\nNote: Quanto maior o numero primo melhor\nSugestão: 7919\n"))
while prime_number_check(N) == False :
    N =  int(input("O numero digitado não é primo. Por favor insira outro numero.\n"))
    prime_number_check(N)

x = int(input("Agora escolha seu numero privado para o Diffie-Hellmann: "))
    
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