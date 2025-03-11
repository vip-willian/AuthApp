<template>
  <div class="welcome-container">
    <h2>首页大厅</h2>
    <div v-if="loading">Loading....</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <p>login in as: {{ user }}</p>
    </div>
  </div>
</template>

<script>
import {getCurrentLoginUser} from "@/services/authService";

export default {
  data() {
    return {
      user: null,
      loading: true,
      error: null
    }
  },
  created() {
    this.fetchLoginUser();
  },
  methods: {
    async fetchLoginUser() {
      try {
        const response = await getCurrentLoginUser()
        this.user = response.data;
      } catch (error) {
        this.error = 'Failed to fetch current login user'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.welcome-container {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
  text-align: center;
  max-width: 400px;
  margin: 0 auto;
  color: red;
  font-weight: bold;
  font-size: 30px;
}
</style>