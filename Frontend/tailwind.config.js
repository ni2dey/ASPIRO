/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'background': "url('/src/assets/img/background.jpg')",
      },
      colors: {
        darkblue: '#004b87',
        blue: '#0077cc',
        lightblue: '#CDFDFE',
        lightgreen: '#CFFFDA',
        darkgreen: '#1f4e2a',
        green: '#2c6a36',
        purple: '#5A4FCF',
        word: '#0A1F44',
        popup: '#80EF80'
      },
      fontFamily: {
        borel: ['Borel', 'cursive'],
      },
    },
  },
  plugins: [],
}
