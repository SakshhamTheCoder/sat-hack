import React, { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
// import Slider from "react-slick";
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";
// import img1 from '/image1.jpg';
// import img2 from '/image2.jpg';
// import img3 from '/image3.jpg';
// import img5 from '/image5.jpg';
// import img6 from '/image6.jpg';
import Navbar from '../components/Navbar/';

function Home() {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3500,
    arrows: true,
  };

  const [msg, setMsg] = useState([]);

  // const ws = new WebSocket("ws://127.0.0.1:8000/ws");
  // ws.onopen = () => {
  //   console.log("Connected to the server");
  // };

  // ws.onmessage = (event) => {
  //   setMsg((prev) => [...prev, event.data]);
  // };
  // const images = [img1, img2, img3, img5, img6];

  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-black to-gray-900 text-white">
      <Navbar tranparent />
      <div className="mx-10 mb-10 mt-6 p-2">
        {/* <Slider {...settings} className="relative">
          {images.map((imgUrl, index) => (
            <div key={index} className="p-2">
              <img
                loading='lazy'
                src={imgUrl}
                alt={`Slide ${index + 1}`}
                className="select-none w-full h-[150px] md:h-[400px] object-cover rounded-lg transition-transform duration-500 ease-in-out transform hover:scale-105 hover:shadow-lg"
              />
            </div>
          ))}
        </Slider> */}
      </div>

      <div className="flex flex-col items-center justify-center text-center h-full pb-8 p-2">
        <h1 className="text-3xl md:text-5xl font-bold mb-6">
          Catastrophic Bond <span className="text-indigo-400">Price Prediction</span>
        </h1>
        <p className="text-lg md:text-xl mb-10 max-w-lg mx-auto">
          is a free online tool that allows you to.
        </p>

        <div className="flex flex-col md:flex-row justify-evenly w-full space-y-6 md:space-y-0">
          <div>
            <h2 className="text-2xl font-bold mb-4">ABC</h2>
            <p className="text-lg">
              {/* Click on the upload button and select an image from your device. */}
            </p>
            <p>{
              msg.map((m, index) => (
                <p key={index}>{m}</p>
              ))
            }</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
