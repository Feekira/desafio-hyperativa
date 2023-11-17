# Desafio-hyperativa

Teste técnico utilizando python ( Django ) é necessario python version 3.9 > 

### Instale o pip primeiro
    sudo apt-get install python3-pip

### Em seguida, instale o virtualenv usando pip3
    sudo pip3 install virtualenv 

### Agora crie um ambiente virtual
    virtualenv -p python3 .env

### Acessar o seu ambiente virtual
    source .env/bin/activate

### Agora que estamos na env, vamos instalar os pacotes.
    pip install -r requeriments.txt

### Executar o projeto com runserver.
    python3 manage.py runserver


### Instale o postman para consumir a API
    pip install postman

### Certo, por onde comecar ? 

   * Com tudo instalado e com o postman aberto, nossa primeira URL a ser consumida será o http://localhost:8000/token/
   * Essa url nos dará o token para termos acesso aos demais verbos ( ou contratos ) da nossa API.

### configuração do postman
   
   * Na aba Authorization selecionar o **type Bearer Token** com isso será disponibilizado um campo para inserirmos o token. 
