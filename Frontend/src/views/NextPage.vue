<template>
  <div class="relative min-h-screen flex flex-col">
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <div class="relative z-10 flex flex-col flex-grow">
      <NavBar />

      <!-- Loader -->
      <div v-if="loading" class="min-h-screen flex items-center justify-center p-6">
        <div class="loader"></div>
      </div>

      <!-- Main Form -->
      <div v-else class="min-h-screen flex flex-col items-center justify-center p-6 mt-16">
        <div class="w-full max-w-3xl flex flex-col items-center text-center space-y-6">
          <h1 class="text-4xl font-bold text-gray-900">🚀 Let's Discover Your Career Path!</h1>
          <p class="text-gray-600 text-lg">Answer all the questions to get customized guidance designed specifically for you.</p>

          <form @submit.prevent="submitForm" class="w-full flex flex-col items-center space-y-6">
            <div
              v-for="(question, index) in questions"
              :key="index"
              class="w-full p-6 md:p-8 rounded-xl border shadow-sm"
              :class="[
                errors[index] ? 'border-red-500 bg-red-50' : index % 2 === 0 ? 'bg-lightblue' : 'bg-lightgreen'
              ]"
            >
              <label class="block text-gray-800 font-semibold mb-4 text-lg text-left">{{ question.text }}</label>

              <div
                v-for="(option, i) in question.options"
                :key="i"
                class="flex items-start space-x-3 mb-2 text-left"
              >
                <input
                  type="radio"
                  :name="'question' + index"
                  :value="option.type"
                  v-model="responses[index]"
                  class="w-5 h-5 text-blue focus:ring-blue"
                />
                <label class="text-gray-700">{{ option.text }}</label>
              </div>

              <p v-if="errors[index]" class="text-red-500 text-sm text-center mt-2">This field is required.</p>
            </div>

            <button
              type="submit"
              class="w-full bg-darkblue text-white font-bold py-3 px-6 rounded-lg transition-all hover:bg-blue-800"
            >
              Submit
            </button>
          </form>
        </div>
      </div>

      <Footer class="mt-auto w-full relative z-20" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import NavBar from '../components/Core/NavBar.vue';
import Footer from '../components/Core/Footer.vue';

const router = useRouter();
const loading = ref(true);
onMounted(() => {
  setTimeout(() => {
    loading.value = false;
  }, 2000); // 2-second loader
});

const questions = ref([
  {
    text: "What is your preferred career goal?",
    options: [
      {text: "I want to work in the IT industry and grow my skills in a practical setting.", type: 'A'},
      {text:"I want to specialize in a particular area of technology or business and have advanced knowledge.", type: 'B'},
      {text:"I am unsure and need guidance based on future opportunities.", type: 'C'}
    ]
  },
  {
    text: "How confident are you in your technical skills (programming, software development, etc.)?",
    options: [
      {text: "Very confident, I feel ready to join the workforce.", type: 'A'},
      {text: "Somewhat confident, but I need more expertise in certain areas.", type: 'B'},
      {text: "Not confident, I feel I need more technical knowledge or practice.", type: 'C'}
    ]
  },
  {
    text: "How important is financial stability to you right now?",
    options: [
      {text: "Very important, I want to start earning as soon as possible.", type: 'A'},
      {text: "Somewhat important, but I'm open to studying more if it improves future opportunities.", type: 'B'},
      {text: "Not important, I’m more focused on learning and personal growth at the moment.", type: 'C'}
    ]
  },
  {
    text: "What is your opinion on leadership roles and managerial responsibilities?",
    options: [
      {text: "I enjoy technical roles and would prefer focusing on hands-on work.", type: 'A'},
      {text: "I’m interested in leadership and managerial roles, and I believe an MBA would help.", type:'B'},
      {text: "I’m not sure, I would like to explore more options before deciding.", type: 'C'}
    ]
  },
  {
    text: "What is your opinion on leadership roles and managerial responsibilities?",
    options: [
      {text: "I enjoy technical roles and would prefer focusing on hands-on work.", type: 'A'},
      {text: "I’m interested in leadership and managerial roles, and I believe an MBA would help.", type:'B'},
      {text: "I’m not sure, I would like to explore more options before deciding.", type:'C'}
    ]
  },
  {
    text: " I would like to explore more options before deciding. How do you feel about continuing studies after your B.Tech?",
    options: [
      {text: "I’m excited to learn more and specialize in a specific field.", type: 'A'},
      {text: "I feel neutral and think I might need some time before deciding.", type:'B'},
      {text: "I’m not interested in further studies and prefer entering the workforce immediately.", type:'C'}
    ]
  },
  {
    text: "What kind of work environment do you prefer?",
    options: [
      {text: "A practical, hands-on environment where I can apply my skills immediately.", type: 'A'},
      {text: "A structured, intellectual environment where I can focus on research and deeper learning.", type:'B'},
      {text: "I’m unsure, I want to explore both options.", type:'C'}
    ]
  },
  {
    text: "What is your primary motivation for your career?",
    options: [
      {text: "I want to start my career as soon as possible and start earning.", type: 'A'},
      {text: "I want to pursue higher education to broaden my knowledge and advance in my career later.", type:'B'},
      {text: "I’m still figuring out my motivation and need more time to explore my options.", type:'C'}
    ]
  },
  {
    text: "How do you handle pressure and long-term projects?",
    options: [
      {text: "I prefer quick results and hands-on work with short-term goals.", type: 'A'},
      {text: "I thrive under pressure and enjoy long-term, complex projects that involve deep learning.", type:'B'},
      {text: "I’m not sure, I want to see how I handle such situations in the future.", type:'C'}
    ]
  },
  {
    text: "Do you have a clear idea of what specialization or field you want to work in?",
    options: [
      {text: "Yes, I have a clear idea and I’m ready to pursue that in the job market.", type: 'A'},
      {text: "I’m interested in a particular field but think I need advanced studies for deeper understanding.", type:'B'},
      {text: "No, I’m still figuring it out and need more time or guidance.", type:'C'}
    ]
  },
  {
    text: "What are your thoughts on the current job market in the IT sector?",
    options: [
     {text: "I’m confident that I can easily find a job and start working right away.", type: 'A'},
     {text: "I believe further studies will help me stand out and secure a better position.", type:'B'},
     {text: "I’m unsure about the job market and need to explore the best options.", type:'C'}
    ]
  },
  {
    text: "How do you view networking and professional connections?",
    options: [
      {text: "I’m ready to start building my professional network in the industry.", type: 'A'},
      {text: "I believe that further studies (like an MBA or M.Tech) will help me build valuable connections.", type:'B'},
      {text: "I’m unsure, but I recognize networking as an important aspect of my future career.", type:'C'}
    ]
  },
  {
    text: "How do you feel about continuing education if it requires a significant time investment?",
    options: [
      {text: "I am ready to start working immediately and do not want to spend more time studying.", type: 'A'},
      {text: "I’m willing to invest a few more years in education for long-term benefits.", type:'B'},
      {text: "I need to think more about this before making a decision.", type:'C'}
    ]
  },
  {
    text: "What is your preference in terms of work-life balance?",
    options: [
      {text: "I prefer a more relaxed work-life balance and immediate employment in the IT sector.", type: 'A'},
      {text: "I am okay with the intensity of higher studies and long hours for the benefits later in life.", type:'B'},
      {text: "I’m unsure, I want to understand the potential work-life balance in both scenarios.", type:'C'}
    ]
  },
  {
    text: "What role does personal development and career growth play in your decision?",
    options: [
      {text: "I want to start working and growing in the industry as quickly as possible.", type: 'A'},
      {text: "I’m willing to invest time in education for future career advancement and personal growth.", type:'B'},
      {text: "I’m uncertain about the balance between growth through work and higher education.", type:'C'}
    ]
  },
  {
    text: "Are you willing to move to another city or country for higher studies or a job?",
    options: [
      {text: "Yes, I am open to relocating for a job.", type: 'A'},
      {text: "Yes, I am open to studying abroad or moving to a new city for higher education.", type:'B'},
      {text: "I prefer staying local, but I’m open to suggestions.", type:'C'}
    ]
  },
  {
    text: "Do you prefer theoretical knowledge or practical, hands-on learning?",
    options: [
      {text: "I prefer practical learning with immediate application.", type: 'A'},
      {text: "I value theoretical knowledge and believe it will benefit my career in the long run.", type:'B'},
      {text: "I am unsure, but I want to explore both types of learning.", type:'C'}
    ]
  },
  {
    text: "Are you interested in global career opportunities and expanding your career internationally?",
    options: [
      {text: "Yes, I believe a job in the IT industry will open up global opportunities.", type: 'A'},
      {text: "Yes, I believe higher studies will provide me with a broader perspective for international roles.", type:'B'},
      {text: "I’m not sure, I need more information about international options in both cases.", type:'C'}
    ]
  },
  {
    text: "How do you feel about your current academic performance and knowledge in your field?",
    options: [
      {text: "I feel confident about my current academic knowledge and am ready for the job market.", type: 'A'},
      {text: "I believe I need more in-depth learning before I can confidently join the workforce.", type:'B'},
      {text: "I’m unsure, and I might need further guidance on whether to study or work.", type:'C'}
    ]
  },
  {
    text: "What kind of job do you see yourself in 5-10 years from now?",
    options: [
      {text: "I see myself in a technical role, solving real-world problems and growing in my field.", type: 'A'},
      {text:  "I see myself in a managerial or leadership role, possibly after gaining more knowledge from higher studies.", type:'B'},
      {text: "I’m not sure yet, I need to explore my options and see what fits my career aspirations.", type:'C'}
    ]
  },
  {
    text: "Would you prefer working with cutting-edge technology or exploring research and development?",
    options: [
      {text: "I prefer working with cutting-edge technology in a fast-paced industry environment.", type: 'A'},
      {text: "I prefer focusing on research, development, and innovation, which I believe would be enhanced by higher studies.", type:'B'},
      {text: "I’m not sure, I want to explore both options before deciding.", type:'C'}
    ]
  },
]);

const responses = ref(Array(questions.value.length).fill(null));
const errors = ref(Array(questions.value.length).fill(false));

const validateForm = () => {
  let isValid = true;
  errors.value = responses.value.map(response => {
    if (!response) {
      isValid = false;
      return true;
    }
    return false;
  });
  return isValid;
};

const submitForm = () => {
  if (validateForm()) {
    router.push({
      name: 'Results',
      query: { responses: JSON.stringify(responses.value) },
    });
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
