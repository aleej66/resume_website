# Getting Started with Your Personal Resume Website

Congratulations on setting up your personal resume website! This guide will help you get started with customizing and deploying your site.

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **View your website** at http://127.0.0.1:5000/

## Customizing Your Resume

### 1. Update Your Personal Information

Edit the `resume_data` dictionary in `app.py` to include your personal information:

- Personal details (name, title, contact information)
- Work experience
- Education history
- Skills
- Projects

### 2. Add Your Profile Picture

Place your profile picture in the `static/images/` directory with the filename `profile.jpg`.

### 3. Customize the Look and Feel

- **Colors**: Edit the CSS variables at the top of `static/css/style.css` to change the color scheme.
- **Layout**: Modify the HTML templates in the `templates` directory to change the layout.

## Testing Your Website

Run the included tests to ensure everything is working correctly:

```bash
python -m unittest tests/test_resume_website.py
```

## Deployment Options

### Option 1: Deploy to Heroku

1. Create a Heroku account if you don't have one
2. Install the Heroku CLI
3. Create a `Procfile` with:
   ```
   web: gunicorn app:app
   ```
4. Add gunicorn to requirements.txt
5. Deploy:
   ```bash
   heroku create your-resume-site
   git push heroku main
   ```

### Option 2: Deploy to PythonAnywhere

1. Create a PythonAnywhere account
2. Upload your code
3. Set up a web app with Flask
4. Configure the WSGI file to point to your app.py

## Extending Your Website

Here are some ideas to enhance your resume website:

1. **Add a blog section** to share your thoughts and experiences
2. **Implement a contact form** for visitors to reach out to you
3. **Add a portfolio gallery** with images of your projects
4. **Integrate with GitHub** to automatically display your repositories
5. **Add testimonials** from colleagues or clients

## Troubleshooting

If you encounter any issues:

1. Check that all dependencies are installed
2. Verify that Flask is running correctly
3. Check the browser console for JavaScript errors
4. Ensure all paths in your templates are correct

## Need Help?

If you need assistance, check out these resources:

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)

Happy coding!