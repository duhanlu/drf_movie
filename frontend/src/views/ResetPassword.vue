<template>
    <div>
        <Header/>
    </div>

    <div id="main" class="bg-primary-300 p-6 text-black">
     <div class="rounded bg-white mx-4 my-4 py-6">
        <div class="px-6">
        <h1 class="text-lg font-semibold text-center">Reset Password</h1>
        </div>

        <div class="flex items-center justify-center">
            <div class="w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
                <div class="text-black text-center p-4">
                    <p class="font-bold py-4">Please enter the email</p>
                </div>
                <div class="flex items-center justify-center">
                    <input v-model="email" class="outline-0 h-9 rounded border border-black justify-center text-center placeholder-gray-400" 
                        placeholder="Enter email here"></input>
                </div>
                
                <div class="flex justify-center">
                <button v-on:click="resetPassword" class="bg-black rounded text-white my-4">Submit</button>
                </div>
            </div>
            
        </div>
    </div>
    </div>
    <Footer/>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'
import showMessage from '@/utils/message.js'

export default {
    name: 'ResetPassword',
    data: function() {
        return {
            email:'',
        }
    },
    components: {Header, Footer},
    methods: {
        resetPassword() {
            const email = this.email.trim()
            axios 
                .post('/api/users/reset_password/', {email: email})
                .then(response => {
                    showMessage('Please change your password with the link in your email', 'info', ()=>{
                        this.$router.push({
                            name: 'Login'
                        })
                    })
                })
                .catch(error => {
                    const errorData = error.response.data;
                    const errorMessage = Object.values(errorData).flat();
                    for (let i = 0; i < errorMessage.length; i++) {
                        showMessage(errorMessage[i])
                    }
                })
        },
    }
}
</script>