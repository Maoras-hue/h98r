'use client';

import React, { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuthStore } from '@/lib/stores/auth';
import Layout from '@/components/Layout';
import CreditCard from '@/components/CreditCard';
import ContentGenerator from '@/components/ContentGenerator';
import ContentList from '@/components/ContentList';
import SEOAnalyzer from '@/components/SEOAnalyzer';
import Cookies from 'js-cookie';

export default function DashboardPage() {
  const router = useRouter();
  const { user, isLoading, setUser } = useAuthStore();

  useEffect(() => {
    const token = Cookies.get('access_token');
    if (!token && !isLoading) {
      router.push('/login');
    }
  }, [isLoading, router]);

  if (isLoading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  if (!user) {
    return null;
  }

  return (
    <Layout>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <CreditCard />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          <ContentGenerator />
          <SEOAnalyzer />
        </div>
        <div>
          <ContentList />
        </div>
      </div>
    </Layout>
  );
}
