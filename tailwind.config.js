/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Honk"', "cursive"],
        links: ['"Alumni Sans Pinstripe"', "sans-serif"],
      },
    },
  },
  plugins: [],
};
