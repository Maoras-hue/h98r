'use client';

import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 text-white">
      <nav className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <div className="text-2xl font-bold">✨ H98R</div>
        <div className="space-x-4">
          <Link href="/login" className="hover:underline">
            Login
          </Link>
          <Link href="/register" className="bg-white text-blue-500 px-4 py-2 rounded hover:bg-gray-100">
            Sign Up
          </Link>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 py-20 text-center">
        <h1 className="text-5xl font-bold mb-4">AI Content Generator & SEO Optimizer</h1>
        <p className="text-xl mb-8 opacity-90">
          Generate high-quality content with AI and optimize it for search engines
        </p>

        <button
          onClick={() => router.push('/register')}
          className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 mb-16"
        >
          Get Started Free
        </button>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16">
          <div className="bg-white bg-opacity-10 p-6 rounded-lg backdrop-blur">
            <h3 className="text-xl font-semibold mb-2">✍️ Content Generation</h3>
            <p className="opacity-90">Generate blog posts, social media content, and more with AI</p>
          </div>
          <div className="bg-white bg-opacity-10 p-6 rounded-lg backdrop-blur">
            <h3 className="text-xl font-semibold mb-2">🔍 SEO Optimization</h3>
            <p className="opacity-90">Analyze and optimize your content for search engines</p>
          </div>
          <div className="bg-white bg-opacity-10 p-6 rounded-lg backdrop-blur">
            <h3 className="text-xl font-semibold mb-2">💰 Affordable Pricing</h3>
            <p className="opacity-90">Start free with 10 credits/month, upgrade anytime</p>
          </div>
        </div>
      </main>
    </div>
  );
}
