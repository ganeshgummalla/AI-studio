import React, { useState } from 'react';
import axios from 'axios';

export default function FaceSwap() {
  const [file, setFile] = useState();
  const [refId, setRefId] = useState('character1');
  const [url, setUrl] = useState(null);

  const handle = async () => {
    const form = new FormData();
    form.append('file', file);
    form.append('ref_id', refId);
    const res = await axios.post('http://localhost:8000/api/face/swap', form);
    setUrl(res.data.url);
  };

  return (
    <div className="card p-4">
      <h2 className="font-semibold">Face Swap</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <input value={refId} onChange={e => setRefId(e.target.value)} placeholder="AI Character ID" />
      <button onClick={handle}>Swap</button>
      {url && <img src={url} alt="swap" className="mt-2 w-full" />}
    </div>
  );
}
