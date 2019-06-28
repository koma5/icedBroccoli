# -*- encoding: utf-8 -*-

import rdflib, requests, sys, os

rdfs = rdflib.namespace.RDFS
doap = rdflib.Namespace("http://usefulinc.com/ns/doap#")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")


graph = rdflib.Graph()
me = rdflib.URIRef("http://marcoko.ch/#i")

graph.parse('./succotash_seed.ttl', format="turtle") # maybe get it from github or somewhere else

resources_to_query = []

resources_to_query = graph.query(
"""
SELECT DISTINCT ?dbr
WHERE {
?s ?p ?dbr
FILTER regex(str(?dbr),'http://dbpedia.org/resource/','i')
}
""")

resources_to_query = [s['dbr'].n3() for s in resources_to_query]
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

dbpedia_response = requests.get('https://dbpedia.org/sparql', params)


ttl_to_post = ''
ttl_to_post += str(graph.serialize(format="turtle", encoding='utf-8'))
ttl_to_post += dbpedia_response.text.encode('utf-8')


headers = {
    'content-type': 'text/turtle',        
}

params = {  'graph': sys.argv[1], }

r = requests.post(sys.argv[1], headers=headers, data=ttl_to_post, params=params, auth=(os.environ['AUTH_BROCCOLI_USER'], os.environ['AUTH_BROCCOLI_PASSWORD']))

print(r.text)
