const jid = "559883528062@s.whatsapp.net";
const url1 = `http://127.0.0.1:8000/server/get/user/?jid=${jid}`;

const reqGET = (url) => {
    fetch(url)
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
}

const url2 = `http://127.0.0.1:8000/server/post/create-user/`;

const reqPOST = () => {
    const data = {
        nome: 'Maria Eduarda',
        jid: '559156964584@s.whatsapp.net',
        xpInicial: 50,
        saldoInicial: 500
    }

    fetch(url2, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
        throw new Error('Erro na requisição');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); 
    })
    .catch(error => {
        console.error('Erro:', error);
        return null;
    });
}

let url_test1 = `http://127.0.0.1:8000/server/get/apikey/?apiname=${'Gemine Google IA'}&password=${'1234'}`;
let url_test2 = `http://127.0.0.1:8000/server/post/editUserAttribute/`;

const editUserReqPost = () => {

    let data1 = {
        jid: jid,
        editarAtributo: 'xp',
        novoValor: 80,
        adicionarNoAtributo: true
    }

    fetch(url_test2, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
        body: JSON.stringify(data1)
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
    })
}

console.log(editUserReqPost())