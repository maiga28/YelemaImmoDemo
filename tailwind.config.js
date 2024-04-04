module.exports = {
    content: [
        './templates/**/**/*.html',
        './node_modules/flowbite/**/*.js',
        'node_modules/preline/dist/*.js',
        'node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}',

    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')({
            charts: true,
            forms: true,
            tooltips: true
        }),
        require("@tailwindcss/forms")({
            strategy: 'base', // only generate global styles
            strategy: 'class', // only generate classes
        }),
        require('preline/plugin'),
    ],

    modules: {
        grid: true,
    },

}