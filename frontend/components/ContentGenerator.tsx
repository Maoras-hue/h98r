'use client';

import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { contentAPI } from '@/lib/api/content';
import { useContentStore } from '@/lib/stores/content';
import toast from 'react-hot-toast';

export default function ContentGenerator() {
  const { addContent } = useContentStore();
  const [title, setTitle] = useState('');
  const [prompt, setPrompt] = useState('');
  const [contentType, setContentType] = useState('blog_post');
  const [tone, setTone] = useState('professional');
  const [language, setLanguage] = useState('en');

  const { mutate: generateContent, isPending } = useMutation({
    mutationFn: (data) => contentAPI.generate(data),
    onSuccess: (data) => {
      toast.success('Content generated successfully!');
      addContent(data);
      setTitle('');
      setPrompt('');
    },
    onError: (error: any) => {
      toast.error(error.response?.data?.detail || 'Failed to generate content');
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !prompt.trim()) {
      toast.error('Please fill in all fields');
      return;
    }
    generateContent({
      title,
      prompt,
      content_type: contentType as any,
      tone: tone as any,
      language,
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-2xl font-bold mb-6">Generate Content</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Title</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter content title"
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">Content Type</label>
            <select
              value={contentType}
              onChange={(e) => setContentType(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
            >
              <option value="blog_post">Blog Post</option>
              <option value="social_media">Social Media</option>
              <option value="email">Email</option>
              <option value="newsletter">Newsletter</option>
              <option value="ad_copy">Ad Copy</option>
              <option value="product_description">Product Description</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Tone</label>
            <select
              value={tone}
              onChange={(e) => setTone(e.target.value)}
              className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
            >
              <option value="professional">Professional</option>
              <option value="casual">Casual</option>
              <option value="funny">Funny</option>
              <option value="formal">Formal</option>
              <option value="friendly">Friendly</option>
            </select>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Language</label>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            <option value="de">German</option>
            <option value="it">Italian</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Your Prompt</label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Describe what you want the content to be about..."
            rows={4}
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
          />
        </div>

        <button
          type="submit"
          disabled={isPending}
          className="w-full bg-primary text-white py-2 rounded-lg hover:bg-secondary disabled:opacity-50 disabled:cursor-not-allowed font-semibold"
        >
          {isPending ? 'Generating...' : 'Generate Content'}
        </button>
      </form>
    </div>
  );
}
