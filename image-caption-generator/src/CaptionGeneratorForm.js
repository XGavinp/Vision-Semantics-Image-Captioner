import React, { useState } from 'react';

function CaptionGeneratorForm() {
  const [imageUrl, setImageUrl] = useState('');

  const handleInputChange = (event) => {
    setImageUrl(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Submitted:', imageUrl);
    // Implement your logic to generate caption here
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="image-upload">Upload Image File:</label>
      <input type="file" id="image-upload" accept="image/jpeg, image/png" />
      <br />
      <label htmlFor="url-upload">Or Enter Image URL:</label>
      <input
        type="url"
        id="url-upload"
        value={imageUrl}
        onChange={handleInputChange}
        placeholder="Enter image URL"
      />
      <br />
      <button type="submit">Generate Caption</button>
    </form>
  );
}

export default CaptionGeneratorForm;
