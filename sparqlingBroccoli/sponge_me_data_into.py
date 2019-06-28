import rdflib, requests, sys, os

rdfs = rdflib.namespace.RDFS

graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")

graph.parse(me)

for a in graph.triples((None, rdfs.seeAlso, None)):
    graph.parse(a[2])

ttl_to_post = graph.serialize(format="turtle")

headers = {
    'content-type': 'text/turtle',        
}

params= { 'graph': sys.argv[1], }

r = requests.post(sys.argv[1], headers=headers, data=ttl_to_post, params=params, auth=(os.environ['AUTH_BROCCOLI_USER'], os.environ['AUTH_BROCCOLI_PASSWORD']))

print(r.text)
