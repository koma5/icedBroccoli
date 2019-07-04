FROM stain/jena-fuseki

COPY config.ttl /fuseki
COPY permissions_jena_shiro.ini /fuseki/shiro.ini

CMD ["/jena-fuseki/fuseki-server"]
