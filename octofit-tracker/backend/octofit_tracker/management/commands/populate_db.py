from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from djongo import models

from pprint import pprint

# サンプルデータ
USERS = [
    {"name": "Clark Kent", "email": "clark@dc.com", "team": "dc"},
    {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "dc"},
    {"name": "Diana Prince", "email": "diana@dc.com", "team": "dc"},
    {"name": "Tony Stark", "email": "tony@marvel.com", "team": "marvel"},
    {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "marvel"},
    {"name": "Natasha Romanoff", "email": "natasha@marvel.com", "team": "marvel"},
]

TEAMS = [
    {"name": "marvel", "members": ["tony@marvel.com", "steve@marvel.com", "natasha@marvel.com"]},
    {"name": "dc", "members": ["clark@dc.com", "bruce@dc.com", "diana@dc.com"]},
]

ACTIVITIES = [
    {"user_email": "clark@dc.com", "activity": "run", "distance": 5},
    {"user_email": "tony@marvel.com", "activity": "cycle", "distance": 20},
]

LEADERBOARD = [
    {"team": "marvel", "score": 100},
    {"team": "dc", "score": 90},
]

WORKOUTS = [
    {"name": "Pushups", "difficulty": "easy"},
    {"name": "Squats", "difficulty": "medium"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # コレクション削除
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # データ挿入
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # emailユニークインデックス
        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_dbにテストデータを投入しました'))
        # コレクションとサンプルデータ表示
        for col in db.list_collection_names():
            self.stdout.write(f"Collection: {col}")
            pprint(list(db[col].find().limit(2)))
