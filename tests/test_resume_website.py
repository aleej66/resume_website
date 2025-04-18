import unittest
import os
from app import app, db
from models import PersonalInfo, Education, Experience, Achievement, Skill, Project, ProjectTechnology

class ResumeWebsiteTestCase(unittest.TestCase):
    """Test cases for the resume website"""

    def setUp(self):
        """Set up test client and database"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        self.app = app.test_client()

        # Create the database and tables
        with app.app_context():
            db.create_all()

            # Add test data
            personal_info = PersonalInfo(
                name="John Doe",
                title="Software Engineer",
                email="john.doe@example.com",
                phone="+1 (123) 456-7890",
                location="New York, NY",
                about="Experienced software engineer with a passion for building scalable web applications."
            )
            db.session.add(personal_info)

            education = Education(
                degree="Master of Science in Computer Science",
                institution="Stanford University",
                location="Stanford, CA",
                period="2018 - 2020"
            )
            db.session.add(education)

            experience = Experience(
                position="Senior Software Engineer",
                company="Tech Solutions Inc.",
                location="New York, NY",
                period="2020 - Present",
                description="Lead developer for cloud-based enterprise applications."
            )
            db.session.add(experience)
            db.session.flush()

            achievement = Achievement(
                text="Reduced system downtime by 40% through implementation of robust error handling",
                experience_id=experience.id
            )
            db.session.add(achievement)

            skill = Skill(
                name="Python",
                category="programming"
            )
            db.session.add(skill)

            project = Project(
                name="E-commerce Platform",
                description="Built a scalable e-commerce platform with payment processing.",
                link="https://github.com/johndoe/ecommerce"
            )
            db.session.add(project)
            db.session.flush()

            technology = ProjectTechnology(
                name="Python",
                project_id=project.id
            )
            db.session.add(technology)

            db.session.commit()

    def tearDown(self):
        """Clean up after tests"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        """Test that the home page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Personal Resume', response.data)

    def test_experience_page(self):
        """Test that the experience page loads correctly"""
        response = self.app.get('/experience')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Work Experience', response.data)

    def test_education_page(self):
        """Test that the education page loads correctly"""
        response = self.app.get('/education')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Education', response.data)

    def test_skills_page(self):
        """Test that the skills page loads correctly"""
        response = self.app.get('/skills')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Skills', response.data)

    def test_projects_page(self):
        """Test that the projects page loads correctly"""
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Projects', response.data)

    def test_navigation_links(self):
        """Test that all navigation links are present on the home page"""
        response = self.app.get('/')
        self.assertIn(b'href="/experience"', response.data)
        self.assertIn(b'href="/education"', response.data)
        self.assertIn(b'href="/skills"', response.data)
        self.assertIn(b'href="/projects"', response.data)

    def test_personal_info_displayed(self):
        """Test that personal information is displayed on the home page"""
        response = self.app.get('/')
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Software Engineer', response.data)
        self.assertIn(b'john.doe@example.com', response.data)

    def test_admin_dashboard(self):
        """Test that the admin dashboard loads correctly"""
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Resume Admin Dashboard', response.data)

    def test_edit_personal_info(self):
        """Test that the personal info edit page loads correctly"""
        response = self.app.get('/admin/personal')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Edit Personal Information', response.data)

    def test_list_education(self):
        """Test that the education list page loads correctly"""
        response = self.app.get('/admin/education')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Manage Education', response.data)

    def test_add_education(self):
        """Test adding a new education entry"""
        data = {
            'degree': 'Bachelor of Science',
            'institution': 'Test University',
            'location': 'Test City',
            'period': '2010 - 2014'
        }
        response = self.app.post('/admin/education/add', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Education entry added successfully', response.data)

        # Verify the new entry is in the database
        with app.app_context():
            education = Education.query.filter_by(institution='Test University').first()
            self.assertIsNotNone(education)
            self.assertEqual(education.degree, 'Bachelor of Science')

    def test_edit_education(self):
        """Test editing an education entry"""
        # First, get the ID of the education entry
        with app.app_context():
            education = Education.query.first()
            education_id = education.id

        data = {
            'degree': 'Updated Degree',
            'institution': 'Updated University',
            'location': 'Updated City',
            'period': '2015 - 2019'
        }
        response = self.app.post(f'/admin/education/edit/{education_id}', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Education entry updated successfully', response.data)

        # Verify the entry was updated in the database
        with app.app_context():
            updated_education = Education.query.get(education_id)
            self.assertEqual(updated_education.degree, 'Updated Degree')
            self.assertEqual(updated_education.institution, 'Updated University')

if __name__ == '__main__':
    unittest.main()
