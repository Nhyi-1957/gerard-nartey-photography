
# Clone the empty repo from GitHub
git clone https://github.com/YOUR_USERNAME/gerard-nartey-photography.git
cd gerard-nartey-photography
npm create vite@latest
# Name: gerard-nartey-photography
# Framework: React
# Variant: JavaScript or TypeScript

cd gerard-nartey-photography
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"]