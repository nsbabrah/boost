import Vue from 'vue'
import Router from 'vue-router'
import Autoround from '@/components/autoround/AutoroundParent'
import ListLike from '@/components/listlike/ListLikeParent'
import Manage from '@/components/manage/ManageParent'
import Dashboard from '@/components/dashboard/DashboardParent'
import Boost from '@/components/boost/BoostParent'
import Ebook from '@/components/ebook/Ebook'

Vue.use(Router)

export default new Router({
  routes: [

    {
      path: '/Dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/Autoround',
      name: 'Autoround',
      component: Autoround
    },
    {
      path: '/',
      name: 'Autoround',
      component: Autoround
    }, {
      path: '/ManageAccount',
      name: 'ManageAccount',
      component: Manage
    },
    {
      path: '/Listlike',
      name: 'ListLike',
      component: ListLike
    },
    {
      path: '/Ebook',
      name: 'Ebook',
      component: Ebook
    },
    {
      path: '/Boost',
      name: 'Boost',
      component: Boost
    }
  ]
})
