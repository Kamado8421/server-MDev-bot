# API Documentation

![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Introdução

Esta é a documentação para a API desenvolvida por Luhdev, parte do projeto MDev Systems. Esta API, construída com Django, é utilizada em um projeto Node.js. Abaixo, você encontrará as rotas disponíveis, seus usos e exemplos de requisições utilizando `fetch` em JavaScript.


Para baixar os pacotes python use `pip freeze > requirements.txt`

## Endpoints

### GET /get/user/

Obtém um usuário pelo número de telefone (jid).

#### Exemplo de Requisição

```javascript
fetch('/get/user/?jid=123456789', {
    method: 'GET'
})
.then(response => response.json())
.then(data => console.log(data));
```


<p align="center">   Feito com ❤️ por Luhdev - MDev Systems </p>
