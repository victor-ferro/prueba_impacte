import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListTemperature from '@/components/Temperature/ListTemperature'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/temperature',
      name: 'ListTemperature',
      component: ListTemperature
    },

  ],
  mode: 'history'
})
