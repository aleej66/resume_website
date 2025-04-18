# filename: models.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

# 创建 Flask 应用实例并配置数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # 替换为实际数据库 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy，绑定应用实例
db = SQLAlchemy(app)


# 以下为模型类的定义，不需要更改
class PersonalInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    about = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'name': self.name,
            'title': self.title,
            'email': self.email,
            'phone': self.phone,
            'location': self.location,
            'about': self.about
        }


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'degree': self.degree,
            'institution': self.institution,
            'location': self.location,
            'period': self.period
        }


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        achievements = [a.text for a in self.achievements]
        return {
            'position': self.position,
            'company': self.company,
            'location': self.location,
            'period': self.period,
            'description': self.description,
            'achievements': achievements
        }


class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    experience_id = db.Column(db.Integer, db.ForeignKey('experience.id'), nullable=False)
    experience = db.relationship('Experience',
                                 backref=db.backref('achievements', lazy=True, cascade="all, delete-orphan"))


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # programming, frameworks, tools, languages

    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category
        }


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(255))

    def to_dict(self):
        technologies = [t.name for t in self.technologies]
        return {
            'name': self.name,
            'description': self.description,
            'technologies': technologies,
            'link': self.link
        }


class ProjectTechnology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('technologies', lazy=True, cascade="all, delete-orphan"))
