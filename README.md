# Personal Resume Website

A Flask-based personal resume website that showcases your professional experience, education, skills, and projects.

## Features

- Responsive design that works on desktop, tablet, and mobile devices
- Separate pages for different sections of your resume
- Clean and modern UI with smooth animations
- Easy to customize with your own information

## Prerequisites

- Python 3.6 or higher
- Flask

## Installation

1. Clone this repository or download the source code:

```bash
git clone https://github.com/yourusername/resume-website.git
cd resume-website
```

2. Create a virtual environment and activate it:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Update the resume data in `app.py` with your personal information.
2. Replace the default profile image in `static/images/profile.jpg` with your own photo.
3. Customize the colors and styles in `static/css/style.css` if desired.

## Running the Application

To run the application locally:

```bash
python app.py
```

The website will be available at http://127.0.0.1:5000/

## Project Structure

```
resume_website/
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── static/                 # Static files
│   ├── css/                # CSS stylesheets
│   │   └── style.css       # Main stylesheet
│   ├── js/                 # JavaScript files
│   │   └── script.js       # Main JavaScript file
│   └── images/             # Image files
│       └── profile.jpg     # Profile picture
├── templates/              # HTML templates
│   ├── layout.html         # Base template
│   ├── index.html          # Home page
│   ├── experience.html     # Experience page
│   ├── education.html      # Education page
│   ├── skills.html         # Skills page
│   └── projects.html       # Projects page
└── tests/                  # Test files
    └── test_resume_website.py  # Test cases
```

## Running Tests

To run the tests:

```bash
python -m unittest tests/test_resume_website.py
```

## Deployment

This application can be deployed to various platforms:

### Heroku

1. Create a `Procfile` with the following content:
```
web: gunicorn app:app
```

2. Add `gunicorn` to your `requirements.txt`:
```
Flask==2.0.1
gunicorn==20.1.0
```

3. Deploy to Heroku:
```bash
heroku create your-resume-website
git push heroku main
```

### PythonAnywhere

1. Upload your code to PythonAnywhere
2. Set up a web app with Flask
3. Configure the WSGI file to point to your app.py

## Customization

- **Colors**: Edit the CSS variables in `static/css/style.css` to change the color scheme.
- **Content**: Update the resume data in `app.py` to reflect your personal information.
- **Layout**: Modify the HTML templates in the `templates` directory to change the layout.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Roboto font

# Resume Website with SQLite Database

This is a Flask-based resume website that allows users to view and edit their resume information. The resume data is stored in a SQLite database, making it easy to update and maintain.

## Features

- Display resume information including personal details, education, experience, skills, and projects
- Admin interface for editing all resume sections
- SQLite database for persistent storage
- Responsive design for mobile and desktop viewing

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd resume_website
```

2. Create a virtual environment and activate it:
```
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Initialize the database:
```
python init_db.py
```

5. Run the application:
```
python app.py
```

6. Open your browser and navigate to `http://localhost:5000` to view the resume.

## Usage

### Viewing the Resume

- Home page: View personal information and summaries of all sections
- Experience page: View detailed work experience
- Education page: View educational background
- Skills page: View skills categorized by type
- Projects page: View projects with descriptions and technologies used

### Editing the Resume

1. Click on the "Admin" link in the navigation bar to access the admin dashboard.
2. From the dashboard, you can:
   - Edit personal information
   - Add, edit, or delete education entries
   - Add, edit, or delete experience entries (with achievements)
   - Add, edit, or delete skills
   - Add, edit, or delete projects (with technologies)

## Project Structure

- `app.py`: Main application file with routes and configuration
- `models.py`: Database models for all resume sections
- `forms.py`: WTForms classes for form handling
- `init_db.py`: Script to initialize the database with sample data
- `templates/`: HTML templates for the website
  - `templates/admin/`: Templates for the admin interface
- `static/`: Static files (CSS, JavaScript, images)
- `tests/`: Test files

## Technologies Used

- Flask: Web framework
- SQLAlchemy: ORM for database operations
- Flask-WTF: Form handling and validation
- SQLite: Database
- HTML/CSS/JavaScript: Frontend

## Testing

Run the tests with:
```
python -m unittest discover
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
