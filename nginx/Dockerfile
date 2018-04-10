FROM nginx:latest
RUN apt-get update && apt-get install openssl
RUN openssl genrsa -out /etc/ssl/certs/apiexplorer.key 4096
RUN openssl req -new -x509 -key /etc/ssl/certs/apiexplorer.key -sha256 -out /etc/ssl/certs/apiexplorer.crt -days 1095 -subj "/C=US/ST=California/L=Santa Clara/O=Palo Alto Networks/OU= Developer Relations/CN=apiexplorer"
COPY nginx.conf /etc/nginx/nginx.conf

