import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";

import MainPage from "../page/mainPage";

function App() {
	return (
		<Router>
			<div>
				<Route path="/" component={MainPage} />
			</div>
		</Router>
	);
}

export default App;
