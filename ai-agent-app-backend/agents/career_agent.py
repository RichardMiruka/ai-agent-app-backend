from agents.base_agent import BaseAgent

class CareerAgent(BaseAgent):
    """
    A career guidance agent that helps users with career-related tasks such as:
    - Creating professional summaries of technical and soft skills
    - Generating career narratives based on work experience
    - Evaluating job fit by comparing skills and experience against job descriptions
    """
    
    def __init__(self):
        """Initializes the CareerAgent with predefined skills and experience."""
        super().__init__(
            name="CareerGuide",
            description=(
                "I'm the career specialist. I can provide information about "
                "skills, experience, and job suitability."
            ),
            avatar="career_avatar.png"
        )

        self.skills = {
            "languages": ["Python", "JavaScript", "TypeScript", "Java", "SQL"],
            "frameworks": ["React", "Vue.js", "Node.js", "Django", "Flask", "Spring Boot"],
            "tools": ["Git", "Docker", "AWS", "Azure", "CI/CD", "Kubernetes"],
            "soft_skills": [
                "Team leadership", "Project management", "Agile methodologies", 
                "Technical writing", "Client communication"
            ]
        }

        self.experience = [
            {
                "title": "Senior Full Stack Developer",
                "company": "Tech Innovations Inc.",
                "period": "2020-Present",
                "responsibilities": [
                    "Led development of cloud-based SaaS platform",
                    "Managed team of 5 developers",
                    "Implemented CI/CD pipeline reducing deployment time by 40%",
                    "Architected microservices infrastructure"
                ]
            },
            {
                "title": "Full Stack Developer",
                "company": "WebSolutions Co.",
                "period": "2017-2020",
                "responsibilities": [
                    "Developed responsive web applications using React and Node.js",
                    "Implemented RESTful APIs and database schemas",
                    "Collaborated with UX/UI designers to implement user-friendly interfaces",
                    "Participated in code reviews and mentored junior developers"
                ]
            },
            {
                "title": "Junior Developer",
                "company": "StartUp Labs",
                "period": "2015-2017",
                "responsibilities": [
                    "Built and maintained client websites",
                    "Developed custom WordPress plugins",
                    "Implemented responsive designs and cross-browser compatibility",
                    "Assisted in database design and optimization"
                ]
            }
        ]

    def get_skills_summary(self):
        """Generates a professional summary of the user's skills formatted in markdown."""
        prompt = f"""
        Generate a professional summary of the following skills for a portfolio website:

        Programming Languages: {', '.join(self.skills['languages'])}
        Frameworks & Libraries: {', '.join(self.skills['frameworks'])}
        Tools & Platforms: {', '.join(self.skills['tools'])}
        Soft Skills: {', '.join(self.skills['soft_skills'])}

        Format the response in markdown with appropriate sections and highlights.
        """
        return self.get_response(prompt)

    def get_experience_summary(self):
        """Generates a professional career summary based on work experience in markdown format."""
        experience_text = "# Work Experience\n\n"
        for job in self.experience:
            experience_text += f"## {job['title']} at {job['company']}\n"
            experience_text += f"**{job['period']}**\n\n"
            experience_text += "**Responsibilities:**\n"
            for resp in job['responsibilities']:
                experience_text += f"- {resp}\n"
            experience_text += "\n"

        prompt = f"""
        Based on the following work experience, generate a professional career summary for a portfolio website:

        {experience_text}

        Highlight career progression, key achievements, and growth. Format the response in markdown.
        """
        return self.get_response(prompt)

    def assess_job_fit(self, job_description):
        """Evaluates job fit by comparing skills and experience against a given job description."""
        skills_flat = [skill for skill_category in self.skills.values() for skill in skill_category]
        experience_flat = [resp for job in self.experience for resp in job['responsibilities']]

        prompt = f"""
        Assess the fit for the following job description based on the skills and experience provided:

        Job Description:
        {job_description}

        Skills:
        {', '.join(skills_flat)}

        Experience:
        {' '.join(experience_flat)}

        Provide an analysis of strengths, potential gaps, and overall suitability for the role. Format the response in markdown.
        """
        return self.get_response(prompt)

    def get_job_recommendations(self, skills):
        """Generates job recommendations based on provided skills formatted in markdown."""
        prompt = f"""
        Based on the following skills, generate job recommendations for a portfolio website:

        {', '.join(skills)}

        Format the response in markdown.
        """
        return self.get_response(prompt)
