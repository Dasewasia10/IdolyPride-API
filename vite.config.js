import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
	plugins: [react()],
	build: {
		assetsDir: "src/assets",
		rollupOptions: {
			output: {
				assetFileNames: "assets/[name].[ext]",
			},
		},
	},
});
