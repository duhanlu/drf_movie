<template>
<div class="flex items-center justify-center">
    <div class="w-full px-2 mx-auto" style="max-width:1440px">
        <div id="movie-list" class="p-2 grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">

            <div class="movie" v-for="movie in info.results" :key="movie.id">
            <a :href="'/movie/' + movie.id">
                <div class="relative">
                        <div class="h-full w-full min-h-[259px]" style="min-height:259px;max-height:300px;height:274px">
                            <img :src="movie.image_url" 
                                alt="Movie Image" 
                                class="rounded h-full w-full" 
                                @error="(e) => e.target.src = 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSPNZGVH2GVKwKtvWMHfNyF2fSK1fh_f84DMOQ2xgZ-UTdHNh3H'">
                        </div>
                        <div v-if="movie.is_top" class="rounded absolute top-0 bg-purple-600 px-1 text-sm">Top</div>
                        <div v-if="movie.quality == 1" class="rounded absolute bottom-0 bg-blue-500 px-1 text-sm">720P</div>
                        <div v-if="movie.quality == 2" class="rounded absolute bottom-0 bg-blue-500 px-1 text-sm">1080P</div>
                        <div v-if="movie.quality == 3" class="rounded absolute bottom-0 bg-blue-500 px-1 text-sm">4K</div>
                    </div>
                    <p>{{ movie.movie_name }} ({{ movie.release_year }})</p>
                    <p class="text-sm text-primary-200">{{ movie.language}}</p>
            </a>
            </div>

        </div>
    </div>
</div>

<Page :info="info"/>
</template>

<script>
import axios from 'axios'
import Page from '@/components/Page.vue'

export default {
    name: 'MovieList',
    data: function(){
        return {
            info: ''
        }
    },
    components: { Page },

    mounted(){
        // axios send request
        this.get_movie_data()
    },
    methods: {
        get_movie_data: function() {
            let url = 'api/movie'
            const page = Number(this.$route.query.page)
            const search = this.$route.query.search;
            const category_id = this.$route.query.category_id;
            const region = this.$route.query.region;
            const params = new URLSearchParams();
            if (page) {
                params.append('page', page)
            }
            if (search) {
                params.append('movie_name', search)
            }
            if (category_id) {
                params.append('category_id', category_id)
            }
            if (region) {
                params.append('region', region)
            }

            url = url + "?" + params.toString()

            axios
            .get(url)
            .then(response => {
                this.info = response.data;
                console.log(this.info); // Debug the movie objects
    })
            .catch(error => {
                console.log(error)

            })
        }
    },
    watch: {
        // listen route change
        $route() {
            this.get_movie_data()
        }
    }
}
</script>

<!--- link: https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2874262709.jpg -->
