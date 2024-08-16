def skill_gap_analysis(cv_data, job_requirements):
    """Compare candidate's skills with job requirements and highlight gaps."""
    matched_skills = [skill for skill in cv_data['skills'] if skill in job_requirements['skills']]
    missing_skills = [skill for skill in job_requirements['skills'] if skill not in cv_data['skills']]
    return matched_skills, missing_skills
