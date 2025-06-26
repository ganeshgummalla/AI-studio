import React, { useState } from 'react';
import axios from 'axios';

export default function VideoGenerator() {
  const [prompt, setPrompt] = useState('');
  const [length, setLength] = useState(5);
  const [url, setUrl] = useState(null);

  const handle = async () => {
    const form = new FormData();
    form.append('prompt', prompt);
    form.append('length', length);
    const res = await axios.post('http://localhost:8000/api/video/gen', form);
    setUrl(res.data.url);
  };

  return (
    <div className="card p-4">
      <h2 className="font-semibold">Video Generator</h2>
      <input value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Prompt" />
      <input type="number" value={length} onChange={e => setLength(+e.target.value)} />
      <button onClick={handle}>Generate</button>
      {url && <video src={url} controls className="mt-2 w-full" />}
    </div>
  );
}
