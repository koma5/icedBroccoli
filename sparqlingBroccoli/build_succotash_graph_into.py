import rdflib, requests, sys

rdfs = rdflib.namespace.RDFS
doap = rdflib.Namespace("http://usefulinc.com/ns/doap#")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")


graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")

graph.parse('./succotash_seed.ttl', format="turtle") # maybe get it from github or somewhere else

resourcesToFetch = []

for a in graph.triples((None, doap['programming-language'], None)):
    resourcesToFetch.append(a[2])
    #graph.parse(a[2])


for a in graph.triples((None, dbo['computingPlatform'], None)):
    resourcesToFetch.append(a[2])
    #graph.parse(a[2])



print(set(resourcesToFetch))
"""
ttl_to_post = graph.serialize(format="turtle")

headers = {
    'content-type': 'text/turtle',        
}

r = requests.post(sys.argv[1], headers=headers, data=ttl_to_post)

"""
