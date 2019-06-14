<template>
  <div>
    <h4 v-if="loading">Loading...</h4>
    <repo-item
      v-for="repo in user.allRepos.edges"
      :key="repo.node.url"
      :repo="repo">
    </repo-item>
  </div>
</template>

<script>
  import { ALL_REPOS_QUERY } from '../constants/graphql'
  import RepoItem from './RepoItem'

  export default {
    name: 'RepoList',
    data () {
      return {
        allRepos: [],
        loading: 0
      }
    },
    components: {
      RepoItem
    },
    apollo: {
      user: {
        query: ALL_REPOS_QUERY
      }
    }
  }
</script>

