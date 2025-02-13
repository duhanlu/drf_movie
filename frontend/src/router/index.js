import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Register from '../views/Register.vue'
import ActivateEmail from '../views/ActivateEmail.vue'
import Login from '../views/Login.vue'
import ResetPassword from '../views/ResetPassword.vue'
import Personal from '../views/Personal.vue'
import ChangePassword from '../views/ChangePassword.vue'
import store from '../store'
import Collect from '../views/Collect.vue'
import MembershipCard from '../views/MembershipCard.vue'
import Orders from '../views/Order.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  
  {
    path: '/activate/:uid/:token',
    name: 'ActivateEmail',
    component: ActivateEmail
  },
  {
    path: '/reset_password',
    name: 'ResetPassword',
    component: ResetPassword
  },
  {
    path: '/personal',
    name: 'Personal',
    component: Personal,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/collects',
    name: 'Collect',
    component: Collect,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/change_password',
    name: 'ChangePassword',
    component: ChangePassword,
    meta: {
      requireLogin:true
    }
  },
  {
    path: '/membership_card',
    name: 'MembershipCard',
    component: MembershipCard,
  },
  {
    path: '/orders',
    name: 'Order',
    component: Orders,
  },

  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

const token = localStorage.getItem('token')
if (token) {
  store.commit('setLoginStatus', true)
}


router.beforeEach((to, from, next) => {
  if (store.state.isLogin && to.name === 'Login' || store.state.isLogin && to.name === 'Register'){
    next({name: 'home'})
  }
  else if (to.matched.some(record => record.meta.requireLogin) && !store.state.isLogin) {
    next({name: 'Login', query: {jump: to.path}})
  }else {
    next()
  }
})

export default router
