import axios from "axios";

const api = axios.create({
    baseURL: "http://34.202.213.6:8000",
});

export default api;