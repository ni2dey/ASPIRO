<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background Overlay with Light Effect -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <div class="relative z-10 flex flex-col flex-grow">
      <NewNav />

      <!-- Content Wrapper with Side Margin -->
      <div class="max-w-6xl mx-auto w-full px-8 lg:px-16">
        <!-- Hero Section -->
        <section class="flex flex-col lg:flex-row items-center justify-between py-20 lg:py-32">
          <!-- Left Content -->
          <div class="lg:w-1/2 text-center lg:text-left">
            <h1 class="text-4xl lg:text-5xl font-extrabold leading-tight text-gray-900">
              Discover Your Perfect Career Path<br />
              with Our <span class="text-blue">Smart Recommendation System</span>
            </h1>
            <p class="mt-6 text-gray-700 text-lg">
              Not sure what job suits your skills and interests? Our system analyzes your strengths to recommend personalized career options—making your path to success clearer and easier than ever.
            </p>

            <!-- Buttons -->
            <div class="mt-8 flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <router-link to="/form">
                <button class="bg-blue hover:bg-darkblue text-white font-semibold py-3 px-6 rounded-lg text-lg transition-all shadow-lg">
                  Get Started
                </button>
              </router-link>
              <router-link to="/about">
                <button class="bg-slate-50 hover:bg-lightblue text-blue hover:text-blue font-semibold py-3 px-6 rounded-lg text-lg transition-all shadow-lg">
                  Learn More
                </button>
              </router-link>
            </div>
          </div>

          <!-- Right Image -->
          <div class="lg:w-1/2 mt-12 lg:mt-0 flex justify-end pr-4">
            <img
              src="/src/assets/img/hero.png"
              alt="Career Exploration Illustration"
              class="w-full max-w-md"
            />
          </div>
        </section>

        <Grid />  
      </div> 

      <div class="mt-20">
          <CurvedBanner />
      </div> 
      <div class="mt-20">
        <FAQ /> 
      </div>
      <Footer class="mt-auto w-full relative z-20" />
    </div>
  </div>
</template>

<script setup>
import Footer from '../components/Core/Footer.vue';
import CurvedBanner from '../components/Core/CurvedBanner.vue';
import FAQ from '../components/Core/FAQ.vue';
import Grid from '../components/Core/Grid.vue';
import NewNav from '../components/Core/NewNav.vue';
</script>
