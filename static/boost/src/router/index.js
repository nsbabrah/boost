import Vue from 'vue'
import Router from 'vue-router'
import Autoround from '@/components/autoround/AutoroundParent'
import ListLike from '@/components/listlike/ListLikeParent'
import Manage from '@/components/manage/ManageParent'

Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/',
      name: 'Autoround',
      component: Autoround
    },
    {
      path: '/Autoround',
      name: 'Autoround',
      component: Autoround
    },{
      path: '/ManageAccount',
      name: 'ManageAccount',
      component: Manage
    },
    {
      path: '/Listlike',
      name: 'ListLike',
      component: ListLike
    }
  ]
})
