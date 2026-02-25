from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data...')

        # Create users (superheroes)
        users_data = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'password': 'avengers123'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'password': 'webslinger456'},
            {'username': 'thor', 'email': 'thor@marvel.com', 'password': 'mjolnir789'},
            {'username': 'batman', 'email': 'batman@dc.com', 'password': 'gotham123'},
            {'username': 'superman', 'email': 'superman@dc.com', 'password': 'krypton456'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'password': 'amazon789'},
        ]

        users = []
        for data in users_data:
            user = User(**data)
            user.save()
            users.append(user)
            self.stdout.write(f"Created user: {user.username}")

        # Create teams
        team_marvel = Team(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'thor'],
        )
        team_marvel.save()
        self.stdout.write(f"Created team: {team_marvel.name}")

        team_dc = Team(
            name='Team DC',
            members=['batman', 'superman', 'wonderwoman'],
        )
        team_dc.save()
        self.stdout.write(f"Created team: {team_dc.name}")

        # Create activities
        activities_data = [
            {'user': 'ironman', 'activity_type': 'Flying', 'duration': 60.0, 'date': date(2024, 1, 10)},
            {'user': 'spiderman', 'activity_type': 'Web Swinging', 'duration': 45.0, 'date': date(2024, 1, 11)},
            {'user': 'thor', 'activity_type': 'Hammer Throw', 'duration': 30.0, 'date': date(2024, 1, 12)},
            {'user': 'batman', 'activity_type': 'Martial Arts', 'duration': 90.0, 'date': date(2024, 1, 10)},
            {'user': 'superman', 'activity_type': 'Flying', 'duration': 120.0, 'date': date(2024, 1, 11)},
            {'user': 'wonderwoman', 'activity_type': 'Lasso Training', 'duration': 75.0, 'date': date(2024, 1, 12)},
        ]

        for data in activities_data:
            activity = Activity(**data)
            activity.save()
            self.stdout.write(f"Created activity: {activity.user} - {activity.activity_type}")

        # Create leaderboard entries
        leaderboard_data = [
            {'user': 'ironman', 'score': 950},
            {'user': 'spiderman', 'score': 870},
            {'user': 'thor', 'score': 920},
            {'user': 'batman', 'score': 990},
            {'user': 'superman', 'score': 1000},
            {'user': 'wonderwoman', 'score': 980},
        ]

        for data in leaderboard_data:
            entry = Leaderboard(**data)
            entry.save()
            self.stdout.write(f"Created leaderboard entry: {entry.user} - {entry.score}")

        # Create workouts
        workouts_data = [
            {
                'name': 'Avengers Strength Training',
                'description': 'High intensity strength workout inspired by Earth\'s mightiest heroes',
                'exercises': ['Bench Press', 'Deadlift', 'Squat', 'Pull-ups', 'Overhead Press'],
            },
            {
                'name': 'Justice League Cardio Blast',
                'description': 'Speed and endurance workout for defenders of justice',
                'exercises': ['Sprints', 'Jump Rope', 'Box Jumps', 'Burpees', 'Mountain Climbers'],
            },
            {
                'name': 'Spider Agility Drill',
                'description': 'Flexibility and agility training like your friendly neighborhood hero',
                'exercises': ['Ladder Drills', 'Cone Drills', 'Balance Beam', 'Tumbling', 'Handstands'],
            },
            {
                'name': 'Gotham Night Patrol',
                'description': 'Stealth and martial arts conditioning',
                'exercises': ['Shadowboxing', 'Parkour', 'Obstacle Course', 'Rock Climbing', 'Yoga'],
            },
        ]

        for data in workouts_data:
            workout = Workout(**data)
            workout.save()
            self.stdout.write(f"Created workout: {workout.name}")

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with superhero test data!'))
