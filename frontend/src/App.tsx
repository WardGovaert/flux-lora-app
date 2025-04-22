import { JobForm } from './components/JobForm';
import { JobList } from './components/JobList';

export default function App() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-xl font-bold mb-4">Flux LoRA Trainer</h1>
      <JobForm />
      <JobList />
    </div>
  );
}