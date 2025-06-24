<template>
  <nav class="bg-darkblue shadow-md px-8 py-4 flex items-center justify-between">
    <!-- Logo -->
    <router-link to="/">
      <img src="/src/assets/img/lightlogo.png" alt="Logo" class="h-16 cursor-pointer" />
    </router-link>

    <!-- Search Bar -->
    <div class="relative flex items-center bg-gray-100 rounded-full px-4 py-3 w-2/3 sm:w-1/5 md:w-1/2 z-30">
      <i class="fa fa-search text-gray-500 ml-2 mr-2"></i>
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search for courses"
        class="bg-transparent focus:outline-none flex-1 text-sm"
      />
    </div>

    <!-- Right Side Links -->
    <div class="flex items-center gap-6 text-white text-lg">
      <router-link to="/about" class="hover:underline">About Us</router-link>

      <!-- Show Login if not logged in -->
      <router-link v-if="!userStore.isLoggedIn" to="/login">
        <button class="px-5 py-2 text-white text-lg">
          Log In
        </button>
      </router-link>

      <!-- Show Profile Dropdown if logged in -->
      <div v-else class="relative" @click="toggleDropdown">
        <i class="fa-solid fa-user text-white text-2xl cursor-pointer"></i>
        <div v-if="showDropdown" class="absolute right-0 mt-2 bg-white rounded-md shadow-lg w-40 z-40">
          <router-link to="/profile" class="block px-4 py-2 hover:bg-gray-100">View Profile</router-link>
          <button @click="logout" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Log Out</button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "/src/store.js";

const searchQuery = ref("");
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
