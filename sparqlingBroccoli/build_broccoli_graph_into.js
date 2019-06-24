gql = require('graphql-request')
const request = require('request')
const rdf = require('rdf');
const { NamedNode, BlankNode, Literal } = rdf;

const foaf = new rdf.ns('http://xmlns.com/foaf/0.1/');
const doap = new rdf.ns('http://usefulinc.com/ns/doap#');
const succotash = new rdf.ns('http://5th.ch/succotash/');
const me = new NamedNode('http://marcoko.ch/#i');

const query = `
query {
    viewer {
        allRepos: repositories(first: 100) {
            edges {
                node {
                    url
                    name
                    description
                    descriptionHTML
                    homepageUrl
                }
            }
        }
    }
}`

headers = { authorization: 'bearer ' + process.env['GITHUB_TOKEN'] }
const client = new gql.GraphQLClient('https://api.github.com/graphql', {headers: headers});

var gBroccoli = new rdf.Graph();
var newTriples = [];


client.request(query)
.then(data => {
    data.viewer.allRepos.edges.forEach(function blahh(r) {

        node = succotash('#' + r.node.name)

        newTriples.push(
            new rdf.Triple(
                node,
                doap('name'),
                new Literal(r.node.name, '@en')
            )
        );

        newTriples.push(
            new rdf.Triple(
                node,
                rdf.rdfns('type'),
                doap('Project')
            )
        );




        homepage = r.node.homepageUrl;
        if (homepage) {
            try {
                newTriples.push(
                    new rdf.Triple(
                        node,
                        doap('homepage'),
                        new NamedNode(homepage)
                    )
                );
            } catch(error) { console.log("failed to parse homepage.", r.node.name, homepage, error); }
        }

        description = r.node.description;
        if (description) {
            try {
                newTriples.push(
                    new rdf.Triple(
                        node,
                        doap('description'),
                        new Literal(description, '@en')
                    )
                );
            } catch(error) { console.log("failed to parse decription", r.node.name, description, error); }
        }

        newTriples.push(
            new rdf.Triple(
                node,
                doap('repository'),
                new NamedNode(r.node.url)
            )
        );


        newTriples.push(
            new rdf.Triple(
                node,
                foaf('maker'),
                me
            )
        );



    })
    
    newTriplesAsString = '';

    newTriples.forEach(t => {
        newTriplesAsString += t.toNT();
        console.log(t.toNT());
    });


    request(
        {
            uri: process.argv[2],
            headers: { 'content-type': 'application/n-triples' },
            body: newTriplesAsString,
            method: 'POST'
        }, (error, res, body) => {
            if (error) {
                console.error(error)
                return
            }

            console.log(`statusCode: ${res.statusCode}`)
            console.log(body)
        }
    );

});
