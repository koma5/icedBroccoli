# -*- encoding: utf-8 -*-

import rdflib, requests, sys, os

rdfs = rdflib.namespace.RDFS
doap = rdflib.Namespace("http://usefulinc.com/ns/doap#")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")


graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")

graph.parse(sys.argv[2], format="turtle")

ttl_to_post = str(graph.serialize(format="turtle", encoding='utf-8'))

headers = {
    'content-type': 'text/turtle',        
}

params = {  'graph': sys.argv[1], }

r = requests.put(sys.argv[1], headers=headers, data=ttl_to_post, params=params, auth=(os.environ['AUTH_BROCCOLI_USER'], os.environ['AUTH_BROCCOLI_PASSWORD']))

print(r.text)
