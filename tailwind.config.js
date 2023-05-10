/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './**/*.{html.j2, html, js}'],
  theme: {
    extend: {
      colors:{
        'lp-1': "#F6F6F6",
        'lp-2': "#D6E4F0",
        'lp-3': "#1E56A0",
        'lp-4': "#163172"
      },
      backgroundSize:{
        '25%':'25%'
      },
      fontFamily:{
        sans: ['Montserrat', 'sans-serif']
      },
      backgroundImage:{
        'gradient-radial':'radial-gradient(var(--gradient-color-stops))'
      },
      minWidth:{
        '3/4':'75%',
        '1/2':'50%',
        '2/5':'40%',
        '30%':'30%',
        '1/4':'25%'
      },
      screens:{
        'xs': {'max':'639px'},
        'xm': {'max':'768px'},
        'xg': {'max':'1024px'},
      },

      keyframes: {
        'waveright' : {
          '0%, 100%' : {'transform': 'translateX(-100%) scaleX(300%)'},
          '50%' : {'transform': 'translate(100%) scaleX(300%)'}
        },
        'waveleft' : {
          '0%, 100%' : {'transform': 'translateX(100%) scaleX(300%)'},
          '50%' : {'transform': 'translateX(-100%) scaleX(300%)'}
        },
      },

      animation:{
        'wave1': 'waveleft 44s ease-in infinite',
        'wave2': 'waveright 57s ease-in infinite',
        'wave3': 'waveleft 83s ease-in infinite',
        'wave4': 'waveright 129s ease-in infinite'
      }
    },
  },
  plugins: [
  ],
}
