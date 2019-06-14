import gql from 'graphql-tag'

export const ALL_REPOS_QUERY = gql`
query AllReposQuery {
  viewer {
      allRepos: repositories(first: 100) {
      edges {
        node {
          url
          name
        }
      }
    }
  }
}
`
