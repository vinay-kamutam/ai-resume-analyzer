import { useState } from "react";
import api from "../api/api";

import SummaryCard from "./cards/SummaryCard";
import RoleCard from "./cards/RoleCard";
import SkillsCard from "./cards/SkillsCard";
import EducationCard from "./cards/EducationCard";
import CertificationCard from "./cards/CertificationCard";
import ATSScoreCard from "./cards/ATSScoreCard";
import JobDescription from "./JobDescription";
import JobMatchCard from "./cards/JobMatchCard";

function ResumeUpload() {

    const [selectedFile, setSelectedFile] = useState(null);
    const [analysis, setAnalysis] = useState(null);
    const [atsData, setAtsData] = useState(null);
    const [jobDescription, setJobDescription] = useState("");
    const [loading, setLoading] = useState(false);
    const [jobMatchData, setJobMatchData] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const uploadResume = async () => {

        if (!selectedFile) {
            alert("Please select a resume first.");
            return;
        }

        setLoading(true);

        try {

            // Resume Analysis
            const resumeForm = new FormData();
            resumeForm.append("file", selectedFile);

            const resumeResponse = await api.post(
                "/upload-resume",
                resumeForm
            );
            console.log("Resume Response:");
            console.log(resumeResponse.data);

            setAnalysis(resumeResponse.data);

            // ATS Score
            const atsForm = new FormData();
            atsForm.append("file", selectedFile);

            const atsResponse = await api.post(
                "/ats-score",
                atsForm
            );

            console.log("ATS Response:");
            console.log(atsResponse.data);

            setAtsData(atsResponse.data);

            
            // Job Match
        if (jobDescription.trim() !== "") {

            const jobForm = new FormData();

            jobForm.append("file", selectedFile);
            jobForm.append("job_description", jobDescription);

            const jobResponse = await api.post(
                "/job-match",
                jobForm
            );

            console.log("Job Match Response:");
            console.log(jobResponse.data);

            setJobMatchData(jobResponse.data);

        }

        } catch (error) {

            console.error(error);
            alert("Resume upload failed.");

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="bg-white rounded-3xl shadow-2xl p-10">

            <h2 className="text-2xl font-semibold mb-6">
                📄 Upload Resume
            </h2>

            <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                className="mt-6 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-8 py-3 rounded-xl transition duration-300 shadow-lg hover:shadow-xl"
            />

            {selectedFile && (
                <p className="mb-6">
                    <strong>Selected File:</strong>
                    <br />
                    {selectedFile.name}
                </p>
            )}

            <JobDescription
                jobDescription={jobDescription}
                setJobDescription={setJobDescription}
            />

            <button
                onClick={uploadResume}
                disabled={loading}
                className="mt-6 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-6 py-3 rounded-lg transition"
            >
                {loading ? "⏳ Analyzing Resume..." : "🚀 Analyze Resume"}
            </button>

            {analysis && (

                <div className="mt-10 space-y-6">

                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                        <SummaryCard
                            summary={analysis.analysis.professional_summary}
                        />

                        <RoleCard
                            role={analysis.analysis.recommended_role}
                        />

                    </div>

                    <SkillsCard
                        skills={analysis.analysis.technical_skills}
                    />

                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                        <EducationCard
                            education={analysis.analysis.education}
                        />

                        <CertificationCard
                            certifications={analysis.analysis.certifications}
                        />

                    </div>

                </div>

            )}

            {atsData && (

                <div className="mt-10">

                    <ATSScoreCard
                        ats={atsData?.ats_analysis}
                    />

                </div>

            )}
            {jobMatchData && (

                <div className="mt-10">

                    <JobMatchCard
                        match={jobMatchData.job_match}
                    />

                </div>

            )}

        </div>

    );

}

export default ResumeUpload;