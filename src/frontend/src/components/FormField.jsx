import React from 'react';

const FormField = ({ 
  label, 
  type, 
  name, 
  value, 
  onChange, 
  placeholder, 
  required, 
  min, 
  max 
}) => (
  <div>
    <label className="block text-sm font-semibold text-gray-700 mb-2">{label}</label>
    <input
      type={type}
      name={name}
      value={value}
      onChange={onChange}
      className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
      placeholder={placeholder}
      required={required}
      min={min}
      max={max}
    />
  </div>
);

export default FormField;