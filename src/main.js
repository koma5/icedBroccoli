import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import 'tachyons'
import Vue from 'vue'
import VueApollo from 'vue-apollo'

import App from './App'

Vue.config.productionTip = false

let token = localStorage.getItem('GITHUB_AUTH_TOKEN')

const httpLink = new HttpLink({
  headers: { authorization: `Bearer ${token}` },
  uri: 'https://api.github.com/graphql'
})

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
})

Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
  defaultOptions: {
    $loadingKey: 'loading'
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  provide: apolloProvider.provide(),
  render: h => h(App)
})
