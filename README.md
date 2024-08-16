# Projeto de Comunicação TCP Cliente-Servidor em Python

## Índice

- [Visão Geral](#visão-geral)
- [Arquivos Incluídos](#arquivos-incluídos)
- [Como Executar](#como-executar)
  - [Executando o Servidor](#executando-o-servidor)
  - [Executando o Cliente](#executando-o-cliente)
- [Como Funciona](#como-funciona)
- [Exemplo de Funcionamento](#exemplo-de-funcionamento)
- [Licença](#licença)

## Visão Geral

Este projeto implementa uma comunicação simples entre um cliente (Alice) e um servidor (Bob) utilizando o protocolo TCP utlizando a cifra de cesar para criptofrafia e o método Diffie-Hellmann para troca de chaves em Python. O servidor aguarda a conexão de um cliente, processa a mensagem recebida convertendo-a em letras maiúsculas, e envia a resposta de volta ao cliente. O Objetivo é intecptar a troca de mensagens através do Wireshark e constatar a criptografia da mensagem. O codigo conta com um gerador de números primos aleatórios para aplicar o Diffie-Hellmann.

## Arquivos Incluídos

- **Simple_tcpServer.py**: Script que implementa o servidor TCP.
- **Simple_tcpClient.py**: Script que implementa o cliente TCP.

## Como Executar

### Executando o Servidor

1. Abra um terminal e navegue até o diretório onde o arquivo `Simple_tcpServer.py` está localizado.
2. Execute o script do servidor com o seguinte comando:

   ```bash
   python3 Simple_tcpServer.py
   
O servidor ficará em execução, aguardando conexões de clientes. Após uma conexão estabelecida será solicitado um número privado para o método de Diffie-Hellmann e posteriormente a mensagem recebida será capitalizada e enviada de volta ao cliente.

### Executando o Cliente

1. Abra outro terminal e navegue até o diretório onde o arquivo Simple_tcpClient.py está localizado.
2. Execute o script do cliente com o seguinte comando:

   ```bash
   python3 Simple_tcpClient.py
   
O cliente solicitará um número privado para o método de Diffie-Hellmann e posteriormente uma mensagem em lower case para enviar ao servidor. Após enviar a mensagem, o cliente receberá a resposta do servidor, que será exibida no terminal.

## Como Funciona

### Servidor (Simple_tcpServer.py)

- **Configuração:** O servidor é configurado para escutar em um endereço IP e porta específicos.
- **Conexão:** Ele aguarda até que um cliente se conecte.
- **Chave Pública:** Cliente e servidor efetuam a troca de chave pública para o Diffie-Hellmann
- **Processamento:** Quando o cliente envia uma mensagem, o servidor converte a mensagem em letras maiúsculas.
- **Resposta:** A mensagem processada é enviada de volta ao cliente.
- **Finalização:** A conexão é fechada após o envio da resposta.

### Cliente (Simple_tcpClient.py)

- **Conexão:** O cliente se conecta ao servidor usando o endereço IP e a porta configurados.
- **Diffie-Hellmann:** O cliente gera dois numeros primos para serem usados no método.
- **Chave Pública:** Cliente e servidor efetuam a troca de chave pública para o Diffie-Hellmann
- **Envio de Mensagem:** O cliente envia uma mensagem digitada pelo usuário ao servidor.
- **Recebimento de Resposta:** O cliente recebe e exibe a resposta do servidor.
- **Finalização:** A conexão é fechada após o recebimento da resposta.

## Exemplo de Funcionamento

### Cliente 

![Alice - Client ](https://github.com/user-attachments/assets/bfd97526-2ac2-44fa-ad8c-dcbc45b9cd6c)

### Servidor
![Bob - Server](https://github.com/user-attachments/assets/f9ba75f9-e546-4a9a-9260-e30f8efbf6da)

### Wireshark

#### Mensagem enviada pela Alice - Client
![Wireshark - Requisição Alice - Client](https://github.com/user-attachments/assets/8edc7bd8-c7e0-458e-86b0-d817aa0278c5)

#### Mensagem devolvida pelo Bob - Server
![Wireshark - Resposta Bob - Server](https://github.com/user-attachments/assets/83448f1b-f114-4411-a5b5-170b99fe7432)

## Licença

Este projeto é de código aberto e está licenciado sob a Licença MIT. Sinta-se à vontade para utilizá-lo, modificá-lo e distribuí-lo conforme necessário.
