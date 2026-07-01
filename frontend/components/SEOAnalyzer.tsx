'use client';

import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { seoAPI } from '@/lib/api/seo';
import toast from 'react-hot-toast';

export default function SEOAnalyzer() {
  const [content, setContent] = useState('');
  const [seoAnalysis, setSeoAnalysis] = useState<any>(null);

  const { mutate: analyzeSEO, isPending } = useMutation({
    mutationFn: (text: string) => seoAPI.analyze(text),
    onSuccess: (data) => {
      setSeoAnalysis(data);
      toast.success('SEO analysis complete!');
    },
    onError: () => {
      toast.error('Failed to analyze SEO');
    },
  });

  const handleAnalyze = () => {
    if (!content.trim()) {
      toast.error('Please enter content to analyze');
      return;
    }
    analyzeSEO(content);
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-2xl font-bold mb-6">SEO Analyzer</h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Content to Analyze</label>
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="Paste your content here for SEO analysis..."
            rows={6}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          />
        </div>

        <button
          onClick={handleAnalyze}
          disabled={isPending}
          className="w-full bg-primary text-white py-2 rounded-lg hover:bg-secondary disabled:opacity-50 disabled:cursor-not-allowed font-semibold"
        >
          {isPending ? 'Analyzing...' : 'Analyze SEO'}
        </button>

        {seoAnalysis && (
          <div className="mt-6 space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-blue-50 p-4 rounded">
                <p className="text-sm text-gray-600">SEO Score</p>
                <p className="text-3xl font-bold text-primary">{seoAnalysis.seo_score}</p>
              </div>
              <div className="bg-green-50 p-4 rounded">
                <p className="text-sm text-gray-600">Word Count</p>
                <p className="text-3xl font-bold text-green-600">{seoAnalysis.word_count}</p>
              </div>
            </div>

            {seoAnalysis.issues.length > 0 && (
              <div className="bg-yellow-50 p-4 rounded">
                <h3 className="font-semibold text-yellow-900 mb-2">Issues Found</h3>
                <ul className="list-disc list-inside space-y-1 text-sm text-yellow-800">
                  {seoAnalysis.issues.map((issue: string, idx: number) => (
                    <li key={idx}>{issue}</li>
                  ))}
                </ul>
              </div>
            )}

            {seoAnalysis.recommendations.length > 0 && (
              <div className="bg-blue-50 p-4 rounded">
                <h3 className="font-semibold text-blue-900 mb-2">Recommendations</h3>
                <ul className="list-disc list-inside space-y-1 text-sm text-blue-800">
                  {seoAnalysis.recommendations.map((rec: string, idx: number) => (
                    <li key={idx}>{rec}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
