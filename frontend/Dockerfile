FROM nginx:alpine

ADD ./frontend/default.conf /etc/nginx/conf.d/
ADD ./templates/clientes.html /usr/share/nginx/html/index.html
ADD ./static/js/* /usr/share/nginx/html/static/js/