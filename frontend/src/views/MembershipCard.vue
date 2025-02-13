<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4">
    <Header/>

    <div id="main" class="p-12">
        <div class="grid grid-cols-3 gap-3">

            <div v-for="card in info.results" v-bind="card" class="flex flex-col justify-center">
                <div class="text-4xl text-center">
                    {{ card.card_name }}
                </div>
                <div class="text-4xl text-center">
                    ${{ card.card_price }}
                </div>
                <button v-on:click="pay(card)" data-pay_type="alipay" class="rounded text-center bg-black text-white px-4 py-2">Buy Membership Card</button>
            </div>
        </div>
    </div>

    <Footer/>
</div>
</template>


<script>

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'

export default{
    name: 'MembershipCard',
    components: { Header, Footer },
    data: function(){
        return {
            info: '',
            pay_url:''
        }
    },
    mounted() {
        this.get_card_info()
    },
    methods: {
        get_card_info(){
            axios
                .get('api/cards/')
                .then(response => {
                    this.info = response.data
                })
        },
        pay(card){
            axios
                .get('/api/alipay/?card_id=' + card.id, {
                    headers: {
                        'Authorization': 'JWT ' + localStorage.getItem('token')
                    }})
                .then(response => {
                    window.location.href = response.data
                })
        }
    }
    
}

</script>
