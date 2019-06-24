import rdflib, requests, sys

rdfs = rdflib.namespace.RDFS
doap = rdflib.Namespace("http://usefulinc.com/ns/doap#")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")


graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")

graph.parse('./succotash_seed.ttl', format="turtle") # maybe get it from github or somewhere else

resources_to_query = []

for a in graph.triples((None, doap['programming-language'], None)):
    resources_to_query.append(a[2])


for a in graph.triples((None, dbo['computingPlatform'], None)):
    resources_to_query.append(a[2])


resources_to_query = set(resources_to_query)
resources_to_query = [s.n3() for s in resources_to_query]
sparql_values = ' '.join(resources_to_query)

sparql_query = """
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>

CONSTRUCT {{

    ?res dbo:abstract ?abs .
    ?res rdfs:label ?label .

}}
WHERE {{

    ?res dbo:abstract ?abs .
    ?res rdfs:label ?label .

    VALUES ?res {{
        {0}
    }}
}}
""".format(sparql_values)

params = {
    'query': sparql_query,
    'format': 'text/turtle'
}

r = requests.get('https://dbpedia.org/sparql', params)

print(r.text)


ttl_to_post = r.text

headers = {
    'content-type': 'text/turtle',        
}

r = requests.post(sys.argv[1], headers=headers, data=ttl_to_post)
