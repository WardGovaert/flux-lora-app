import { useEffect, useState } from 'react';
import { listJobs } from '../services/api';

export function JobList() {
  const [jobs, setJobs] = useState([] as any[]);
  useEffect(() => { listJobs().then(res => setJobs(res.data)); }, []);
  return (
    <ul className="p-4">
      {jobs.map(j => (
        <li key={j.id}>{j.id} - {j.status}</li>
      ))}
    </ul>
  );
}