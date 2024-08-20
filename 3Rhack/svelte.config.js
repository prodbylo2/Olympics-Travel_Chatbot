import adapter from '@sveltejs/adapter-auto';
import sveltePreprocess from 'svelte-preprocess';

export default {
  kit: {
    adapter: adapter(),
  },
  preprocess: sveltePreprocess(),
};

// // svelte.config.js
// import sveltePreprocess from 'svelte-preprocess';
// import { sveltekit } from '@sveltejs/kit/vite';
// import path from 'path';

// export default {
//   preprocess: sveltePreprocess(),
//   kit: {
//     // Kit configurations
//   },
//   vite: {
//     plugins: [sveltekit()],
//     resolve: {
//       alias: {
//         $components: path.resolve('./src/components'),
//         // Add more aliases if needed
//       }
//     },
//     server: {
//       fs: {
//         allow: ['C:/Users/menon/Desktop/Projects/3R']
//       }
//     }
//   }
// };


