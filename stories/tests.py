from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from .forms import StoryForm
from .models import Story
from .services import generate_story


class StoryModelTests(TestCase):
    def test_story_creation(self):
        story = Story.objects.create(
            genre='Fantasy',
            main_character='A young engineer',
            location='A mysterious city',
            theme='Friendship',
            mood='Adventure',
            story_length='Medium',
            title='The Engineer of the Hidden City',
            content='A magical story unfolds under the city lights.',
        )
        self.assertEqual(str(story), 'The Engineer of the Hidden City')
        self.assertEqual(Story.objects.count(), 1)

    def test_required_fields(self):
        story = Story(genre='Fantasy', main_character='', location='A city')
        with self.assertRaises(Exception):
            story.full_clean()


class StoryFormTests(TestCase):
    def test_valid_form(self):
        form = StoryForm(data={
            'genre': 'Fantasy',
            'main_character': 'A young engineer',
            'location': 'A mysterious city',
            'theme': 'Friendship',
            'mood': 'Adventure',
            'story_length': 'Medium',
        })
        self.assertTrue(form.is_valid())

    def test_empty_required_fields(self):
        form = StoryForm(data={
            'genre': '',
            'main_character': '',
            'location': '',
            'theme': '',
            'mood': '',
            'story_length': '',
        })
        self.assertFalse(form.is_valid())

    def test_invalid_choices(self):
        form = StoryForm(data={
            'genre': 'Not Real',
            'main_character': 'A young engineer',
            'location': 'A mysterious city',
            'theme': 'Friendship',
            'mood': 'Adventure',
            'story_length': 'Medium',
        })
        self.assertFalse(form.is_valid())


class StoryGenerationTests(TestCase):
    def test_generate_story_output(self):
        result = generate_story(
            'Fantasy',
            'A young engineer',
            'A mysterious city',
            'Friendship',
            'Adventure',
            'Medium',
        )
        self.assertIn('title', result)
        self.assertIn('story', result)
        self.assertIn('genre', result)
        self.assertTrue(result['title'])
        self.assertTrue(result['story'])
        self.assertIn('A young engineer', result['story'])
        self.assertIn('A mysterious city', result['story'])
        self.assertIn('Friendship', result['story'])

    def test_story_changes_on_regeneration(self):
        first = generate_story('Fantasy', 'A young engineer', 'A mysterious city', 'Friendship', 'Adventure', 'Medium')
        second = generate_story('Fantasy', 'A young engineer', 'A mysterious city', 'Friendship', 'Adventure', 'Medium')
        self.assertNotEqual(first['title'], second['title'])


class ApiServiceTests(TestCase):
    @patch('stories.api_services.requests.get')
    def test_successful_api_response(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'content': 'Keep moving forward.', 'author': 'Maya'}
        result = __import__('stories.api_services', fromlist=['get_random_quote']).get_random_quote()
        self.assertEqual(result['quote'], 'Keep moving forward.')
        self.assertEqual(result['author'], 'Maya')

    @patch('stories.api_services.requests.get')
    def test_api_failure(self, mock_get):
        mock_get.side_effect = Exception('network down')
        result = __import__('stories.api_services', fromlist=['get_random_quote']).get_random_quote()
        self.assertEqual(result, {'quote': '', 'author': ''})


class StoryViewTests(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_generate_view(self):
        response = self.client.post(reverse('generate_story'), {
            'genre': 'Fantasy',
            'main_character': 'A young engineer',
            'location': 'A mysterious city',
            'theme': 'Friendship',
            'mood': 'Adventure',
            'story_length': 'Medium',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The')

    def test_story_detail_view(self):
        story = Story.objects.create(
            genre='Fantasy',
            main_character='A young engineer',
            location='A mysterious city',
            theme='Friendship',
            mood='Adventure',
            story_length='Medium',
            title='Hidden City',
            content='A story of courage and friendship.',
        )
        response = self.client.get(reverse('story_detail', args=[story.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hidden City')

    def test_story_history_view(self):
        Story.objects.create(
            genre='Fantasy',
            main_character='A young engineer',
            location='A mysterious city',
            theme='Friendship',
            mood='Adventure',
            story_length='Medium',
            title='Story One',
            content='One story.',
        )
        response = self.client.get(reverse('story_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Story One')

    def test_delete_story(self):
        story = Story.objects.create(
            genre='Fantasy',
            main_character='A young engineer',
            location='A mysterious city',
            theme='Friendship',
            mood='Adventure',
            story_length='Medium',
            title='Delete Me',
            content='Delete this story.',
        )
        response = self.client.post(reverse('story_delete', args=[story.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Story.objects.filter(pk=story.pk).exists())
