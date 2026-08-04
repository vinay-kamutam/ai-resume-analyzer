def job_match_prompt(resume_text: str, job_description: str):

    return f"""
You are a Senior Technical Recruiter.

Compare the candidate's resume with the job description.

Return ONLY valid JSON.

IMPORTANT RULES:

1. Never use Python values like None, True, or False.
2. Use null instead of None.
3. Every list must contain only strings.
4. If there are no values, return an empty list [].
5. match_percentage must be an integer between 0 and 100.
6. Always include every field.
7. Always close the JSON with }}.
8. Do not include markdown.
9. Do not include explanations outside the JSON.

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