<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background Overlay -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <div class="relative z-10 flex flex-col flex-grow">
      <NavBar />

      <!-- Loader -->
      <div v-if="loading" class="min-h-screen flex items-center justify-center p-6">
        <div class="loader"></div>
      </div>

      <!-- Form Content -->
      <div v-else class="min-h-screen flex flex-col items-center justify-center p-6">
        <div class="max-w-6xl mx-auto w-full px-8 lg:px-16 flex flex-col md:flex-row gap-8 items-center justify-center">
          <!-- Form Section (left side) -->
          <div class="w-full md:w-2/3">
            <h2 class="text-4xl font-extrabold text-gray-900 text-left">Let’s Get to Know You! 👋</h2>
            <p class="text-gray-600 mt-2 text-left">
              We’re almost there — just a few quick details to get you started on your journey 🚀
            </p>

            <form
              @submit.prevent="goToNextPage"
              class="mt-6 w-full bg-lightblue shadow-md rounded-lg p-6"
            >
              <!-- Name -->
              <div class="mb-4">
                <label class="block text-gray-700 font-medium">Name:</label>
                <input
                  type="text"
                  v-model="formData.name"
                  class="w-full border p-3 rounded"
                  @blur="validateField('name')"
                />
                <p v-if="touched.name && errors.name" class="text-red-500 text-sm mt-1">
                  {{ errors.name }}
                </p>
              </div>

              <!-- Age -->
              <div class="mb-4">
                <label class="block text-gray-700 font-medium">Age:</label>
                <input
                  type="number"
                  v-model="formData.age"
                  class="w-full border p-3 rounded"
                  @blur="validateField('age')"
                />
                <p v-if="touched.age && errors.age" class="text-red-500 text-sm mt-1">
                  {{ errors.age }}
                </p>
              </div>

              <!-- Education Level -->
              <div class="mb-4">
                <label class="block text-gray-700 font-medium">Level of Education:</label>
                <select
                  v-model="formData.educationLevel"
                  class="w-full border p-3 rounded"
                  @change="validateField('educationLevel')"
                >
                  <option value="" disabled>Select</option>
                  <option value="undergraduate">Undergraduate</option>
                  <option value="postgraduate">Postgraduate</option>
                </select>
                <p v-if="touched.educationLevel && errors.educationLevel" class="text-red-500 text-sm mt-1">
                  {{ errors.educationLevel }}
                </p>
              </div>

              <!-- CGPA Fields -->
              <div v-if="formData.educationLevel === 'undergraduate'" class="mb-4">
                <label class="block text-gray-700 font-medium">Undergraduate CGPA:</label>
                <input
                  type="text"
                  v-model="formData.undergradCgpa"
                  class="w-full border p-3 rounded"
                  @blur="validateField('undergradCgpa')"
                />
                <p v-if="touched.undergradCgpa && errors.undergradCgpa" class="text-red-500 text-sm mt-1">
                  {{ errors.undergradCgpa }}
                </p>
              </div>

              <div v-if="formData.educationLevel === 'postgraduate'" class="mb-4">
                <label class="block text-gray-700 font-medium">Undergraduate CGPA:</label>
                <input
                  type="text"
                  v-model="formData.undergradCgpa"
                  class="w-full border p-3 rounded"
                  @blur="validateField('undergradCgpa')"
                />
                <p v-if="touched.undergradCgpa && errors.undergradCgpa" class="text-red-500 text-sm mt-1">
                  {{ errors.undergradCgpa }}
                </p>
              </div>

              <div v-if="formData.educationLevel === 'postgraduate'" class="mb-4">
                <label class="block text-gray-700 font-medium">Postgraduate CGPA:</label>
                <input
                  type="text"
                  v-model="formData.postgradCgpa"
                  class="w-full border p-3 rounded"
                  @blur="validateField('postgradCgpa')"
                />
                <p v-if="touched.postgradCgpa && errors.postgradCgpa" class="text-red-500 text-sm mt-1">
                  {{ errors.postgradCgpa }}
                </p>
              </div>

              <!-- Research Experience -->
              <div class="mb-4">
                <label class="block text-gray-700 font-medium">Research Experience:</label>
                <select
                  v-model="formData.researchExperience"
                  class="w-full border p-3 rounded"
                  @change="validateField('researchExperience')"
                >
                  <option value="" disabled>Select</option>
                  <option value="no">No</option>
                  <option value="yes">Yes</option>
                </select>
                <p v-if="touched.researchExperience && errors.researchExperience" class="text-red-500 text-sm mt-1">
                  {{ errors.researchExperience }}
                </p>
              </div>

              <div v-if="formData.researchExperience === 'yes'" class="mb-4">
                <label class="block text-gray-700 font-medium">Describe Research:</label>
                <textarea
                  v-model="formData.researchDetails"
                  class="w-full border p-3 rounded"
                  @blur="validateField('researchDetails')"
                ></textarea>
                <p v-if="touched.researchDetails && errors.researchDetails" class="text-red-500 text-sm mt-1">
                  {{ errors.researchDetails }}
                </p>
              </div>

              <button
                type="submit"
                :disabled="!isFormValid"
                class="w-full bg-blue text-white font-bold py-3 px-6 mt-4 rounded-lg disabled:bg-gray-400"
              >
                Next
              </button>
            </form>
          </div>

          <!-- Image Section (right side) -->
          <div class="hidden md:block w-full md:w-1/3">
            <img
              src="/src/assets/img/faq.png"
              alt="Career Steps"
              class="w-full h-auto"
            />
          </div>
        </div>
      </div>

      <Footer class="mt-auto w-full relative z-20" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import NavBar from '../components/Core/NavBar.vue';
import Footer from '../components/Core/Footer.vue';

const router = useRouter();

const touched = ref({
  name: false,
  age: false,
  educationLevel: false,
  undergradCgpa: false,
  postgradCgpa: false,
  researchExperience: false,
  researchDetails: false
});

const loading = ref(true);
onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 2000);
});

const formData = ref({
  name: '',
  age: '',
  educationLevel: '',
  undergradCgpa: '',
  postgradCgpa: '',
  researchExperience: '',
  researchDetails: ''
});

const errors = ref({
  name: '',
  age: '',
  educationLevel: '',
  undergradCgpa: '',
  postgradCgpa: '',
  researchExperience: '',
  researchDetails: ''
});

const validateField = (field) => {
  const value = formData.value[field];
  switch (field) {
    case 'name':
      errors.value.name = value && value.trim().length >= 3 ? '' : 'Name must be at least 3 characters long.';
      break;
    case 'age':
      errors.value.age = value && Number(value) > 18 ? '' : 'Age must be greater than 18.';
      break;
    case 'educationLevel':
      errors.value.educationLevel = value ? '' : 'Please select your level of education.';
      break;
    case 'undergradCgpa':
      errors.value.undergradCgpa = /^\d(\.\d{1,2})?$|^10(\.0{1,2})?$/.test(value) ? '' : 'Enter a valid CGPA between 0.0 and 10.0.';
      break;
    case 'postgradCgpa':
      errors.value.postgradCgpa = /^\d(\.\d{1,2})?$|^10(\.0{1,2})?$/.test(value) ? '' : 'Enter a valid CGPA between 0.0 and 10.0.';
      break;
    case 'researchExperience':
      errors.value.researchExperience = value ? '' : 'Please select an option.';
      break;
    case 'researchDetails':
      const wordCount = value ? value.trim().split(/\s+/).length : 0;
      errors.value.researchDetails = wordCount >= 5 ? '' : 'Description must contain at least 5 words.';
      break;
  }
};

const isFormValid = computed(() => {
  const { name, age, educationLevel, undergradCgpa, postgradCgpa, researchExperience, researchDetails } = formData.value;
  const fieldsToValidate = ['name', 'age', 'educationLevel', 'researchExperience'];
  if (educationLevel === 'undergraduate') fieldsToValidate.push('undergradCgpa');
  if (educationLevel === 'postgraduate') fieldsToValidate.push('undergradCgpa', 'postgradCgpa');
  if (researchExperience === 'yes') fieldsToValidate.push('researchDetails');
  return fieldsToValidate.every((field) => !errors.value[field]);
});

const goToNextPage = () => {
  Object.keys(touched.value).forEach((field) => {
    touched.value[field] = true;
    validateField(field);
  });

  if (isFormValid.value) {
    router.push('/next');
  }
};
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
</style>
