# _Blog base API_

A intenção do projeto é fornecer uma base simples e extensivel para um blog. A projeto fornece uma API simples para ser consumida por qualquer serviço. 

### As tecnologias "core" utilizadas são:

- Python
- Django
- DRF

## Como rodar:
Clone ou faça download do projeto

```sh
git clone https://github.com/Ssousuke/blog-api.git
```


Pelo Terminal, dentro da pasta do projeto, crie um ambiente virtual

```sh
Windows: python -m venv venv
Linux: python3 -m venv venv
```

Ative o ambiente virtual
```sh
Windows: venv\Scripts\Activate
Linux: source ./venv/bin/activate
```
Instale as dependencias
```sh
pip install -r requirements.txt
```

## Variaveis de ambiente
OBS: Você pode configurar o banco de dados que achar necessário, mas as variaveis de ambiente dendo do settings.py são do postreSQL. 

### Crie um arquivo .env

dentro desse arquivo coloque as variaveis ambiente relacionadas ao django e ao banco de dados que vai usar
```sh
SECRET_KEY
DEBUG
...
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Migrações

Após a configuração do ambiente, você pode em seguida fazer o processo de migração.
```sh
python manage.py makemigrations
python manage.py migrate
```

Após isso você tambem pode criar um usuário para fazer publicações e fazer as requisições da API.
