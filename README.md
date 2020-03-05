Projeto clientes-microservice-mongodb com as 3 camadas separadas:
<br> <br>
>frontend: utiliza nginx para redirecionar /api/clientes para o backend
<br> <br>
>backend: api em python
<br> <br>
> mongo: banco de dados

Acessar PwD

Criar arquivo stack-deploy.yml

Executar:

> git clone

> cd nginx-clientes-microservice-mongodb

> docker network create -d overlay net

> docker stack deploy -c stack-deploy.yml clientes
