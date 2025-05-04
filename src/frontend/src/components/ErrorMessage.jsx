import React from 'react';

const ErrorMessage = ({ message }) => (
  <div className="mb-8 p-4 bg-red-50 border-l-4 border-red-500 text-red-700 rounded-lg shadow-sm mx-auto max-w-xl">
    <div className="flex items-center">
      <span className="text-xl mr-2">⚠️</span>
      <p className="font-medium">{message}</p>
    </div>
  </div>
);

export default ErrorMessage;