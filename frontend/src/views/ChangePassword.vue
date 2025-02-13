<template>
    <Header/>

    <div id="main" class="bg-primary-300 p-6 text-black">
     <div class="rounded bg-white mx-4 my-4 py-6">
      <div class="px-6">
       <h1 class="text-lg font-semibold">个人中心</h1>
      </div>
     </div>
     <div class="rounded bg-white mx-4 mt-4 py-6">
      <div id="tabs" class="flex justify-start items-center py-4 bg-gray-100">
       <div class="px-4 text-md">
        <a href="http://127.0.0.1:8080/personal" class="underline-gray">账号信息</a>
       </div>
       <div class="px-4 text-md">
        <a href="http://127.0.0.1:8080/change_password">修改密码</a>
       </div>
      </div>
      <div class="mt-4 mb-3">
       <div class="not-prose relative">
        <div class="ml-4 text-lg">
         <div class="py-2 text-md">
          <form action="" method="post" class="w-[300px]">
           <div class="flex items-center justify-between py-2">
            <label for="old_password">原始密码:</label>
            <input v-model="current_password" id="old_password" type="password" name="old_password" class="mx-2 outline-0 rounded border border-solid border-gray-500" value="" />
           </div>
           <div class="flex items-center justify-between py-2">
            <label for="new_password">新密码:</label>
            <input v-model="new_password" id="new_password" type="password" name="new_password" class="mx-2 outline-0 rounded border border-solid border-gray-500" value="" />
           </div>
           <div class="flex items-center justify-between py-2">
            <label for="confirm">确认密码:</label>
            <input v-model="re_new_password" id="confirm_password" type="password" name="confirm_password" class="mx-2 outline-0 rounded border border-solid border-gray-500" value="" />
           </div>
           <button v-on:click.prevent="setPassword" type="button" id="change_password" class="mb-2 rounded border bg-blue-500 text-white text-sm h-8 w-16">提交</button>
          </form>
         </div>
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
import showMessage from '@/utils/message.js'
import axios from 'axios'

export default {
    name: 'ChangePassword',
    components: { Header, Footer },
    methods: {
        setPassword() {
            const current_password = this.current_password.trim()
            const new_password = this.new_password.trim()
            const re_new_password = this.re_new_password.trim()
            if (current_password === '') {
                showMessage('Current password cannot be empty')
                return
            }
            if (new_password === '') {
                showMessage('New password cannot be empty')
                return
            }
            if (re_new_password !== new_password) {
                showMessage('New password does not match')
                return
            }
            const formData = {
                current_password: current_password,
                new_password: new_password,
                re_new_password: re_new_password
            }
            const token = localStorage.getItem('token')
            axios   
                .post('/api/users/set_password/', formData, {
                    headers: {
                        'Authorization': 'JWT ' + token
                    }
                })
                .then( response => {
                    showMessage('Password has changed successfully','info', ()=>{
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
        }
    }

}
</script>