from app import app, resume_data
from models import db, PersonalInfo, Education, Experience, Achievement, Skill, Project, ProjectTechnology


def init_db():
    """Initialize the database with sample resume data"""
    with app.app_context():
        # Create all tables
        db.create_all()

        # Check if data already exists
        if PersonalInfo.query.first() is not None:
            print("Database already contains data. Skipping initialization.")
            return

        # Add personal info
        personal_info = PersonalInfo(
            name=resume_data['personal_info']['name'],
            title=resume_data['personal_info']['title'],
            email=resume_data['personal_info']['email'],
            phone=resume_data['personal_info']['phone'],
            location=resume_data['personal_info']['location'],
            about=resume_data['personal_info']['about']
        )
        db.session.add(personal_info)

        # Add education entries
        for edu_data in resume_data['education']:
            education = Education(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                location=edu_data['location'],
                period=edu_data['period']
            )
            db.session.add(education)

        # Add experience entries with achievements
        for exp_data in resume_data['experience']:
            experience = Experience(
                position=exp_data['position'],
                company=exp_data['company'],
                location=exp_data['location'],
                period=exp_data['period'],
                description=exp_data['description']
            )
            db.session.add(experience)

            # Need to flush to get the experience ID
            db.session.flush()

            # Add achievements for this experience
            for achievement_text in exp_data['achievements']:
                achievement = Achievement(
                    text=achievement_text,
                    experience_id=experience.id
                )
                db.session.add(achievement)

        # Add skills
        for category, skills_list in resume_data['skills'].items():
            for skill_name in skills_list:
                skill = Skill(
                    name=skill_name,
                    category=category
                )
                db.session.add(skill)

        # Add projects with technologies
        for project_data in resume_data['projects']:
            project = Project(
                name=project_data['name'],
                description=project_data['description'],
                link=project_data.get('link', '')
            )
            db.session.add(project)

            # Need to flush to get the project ID
            db.session.flush()

            # Add technologies for this project
            for tech_name in project_data['technologies']:
                technology = ProjectTechnology(
                    name=tech_name,
                    project_id=project.id
                )
                db.session.add(technology)

        # Commit all changes
        db.session.commit()
        print("Database initialized with sample resume data.")


if __name__ == '__main__':
    init_db()