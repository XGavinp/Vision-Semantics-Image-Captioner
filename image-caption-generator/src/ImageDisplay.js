import React from 'react';

function ImageDisplay() {
  return (
    <div id="image-container" style={{ display: 'none' }}>
      <h2>Uploaded Image</h2>
      <img id="uploaded-image" src="" alt="Uploaded Image" />
      <div id="caption"></div>
    </div>
  );
}

export default ImageDisplay;
