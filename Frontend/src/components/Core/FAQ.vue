<template>
    <div class="max-w-5xl mx-auto py-16 px-6 lg:px-16 flex flex-col lg:flex-row items-center gap-12">
      <!-- Left Side: Heading + Image -->
      <div class="lg:w-1/2 text-center lg:text-left">
        <h2 class="text-4xl font-extrabold text-word">Frequently Asked Questions</h2>
        <img src="/src/assets/img/questions.png" alt="Course Illustration" class="mt-6 mx-auto lg:mx-0 w-3/4 lg:w-full" />
      </div>
  
      <!-- Right Side: FAQ Boxes -->
      <div class="lg:w-1/2 space-y-4">
        <div
          v-for="(faq, index) in faqs"
          :key="index"
          class="cursor-pointer rounded-xl shadow-md p-5 transition-all duration-300 overflow-hidden"
          :class="[
            activeIndex === index ? 'bg-white shadow-lg' : index % 2 === 0 ? 'bg-lightblue' : 'bg-lightgreen'
          ]"
          @click="toggleFAQ(index)"
        >
          <!-- Question -->
          <div class="flex justify-between items-center">
            <div>
              <p class="text-lg font-semibold text-gray-700">{{ faq.module }}</p>
              <h3 class="font-semibold text-sm">{{ faq.question }}</h3>
            </div>
            <span class="text-2xl transition-transform duration-300" :class="{ 'rotate-45': activeIndex === index }">+</span>
          </div>
  
          <!-- Answer -->
          <transition name="expand">
            <p v-if="activeIndex === index" class="mt-3 text-gray-800 text-sm">
              {{ faq.answer }}
            </p>
          </transition>
        </div>
      </div>
    </div>
</template>
  
<script setup>
  import { ref } from "vue";
  
  // FAQ Data
  const faqs = ref([
  {
    module: "CAREER PATHS",
    question: "What are the best career options after B.Tech in CSE?",
    answer: "You can pursue software development, data science, cybersecurity, cloud computing, artificial intelligence, or even start your own tech business."
  },
  {
    module: "HIGHER EDUCATION",
    question: "Should I go for higher studies like M.Tech, MBA, or MS?",
    answer: "If you want to specialize in a technical field, M.Tech or MS is a good choice. If you're interested in management roles, an MBA can be beneficial."
  },
  {
    module: "PLACEMENTS & JOB SEARCH",
    question: "How can I prepare for job interviews and placements?",
    answer: "Focus on data structures & algorithms, competitive programming, system design, and soft skills. Platforms like LeetCode, CodeChef, and GeeksforGeeks can help."
  },
  {
    module: "CERTIFICATIONS & SKILLS",
    question: "Which certifications can boost my career?",
    answer: "Certifications in AWS, Google Cloud, Data Science, Ethical Hacking, or Full-Stack Development can make you stand out in job applications."
  }
]);

  
  // Track Active Index
  const activeIndex = ref(null);
  
  // Toggle FAQ
  const toggleFAQ = (index) => {
    activeIndex.value = activeIndex.value === index ? null : index;
  };
</script>
  
<style scoped>
  /* Expand transition */
  .expand-enter-active, .expand-leave-active {
    transition: max-height 0.3s ease-out, opacity 0.3s ease;
  }
  .expand-enter-from, .expand-leave-to {
    max-height: 0;
    opacity: 0;
  }
  .expand-enter-to, .expand-leave-from {
    max-height: 200px;
    opacity: 1;
  }
</style>
  