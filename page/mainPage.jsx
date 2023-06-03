import React from "react";
import { useLocation } from "react-router-dom";

const MainPage = () => {
	const location = useLocation();

	const customBackgroundStyle = {
		backgroundImage: `url(${location.pathname}/assets/bg.png')`,
		backgroundSize: "cover",
		backgroundPosition: "center",
		backgroundRepeat: "no-repeat",
		height: "100vh",
	};

	return (
		<>
			<div style={customBackgroundStyle} className="bg-gray-100 h-screen">
				<div className="flex absolute h-8 md:h-12 lg:h-16 w-auto top-6 left-10 flex-row gap-10 items-center z-50">
					<img
						className="h-4 md:h-8 lg:h-12 w-auto"
						src={`${location.pathname}/assets/pojok.png`}
						alt="idoly-pride-blue-logo"
					/>
					<img
						className="h-8 md:h-12 lg:h-16 w-auto"
						src={`${location.pathname}/assets/dase.png`}
						alt="dasesplace-logo"
					/>
				</div>
				<div className="relative z-20">
					<img
						className="opacity-0 lg:opacity-100 lg:h-screen w-auto absolute top-0 left-0 ml-4"
						src={`${location.pathname}/assets/1.png`}
						alt="Hayasaka-Mei-1"
					/>
					<img
						className="opacity-0 lg:opacity-100 lg:h-screen w-auto absolute top-0 right-0 mr-4"
						src={`${location.pathname}/assets/2.png`}
						alt="Hayasaka-Mei-6"
					/>
				</div>

				<div className="flex flex-col h-screen justify-center items-center p-4 mx-auto">
					<div className="text-center">
						<img
							src={`${location.pathname}/assets/middle.png`}
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
						Copyright by QualiArts. Created by Dasewasia @2023
					</div>
				</div>
			</div>
		</>
	);
};

export default MainPage;
