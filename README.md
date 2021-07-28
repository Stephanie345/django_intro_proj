# Curso Intro django
## Overview

![overview_django](https://user-images.githubusercontent.com/21146338/126917648-f5dc0f58-119f-46f7-bb00-446b36d7dc1c.PNG)

### 1 HTTP 

![request_response](https://user-images.githubusercontent.com/21146338/127257985-3cbef4de-3406-47dc-9764-174ccb702511.PNG)

## 1.1 HTTP Explicação
HTTP funciona como um protocolo de requisição-resposta permitindo a comunicação entre clientes e servidores.Uma socilitação HTTP ou HTTP Request é uma maneira do navegador mostrar uma página da internet, utilizando um dos métodos de solicitação do protocolo HTTP.
-Cliente: browser que solicita, recebe e apresenta objetos da web
-Servidor: envia objetos em resposta a pedidos
Sequência de ações:
-cliente inicia conexão TCP para o servidor na porta 80
-servidor aceita uma conexão TCP do cliente
-Mensagens HTTP são trocadas entre browser(cliente HTTP) e o servidor web(servidor HTTP)
-conexão TCP é fechada.
Um cliente inicia uma requisição estabelendo uma conexão TCP para porta de um servidor, normalmente a porta 80.Um servidor HTTP ouvindo naquela porta(80) espera por uma mensagem de requisição de cliente. Recebendo a requisição,o servidor retorna uma linha de estado, como "http://127.0.0.1:8080/", e uma mensagem.O protocolo HTTP define 8 métodos(GET, HEAD, POST, PUT, DELETE, TRACE,OPTIONS e CONNECT) que indicam a ação a ser realizada no recurso especificado.Os métodos GET e POST são os que aparecem mais no desenvolvimento web.
HTTP é "stateless" o servidor não mantém informação sobre os pedidos passados pelos clientes. Caso queira de alguma forma manter os dados, pode-se utilizar os mecanismos de session (sessão) e cookies.O método GET requisita objetos ao servidor web,mostras os dados na url.O método POST usado para enviar dados ao servidor

