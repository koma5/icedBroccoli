import gql from 'graphql-tag'

export const ALL_REPOS_QUERY = gql`
query AllReposQuery {
  user(login: "koma5") {
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
