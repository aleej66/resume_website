from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class PersonalInfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    location = StringField('Location', validators=[DataRequired(), Length(max=100)])
    about = TextAreaField('About Me', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

class AchievementForm(FlaskForm):
    id = HiddenField()
    text = TextAreaField('Achievement', validators=[DataRequired()])

class ExperienceForm(FlaskForm):
    id = HiddenField()
    position = StringField('Position', validators=[DataRequired(), Length(max=100)])
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(max=100)])
    period = StringField('Period', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    achievements = FieldList(FormField(AchievementForm), min_entries=1)
    submit = SubmitField('Save Changes')

class EducationForm(FlaskForm):
    id = HiddenField()
    degree = StringField('Degree', validators=[DataRequired(), Length(max=100)])
    institution = StringField('Institution', validators=[DataRequired(), Length(max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(max=100)])
    period = StringField('Period', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Save Changes')

class SkillForm(FlaskForm):
    id = HiddenField()
    name = StringField('Skill Name', validators=[DataRequired(), Length(max=100)])
    category = StringField('Category', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Save Changes')

class TechnologyForm(FlaskForm):
    id = HiddenField()
    name = StringField('Technology', validators=[DataRequired(), Length(max=100)])

class ProjectForm(FlaskForm):
    id = HiddenField()
    name = StringField('Project Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    link = StringField('Link', validators=[Length(max=255)])
    technologies = FieldList(FormField(TechnologyForm), min_entries=1)
    submit = SubmitField('Save Changes')