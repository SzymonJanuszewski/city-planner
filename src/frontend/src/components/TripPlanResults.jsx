import React from 'react';
import DayPlan from './DayPlan';

const TripPlanResults = ({ tripPlan }) => (
  <div className="space-y-8 max-w-4xl mx-auto">
    <h2 className="text-3xl font-bold text-center text-gray-800">
      Your Trip to {tripPlan.city} 🌆
    </h2>
    
    {tripPlan.days.map((day) => (
      <DayPlan key={day.day_number} day={day} />
    ))}
  </div>
);

export default TripPlanResults;