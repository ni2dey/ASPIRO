<template>
    <nav class="w-full px-6 lg:px-10 py-5 flex items-center justify-between z-50">
      <!-- Logo -->
      <router-link to="/" class="flex items-center">
        <img src="/src/assets/img/mainlogo.png" alt="Logo" class="h-16 w-auto mt-2" />
        <span class="text-3xl font-semibold text-darkblue" style="font-family: 'Red Hat Display', sans-serif;">
            Aspiro.
        </span>
      </router-link>
  
      <!-- Navigation Links -->
      <div class="hidden md:flex space-x-10 text-gray-800 font-medium text-lg">
        <router-link to="/careers" class="hover:text-blue transition">Careers</router-link>
        <router-link to="/about" class="hover:text-blue transition">About</router-link>
        <router-link to="/contact" class="hover:text-blue transition">Contact</router-link>
        <router-link to="/blog" class="hover:text-blue transition">Blog</router-link>
      </div>
  
      <!-- Right Buttons -->
      <div class="flex items-center gap-5">
        <router-link to="/form">
          <button class="px-6 py-2.5 bg-blue text-white rounded-lg font-semibold text-lg hover:bg-darkblue transition">
            Get Started
          </button>
        </router-link>
  
        <!-- Login -->
        <router-link v-if="!userStore.isLoggedIn" to="/login">
          <button class="text-darkblue font-medium text-lg hover:text-blue transition">
            Log In
          </button>
        </router-link>
  
        <!-- Profile dropdown if logged in -->
        <div v-else class="relative" @click="toggleDropdown">
          <i class="fa-solid fa-user text-darkblue text-2xl cursor-pointer"></i>
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 bg-white rounded-md shadow-md w-44 z-40 text-base"
          >
            <router-link to="/profile" class="block px-4 py-2 hover:bg-gray-100">View Profile</router-link>
            <button @click="logout" class="block w-full text-left px-4 py-2 hover:bg-gray-100">
              Log Out
            </button>
          </div>
        </div>
      </div>
    </nav>
</template>
  
<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import { useUserStore } from "/src/store.js";
  
  const showDropdown = ref(false);
  const router = useRouter();
  const userStore = useUserStore();
  
  const toggleDropdown = () => {
    showDropdown.value = !showDropdown.value;
  };
  
  const logout = () => {
    userStore.logout();
    showDropdown.value = false;
    router.push("/");
  };
</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Radley:ital@0;1&family=Red+Hat+Display:ital,wght@0,300..900;1,300..900&display=swap');
</style>
  