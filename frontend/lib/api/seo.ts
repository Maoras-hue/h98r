import apiClient from '../api';

export interface SEOAnalysis {
  seo_score: number;
  word_count: number;
  heading_count: number;
  issues: string[];
  recommendations: string[];
}

export interface Keywords {
  keywords: string[];
}

export interface MetaTags {
  title: string;
  description: string;
  keywords: string;
  og_title: string;
  og_description: string;
}

export interface Readability {
  word_count: number;
  sentence_count: number;
  paragraph_count: number;
  avg_words_per_sentence: number;
  flesch_kincaid_grade: number;
  readability_level: string;
}

export const seoAPI = {
  analyze: async (content: string): Promise<SEOAnalysis> => {
    const response = await apiClient.post('/seo/analyze', { content });
    return response.data;
  },

  extractKeywords: async (content: string): Promise<Keywords> => {
    const response = await apiClient.post('/seo/keywords', { content });
    return response.data;
  },

  generateMeta: async (title: string, content: string): Promise<MetaTags> => {
    const response = await apiClient.post('/seo/meta', { title, content });
    return response.data;
  },

  checkReadability: async (content: string): Promise<Readability> => {
    const response = await apiClient.post('/seo/readability', { content });
    return response.data;
  },
};
