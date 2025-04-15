from datetime import date
from cv_models import CV, ContactInformation, Education, WorkExperience, Project, Skill, Language, Certification

# Create CV instance
cv = CV(
    contact=ContactInformation(
        full_name="Alex Johnson",
        email="alex.johnson@example.com",
        phone="+1 (555) 123-4567",
        location="San Francisco, CA",
        website="https://alexjohnson.dev",
        linkedin="https://linkedin.com/in/alexjohnson",
        github="https://github.com/alexjohnson"
    ),
    summary="Senior Full Stack JavaScript Developer with 10 years of experience in building scalable web applications. Expert in modern JavaScript frameworks, cloud technologies, and microservices architecture. Proven track record of leading development teams and delivering high-performance applications.",
    education=[
        Education(
            institution="Stanford University",
            degree="Master of Science",
            field_of_study="Computer Science",
            start_date=date(2010, 9, 1),
            end_date=date(2012, 6, 1),
            gpa=3.8,
            location="Stanford, CA",
            description="Specialized in Web Technologies and Distributed Systems"
        ),
        Education(
            institution="University of California, Berkeley",
            degree="Bachelor of Science",
            field_of_study="Computer Science",
            start_date=date(2006, 9, 1),
            end_date=date(2010, 6, 1),
            gpa=3.9,
            location="Berkeley, CA"
        )
    ],
    work_experience=[
        WorkExperience(
            company="TechCorp Inc.",
            position="Senior Full Stack Developer",
            start_date=date(2018, 3, 1),
            end_date=date(2023, 12, 31),
            location="San Francisco, CA",
            description=[
                "Led a team of 5 developers in building a scalable e-commerce platform",
                "Implemented microservices architecture using Node.js and React",
                "Optimized application performance, reducing load times by 40%"
            ],
            achievements=[
                "Successfully migrated legacy system to modern stack",
                "Reduced server costs by 30% through optimization",
                "Implemented CI/CD pipeline reducing deployment time by 60%"
            ],
            technologies=["Node.js", "React", "TypeScript", "AWS", "Docker", "Kubernetes"]
        ),
        WorkExperience(
            company="WebSolutions Ltd.",
            position="Full Stack Developer",
            start_date=date(2013, 1, 1),
            end_date=date(2018, 2, 28),
            location="San Francisco, CA",
            description=[
                "Developed and maintained multiple web applications",
                "Implemented RESTful APIs and real-time features",
                "Collaborated with UX team to improve user experience"
            ],
            technologies=["JavaScript", "Express.js", "MongoDB", "Angular", "AWS"]
        )
    ],
    projects=[
        Project(
            name="E-commerce Platform",
            description="A scalable e-commerce platform handling 1M+ daily transactions",
            start_date=date(2020, 1, 1),
            end_date=date(2021, 12, 31),
            technologies=["Node.js", "React", "MongoDB", "Redis", "AWS"],
            role="Lead Developer",
            url="https://github.com/alexjohnson/ecommerce-platform",
            achievements=[
                "Implemented real-time inventory management",
                "Reduced checkout time by 50%",
                "Achieved 99.99% uptime"
            ]
        ),
        Project(
            name="Task Management System",
            description="Enterprise-level task management system with real-time collaboration",
            start_date=date(2019, 6, 1),
            end_date=date(2019, 12, 31),
            technologies=["Node.js", "Vue.js", "WebSocket", "PostgreSQL"],
            role="Full Stack Developer",
            url="https://github.com/alexjohnson/task-manager"
        )
    ],
    skills=[
        Skill(
            category="Frontend",
            items=["React", "Vue.js", "TypeScript", "HTML5", "CSS3", "SASS"]
        ),
        Skill(
            category="Backend",
            items=["Node.js", "Express", "NestJS", "GraphQL", "REST APIs"]
        ),
        Skill(
            category="Database",
            items=["MongoDB", "PostgreSQL", "Redis", "Elasticsearch"]
        ),
        Skill(
            category="DevOps",
            items=["Docker", "Kubernetes", "AWS", "CI/CD", "Git"]
        )
    ],
    languages=[
        Language(
            name="English",
            proficiency="Native"
        ),
        Language(
            name="Spanish",
            proficiency="Professional"
        )
    ],
    certifications=[
        Certification(
            name="AWS Certified Solutions Architect",
            issuer="Amazon Web Services",
            date_obtained=date(2021, 3, 15),
            expiration_date=date(2024, 3, 15),
            credential_id="AWS-123456"
        ),
        Certification(
            name="Professional Scrum Master I",
            issuer="Scrum.org",
            date_obtained=date(2020, 6, 1),
            credential_id="PSM-I-789012"
        )
    ],
    interests=[
        "Open Source Contribution",
        "Technical Writing",
        "Mountain Biking",
        "Photography"
    ]
)

# Print the CV instance
print(cv.model_dump_json(indent=2))
