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
         <div class="py-2">
           用户名： andy 
         </div>
         <div class="py-2">
           手机号：12312312312 
         </div>
         <div class="py-2">
           会员状态： 会员\ 非会员 
         </div>
         <div class="py-2">
           到期时间：***** 
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
import PersonalNav from '@/components/PersonalNav.vue'

export default {
    name: 'Personal',
    components: { Header, Footer, PersonalNav }

}
</script>