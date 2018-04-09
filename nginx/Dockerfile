FROM nginx:latest
RUN apt-get update && apt-get install openssl
RUN openssl genrsa -out /etc/ssl/certs/apollo1.key 4096
RUN openssl req -new -x509 -key /etc/ssl/certs/apollo1.key -sha256 -out /etc/ssl/certs/apollo1.crt -days 1095 -subj "/C=US/ST=California/L=Santa Clara/O=Palo Alto Networks/OU= Developer Relations/CN=apiexplorer"
COPY nginx.conf /etc/nginx/nginx.conf

