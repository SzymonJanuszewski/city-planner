import React from 'react';

const DaySummary = ({ day }) => (
  <div className="mt-6 pt-4 border-t border-gray-200">
    <div className="flex flex-wrap gap-4 text-sm text-gray-600 mb-3">
      <span className="bg-blue-50 px-4 py-2 rounded-full">
        ⏱️ Total time: {Math.round(day.total_time / 60)} hours
      </span>
      <span className="bg-blue-50 px-4 py-2 rounded-full">
        🏃 Walking distance: {day.total_distance.toFixed(1)} km
      </span>
    </div>
    <a
      href={day.google_maps_link}
      target="_blank"
      rel="noopener noreferrer"
      className="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium text-sm hover:underline"
    >
      🗺️ View route on Google Maps
    </a>
  </div>
);

export default DaySummary;