<template>
    <div class="relative min-h-screen flex flex-col">
        <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
            <div class="absolute inset-0 bg-gray-600 bg-opacity-90"></div>
        </div>
      <!-- Success Popup -->
      <div
        v-if="showSuccessPopup"
        class="absolute top-10 left-1/2 transform -translate-x-1/2 bg-popup text-white py-3 px-6 rounded-lg shadow-lg z-20"
      >
        Successfully Logged In!
      </div>
  
      <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-lg shadow-lg p-10 w-96 sm:w-[30rem] z-10">
        <router-link to="/">
          <button class="absolute top-4 right-7 text-gray-500 hover:text-gray-800 text-3xl focus:outline-none">&times;</button>
        </router-link>
  
        <h2 class="text-3xl font-bold text-left mb-6 text-gray-600">Log In</h2>
  
        <div v-if="!showPhoneInput">
          <input
            v-model="email"
            type="email"
            placeholder="Email Address"
            @blur="$v.email.$touch()"
            :class="[
              'w-full px-4 py-3 mb-2 border rounded-md focus:outline-none',
              $v.email.$invalid && $v.email.$dirty ? 'focus:ring-red-600 border-red-500' : 'focus:ring-green'
            ]"
          />
          <p v-if="$v.email.$invalid && $v.email.$dirty" class="text-red-500 text-sm mb-2">Please enter a valid email address.</p>
  
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            @blur="$v.password.$touch()"
            :class="[
              'w-full px-4 py-3 mb-2 border rounded-md focus:outline-none',
              $v.password.$invalid && $v.password.$dirty ? 'focus:ring-red-600 border-red-500' : 'focus:ring-green'
            ]"
          />
          <p v-if="$v.password.$invalid && $v.password.$dirty" class="text-red-500 text-sm mb-2">Please enter a valid password.</p>
  
          <button
            :disabled="$v.email.$invalid || $v.password.$invalid"
            @click="logInWithEmail"
            class="w-full py-3 bg-darkblue text-white rounded-md hover:bg-blue disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            Log In
          </button>
  
          <div class="flex items-center my-4">
            <hr class="flex-grow border-t border-gray-300" />
            <span class="px-2 text-gray-500 text-lg">or</span>
            <hr class="flex-grow border-t border-gray-300" />
          </div>
  
          <button @click="showPhoneInput = true" class="w-full py-3 flex items-center justify-center gap-2 border border-gray-300 rounded-md hover:bg-gray-100">
            <i class="fa-solid fa-phone text-darkblue"></i> Continue With Phone
          </button>
  
          <button class="w-full py-3 flex items-center justify-center gap-2 border border-gray-300 rounded-md hover:bg-gray-100 mt-4">
            <img src="/src/assets/img/google.jpeg" alt="Google" class="h-5 w-5" />
            Continue With Google
          </button>
        </div>
  
        <!-- Phone Input Section -->
        <div v-if="showPhoneInput" class="mt-4">
          <input
            v-model="phone"
            type="text"
            placeholder="Phone No."
            @blur="$v.phone.$touch()"
            :class="[
              'w-full px-4 py-3 mb-2 border rounded-md focus:outline-none',
              $v.phone.$invalid && $v.phone.$dirty ? 'focus:ring-red-600 border-red-500' : 'focus:ring-green-700'
            ]"
          />
          <p v-if="$v.phone.$invalid && $v.phone.$dirty" class="text-red-500 text-sm mb-2">Please enter a valid phone number.</p>
  
          <button
            :disabled="$v.phone.$invalid"
            @click="sendPhoneOTP"
            class="w-full py-3 bg-darkblue text-white rounded-md hover:bg-blue disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            Send One Time Password
          </button>
  
          <div class="flex items-center my-4">
            <hr class="flex-grow border-t border-gray-300" />
            <span class="px-2 text-gray-500 text-lg">or</span>
            <hr class="flex-grow border-t border-gray-300" />
          </div>
  
          <button @click="navigateToEmailSection" class="w-full py-3 flex items-center justify-center gap-2 border border-gray-300 rounded-md hover:bg-gray-100">
            <i class="fa-solid fa-envelope text-darkblue"></i> Continue With Email
          </button>
        </div>
  
        <p class="text-center text-gray-600 mt-4">
          New to Aspiro? <router-link to="/signup" class="text-blue hover:underline">Create account</router-link>
        </p>
      </div>
    </div>
</template>
  
<script setup lang="ts">
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import useVuelidate from '@vuelidate/core';
  import { required, email as emailValidator, minLength, helpers } from '@vuelidate/validators';
  import { useUserStore } from '/src/store.js';
  
  const phonePattern = helpers.withMessage(
    'Phone number must start with a digit and be exactly 10 digits.',
    (value: string) => /^[0-9]{10}$/.test(value)
  );
  
  const email = ref<string>('');
  const password = ref<string>('');
  const phone = ref<string>('');
  const showPhoneInput = ref<boolean>(false);
  const showSuccessPopup = ref<boolean>(false);
  
  const router = useRouter();
  const userStore = useUserStore();
  
  // Validation rules
  const rules = {
    email: { required, email: emailValidator },
    password: { required, minLength: minLength(8) },
    phone: { required, phonePattern },
  };
  
  const $v = useVuelidate(rules, { email, password, phone });
  
  const navigateToEmailSection = () => {
    showPhoneInput.value = false;
  };
  
  const logInWithEmail = () => {
    console.log('Attempting login with email:', email.value, password.value);
  
    // Ensure $v is accessed correctly
    $v.value.$touch(); // Mark fields as touched
    if ($v.value.email.$invalid || $v.value.password.$invalid) {
      console.log('Invalid inputs detected:', $v.value.email.$invalid, $v.value.password.$invalid);
      return;
    }
  
    // Simulate successful login
    userStore.login();
    showSuccessPopup.value = true;
  
    setTimeout(() => {
      showSuccessPopup.value = false; // Hide popup after 2 seconds
      router.push('/'); // Navigate to home page
    }, 2000);
  };
  
  const sendPhoneOTP = () => {
    if ($v.phone.$invalid) {
      console.log('Invalid phone number:', $v.phone.$invalid);
      return;
    }
  
    userStore.login();
    showSuccessPopup.value = true;
  
    setTimeout(() => {
      showSuccessPopup.value = false;
    }, 2000); // 2-second delay
  };
  
  const submitForm = () => {
    $v.value.$touch();
    if (!$v.value.$invalid) {
      alert('Account created successfully!');
    } else {
      console.log('Validation errors:', $v.value);
    }
  };
</script>
  