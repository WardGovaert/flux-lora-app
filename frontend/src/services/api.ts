import axios from 'axios';

const api = axios.create({ baseURL: 'http://localhost:8000/jobs' });

export const createJob = (data: any) => api.post('/', data);
export const listJobs = () => api.get('/');