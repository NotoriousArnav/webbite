/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}"],
    theme: {
    extend: {
      colors: {
        primary: '#080705',   // Replace with your primary color
        secondary: '#40434e', // Replace with your secondary color
        accent: '#faa613',    // Replace with your accent color
        background: '#9dbebb', // Replace with your background color
        highlight: '#f44708', // Replace with your highlight color
      },
    },
  },
  plugins: [],
}

