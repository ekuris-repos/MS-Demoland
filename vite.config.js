import { defineConfig } from 'vite';

// With the flat layout (site assets at repo root alongside Developer/ and
// Non-Developer/), Vite serves everything directly — no custom plugins needed.
// Course statuses come from the static api/course-statuses.json file.

export default defineConfig({
  // Nothing extra required — Vite serves the repo root as-is.
});
