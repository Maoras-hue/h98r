'use client';

import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { userAPI } from '@/lib/api/users';

export default function CreditCard() {
  const { data: credits } = useQuery({
    queryKey: ['credits'],
    queryFn: () => userAPI.getCredits(),
    refetchInterval: 30000, // Refetch every 30 seconds
  });

  return (
    <div className="bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg p-6 shadow-lg">
      <h3 className="text-lg font-semibold mb-2">Your Credits</h3>
      <div className="text-3xl font-bold mb-2">{credits?.available_credits.toFixed(1) || '0'}</div>
      <p className="text-sm opacity-90">Available credits this month</p>
      <div className="mt-4 bg-white bg-opacity-20 rounded p-2">
        <p className="text-xs">{credits?.total_credits.toFixed(1) || '0'} total • {credits?.used_credits.toFixed(1) || '0'} used</p>
      </div>
    </div>
  );
}
