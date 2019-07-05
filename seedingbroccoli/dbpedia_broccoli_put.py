# -*- encoding: utf-8 -*-

import rdflib, requests, sys, os

rdfs = rdflib.namespace.RDFS
doap = rdflib.Namespace("http://usefulinc.com/ns/doap#")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")


# query broccoli for all links to dbpedia resources

graph = rdflib.Graph()

resources_to_query = []

sparql_query_links_to_external = """
SELECT DISTINCT ?dbr
WHERE {
?s ?p ?dbr
FILTER regex(str(?dbr),'http://dbpedia.org/resource/','i')
}
"""

params = {
    'query': sparql_query_links_to_external,
    'format': 'text/csv'
}

broccoli_response = requests.get(sys.argv[2], params)
resources_to_query = ['<{}>'.format(r) for r in broccoli_response.text.split() ]


# query dbpedia for these ^ resources

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

dbpedia_response = requests.post('https://dbpedia.org/sparql', params)


# PUT it to broccoli

ttl_to_post = dbpedia_response.text.encode('utf-8')


headers = {
    'content-type': 'text/turtle',        
}

params = {  'graph': sys.argv[1], }

r = requests.put(sys.argv[1], headers=headers, data=ttl_to_post, params=params, auth=(os.environ['AUTH_BROCCOLI_USER'], os.environ['AUTH_BROCCOLI_PASSWORD']))

print(r.text)

