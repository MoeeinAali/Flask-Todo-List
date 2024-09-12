from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class TaskStatus(Enum):
    ONGOING = 'ongoing'
    DONE = 'done'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Enum(TaskStatus), nullable=False, default=TaskStatus.ONGOING)

    def toggle_status(self):
        if self.status == TaskStatus.ONGOING:
            self.status = TaskStatus.DONE
        else:
            self.status = TaskStatus.ONGOING

    def __repr__(self):
        return f'<Task {self.name}>'
