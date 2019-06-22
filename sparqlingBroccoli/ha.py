import rdflib, requests, html, time

rdfs = rdflib.namespace.RDFS

graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")
broccoli = rdflib.URIRef("http://127.0.0.1:3030/broccoli/data")

graph.parse(me)

for a in graph.triples((None, rdfs.seeAlso, None)):
    graph.parse(a[2])

ttl_to_post = graph.serialize(format="turtle")

headers = {
    'content-type': 'text/turtle',        
}


r = requests.post('http://127.0.0.1:3030/broccoli/data', headers=headers, data=ttl_to_post)
