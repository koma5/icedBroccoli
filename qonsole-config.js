/** Spp/js/app/qonsole-config.jswebapp/js/app/qonsole-config.jstandalone configuration for qonsole on index page */

define( [], function() {
  return {
    prefixes: {
      "rdf":      "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "rdfs":     "http://www.w3.org/2000/01/rdf-schema#",
      "owl":      "http://www.w3.org/2002/07/owl#",
      "xsd":      "http://www.w3.org/2001/XMLSchema#",
      "foaf":     "http://xmlns.com/foaf/0.1/",
      "doap":     "http://usefulinc.com/ns/doap#",
    },
    queries: [
      { "name": "selection of triples",
        "query": "SELECT ?subject ?predicate ?object\nWHERE {\n" +
                 "  ?subject ?predicate ?object\n}\n" +
                 "LIMIT 42"
      },
	  { "name": "named graphs tripple counts",
		"query": "SELECT ?graph (count(?s) as ?count)\n" + 
				 "WHERE { GRAPH ?graph { ?s ?p ?o }}\n" + 
				 "GROUP BY ?graph",
	  },
      { "name": "selection projects",
        "query": "SELECT ?project ?description\n" +
                 "WHERE {\n" +
                 "  ?project a doap:Project . \n" +
                 "  ?project doap:description ?description . \n}",
        "prefixes": ["doap"]
      
      },
    ]
  };
} );

