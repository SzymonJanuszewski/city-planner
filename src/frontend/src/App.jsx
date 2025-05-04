import React, { useState } from 'react';
import Header from './components/Header';
import TripPlannerForm from './components/TripPlannerForm';
import ErrorMessage from './components/ErrorMessage';
import TripPlanResults from './components/TripPlanResults';

const App = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [tripPlan, setTripPlan] = useState(null);
  
  const [formData, setFormData] = useState({
    city: '',
    days: 3,
    activity_level: 'medium',
    max_walking_time: 30,
    early_start: false
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/plan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch trip plan');
      }

      const data = await response.json();
      setTripPlan(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto p-6">
        <Header />
        
        <TripPlannerForm
          formData={formData}
          handleInputChange={handleInputChange}
          handleSubmit={handleSubmit}
          loading={loading}
        />
        
        {error && <ErrorMessage message={error} />}
        
        {tripPlan && <TripPlanResults tripPlan={tripPlan} />}
      </div>
    </div>
  );
};

export default App;