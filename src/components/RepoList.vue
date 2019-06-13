<template>
  <div>
    <repo-item
      v-for="repo in allRepos"
      :key="repo.id"
      :repo="repo">
    </repo-item>
  </div>
</template>

<script>
  import RepoItem from './RepoItem'

  export default {
    name: 'RepoList',
    data () {
      return {
        allRepos: [
          {
            id: '1',
            name: 'waylett',
            url: 'https://github.com/koma5/waylett'
          }, {
            id: '2',
            name: 'iceBroccoli',
            url: 'http://github.com/koma5/icedBroccoli/'
          }
        ]
      }
    },
    components: {
      RepoItem
    }
  }
</script>

