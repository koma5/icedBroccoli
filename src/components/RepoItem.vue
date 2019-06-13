<template>
  <div>{{repo.name}} ({{repo.url}})</div>
</template>

<script>
  export default {
    name: 'RepoItem',
    props: ['repo']
  }
</script>
