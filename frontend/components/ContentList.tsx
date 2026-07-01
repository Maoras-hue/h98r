'use client';

import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { contentAPI } from '@/lib/api/content';
import Link from 'next/link';
import { formatDistanceToNow } from 'date-fns';

export default function ContentList() {
  const { data: contents, isLoading } = useQuery({
    queryKey: ['contents'],
    queryFn: () => contentAPI.getContents(),
  });

  if (isLoading) {
    return <div className="text-center py-8">Loading contents...</div>;
  }

  if (!contents || contents.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6 text-center">
        <p className="text-gray-500">No content generated yet. Create your first one!</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-bold mb-6">Your Contents</h2>
      {contents.map((content) => (
        <Link href={`/dashboard/content/${content.id}`} key={content.id}>
          <div className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow cursor-pointer">
            <div className="flex justify-between items-start">
              <div className="flex-1">
                <h3 className="font-semibold text-lg">{content.title}</h3>
                <p className="text-gray-500 text-sm mt-1">
                  {content.content.substring(0, 100)}...
                </p>
                <div className="flex gap-2 mt-2 flex-wrap">
                  <span className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded">
                    {content.content_type}
                  </span>
                  <span className="px-2 py-1 bg-purple-100 text-purple-700 text-xs rounded">
                    {content.tone}
                  </span>
                  <span className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded">
                    SEO: {content.seo_score}
                  </span>
                </div>
              </div>
              <p className="text-xs text-gray-400">
                {formatDistanceToNow(new Date(content.created_at), { addSuffix: true })}
              </p>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
