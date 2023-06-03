import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";

import MainPage from "../page/mainPage";

function App() {
	return (
		<Router>
			<div>
				<Routes>
					<Route path="/" element={<MainPage />} />
				</Routes>
			</div>
		</Router>
	);
}

export default App;
