# Projeto de Comunicação TCP Cliente-Servidor em Python

Este projeto implementa uma comunicação simples entre um cliente e um servidor utilizando o protocolo TCP (Transmission Control Protocol) em Python. O servidor aguarda a conexão de um cliente, processa a mensagem recebida convertendo-a em letras maiúsculas, e envia a resposta de volta ao cliente.

## Índice

- [Visão Geral](#visão-geral)
- [Arquivos Incluídos](#arquivos-incluídos)
- [Como Executar](#como-executar)
  - [Executando o Servidor](#executando-o-servidor)
  - [Executando o Cliente](#executando-o-cliente)
- [Como Funciona](#como-funciona)
- [Possíveis Melhorias](#possíveis-melhorias)
- [Licença](#licença)

## Visão Geral

Este projeto serve como uma introdução à programação de redes em Python. Ele demonstra como configurar um servidor que pode aceitar conexões de clientes, processar dados e responder de forma adequada. O cliente, por sua vez, se conecta ao servidor, envia uma mensagem e espera uma resposta.

## Arquivos Incluídos

- **Simple_tcpServer.py**: Script que implementa o servidor TCP.
- **Simple_tcpClient.py**: Script que implementa o cliente TCP.

## Como Executar

### Executando o Servidor

1. Abra um terminal e navegue até o diretório onde o arquivo `Simple_tcpServer.py` está localizado.
2. Execute o script do servidor com o seguinte comando:

   ```bash
   python3 Simple_tcpServer.py
