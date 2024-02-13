import React from 'react';
import CaptionGeneratorForm from './CaptionGeneratorForm';
import ImageDisplay from './ImageDisplay';
import './App.css'; // Make sure to import your CSS file

function App() {
  return (
    <div className="container">
      <h1>Image Caption Generator</h1>
      <CaptionGeneratorForm />
      <ImageDisplay />
    </div>
  );
}

export default App;
