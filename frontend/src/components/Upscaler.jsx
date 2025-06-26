import React, { useState } from 'react';
import axios from 'axios';

export default function Upscaler() {
  const [file, setFile] = useState();
  const [url, setUrl] = useState(null);

  const handle = async () => {
    const form = new FormData();
    form.append('file', file);
    const res = await axios.post('http://localhost:8000/api/image/upscale', form);
    setUrl(res.data.url);
  };

  return (
    <div className="card p-4">
      <h2 className="font-semibold">Image Upscaler</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handle}>Upscale</button>
      {url && <img src={url} alt="upscaled" className="mt-2 w-full" />}
    </div>
  );
}
