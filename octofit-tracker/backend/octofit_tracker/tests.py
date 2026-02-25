from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='ironman',
            email='ironman@marvel.com',
            password='avengers123',
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'ironman')
        self.assertEqual(self.user.email, 'ironman@marvel.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'ironman')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'thor'],
        )

    def tearDown(self):
        Team.objects.all().delete()

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Team Marvel')
        self.assertIn('ironman', self.team.members)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Team Marvel')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user='batman',
            activity_type='Martial Arts',
            duration=90.0,
            date=date(2024, 1, 10),
        )

    def tearDown(self):
        Activity.objects.all().delete()

    def test_activity_creation(self):
        self.assertEqual(self.activity.user, 'batman')
        self.assertEqual(self.activity.activity_type, 'Martial Arts')
        self.assertEqual(self.activity.duration, 90.0)

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'batman - Martial Arts')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user='superman',
            score=1000,
        )

    def tearDown(self):
        Leaderboard.objects.all().delete()

    def test_leaderboard_creation(self):
        self.assertEqual(self.entry.user, 'superman')
        self.assertEqual(self.entry.score, 1000)

    def test_leaderboard_str(self):
        self.assertEqual(str(self.entry), 'superman: 1000')


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Avengers Strength Training',
            description='High intensity workout',
            exercises=['Bench Press', 'Deadlift', 'Squat'],
        )

    def tearDown(self):
        Workout.objects.all().delete()

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Avengers Strength Training')
        self.assertIn('Deadlift', self.workout.exercises)

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Avengers Strength Training')


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create(username='thor', email='thor@marvel.com', password='mjolnir')

    def tearDown(self):
        User.objects.all().delete()

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'password': 'web123'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Team.objects.create(name='Team DC', members=['batman', 'superman'])

    def tearDown(self):
        Team.objects.all().delete()

    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Activity.objects.create(
            user='wonderwoman', activity_type='Lasso Training', duration=75.0, date=date(2024, 1, 12)
        )

    def tearDown(self):
        Activity.objects.all().delete()

    def test_get_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Leaderboard.objects.create(user='batman', score=990)

    def tearDown(self):
        Leaderboard.objects.all().delete()

    def test_get_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Workout.objects.create(
            name='Gotham Night Patrol',
            description='Stealth and martial arts',
            exercises=['Shadowboxing', 'Parkour'],
        )

    def tearDown(self):
        Workout.objects.all().delete()

    def test_get_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
