import { defineConfig } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

// Auto-discover course HTML files in courses/
function getCourseEntries() {
  const coursesDir = resolve(__dirname, 'courses');
  const entries = {
    main: resolve(__dirname, 'index.html'),
  };
  if (fs.existsSync(coursesDir)) {
    for (const file of fs.readdirSync(coursesDir)) {
      if (file.endsWith('.html')) {
        const name = file.replace('.html', '');
        entries[`courses/${name}`] = resolve(coursesDir, file);
      }
    }
  }
  return entries;
}

export default defineConfig({
  build: {
    rollupOptions: {
      input: getCourseEntries(),
    },
  },
});
