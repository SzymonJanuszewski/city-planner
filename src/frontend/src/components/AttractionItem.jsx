import React from 'react';

const AttractionItem = ({ attraction, walkingTime }) => (
  <div className="border-l-4 border-blue-500 pl-4 py-3 hover:bg-blue-50 transition-colors rounded-r-lg">
    <div className="flex items-center gap-2 mb-2">
      <span className="text-xl">📍</span>
      <h4 className="font-semibold text-lg text-gray-800">{attraction.name}</h4>
    </div>
    
    <p className="text-gray-600 text-sm mb-3">{attraction.description}</p>
    
    <div className="flex gap-6 text-sm text-gray-500">
      <span className="flex items-center gap-2 bg-gray-100 px-3 py-1 rounded-full">
        <span>⏰</span>
        {attraction.visit_time} min
      </span>
      
      {walkingTime && (
        <span className="flex items-center gap-2 bg-gray-100 px-3 py-1 rounded-full">
          <span>🚶</span>
          {walkingTime} min to next
        </span>
      )}
    </div>
  </div>
);

export default AttractionItem;