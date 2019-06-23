gql = require('graphql-request')
const rdf = require('rdf');
const { NamesNode, BlankNode, Literal } = rdf;

const foaf = rdf.ns('http://xmlns.com/foaf/0.1/');

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

var Graph = new rdf.Graph();


client.request(query)
.then(data => {
    data.viewer.allRepos.edges.forEach(r => {
        console.log(new rdf.Triple(
                new BlankNode(),
                rdf.rdfsns('label'),
                new Literal(r.node.name, '@en')).toNT()
        ); 
    })
});
