import apiClient from '../api';

export interface UserCredit {
  id: number;
  user_id: number;
  total_credits: number;
  used_credits: number;
  available_credits: number;
  last_reset: string;
  next_reset?: string;
}

export const userAPI = {
  getCredits: async (): Promise<UserCredit> => {
    const response = await apiClient.get('/users/credits');
    return response.data;
  },
};
