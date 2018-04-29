FROM nginx:stable
ARG APPFQDN
ARG APPEIP
ENV x_APPFQDN=${APPFQDN}
ENV x_APPEIP=${APPEIP}
RUN if [ "x$x_APPFQDN" = "x" ]; then export CN=apiexplorer; else export CN=${x_APPFQDN}; fi; echo -n ${CN} > /tmp/cn.txt
RUN if [ "x$x_APPEIP" = "x" ]; then export IP=127.0.0.1; else export IP=${x_APPEIP}; fi; echo -n ${IP} > /tmp/ip.txt
RUN apt-get update && apt-get install openssl
RUN if [ ! -e /etc/ssl/certs/apiexplorer.key ]; then openssl genrsa -out /etc/ssl/certs/apiexplorer.key 4096; fi
RUN cp /etc/ssl/openssl.cnf /tmp/openssl.cnf
RUN IP=$(cat /tmp/ip.txt); CN=$(cat /tmp/cn.txt); printf "[SAN]\nsubjectAltName=DNS:${CN},IP:${IP}\n" >> /tmp/openssl.cnf
RUN if [ ! -e /etc/ssl/certs/apiexplorer.key ]; then CN=$(cat /tmp/cn.txt); openssl req -new -x509 -key /etc/ssl/certs/apiexplorer.key -sha256 -out /etc/ssl/certs/apiexplorer.crt -days 1095 -subj "/C=US/ST=California/L=Santa Clara/O=Palo Alto Networks/OU= Developer Relations/CN=${CN}" -extensions SAN -config /tmp/openssl.cnf; fi
COPY nginx.conf /etc/nginx/nginx.conf
COPY copy_certs.sh /etc/ssl/certs/copy_certs.sh
RUN chmod +x /etc/ssl/certs/copy_certs.sh
