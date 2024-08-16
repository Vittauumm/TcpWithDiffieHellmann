# TcpWithDiffieHellmann
Projeto para demonstrar implementação de um client/server com criptografia usando cifra de cesar e Diffie-Hellmann

Esse projeto contém dois arquivos, sendo Simple_tcpServer que representa o Bob e Simple_tcpClient que representa a Alice.

O cenário proposto é que haja um troca de chaves públicas (G e N) para que sejam calculadas as chaves privadas que servem
para criptografar e descriptografar as mensagens trocadas. O server irá receber a mensagem e devolve-la em caixa alta. Para criptografar foi utilizado a cifra de cesar, e para troca de chaves o método Diffie-Hellmann. 

Client
![Informações enviadas pelo client](https://github.com/user-attachments/assets/b1a78583-8e24-44f5-acb8-c751ff456824)


Server
![Informações Server](https://github.com/user-attachments/assets/8aa089db-475b-4ae8-9dda-fa875d5c9fea)

Mensagem interceptada no Wireshark
![Wireshark](https://github.com/user-attachments/assets/72179bcf-3776-47c2-8116-382a67df1f84)
