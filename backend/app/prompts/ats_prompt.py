def ats_prompt(resume_text: str):

    return f"""
You are a Senior DevOps Hiring Manager with 15+ years of recruitment experience.

Evaluate this resume ONLY for a Junior DevOps Engineer role.

Scoring Criteria:

Technical Skills = 30 points

Projects = 30 points

Experience = 20 points

Education = 10 points

Certifications = 10 points

Total Score = 100

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT include explanations outside JSON.

Return exactly this structure:

{{
  "overall_score": 0,

  "score_breakdown": {{
      "technical_skills": 0,
      "projects": 0,
      "experience": 0,
      "education": 0,
      "certifications": 0
  }},

  "strengths": [],

  "weaknesses": [],

  "missing_skills": [],

  "improvement_suggestions": [],

  "interview_probability": "",

  "hiring_recommendation": ""
}}

Resume:

{resume_text}
"""