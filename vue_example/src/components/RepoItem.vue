<template>
  <div>{{repo.node.name}} ({{repo.node.url}})</div>
</template>

<script>
  export default {
    name: 'RepoItem',
    props: ['repo']
  }
</script>
