FROM stain/jena-fuseki

COPY config.ttl /fuseki
COPY permissions_jena_shiro.ini /fuseki/shiro.ini
COPY qonsole-config.js /jena-fuseki/webapp/js/app/qonsole-config.js

CMD ["/jena-fuseki/fuseki-server"]
