def job_match_prompt(resume_text: str, job_description: str):

    return f"""
You are a Senior Technical Recruiter and DevOps Hiring Manager.

Compare the resume with the job description.

Return ONLY valid JSON.

STRICT RULES:

1. Return ONLY JSON.
2. No markdown.
3. No explanations.
4. Never use None.
5. Never use True or False.
6. Use only null if necessary.
7. Every list must contain strings.
8. If a list has no values, return [].
9. match_percentage MUST ALWAYS be an integer from 0 to 100.
10. Never return 0 unless the resume has absolutely no matching skills.
11. If there are matching skills, the score must be at least 40.
12. Always provide a final recommendation.

Scoring Guide:

90-100 = Excellent Match

80-89 = Strong Match

70-79 = Good Match

60-69 = Moderate Match

40-59 = Partial Match

Below 40 = Weak Match

Return exactly this JSON:

{{
    "match_percentage": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "resume_improvements": [],
    "final_recommendation": ""
}}

Resume:

{resume_text}

Job Description:

{job_description}
"""