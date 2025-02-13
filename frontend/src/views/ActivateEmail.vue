<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen">
        <Header/>
        <div class="text-center text-2xl p-8">
            Activate your account
        </div>
        <div class="flex items-center justify-center">
            <div class="2-1/4 p-4 bg-gray rounded-lg shadow-lg">
                Please click button below to activate your account
            </div>
            <div class="flex justify-center">
                <button v-on:click="activate" class="bg-green-500 text-white px-4 py-2 rounded">Activate Account</button>
            </div>

        </div>

        <Footer/>
    </div>
</template>

<script>
import axios from 'axios'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import showMessage from '@/utils/message.js'

export default {
    name: 'ActivateEmail',
    components: { Header, Footer },
    methods: {
        activate() {
            const uid = this.$route.params.uid
            const token = this.$route.params.token
            const formData = {
                uid: uid,
                token: token
            }
            axios
                .post('/api/users/activation/', formData)
                .then( response => {
                    showMessage("Account has been activated, please login", 'infor', ()=>{
                        this.$route.push({name: 'Login'})
                    })
                })
                .catch (error => {
                    console.log(error)
                    const errorData = error.response.data
                    const errorMessage = Object.values(errorData).flat();
                    for (let i=0; i<errorMessage.length; i++) {
                        showMessage(errorMessage[i], )
                    }
                })
        }
    }

}
</script>