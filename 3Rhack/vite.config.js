import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	build: {
		outDir: 'dist', // Ensure this matches your Dockerfile COPY command
	  }
});


// // vite.config.js
// import { defineConfig } from 'vite';
// import { svelte } from '@sveltejs/vite-plugin-svelte';

// export default defineConfig({
//   plugins: [svelte()],
//   server: {
//     fs: {
//       allow: [
//         'C:/Users/menon/Desktop/Projects/3R'
//       ]
//     }
//   }
// });

// // vite.config.js
// import { defineConfig } from 'vite';
// import svelte from '@sveltejs/vite-plugin-svelte';

// export default defineConfig({
//   plugins: [svelte()],
//   server: {
//     proxy: {
//       '/chat': 'http://localhost:5000'  // Proxy API requests to Flask backend
//     }
//   }
// });







