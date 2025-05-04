import React from 'react';
import AttractionItem from './AttractionItem';
import DaySummary from './DaySummary';

const DayPlan = ({ day }) => (
  <div className="bg-white rounded-xl shadow-lg p-6 space-y-4 hover:shadow-xl transition-shadow">
    <h3 className="text-2xl font-semibold text-gray-800 border-b pb-4">
      Day {day.day_number}
    </h3>
    
    {day.attractions.map((attraction, index) => (
      <AttractionItem 
        key={attraction.place_id} 
        attraction={attraction} 
        walkingTime={index < day.walking_times.length ? day.walking_times[index] : null}
      />
    ))}
    
    <DaySummary day={day} />
  </div>
);

export default DayPlan;