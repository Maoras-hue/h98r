import apiClient from '../api';

export interface ContentCreateRequest {
  title: string;
  content_type: 'blog_post' | 'social_media' | 'email' | 'newsletter' | 'ad_copy' | 'product_description';
  tone: 'professional' | 'casual' | 'funny' | 'formal' | 'friendly';
  language?: string;
  keywords?: string;
  prompt: string;
}

export interface Content {
  id: number;
  user_id: number;
  title: string;
  content: string;
  content_type: string;
  tone: string;
  language: string;
  keywords?: string;
  meta_description?: string;
  seo_score: number;
  model_used: string;
  tokens_used: number;
  created_at: string;
  updated_at: string;
}

export const contentAPI = {
  generate: async (data: ContentCreateRequest): Promise<Content> => {
    const response = await apiClient.post('/content/generate', data);
    return response.data;
  },

  getContents: async (skip: number = 0, limit: number = 10): Promise<Content[]> => {
    const response = await apiClient.get(`/content/?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  getContent: async (id: number): Promise<Content> => {
    const response = await apiClient.get(`/content/${id}`);
    return response.data;
  },

  rewrite: async (contentId: number, tone?: string, style?: string) => {
    const response = await apiClient.post('/content/rewrite', {
      content_id: contentId,
      tone,
      style,
    });
    return response.data;
  },
};
