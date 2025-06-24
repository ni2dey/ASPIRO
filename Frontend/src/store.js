import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
    state: () => ({
        isLoggedIn: false,
    }),
    actions: {
        login() {
            this.isLoggedIn = true;
            localStorage.setItem('isLoggedIn', 'true');
        },
        logout() {
            this.isLoggedIn = false;
            localStorage.removeItem('isLoggedIn');
        },
        initialize() {
            // ✅ Called on app load
            const saved = localStorage.getItem('isLoggedIn');
            this.isLoggedIn = saved === 'true';
        },
    },
});
