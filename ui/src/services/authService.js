import axios from "axios";

const API_URL = 'http://127.0.0.1:5002'

const login = async (email, password) => {
    const response = await axios.post(`${API_URL}/api/user/login`, {email, password}, {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    return response.data;
}

const getAccessToken = () => {
    return localStorage.getItem('access_token')
}

const setHeaders = (axiosInstance) => {
    axiosInstance.interceptors.request.use(
        config => {
            const token = getAccessToken();
            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`
            }
            return config;
        },
        error => {
            return Promise.reject(error)
        }
    );
};

const axiosInstance = axios.create();
setHeaders(axiosInstance);

const getCurrentLoginUser = async () => {
    const response = await axios.get(`${API_URL}/api/user/current`)
    return response.data;
}

export {login, getCurrentLoginUser};