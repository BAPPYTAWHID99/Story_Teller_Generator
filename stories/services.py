import random
from typing import Dict

from .story_data import GENRE_DATA, LENGTH_CONFIG


class StoryGenerator:
    def generate(self, parameters):
        raise NotImplementedError


class TemplateStoryGenerator(StoryGenerator):
    def generate(self, parameters):
        return generate_story(
            parameters['genre'],
            parameters['character'],
            parameters['location'],
            parameters['theme'],
            parameters['mood'],
            parameters['length'],
        )


def _build_title(genre, character, location, theme):
    title_prefixes = [
        f'{character.title()} of the',
        f'The {theme.title()} of',
        f'Whispers in',
        f'Beyond the',
        f'Secrets of',
        f'The Last',
    ]
    location_name = location.strip()
    suffixes = ['City', 'Vale', 'Gate', 'Night', 'Harbor', 'Tower', 'Light', 'Echo']
    if location_name.lower().endswith('city'):
        suffix = 'City'
    elif location_name.lower().endswith('tower'):
        suffix = 'Tower'
    elif location_name.lower().endswith('harbor'):
        suffix = 'Harbor'
    else:
        suffix = random.choice(suffixes)

    base = random.choice(title_prefixes)
    if base.startswith('The '):
        candidate = f'{base} {location_name} {suffix}'
    elif base.startswith('Whispers in'):
        candidate = f'{base} {location_name}'
    else:
        candidate = f'{base} {location_name}'

    candidate = candidate.replace('  ', ' ').strip()
    if candidate.endswith(' '):
        candidate = candidate.rstrip()
    if len(candidate) < 12:
        candidate = f'{candidate} {suffix}'
    return candidate


def _get_story_intro(genre, character, location, mood, theme):
    mood_style = {
        'Adventure': 'The path ahead glittered with danger and possibility, and every step felt like a promise waiting to be tested.',
        'Funny': 'The morning began with a disaster so ridiculous that even the pigeons seemed to be laughing.',
        'Dark': 'The city held its breath beneath a moon that never quite reached the streets.',
        'Emotional': 'Every heart in the place seemed to carry a story no one had spoken aloud.',
        'Inspirational': 'Hope arrived quietly, as if the world had been waiting for one brave act to begin again.',
        'Mysterious': 'Something beneath the fog did not want to be identified, and that was enough to frighten everyone.',
        'Romantic': 'It was the kind of evening when even the wind seemed to notice two hearts circling one another.',
        'Suspenseful': 'The silence felt wrong, and every shadow seemed to be listening.',
        'Hopeful': 'Even the bleakest corner of the city seemed to brighten as a new possibility appeared.',
    }
    data = GENRE_DATA.get(genre, GENRE_DATA['Fantasy'])
    setting = random.choice(data['settings'])
    sentence = (
        f'In {setting}, where the air carried both wonder and warning, {character} arrived with a purpose no one could yet name. '
        f'{mood_style.get(mood, mood_style["Adventure"])} '
    )
    return sentence


def _get_character_role(character, theme):
    roles = [
        f'As someone who understood systems and signals, {character} noticed the hidden pattern beneath the surface before anyone else did.',
        f'{character} had spent years learning to solve problems with patience, and that skill became the key to the crisis.',
        f'Though {character} seemed ordinary at first glance, practical intelligence and quiet courage made the difference when the city faced its greatest test.',
        f'{character} learned that the truest expression of {theme.lower()} was not speech but action, and the city seemed to understand that too.',
    ]
    return random.choice(roles)


def _generate_paragraphs(genre, character, location, theme, mood, length):
    data = GENRE_DATA.get(genre, GENRE_DATA['Fantasy'])
    conflict = random.choice(data['conflicts'])
    event = random.choice(data['events'])
    ending = random.choice(data['endings'])
    theme_title = theme.strip() or 'Friendship'
    if theme_title.lower() == 'friendship':
        theme_drive = (
            'The bond between unlikely allies grew stronger with every obstacle, proving that trust could be a more reliable force than fear.'
        )
    elif theme_title.lower() == 'courage':
        theme_drive = 'Courage was not the absence of fear, but the choice to move forward while it was still present.'
    elif theme_title.lower() == 'hope':
        theme_drive = 'Hope became a practical force, reshaping what the people believed was possible.'
    elif theme_title.lower() == 'love':
        theme_drive = 'Love gave each difficult choice a human cost and a better reason to hold on.'
    else:
        theme_drive = f'The idea of {theme_title.lower()} changed the meaning of every decision made that day.'

    paragraphs = [
        _get_story_intro(genre, character, location, mood, theme),
        f'{_get_character_role(character, theme)} {location} itself seemed to respond, its streets, bridges, and towers shifting into a living map of secrets. {theme_drive}',
        f'When {conflict}, {event}. {character} realized that solving the problem meant understanding more than mechanics or prophecy; it meant learning who the people around them were and what they were willing to protect, especially in the name of {theme_title}.',
        f'At the height of the crisis, the city became a test of loyalty and invention. Each decision carried consequences, and each person was forced to choose whether to protect themselves or stand beside someone else. The tension grew until the stakes were impossible to ignore, and the lesson of {theme_title} became impossible to deny.',
        f'In the decisive moment, {character} used knowledge, courage, and the deep friendships formed along the way to confront the truth. The final struggle was neither simple nor clean, but it was honest, and it changed the heart of {location}.',
        f'By the end, {ending}. The story of {location} was no longer just a place of danger and rumor, but a place where the enduring power of {theme_title.lower()} had changed everyone who remained.'
    ]

    story = ' '.join(paragraphs)
    if length == 'Short':
        target = 320
    elif length == 'Long':
        target = 1050
    else:
        target = 600
    words = story.split()
    if len(words) < target:
        filler = (
            ' They retraced the route by lantern light, shared food and stories, and discovered that even the most difficult places could become kinder when people decided to stand together. '
            'The final chapter felt earned rather than dramatic, as if the city itself had been waiting to breathe again. '
            'No one left unchanged, and no one forgot what had been built in the aftermath of fear.'
        )
        while len(story.split()) < target:
            story += filler
    else:
        story = ' '.join(words[:target])
    return story.strip()


def generate_story(genre, character, location, theme, mood, length):
    character = (character or 'A determined traveler').strip() or 'A determined traveler'
    location = (location or 'a forgotten valley').strip() or 'a forgotten valley'
    theme = (theme or 'Friendship').strip() or 'Friendship'
    genre = genre or 'Fantasy'
    mood = mood or 'Adventure'
    length = length or 'Medium'

    story_text = _generate_paragraphs(genre, character, location, theme, mood, length)
    title = _build_title(genre, character, location, theme)

    return {
        'title': title,
        'story': story_text,
        'genre': genre,
        'character': character,
        'location': location,
        'theme': theme,
        'mood': mood,
    }
