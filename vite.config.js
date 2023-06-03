import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
	plugins: [react()],
	build: {
		rollupOptions: {
			output: {
				manualChunks: undefined,
			},
		},
	},
	optimizeDeps: {
		include: ["react", "react-dom"],
	},
});
