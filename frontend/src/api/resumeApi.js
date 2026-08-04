import api from "./api";

export const uploadResume = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/upload-resume",
        formData
    );

    return response.data;
};

export const getATSScore = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/ats-score",
        formData
    );

    return response.data;
};

export const getJobMatch = async (
    file,
    jobDescription
) => {

    const formData = new FormData();

    formData.append("file", file);

    formData.append(
        "job_description",
        jobDescription
    );

    const response = await api.post(
        "/job-match",
        formData
    );

    return response.data;
};