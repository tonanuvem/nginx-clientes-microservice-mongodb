Projeto clientes-microservice-mongodb com as 3 camadas separadas:
<br> <br>
>Porta 8000: frontend: utiliza nginx para redirecionar /api/clientes para o backend
<br> <br>
>Porta 5000: backend: api em python
<br> <br>
>Porta 27017: mongo: banco de dados
<br> <br>
>Porta 8080: visualizer: visualizador do Cluster Swarm
<br> <br>
>Porta 8081: mongo: visualizador do Banco de Dados

Acessar PwD

Criar arquivo stack-deploy.yml

Executar:

> git clone

> cd nginx-clientes-microservice-mongodb

> docker network create -d overlay net

> docker stack deploy -c stack-deploy.yml clientes
