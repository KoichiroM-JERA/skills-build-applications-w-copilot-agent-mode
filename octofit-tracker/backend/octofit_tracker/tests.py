from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['a', 'b'])
        self.assertEqual(team.name, 'marvel')
        self.assertEqual(team.members, ['a', 'b'])

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='run', distance=5)
        self.assertEqual(activity.activity, 'run')
        self.assertEqual(activity.distance, 5)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='marvel', score=100)
        self.assertEqual(lb.team, 'marvel')
        self.assertEqual(lb.score, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', difficulty='easy')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.difficulty, 'easy')
