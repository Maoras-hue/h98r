import { create } from 'zustand';
import { Content } from '@/lib/api/content';

interface ContentStore {
  contents: Content[];
  selectedContent: Content | null;
  isLoading: boolean;
  setContents: (contents: Content[]) => void;
  addContent: (content: Content) => void;
  setSelectedContent: (content: Content | null) => void;
  setIsLoading: (isLoading: boolean) => void;
}

export const useContentStore = create<ContentStore>((set) => ({
  contents: [],
  selectedContent: null,
  isLoading: false,
  setContents: (contents) => set({ contents }),
  addContent: (content) => set((state) => ({ contents: [content, ...state.contents] })),
  setSelectedContent: (content) => set({ selectedContent: content }),
  setIsLoading: (isLoading) => set({ isLoading }),
}));
