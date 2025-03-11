<template>
  <div class="login-container">
    <h1>用户登录</h1>
    <form @submit.prevent="handleSubmit">
      <!-- 邮箱输入 -->
      <div class="form-group">
        <label for="email">邮箱</label>
        <input
            type="text"
            id="email"
            v-model="formData.email"
            placeholder="请输入邮箱"
            :class="{ 'input-error': errors.email }"
        />
        <span v-if="errors.email" class="error-msg">{{ errors.email }}</span>
      </div>

      <!-- 密码输入 -->
      <div class="form-group">
        <label for="password">密码</label>
        <input
            type="password"
            id="password"
            v-model="formData.password"
            placeholder="请输入密码"
            :class="{ 'input-error': errors.password }"
        />
        <span v-if="errors.password" class="error-msg">{{ errors.password }}</span>
      </div>

      <!-- 提交按钮 -->
      <button type="submit" class="submit-btn" :disabled="isSubmitting">
        {{ isSubmitting ? '登录中...' : '立即登录' }}
      </button>

      <!-- 额外链接 -->
      <div class="extra-links">
        <a href="#">忘记密码？</a>
        <a href="#">注册新账号</a>
      </div>
    </form>
  </div>
</template>

<script setup>
import {reactive, ref} from 'vue'
import {login} from "@/services/authService";
import router from "@/router";
// 响应式数据
const formData = reactive({
  email: '',
  password: ''
})

const errors = reactive({
  email: '',
  password: ''
})

const isSubmitting = ref(false)

// 表单验证规则
const validateForm = () => {
  let isValid = true
  errors.email = ''
  errors.password = ''

  if (!formData.email.trim()) {
    errors.email = '用户名不能为空'
    isValid = false
  }

  if (!formData.password) {
    errors.password = '密码不能为空'
    isValid = false
  } else if (formData.password.length < 6) {
    errors.password = '密码长度不能少于6位'
    isValid = false
  }

  return isValid
}

// 提交处理
const handleSubmit = async () => {
  if (!validateForm()) return

  isSubmitting.value = true

  try {
    // 这里替换为实际的API调用
    const response = await login(formData.email, formData.password)
    // await new Promise(resolve => setTimeout(resolve, 1500)) // 模拟API延迟
    let access_token = response.data.access_token;
    localStorage.setItem("access_token", access_token)
    // 登录成功处理
    await router.push({
      path: '/home'
    })
  } catch (error) {
    alert(error)
    alert('登录失败，请检查用户名和密码')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #666;
}

input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.input-error {
  border-color: #ff4757;
}

.error-msg {
  display: block;
  color: #ff4757;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}

.submit-btn {
  width: 100%;
  padding: 1rem;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.3s ease;
}

.submit-btn:hover {
  background: #2980b9;
}

.submit-btn:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}

.extra-links {
  margin-top: 1.5rem;
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
}

.extra-links a {
  color: #3498db;
  text-decoration: none;
}

.extra-links a:hover {
  text-decoration: underline;
}
</style>