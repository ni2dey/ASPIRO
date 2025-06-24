<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-gray-600 bg-opacity-90"></div>
    </div>

    <!-- Success Popup -->
    <div
      v-if="showPopup"
      class="fixed top-6 left-1/2 transform -translate-x-1/2 z-50 bg-popup text-white px-6 py-3 rounded-lg shadow-lg transition-all duration-500"
    >
      Account successfully created!
    </div>

    <!-- Signup Form -->
    <form
      @submit.prevent="submitForm"
      class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-lg shadow-lg p-10 w-96 sm:w-[30rem] z-10"
    >
      <router-link to="/">
        <button
          class="absolute top-4 right-7 text-gray-500 hover:text-gray-800 text-3xl focus:outline-none"
        >
          &times;
        </button>
      </router-link>

      <h2 class="text-3xl font-bold text-left mb-6 text-gray-600">Sign Up</h2>

      <div class="space-y-4">
        <!-- Name Fields -->
        <div class="grid grid-cols-2 gap-4">
          <div :class="{ 'border-red-500': $v.firstName.$invalid && $v.firstName.$dirty }">
            <input
              v-model.trim="form.firstName"
              type="text"
              placeholder="First Name"
              @blur="$v.firstName.$touch()"
              class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
            />
            <p v-if="$v.firstName.$invalid && $v.firstName.$dirty" class="text-red-500 text-sm mt-1">
              Invalid first name
            </p>
          </div>

          <div :class="{ 'border-red-500': $v.lastName.$invalid && $v.lastName.$dirty }">
            <input
              v-model.trim="form.lastName"
              type="text"
              placeholder="Last Name"
              @blur="$v.lastName.$touch()"
              class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
            />
            <p v-if="$v.lastName.$invalid && $v.lastName.$dirty" class="text-red-500 text-sm mt-1">
              Invalid last name
            </p>
          </div>
        </div>

        <!-- Email -->
        <div :class="{ 'border-red-500': $v.email.$invalid && $v.email.$dirty }">
          <input
            v-model.trim="form.email"
            type="email"
            placeholder="Email Address"
            @blur="$v.email.$touch()"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
          />
          <p v-if="$v.email.$invalid && $v.email.$dirty" class="text-red-500 text-sm mt-1">Invalid email address</p>
        </div>

        <!-- Phone -->
        <div :class="{ 'border-red-500': $v.phone.$invalid && $v.phone.$dirty }">
          <input
            v-model.trim="form.phone"
            type="text"
            placeholder="Phone no."
            @blur="$v.phone.$touch()"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
          />
          <p v-if="$v.phone.$invalid && $v.phone.$dirty" class="text-red-500 text-sm mt-1">Invalid phone number</p>
        </div>

        <!-- Password -->
        <div :class="{ 'border-red-500': $v.password.$invalid && $v.password.$dirty }">
          <input
            v-model.trim="form.password"
            type="password"
            placeholder="Password"
            @blur="$v.password.$touch()"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
          />
          <p v-if="passwordValidationError" class="text-red-500 text-sm mt-1">
            Password must contain at least one upper case letter, one number, and one special character.
          </p>
        </div>

        <!-- Confirm Password -->
        <div :class="{ 'border-red-500': $v.confirmPassword.$invalid && $v.confirmPassword.$dirty }">
          <input
            v-model.trim="form.confirmPassword"
            type="password"
            placeholder="Confirm Password"
            @blur="$v.confirmPassword.$touch()"
            class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green focus:border-transparent"
          />
          <p v-if="$v.confirmPassword.$invalid && $v.confirmPassword.$dirty" class="text-red-500 text-sm mt-1">
            Passwords do not match
          </p>
        </div>

        <!-- Terms Agreement -->
        <div class="flex items-center">
          <input
            type="checkbox"
            v-model="form.agreed"
            @blur="$v.agreed.$touch()"
            class="w-4 h-4"
          />
          <label class="ml-2 text-sm text-gray-500">
            I agree to Aspiro's
            <a href="#" class="text-darkblue hover:underline">Terms & conditions</a>
          </label>
        </div>
        <p v-if="$v.agreed.$invalid && $v.agreed.$dirty" class="text-red-500 text-sm">
          You must agree to the terms
        </p>
      </div>

      <!-- Submit -->
      <button
        type="submit"
        :disabled="isFormInvalid"
        class="w-full py-3 bg-darkblue text-white rounded-md hover:bg-blue disabled:bg-gray-300 disabled:cursor-not-allowed mt-3"
      >
        Create Account
      </button>

      <!-- OR Divider -->
      <div class="flex items-center my-4">
        <hr class="flex-grow border-t border-gray-300" />
        <span class="px-2 text-gray-500 text-lg">or</span>
        <hr class="flex-grow border-t border-gray-300" />
      </div>

      <!-- Google Auth -->
      <button
        class="w-full py-3 flex items-center justify-center gap-2 border border-gray-300 rounded-md hover:bg-gray-100 mt-4"
      >
        <img src="/src/assets/img/google.jpeg" alt="Google" class="h-5 w-5" />
        Sign in with Google
      </button>

      <!-- Login Redirect -->
      <p class="text-center text-gray-600 mt-4">
        Already have an account?
        <router-link to="/login" class="text-darkblue hover:underline">Log in</router-link>
      </p>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref, computed } from 'vue';
import useVuelidate from '@vuelidate/core';
import { required, email } from '@vuelidate/validators';
import { helpers } from '@vuelidate/validators';
import { useRouter } from 'vue-router';

const router = useRouter();
const showPopup = ref(false); // 👈 popup state

// Validation helpers
const phonePattern = helpers.withMessage(
  'Phone number must start with 9 and have exactly 10 digits',
  (value) => /^9\d{9}$/.test(value)
);
const phoneNotRepeating = helpers.withMessage(
  'Phone number cannot have repeating digits more than 3 times',
  (value) => !/(.)\1{3,}/.test(value)
);
const strongPassword = helpers.withMessage(
  'Strong Password',
  (value) => /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(value)
);
const sameAsPassword = helpers.withMessage(
  'Passwords do not match',
  (value, vm) => value === vm?.password
);

// Form state
const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  password: '',
  confirmPassword: '',
  agreed: false,
});

// Validation rules
const rules = reactive({
  firstName: { required },
  lastName: { required },
  email: { required, email },
  phone: { required, phonePattern, phoneNotRepeating },
  password: { required, strongPassword },
  confirmPassword: { required, sameAsPassword },
  agreed: { required },
});

const $v = useVuelidate(rules, form);
const isFormInvalid = computed(() => $v.value.$invalid);
const passwordValidationError = computed(() => $v.value.password.$invalid && $v.value.password.$dirty);

// Submit logic
const submitForm = () => {
  $v.value.$touch();
  if (!$v.value.$invalid) {
    showPopup.value = true;

    setTimeout(() => {
      showPopup.value = false;
      router.push('/login');
    }, 2000);
  } else {
    console.log('Validation errors:', $v.value);
  }
};
</script>
