<template>
  <div id="container" class="flex flex-col min-h-screen bg-primary-300 text-white text-lg">
      <Header/>

    <main class="flex-grow px-4">
      <MovieList/>
    </main>

  </div>
 
    <Footer/>
</template>





<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
  components: {
    Header, Footer, MovieList
  }
}



</script>
