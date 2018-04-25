#!/bin/sh
if [ -d  "$RENEWED_LINEAGE" ]; then
  cp -La $RENEWED_LINEAGE/fullchain.pem $RENEWED_LINEAGE/privkey.pem /etc/ssl/certs
  cd /etc/ssl/certs
  if [ -r ./fullchain.pem ]; then
    mv apiexplorer.crt apiexplorer.crt.orig
    ln -s fullchain.pem  apiexplorer.crt
  fi
  if [ -r privkey.pem ]; then
    mv apiexplorer.key apiexplorer.key.orig
    ln -s privkey.pem  apiexplorer.key
  fi
fi
