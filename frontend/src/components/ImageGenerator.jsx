import React, { useState } from 'react';
import axios from 'axios';

export default function ImageGenerator() {
  const [prompt, setPrompt] = useState('');
  const [url, setUrl] = useState(null);

  const handle = async () => {
    const form = new FormData();
    form.append('prompt', prompt);
    const res = await axios.post('http://localhost:8000/api/image/gen', form);
    setUrl(res.data.url);
  };

  return (
    <div className="card p-4">
      <h2 className="font-semibold">Image Generator</h2>
      <input value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Prompt" />
      <button onClick={handle}>Generate</button>
      {url && <img src={url} alt="gen" className="mt-2 w-full" />}
    </div>
  );
}
