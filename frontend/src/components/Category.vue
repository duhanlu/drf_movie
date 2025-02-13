<template>
    <ul class="flex items-center space-x-5 ml-2">
        <li>
            <a href=http://127.0.0.1:8080/>首页</a>
        </li>
        <li>
            <a href=http://127.0.0.1:8080/>热门</a>
        </li>
        <li v-for="category in info.results" @click="toggle(category)" class="dropdown-menu flex items-center relative hover: cursor-pointer select-none">
            {{ category.category_name }}
            <span>
                <svg xmlns=http://www.w3.org/2000/svg class="h-5 w-5" viewBox="0 0 20 20" fill=currentColor>
                    <path fill-rule=evenodd d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule=evenodd></path>
                </svg>
            </span>
            <div :class="{hidden: !category.hidden}" class="dropdown-item-content absolute top-9 w-32 transition ease-in-out delay-150 z-50 sf-hidden">
                <ul class="bg-primary-700 py-2 px-4">
                    <li class="plx-2 py-2">
                        <a :href="'/?category_id='+ category.id" >All</a>
                    </li>
                    <li v-for="region in regions" class="plx-2 py-2">
                        <a :href="'/?category_id='+category.id+'&region='+region.id">{{ region.name }}</a>
                    </li>
                    
                </ul>
            </div>
        </li>
        
    </ul>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Category',
    data: function() {
        return {
            info: '',
            regions: [
                {id: 1, name: 'China Mainland'},
                {id: 2, name: 'HongKong'},
                {id: 3, name: 'China Taiwan'},
                {id: 4, name: 'United States'},
                {id: 5, name: 'Japan'},
                {id: 6, name: 'korea'},
                {id: 7, name: 'Others'},
            ],
        }
    },

    mounted() {
        this.get_category_info()
    },

    methods: {
        toggle(category) {
            category.hidden = !category.hidden
        },

        get_category_info() {
            axios
                .get('api/category')
                .then(response => {
                    this.info = response.data
                    console.log(this.info)
                })
        }
    },
}
</script>





