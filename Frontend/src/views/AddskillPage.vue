<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <div class="relative z-10 flex flex-col flex-grow">
      <NavBar />

      <!-- Loader -->
      <div v-if="loading" class="min-h-screen flex items-center justify-center p-6">
        <div class="loader"></div>
      </div>

      <!-- Main Content -->
      <div v-if="!loading" class="flex-grow flex items-center justify-center px-4 py-24 relative">
        <div class="w-full max-w-6xl flex flex-col lg:flex-row items-center lg:items-start justify-between gap-12">
          <!-- Left Content -->
          <div class="lg:w-1/2 z-10">
            <h2 class="text-4xl font-bold text-word mb-6 text-left">
              🛠️ Let's Build Your Skill Stack!
            </h2>
            <p class="text-gray-600 text-base mb-6 text-left">
              Choose 4 to 6 skills you're awesome at—or excited to explore! 🧐
            </p>

            <!-- Input and Dropdown -->
            <div class="relative mb-6">
              <input
                v-model="searchQuery"
                @input="filterSkills"
                @focus="showDropdown = true"
                type="text"
                placeholder="Type a skill like Aws, Python..."
                class="w-full px-4 py-3 rounded-xl border focus:ring-2 border-gray-300 focus:outline-none focus:ring-blue-400 disabled:bg-gray-100"
                :disabled="selectedSkills.length >= 6"
              />

              <!-- Dropdown -->
              <ul
                v-if="showDropdown && filteredSkills.length"
                class="absolute w-full bg-white border border-gray-200 rounded-xl shadow-md mt-1 z-10 max-h-60 overflow-auto"
              >
                <li
                  v-for="(skill, index) in filteredSkills.slice(0, 6)"
                  :key="index"
                  @click="selectSkill(skill)"
                  class="px-4 py-2 hover:bg-gray-100 cursor-pointer transition duration-200"
                >
                  {{ skill }}
                </li>
              </ul>

              <div
                v-if="showDropdown && searchQuery && !filteredSkills.length"
                class="absolute w-full bg-white border border-gray-200 rounded-xl shadow-md mt-1 z-10 px-4 py-2 text-gray-500"
              >
                Skill not found...
              </div>
            </div>

            <!-- Selected Skills -->
            <div class="flex flex-wrap gap-3 mb-4">
              <div
                v-for="(skill, index) in selectedSkills"
                :key="index"
                class="bg-lightblue text-gray-700 font-semibold px-4 py-2 rounded-full flex items-center gap-2 shadow transition duration-200"
              >
                {{ skill }}
                <button @click="removeSkill(index)" class="hover:text-red-400 transition">
                  &times;
                </button>
              </div>
            </div>

            <!-- Submit Button -->
            <button
              class="bg-blue text-white hover:bg-darkblue px-6 py-3 rounded-lg font-semibold transition-transform transform hover:scale-105 sm:w-auto block"
              @click="handleSubmit"
            >
              Show me career options
            </button>
          </div>

          <!-- Right Side Image -->
          <div class="lg:w-1/2 flex justify-center z-0">
            <img
              src="/src/assets/img/skills.png"
              alt="Skills Illustration"
              class="w-98 max-w-full opacity-90 pointer-events-none"
            />
          </div>
        </div>
      </div>

      <!-- Footer -->
      <Footer class="mt-18 w-full relative z-20" />
    </div>

    <!-- Custom Popup -->
    <transition name="fade">
      <div
        v-if="showPopup"
        class="fixed top-28 right-6 bg-red-500 text-white px-6 py-3 rounded-xl shadow-lg z-50 transition-opacity duration-300"
      >
        {{ popupMessage }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import NavBar from '../components/Core/NavBar.vue'
import Footer from '../components/Core/Footer.vue'
import { skillsList } from '/src/skills.js'

const router = useRouter()

const loading = ref(true)
onMounted(() => {
  setTimeout(() => {
    loading.value = false
  }, 2000)
})

const searchQuery = ref('')
const selectedSkills = ref([])
const filteredSkills = ref([])
const showDropdown = ref(false)

const showPopup = ref(false)
const popupMessage = ref('')

const showCustomPopup = (message, duration = 3000) => {
  popupMessage.value = message
  showPopup.value = true
  setTimeout(() => {
    showPopup.value = false
  }, duration)
}

const filterSkills = () => {
  const query = searchQuery.value.toLowerCase().trim()
  if (!query) {
    filteredSkills.value = []
    return
  }

  filteredSkills.value = skillsList.filter(skill =>
    skill.toLowerCase().includes(query) &&
    !selectedSkills.value.includes(skill)
  ).slice(0, 6)
}

const selectSkill = (skill) => {
  if (selectedSkills.value.length >= 6) {
    showCustomPopup('You can only select up to 6 skills.')
    return
  }

  if (!selectedSkills.value.includes(skill)) {
    selectedSkills.value.push(skill)
  }
  searchQuery.value = ''
  filteredSkills.value = []
  showDropdown.value = false
}

const removeSkill = (index) => {
  selectedSkills.value.splice(index, 1)
}

const handleSubmit = () => {
  if (selectedSkills.value.length < 4) {
    showCustomPopup('Please select at least 4 skills before submitting.')
    return
  }

  router.push({ path: '/recommend', query: { skills: selectedSkills.value.join(',') } })
}
</script>

<style scoped>
.loader {
  width: 40px;
  aspect-ratio: 1.154;
  --_g: no-repeat radial-gradient(farthest-side,#1e3a8a 90%,#0000);
  background: 
    var(--_g) 50% 0,
    var(--_g) 0 100%,
    var(--_g) 100% 100%;
  background-size: 35% calc(35% * 1.154);
  animation: l16 1s infinite;
}

@keyframes l16 {
  50%, 100% {
    background-position: 100% 100%, 50% 0, 0 100%;
  }
}

/* Fade transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
