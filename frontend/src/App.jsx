import React from 'react';
import Navbar from './components/Navbar';
import ImageGenerator from './components/ImageGenerator';
import FaceSwap from './components/FaceSwap';
import VideoGenerator from './components/VideoGenerator';
import Upscaler from './components/Upscaler';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="p-4 space-y-6">
        <ImageGenerator />
        <Upscaler />
        <FaceSwap />
        <VideoGenerator />
      </main>
    </div>
  );
}
