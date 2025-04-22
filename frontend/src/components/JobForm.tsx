import { useForm } from 'react-hook-form';
import { createJob } from '../services/api';

interface FormData {
  epochs: number;
  learning_rate: number;
  caption_method: string;
  data_path: string;
}

export function JobForm() {
  const { register, handleSubmit } = useForm<FormData>();
  const onSubmit = async (data: FormData) => { await createJob(data); alert('Job created'); };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="p-4 space-y-4">
      <input type="number" placeholder="Epochs" {...register('epochs')} className="input" />
      <input type="number" step="0.0001" placeholder="Learning Rate" {...register('learning_rate')} className="input" />
      <select {...register('caption_method')} className="select">
        <option value="basic">Basic</option>
        <option value="advanced">Advanced</option>
        <option value="custom">Custom</option>
      </select>
      <input type="text" placeholder="Data Path" {...register('data_path')} className="input" />
      <button type="submit" className="btn">Start Training</button>
    </form>
  );
  
}