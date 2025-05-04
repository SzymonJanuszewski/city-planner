import React from 'react';
import FormField from './FormField';

const TripPlannerForm = ({ formData, handleInputChange, handleSubmit, loading }) => (
  <div className="bg-white rounded-xl shadow-lg p-8 mb-8 max-w-xl mx-auto">
    <form onSubmit={handleSubmit} className="space-y-6">
      <FormField 
        label="City"
        type="text"
        name="city"
        value={formData.city}
        onChange={handleInputChange}
        placeholder="Enter city name (e.g. Rome)"
        required
      />

      <FormField 
        label="Number of Days"
        type="number"
        name="days"
        min="1"
        max="7"
        value={formData.days}
        onChange={handleInputChange}
        required
      />

      <div>
        <label className="block text-sm font-semibold text-gray-700 mb-2">Activity Level</label>
        <select
          name="activity_level"
          value={formData.activity_level}
          onChange={handleInputChange}
          className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
        >
          <option value="easy">Easy (3-4 attractions/day) ⭐</option>
          <option value="medium">Medium (4-6 attractions/day) ⭐⭐</option>
          <option value="demanding">Demanding (6-7 attractions/day) ⭐⭐⭐</option>
        </select>
      </div>

      <FormField 
        label="Max Walking Time (minutes)"
        type="number"
        name="max_walking_time"
        value={formData.max_walking_time}
        onChange={handleInputChange}
      />

      <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
        <input
          type="checkbox"
          name="early_start"
          checked={formData.early_start}
          onChange={handleInputChange}
          className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
        />
        <label className="text-sm font-semibold text-gray-700">Early Start 🌅</label>
      </div>

      <button
        type="submit"
        disabled={loading}
        className="w-full bg-blue-600 text-white p-4 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-blue-300 transform transition-transform hover:scale-[1.02] active:scale-[0.98]"
      >
        {loading ? '🔄 Planning...' : '🗺️ Plan My Trip'}
      </button>
    </form>
  </div>
);

export default TripPlannerForm;