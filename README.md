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

> docker stack deploy -c stack-deploy.yml clientes
