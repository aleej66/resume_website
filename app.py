from flask import Flask, render_template, url_for, redirect, request, flash
from flask_wtf.csrf import CSRFProtect
import os
from models import db, PersonalInfo, Education, Experience, Achievement, Skill, Project, ProjectTechnology
from forms import PersonalInfoForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, AchievementForm, \
    TechnologyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_for_development')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resume.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
csrf = CSRFProtect(app)

# Sample resume data - kept for reference and initialization
resume_data = {
    'personal_info': {
        'name': 'John Doe',
        'title': 'Software Engineer',
        'email': 'john.doe@example.com',
        'phone': '+1 (123) 456-7890',
        'location': 'New York, NY',
        'about': 'Experienced software engineer with a passion for building scalable web applications and solving complex problems.'
    },
    'education': [
        {
            'degree': 'Master of Science in Computer Science',
            'institution': 'Stanford University',
            'location': 'Stanford, CA',
            'period': '2018 - 2020'
        },
        {
            'degree': 'Bachelor of Science in Computer Engineering',
            'institution': 'MIT',
            'location': 'Cambridge, MA',
            'period': '2014 - 2018'
        }
    ],
    'experience': [
        {
            'position': 'Senior Software Engineer',
            'company': 'Tech Solutions Inc.',
            'location': 'New York, NY',
            'period': '2020 - Present',
            'description': 'Lead developer for cloud-based enterprise applications. Implemented microservices architecture and CI/CD pipelines.',
            'achievements': [
                'Reduced system downtime by 40% through implementation of robust error handling',
                'Improved application performance by 30% through code optimization',
                'Led a team of 5 developers to deliver projects on time and within budget'
            ]
        },
        {
            'position': 'Software Engineer',
            'company': 'Web Innovations',
            'location': 'San Francisco, CA',
            'period': '2018 - 2020',
            'description': 'Developed and maintained web applications using Python, Flask, and React.',
            'achievements': [
                'Implemented RESTful APIs for mobile and web clients',
                'Contributed to open-source projects and internal libraries',
                'Mentored junior developers and conducted code reviews'
            ]
        }
    ],
    'skills': {
        'programming': ['Python', 'JavaScript', 'Java', 'C++', 'SQL'],
        'frameworks': ['Flask', 'Django', 'React', 'Angular', 'Node.js'],
        'tools': ['Git', 'Docker', 'Kubernetes', 'AWS', 'CI/CD'],
        'languages': ['English (Native)', 'Mandarin (Intermediate)']
    },
    'projects': [
        {
            'name': 'E-commerce Platform',
            'description': 'Built a scalable e-commerce platform with payment processing and inventory management',
            'technologies': ['Python', 'Flask', 'React', 'PostgreSQL', 'AWS'],
            'link': 'https://github.com/johndoe/ecommerce'
        },
        {
            'name': 'Data Visualization Dashboard',
            'description': 'Created an interactive dashboard for visualizing complex datasets',
            'technologies': ['Python', 'D3.js', 'Flask', 'MongoDB'],
            'link': 'https://github.com/johndoe/data-viz'
        }
    ]
}


# Helper function to get resume data from database
def get_resume_data():
    """Get resume data from database and format it like the original resume_data dictionary"""
    resume = {}

    # Get personal info
    personal_info = PersonalInfo.query.first()
    if personal_info:
        resume['personal_info'] = personal_info.to_dict()
    else:
        resume['personal_info'] = {}

    # Get education
    education_list = Education.query.all()
    resume['education'] = [edu.to_dict() for edu in education_list]

    # Get experience with achievements
    experience_list = Experience.query.all()
    resume['experience'] = [exp.to_dict() for exp in experience_list]

    # Get skills grouped by category
    skills = Skill.query.all()
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill.name)
    resume['skills'] = skill_categories

    # Get projects with technologies
    projects_list = Project.query.all()
    resume['projects'] = [proj.to_dict() for proj in projects_list]

    return resume


@app.route('/')
def index():
    """Render the main resume page"""
    resume = get_resume_data()
    return render_template('index.html', resume=resume)


@app.route('/experience')
def experience():
    """Render the experience page"""
    resume = get_resume_data()
    return render_template('experience.html', experience=resume['experience'])


@app.route('/education')
def education():
    """Render the education page"""
    resume = get_resume_data()
    return render_template('education.html', education=resume['education'])


@app.route('/skills')
def skills():
    """Render the skills page"""
    resume = get_resume_data()
    return render_template('skills.html', skills=resume['skills'])


@app.route('/projects')
def projects():
    """Render the projects page"""
    resume = get_resume_data()
    return render_template('projects.html', projects=resume['projects'])


# Admin routes for editing resume data
@app.route('/admin')
def admin():
    """Admin dashboard for editing resume data"""
    return render_template('admin/dashboard.html')


@app.route('/admin/personal', methods=['GET', 'POST'])
def edit_personal():
    """Edit personal information"""
    personal_info = PersonalInfo.query.first()
    if not personal_info:
        flash('No personal information found. Please initialize the database.', 'error')
        return redirect(url_for('admin'))

    form = PersonalInfoForm(obj=personal_info)

    if form.validate_on_submit():
        form.populate_obj(personal_info)
        db.session.commit()
        flash('Personal information updated successfully!', 'success')
        return redirect(url_for('admin'))

    return render_template('admin/edit_personal.html', form=form)


@app.route('/admin/education')
def list_education():
    """List all education entries"""
    education_list = Education.query.all()
    return render_template('admin/list_education.html', education=education_list)


@app.route('/admin/education/add', methods=['GET', 'POST'])
def add_education():
    """Add a new education entry"""
    form = EducationForm()

    if form.validate_on_submit():
        education = Education()
        form.populate_obj(education)
        db.session.add(education)
        db.session.commit()
        flash('Education entry added successfully!', 'success')
        return redirect(url_for('list_education'))

    return render_template('admin/edit_education.html', form=form, is_add=True)


@app.route('/admin/education/edit/<int:id>', methods=['GET', 'POST'])
def edit_education(id):
    """Edit an education entry"""
    education = Education.query.get_or_404(id)
    form = EducationForm(obj=education)

    if form.validate_on_submit():
        form.populate_obj(education)
        db.session.commit()
        flash('Education entry updated successfully!', 'success')
        return redirect(url_for('list_education'))

    return render_template('admin/edit_education.html', form=form, is_add=False)


@app.route('/admin/education/delete/<int:id>', methods=['POST'])
def delete_education(id):
    """Delete an education entry"""
    education = Education.query.get_or_404(id)
    db.session.delete(education)
    db.session.commit()
    flash('Education entry deleted successfully!', 'success')
    return redirect(url_for('list_education'))


@app.route('/admin/experience')
def list_experience():
    """List all experience entries"""
    experience_list = Experience.query.all()
    return render_template('admin/list_experience.html', experience=experience_list)


@app.route('/admin/experience/add', methods=['GET', 'POST'])
def add_experience():
    """Add a new experience entry"""
    form = ExperienceForm()

    if form.validate_on_submit():
        experience = Experience(
            position=form.position.data,
            company=form.company.data,
            location=form.location.data,
            period=form.period.data,
            description=form.description.data
        )
        db.session.add(experience)
        db.session.flush()

        # Add achievements
        for achievement_form in form.achievements:
            achievement = Achievement(
                text=achievement_form.text.data,
                experience_id=experience.id
            )
            db.session.add(achievement)

        db.session.commit()
        flash('Experience entry added successfully!', 'success')
        return redirect(url_for('list_experience'))

    return render_template('admin/edit_experience.html', form=form, is_add=True)


@app.route('/admin/experience/edit/<int:id>', methods=['GET', 'POST'])
def edit_experience(id):
    """Edit an experience entry"""
    experience = Experience.query.get_or_404(id)

    if request.method == 'GET':
        form = ExperienceForm(obj=experience)
        # Clear the achievements FieldList and repopulate it
        form.achievements.pop_entry()
        for achievement in experience.achievements:
            form.achievements.append_entry({'id': achievement.id, 'text': achievement.text})
    else:
        form = ExperienceForm()
        if form.validate_on_submit():
            experience.position = form.position.data
            experience.company = form.company.data
            experience.location = form.location.data
            experience.period = form.period.data
            experience.description = form.description.data

            # Delete existing achievements
            for achievement in experience.achievements:
                db.session.delete(achievement)

            # Add new achievements
            for achievement_form in form.achievements:
                achievement = Achievement(
                    text=achievement_form.text.data,
                    experience_id=experience.id
                )
                db.session.add(achievement)

            db.session.commit()
            flash('Experience entry updated successfully!', 'success')
            return redirect(url_for('list_experience'))

    return render_template('admin/edit_experience.html', form=form, is_add=False)


@app.route('/admin/experience/delete/<int:id>', methods=['POST'])
def delete_experience(id):
    """Delete an experience entry"""
    experience = Experience.query.get_or_404(id)
    db.session.delete(experience)
    db.session.commit()
    flash('Experience entry deleted successfully!', 'success')
    return redirect(url_for('list_experience'))


@app.route('/admin/skills')
def list_skills():
    """List all skills grouped by category"""
    skills = Skill.query.all()
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    return render_template('admin/list_skills.html', skill_categories=skill_categories)


@app.route('/admin/skills/add', methods=['GET', 'POST'])
def add_skill():
    """Add a new skill"""
    form = SkillForm()

    if form.validate_on_submit():
        skill = Skill()
        form.populate_obj(skill)
        db.session.add(skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('list_skills'))

    return render_template('admin/edit_skill.html', form=form, is_add=True)


@app.route('/admin/skills/edit/<int:id>', methods=['GET', 'POST'])
def edit_skill(id):
    """Edit a skill"""
    skill = Skill.query.get_or_404(id)
    form = SkillForm(obj=skill)

    if form.validate_on_submit():
        form.populate_obj(skill)
        db.session.commit()
        flash('Skill updated successfully!', 'success')
        return redirect(url_for('list_skills'))

    return render_template('admin/edit_skill.html', form=form, is_add=False)


@app.route('/admin/skills/delete/<int:id>', methods=['POST'])
def delete_skill(id):
    """Delete a skill"""
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    flash('Skill deleted successfully!', 'success')
    return redirect(url_for('list_skills'))


@app.route('/admin/projects')
def list_projects():
    """List all projects"""
    projects_list = Project.query.all()
    return render_template('admin/list_projects.html', projects=projects_list)


@app.route('/admin/projects/add', methods=['GET', 'POST'])
def add_project():
    """Add a new project"""
    form = ProjectForm()

    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            link=form.link.data
        )
        db.session.add(project)
        db.session.flush()

        # Add technologies
        for tech_form in form.technologies:
            tech = ProjectTechnology(
                name=tech_form.name.data,
                project_id=project.id
            )
            db.session.add(tech)

        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('list_projects'))

    return render_template('admin/edit_project.html', form=form, is_add=True)


@app.route('/admin/projects/edit/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    """Edit a project"""
    project = Project.query.get_or_404(id)

    if request.method == 'GET':
        form = ProjectForm(obj=project)
        # Clear the technologies FieldList and repopulate it
        form.technologies.pop_entry()
        for tech in project.technologies:
            form.technologies.append_entry({'id': tech.id, 'name': tech.name})
    else:
        form = ProjectForm()
        if form.validate_on_submit():
            project.name = form.name.data
            project.description = form.description.data
            project.link = form.link.data

            # Delete existing technologies
            for tech in project.technologies:
                db.session.delete(tech)

            # Add new technologies
            for tech_form in form.technologies:
                tech = ProjectTechnology(
                    name=tech_form.name.data,
                    project_id=project.id
                )
                db.session.add(tech)

            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('list_projects'))

    return render_template('admin/edit_project.html', form=form, is_add=False)


@app.route('/admin/projects/delete/<int:id>', methods=['POST'])
def delete_project(id):
    """Delete a project"""
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('list_projects'))


@app.before_first_request
def create_tables():
    db.create_all()
    # Check if we need to initialize the database
    if PersonalInfo.query.first() is None:
        from init_db import init_db
        init_db()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建所有数据库表
    app.run(debug=True)
