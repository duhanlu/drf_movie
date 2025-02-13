<template>
    <Header/>

    <div class="rounded bg-white mx-4 my-4 py-6">
      <div class="px-6">
       <h1 class="text-lg font-semibold justify-center">我的收藏</h1>
      </div>
     </div>
     <div class="rounded bg-white mx-4 mt-4 py-6">
        <div v-if="info">
        <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <div class="movie" v-for="movie in info">
         <a :href="'/movie/' + movie.id">
          <div class="relative">
           <div class="cover">
            <img :src="movie.image_url" alt="" class="rounded h-full w-full" />
           </div>
          </div><p>{{ movie.movie_name }}</p><p class="text-sm text-primary-200">{{ movie.language }}</p></a>
        </div>
        </div>
        </div>
        <div v-else class="text-ceenter text-2xl">No saved movie</div>
     </div>

    <Footer/>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'
export default {
    name: 'Collect',
    data: function(){
        return {
            info: ''
        }
    },
    components: { Header, Footer },
    mounted() {
        this.get_collect_movie()
    },

    methods: {
        get_collect_movie() {
            axios 
                .get('api/collects/', {
                    headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }
                })
                .then(response => {
                    this.info = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    },

    }
</script>