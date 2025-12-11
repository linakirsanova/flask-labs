from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, TodoList, Todo
from random import randint
from datetime import datetime, timedelta


def users(count=10):
    fake = Faker()
    i = 0
    while i < count:
        u = User(
            username=fake.user_name()[:64],
            email=fake.email()[:64],
            password='password',
            member_since=fake.past_date(),
            last_seen=fake.past_date(),
            is_admin=fake.boolean(chance_of_getting_true=5)
        )
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def todolists(count=75):
    fake = Faker()
    user_count = User.query.count()
    if user_count == 0:
        return
    
    i = 0
    while i < count:
        user = User.query.offset(randint(0, user_count - 1)).first()
        if not user:
            break
        
        title = fake.sentence(nb_words=4)[:128].rstrip('.')
        created_at = fake.past_date()
        
        tl = TodoList(
            title=title,
            creator=user.username,
            created_at=created_at
        )
        db.session.add(tl)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def todos():
    fake = Faker()
    todolist_count = TodoList.query.count()
    user_count = User.query.count()
    
    if todolist_count == 0 or user_count == 0:
        return
    
    for todolist in TodoList.query.all():
        tasks_per_list = randint(5, 75)
        for _ in range(tasks_per_list):
            user = User.query.offset(randint(0, user_count - 1)).first()
            if not user:
                break
            
            description = fake.sentence(nb_words=6)[:128]
            created_at = fake.past_date()
            is_finished = fake.boolean(chance_of_getting_true=30)
            finished_at = None
            
            if is_finished:
                finished_at = created_at + timedelta(days=randint(1, 30))
            
            todo = Todo(
                description=description,
                todolist_id=todolist.id,
                creator=user.username,
                created_at=created_at
            )
            todo.is_finished = is_finished
            todo.finished_at = finished_at
            
            db.session.add(todo)
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fill_db():
    print("Generating fake users...")
    users(10)
    print("Generating fake todo lists...")
    todolists(75)
    print("Generating fake todos...")
    todos()
    print("Done! Database filled with fake data.")

