<template>

<div id="header" class="h-12 py-1 bg-primary-100 flex items-center justify-center">
    <div claa="w-full px-4" style="max-width:1440px">
   
    <div class="flex justify-between">
    <div id = "nav" class="flex items-center">
        <Category/>
    </div>

<div class="flex items-center space-x-2">
    <div class="relative shrink">
            <input v-model="keyword" type=text name=keyword class="outline-0 h-9 rounded bg-primary-700 border border-gray-600 placeholder-gray-400 w-64 px-2 py-1 max-w-[180px]" placeholder=请输入关键词 value>
            <div class="absolute top-0 right-0 flex items-center h-full">
                <div class="rounded text-xs text-gray-400 px-2 mr-2">
                    <button v-on:click.prevent="searchMovies">
                        <svg xmlns=http://www.w3.org/2000/svg class="h-4 w-4" fill=none viewBox="0 0 24 24" stroke=currentColor stroke-width=2>
                            <path stroke-linecap=round stroke-linejoin=round d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                        </svg>
                    </button>
                </div>
            </div>

    </div>
    <div v-if="$store.state.isLogin" @click="toggleMenu" id="userinfo" class="flex relative hover: cursor-pointer items-center justify-center rounded border border-solid text-white text-lg h-9 text-center">
        <div id="username" class="px-2">{{ username }}</div>
        <div class="pr-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="none" width="16" height="16">
            <path d="M7 10l5 5 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </div>
        <div :class="{hidden: !showMenu}" id="userinfo_menu" class="absolute top-[40px] w-32 transition ease-in-out delay-150 z-50 sf-hidden">
            <ul class="bg-primary-700 py-2 px-4 text-sm">
                <li class="plx-2 py-2">
                    <a href="/personal">Account</a>
                </li>
                <li class="plx-2 py-2">
                    <a href="/collects">Favorite</a>
                </li>
    
                <li class="plx-2 py-2">
                    <router-link to="/" v-on:click.prevent="logout()">Log out</router-link>
                </li>
            </ul>
        </div>
    </div>
    <div v-else class="text-white flex-shrink-0 pr-2">
        <a href=http://127.0.0.1:8080/login/>登录</a>
        / <a href=http://127.0.0.1:8080/register/>注册</a>
    </div>
</div>
</div>
</div>
</div>

</template>

<script>
import Category from '@/components/Category.vue'
import axios from 'axios'

export default {
    name: 'Header',
    components: {  Category },
    data: function() {
        return {
            keyword: '',
            username: '',
            showMenu: false,
        }
    },
    mounted() {
        this.username = localStorage.getItem('username')
        // check login status
        const currentTime = Date.now()
        const expiredTime = localStorage.getItem('expiredTime')
        const refreshToken = localStorage.getItem('refreshToken')

        if (expiredTime > currentTime) {
            this.$store.commit('setLoginStatus', true)
        }else if (refreshToken){
            axios
                .post('/api/jwt/refresh/', {refresh: refreshToken})
                .then(response => {
                    const token = response.data.access
                    localStorage.setItem("token", token)
                    // update expire time
                    const expiredTIme = Date() + 1 * 60 * 1000
                    localStorage.setItem('expiredTime', expiredTime)
                    this.$store.commit('setLoginStatus', true)
                })
                .catch( error => {
                    console.log(error)
                    this.$store.commit('setLoginStatus', false)
                    localStorage.clear()
                })
        }
        else {
            this.$store.commit('setLoginStatus', false)
            localStorage.clear()
        }
    },

    methods: {
        searchMovies() {
            const keyword = this.keyword.trim()
            this.$router.push({
                name: 'home',
                query: { search: keyword }
            })
        },
        toggleMenu() {
            this.showMenu = !this.showMenu
        },
        logout(){
            localStorage.clear()
            this.$store.commit('setLoginStatus', false)
        }
    },
}

</script>