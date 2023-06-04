import React, { useState, useEffect } from "react";

const MainPage = () => {
	const [isDarkMode, setIsDarkMode] = useState(
		localStorage.getItem("isDarkMode") === "true"
	);

	const customBackgroundStyle = {
		backgroundImage: "url('/assets/bg.png')",
		backgroundSize: "cover",
		backgroundPosition: "center",
		backgroundRepeat: "no-repeat",
		height: "100vh",
	};

	useEffect(() => {
		if (isDarkMode) {
			document.documentElement.classList.add("dark");
		} else {
			document.documentElement.classList.remove("dark");
		}
		localStorage.setItem("isDarkMode", isDarkMode);
	}, [isDarkMode]);

	const toggleDarkMode = () => {
		setIsDarkMode(!isDarkMode);
	};
	return (
		<>
			<div
				style={customBackgroundStyle}
				className={`bg-gray-100 ${
					isDarkMode ? "dark:bg-gray-900" : ""
				} h-screen`}>
				<div className="flex absolute h-8 md:h-12 lg:h-16 w-auto top-6 left-10 flex-row gap-10 items-center z-50">
					<img
						className="h-4 md:h-8 lg:h-12 w-auto"
						src={`/assets/pojok.png`}
						alt="idoly-pride-blue-logo"
					/>
					<img
						className="h-8 md:h-12 lg:h-16 w-auto"
						src={`/assets/dase.png`}
						alt="dasesplace-logo"
					/>
				</div>
				<div className="relative z-20">
					<img
						className="opacity-0 lg:opacity-100 h-full lg:h-screen w-auto absolute top-0 left-0 ml-4"
						src={`/assets/1.png`}
						alt="Hayasaka-Mei-1"
					/>
					<img
						className="opacity-0 lg:opacity-100 h-full lg:h-screen w-auto absolute top-0 right-0 mr-4"
						src={`/assets/2.png`}
						alt="Hayasaka-Mei-6"
					/>
				</div>

				<div className="flex flex-col h-screen justify-center items-center p-4 mx-auto">
					<div className="text-center">
						<img
							src={`/assets/middle.png`}
							alt="Gambar"
							className="mx-auto w-24 md:w-32 lg:w-64 h-auto mb-4"
						/>
						<h1 className="text-2xl font-bold mb-2">IdolyP API</h1>
						<p className="text-gray-900 bg-blue-300 mb-4 bg-opacity-40 rounded-2xl p-4">
							This is a repository to see list of api that I use for IdolyP
							website!
						</p>
					</div>

					<div className="flex flex-col mt-8 text-center">
						<h2 className="text-xl font-bold mb-4 bg-blue-300 bg-opacity-20 rounded-2xl">
							<u>Available API:</u>
						</h2>
						<div className="flex flex-row font-bold text-lg lg:text-2xl gap-4">
							<div className="text-white hover:text-blue-900 bg-blue-700 hover:bg-blue-200 border hover:border-2 hover:border-black p-2 rounded-lg">
								<a
									href="https://idoly-pride-api.vercel.app/api/card"
									target="_blank">
									Card
								</a>
							</div>
							<div className="text-white hover:text-blue-900 bg-blue-700 hover:bg-blue-200 border hover:border-2 hover:border-black p-2 rounded-lg">
								<a
									href="https://idoly-pride-api.vercel.app/api/idol"
									target="_blank">
									Idol
								</a>
							</div>
						</div>
					</div>
					<div className="flex absolute text-sm bottom-8">
						&copy; Copyright by QualiArts. Created by Dasewasia @2023
					</div>
				</div>
			</div>

			<button
				className={`absolute z-[100] bottom-auto top-4 right-4 lg:top-auto lg:bottom-8 lg:right-8 p-2 rounded-full shadow-md ${
					isDarkMode ? "bg-gray-200" : "bg-gray-800"
				} transition-colors duration-300`}
				onClick={toggleDarkMode}
				title="Dark mode toggle">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					strokeWidth="2"
					strokeLinecap="round"
					strokeLinejoin="round"
					className={`w-6 h-6 ${
						isDarkMode ? "text-gray-800" : "text-gray-200"
					} transition-colors duration-300`}>
					{isDarkMode ? (
						<path d="M21 12.79A9 9 0 0 1 12.07 21a9 9 0 0 1-9-9.94 8.998 8.998 0 0 1 4.1-7.54A4.996 4.996 0 0 0 11 5a5 5 0 0 0 0-10 1 1 0 0 1 0-2 7 7 0 1 1 6.33 10.29" />
					) : (
						<path d="M12 22s-6.5-2-6.5-10a6.5 6.5 0 1 1 13 0c0 8-6.5 10-6.5 10zM12 11V2" />
					)}
				</svg>
			</button>
		</>
	);
};

export default MainPage;
