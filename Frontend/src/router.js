import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import FormPage from './views/FormPage.vue';
import NextPage from './views/NextPage.vue';
import Results from './views/Results.vue';
import LoginPage from './views/LoginPage.vue';
import SignupPage from './views/SignupPage.vue';
import AddskillPage from './views/AddskillPage.vue';
import RecommendPage from './views/RecommendPage.vue';
import { useUserStore } from '/src/store.js';

const routes = [
  { path: '/', name: 'HomePage', component: HomePage },
  { path: '/form', name: 'FormPage', component: FormPage, meta: { requiresAuth: true } },
  { path: '/next', name: 'NextPage', component: NextPage, meta: { requiresAuth: true } },
  { path: '/results', name: 'Results', component: Results, meta: { requiresAuth: true } },
  { path: '/addskill', name: 'AddskillPage', component: AddskillPage, meta: { requiresAuth: true } },
  { path: '/recommend', name: 'RecommendPage', component: RecommendPage, meta: { requiresAuth: true } },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/signup', name: 'SignupPage', component: SignupPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Navigation Guard
router.beforeEach((to, from, next) => {
  const userStore = useUserStore(); // use store here
  if (to.meta.requiresAuth && !userStore.isLoggedIn) {
    // Show popup via event
    window.dispatchEvent(new CustomEvent('show-login-popup'));
    next('/login');
  } else {
    next();
  }
});

export default router;
