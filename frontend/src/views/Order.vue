
<template>
<div id="container" class="flex flex-col min-h-screen bg-primary-300 text-white text-lg pd-20">
    <Header/>
    <div id="main" class="bg-primary-300 p-6 text-black">
        <div class="rounded bg-white mx-4 my-4 py-6">
            <div class="px-6">
                <h1 class="text-lg font-semibold">我的订单</h1>
            </div>
        </div>

        <div class="rounded bg-white mx-4 mt-4 py-6">
      <div id="tabs" class="flex justify-start items-center py-4">
       <div class="px-4 text-md">
        <a href="/orders" class="order-status" data-order-status="all">全部订单</a>
       </div>
       <div class="px-4 text-md">
        <a href="/orders/?pay_status=paying" class="order-status" data-order-status="unpay">未付款</a>
       </div>
       <div class="px-4 text-md">
        <a href="/orders/?pay_status=trade_success" class="order-status" data-order-status="payed">已付款</a>
       </div>
       <div class="flex items-center ml-4">
        <div class="relative shrink">
         <form>
          <input type="text" name="order_sn" class="outline-0 h-9 rounded border border-gray-600 placeholder-gray-400 w-64 px-2 py-1" placeholder="请输入订单号" value="" />
          <div class="absolute top-0 right-0 flex items-center h-full">
           <div class="rounded text-xs text-gray-400 px-2 mr-2">
            <button>
             <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewbox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
             </svg></button>
           </div>
          </div>
         </form>
         <div class="mt-4 mb-3">
       <div class="not-prose relative bg-slate-50 rounded-xl overflow-hidden dark:bg-slate-800/25">
        <div class="absolute inset-0 bg-grid-slate-100 [mask-image:linear-gradient(0deg,#fff,rgba(255,255,255,0.6))] dark:bg-grid-slate-700/25 dark:[mask-image:linear-gradient(0deg,rgba(255,255,255,0.1),rgba(255,255,255,0.5))]" style="background-position:10px 10px"></div>
        <div class="relative rounded-xl overflow-auto">
         <div class="shadow-sm overflow-hidden my-8">
          <table class="border-collapse table-auto w-full text-sm">
           <thead>
            <tr>
             <th class="border-b dark:border-slate-600 font-medium p-4 pl-8 pt-0 pb-3 text-slate-400 dark:text-slate-200 text-left">订单号</th>
             <th class="border-b dark:border-slate-600 font-medium p-4 pt-0 pb-3 text-slate-400 dark:text-slate-200 text-left">商品名称</th>
             <th class="border-b dark:border-slate-600 font-medium p-4 pt-0 pb-3 text-slate-400 dark:text-slate-200 text-left">购买日期</th>
             <th class="border-b dark:border-slate-600 font-medium p-4 pt-0 pb-3 text-slate-400 dark:text-slate-200 text-left">金额</th>
             <th class="border-b dark:border-slate-600 font-medium p-4 pt-0 pb-3 text-slate-400 dark:text-slate-200 text-left">订单状态</th>
            </tr>
           </thead>
           <tbody class="bg-white dark:bg-slate-800">
            <tr v-for="order in info.results">
             <td class="border-b border-slate-100 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400">{{ order.order_sn }}</td>
             <td class="border-b border-slate-100 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400">{{ order.card.card_name }}</td>
             <td class="border-b border-slate-100 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400">{{ order.create_at }}</td>
             <td class="border-b border-slate-100 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400">{{ order.order_amount }}</td>
             <td class="border-b border-slate-100 dark:border-slate-700 p-4 text-slate-500 dark:text-slate-400">{{ order.pay_status }}</td>
             <td class="border-b border-slate-100 dark:border-slate-700 py-4 text-slate-500 dark:text-slate-400"><button class="pay rounded border bg-gray-500 hover:bg-blue-500 hover:text-white text-sm h-8 w-16 text-primary-100">去支付</button></td>
            </tr>
           </tbody>
          </table>
         </div>
        </div>
       </div>
       </div>
        </div>
       </div>
      </div>

      </div>
    </div>

</div>

<!-- paginator start -->
<Page :info="info" />
<!-- paginator end -->
<Footer/>
</template>

<script>
import axios from 'axios';
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import showMessage from '@/utils/message';
import Page from '@/components/Page.vue';


export default {
    name: 'Order',
    components: {
        Header, Footer, Page
    },
    data: function(){
        return {
            info: ''
        }
    },
    mounted(){
        this.get_orders()
    },
    methods: {
        get_orders(){
            let url = 'api/orders'
            const page = Number(this.$route.query.page);
            const pay_status = this.$route.query.pay_status;
            const params = new URLSearchParams();
            if (page) {
                params.append('page', page)
            }
            if (pay_status) {
                params.append('pay_status', pay_status)
            }

            url = url + "?" + params.toString()
            axios
                .get(url)
                .then(response => {
                    this.info = response.data
                })
        }
    },
    watch: {
        $route(){
            this.get_orders()
        }
    }
}
</script>