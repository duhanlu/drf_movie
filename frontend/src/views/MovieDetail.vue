<template>

 <div id="container" class="flex flex-col min-h-screen bg-primary-300 text-white text-lg pd-20">
      <Header/>
    <div class="container mx-auto p-4 h-96">
      <div class="w-full px-2" style="max-width:1440px">
      <div id="main" class="bg-primary-300 p-6 text-black">
       <div class="flex rounded bg-white mx-4 py-6">
        <div class="mx-6">
         <div style="min-height:259px;max-height:300px;height:274px">
          <img :src="movie.image_url" class="h-full w-full">
         </div>
         <button v-on:click="collect_or_cancle(movie.id)"
            id="collect" :class="collectStatus ? 'bg-gray-500' : 'bg-blue-500'"
            class="copy text-white w-full px-4 py-1 mt-2 text-sm rounded border">{{ collectMessage }}</button>
        </div>
        <div id="info" data-movie-id="443">
         <ul>
          <li class="text-lg font-semibold">{{ movie.movie_name }} ({{ movie.release_year }}) </li>
          <li>导演: {{ movie.director  }}</li>
          <li>编剧: {{ movie.scriptwriter }}</li>
          <li>主演: {{ movie.actors}}</li>
          <li>语言: {{ movie.language }}</li>
          <li>首播: {{ movie.release_date }}</li>
          <li>集数: {{ movie.duration }}</li>
          <li>类型: {{ movie.types }}</li>
          <li> 制片国家/地区: 
            <span v-if="movie.region === 1">China Mainland</span>
            <span v-else-if="movie.region === 2">HongKong</span>
            <span v-else-if="movie.region === 3">Taiwan</span>
            <span v-else-if="movie.region === 4">United States</span>
            <span v-else-if="movie.region === 5">Korean</span>
            <span v-else-if="movie.region === 6">Japan</span>
         </li>
          <li>又名: {{ movie.alternate_name}}</li>
          <li>豆瓣评分: {{ movie.rate }}</li>
         </ul>
        </div>
       </div>
       <div class="rounded bg-white mx-4 my-4 py-6">
        <div class="px-6">
         <h1 class="text-lg mb-6 font-semibold">简介</h1>
         <p>{{ movie.review }}</p>
        </div>
        
    </div>
        <div id="download_info" class="rounded bg-white mx-4 mt-4 py-6">
        <h1 class="text-lg mb-6 font-semibold px-6">网盘地址</h1>
            <div v-if="movie.download_info" class="px-6">
                <div v-if="downloadInfo">
                    {{ movie.download_info }}
                </div>
                <div v-else class="flex justify-center items-center mx-6 rounded h-28 bg-gradient-to-r">
                    <button v-on:click="check_member_status" id="check_member" class="rounded text-center bg-black text-white px-4 py-2">download info</button>
                </div>
               
            </div>
            <div v-else class="px-6">
                No Link
            </div>
       
       </div>
      </div>
     </div>
     </div>
 </div>
    <Footer/>
 
    

</template>


<script>
import axios from 'axios'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import showMessage from '@/utils/message';


export default {
    name: 'MovieDetail',
    data: function() {
        return {
            movie: {},
            collectStatus:false,
            collectMessage:'',
            downloadInfo: false,
            userinfo: ''
        }
    },

    components: {
        Header, Footer
    },

    mounted() {
        this.get_movie_info();
        // check if user is loged in
        if (!this.$store.state.isLogin){
            this.collectStatus = false
            this.collectMessage = 'Save'
        }else {
            const movie_id = this.$route.params.id
            this.get_collect_status(movie_id)
        }
    }, 
    methods: {
        get_movie_info: function(){
            axios
                .get('/api/movie/' + this.$route.params.id)
                .then(response => (this.movie= response.data))
        },
        get_collect_status(movie_id){
            axios
                .get('/api/collects/' + movie_id + '/is_collected/', {
                    headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }
                })
                .then(response => {
                    this.collectStatus = response.data.is_collected
                    if (this.collectStatus){
                        this.collectMessage = "Unsave"
                    }else{
                        this.collectMessage = "Save"
                    }
                })
        },
        // collect or cancle collecte
        collect_or_cancle(movie_id){
            if (!this.$store.state.isLogin){
                showMessage('Please Login First', 'error', ()=> {
                    this.$router.push({
                        name: 'Login'
                    })
                })
                return
            }else{
                if (this.collectStatus) {
                    this.cancle_collect_movie(movie_id)
                }else {
                    this.collect_movie(movie_id)
                }
            }
        },
        collect_movie(movie_id){
            axios
                .post('/api/collects/', {movie_id: movie_id}, {
                    headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }
                })
                .then(response => {
                    const status_code = response.data.status_code
                    const message = response.data.message
                    if (status_code === 0){
                        this.collectStatus = true
                        this.collectMessage = 'Unsave'
                        showMessage(message, 'info')
                    }else {
                        showMessage(message, 'error')
                    }
                    
                })
                .catch(error => {
                    showMessage(error, 'error')
                })
        },
        cancle_collect_movie(movie_id){
            axios
                .delete('/api/collects/' + movie_id + '/', {
                    headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }
                })
                .then(response => {
                    const message = response.data.message
                    if (message === 'Uncollect Successfully'){
                        this.collectStatus = false
                        this.collectMessage = 'Save'
                    }
                    showMessage(message, 'info')
                })
                .catch(error => {
                    showMessage('Uncollect Unsuccessfully', 'error')
                })
        },
        check_member_status(){
            if(!this.$store.state.isLogin){
                showMessage('Please login first')
                return 
            }
            axios
                .get('/api/users/me', {headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }})
                .then(response => {
                    this.userinfo = response.data
                    if (this.userinfo.profile.is_upgrade) {
                        this.downloadInfo = true
                    }
                    else {
                        alert('redirect to membership page')
                        this.$router.push({
                            name: 'MembershipCard'
                        })
                    }
                })
        }
    }
}
</script>