import Vue from 'vue'
import Router from 'vue-router'
import Autoround from '@/components/autoround/AutoroundParent'
import ListLike from '@/components/listlike/ListLikeParent'

Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/',
      name: 'Autoround',
      component: Autoround
    },
    {
      path: '/listlike',
      name: 'ListLike',
      component: ListLike
    }
  ]
})
