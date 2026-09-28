from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .api_services import get_random_quote
from .forms import StoryForm
from .models import Story
from .services import TemplateStoryGenerator


def home(request):
    form = StoryForm(initial={
        'genre': 'Fantasy',
        'main_character': 'A young engineer',
        'location': 'A mysterious city',
        'theme': 'Friendship',
        'mood': 'Adventure',
        'story_length': 'Medium',
    })
    return render(request, 'stories/home.html', {'form': form})


def generate_story_view(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            generator = TemplateStoryGenerator()
            generated = generator.generate({
                'genre': data['genre'],
                'character': data['main_character'],
                'location': data['location'],
                'theme': data['theme'],
                'mood': data['mood'],
                'length': data['story_length'],
            })
            quote = get_random_quote()
            story = Story.objects.create(
                genre=data['genre'],
                main_character=data['main_character'],
                location=data['location'],
                theme=data['theme'],
                mood=data['mood'],
                story_length=data['story_length'],
                title=generated['title'],
                content=generated['story'],
                quote=quote.get('quote', ''),
                quote_author=quote.get('author', ''),
            )
            return render(request, 'stories/story_detail.html', {
                'story': story,
                'quote': quote,
                'show_quote': bool(quote.get('quote')),
            })
    else:
        form = StoryForm(initial={
            'genre': 'Fantasy',
            'main_character': 'A young engineer',
            'location': 'A mysterious city',
            'theme': 'Friendship',
            'mood': 'Adventure',
            'story_length': 'Medium',
        })
    return render(request, 'stories/generate.html', {'form': form})


def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    quote = {'quote': story.quote, 'author': story.quote_author} if story.quote else {'quote': '', 'author': ''}
    return render(request, 'stories/story_detail.html', {'story': story, 'quote': quote, 'show_quote': bool(story.quote)})


def regenerate_story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    generator = TemplateStoryGenerator()
    generated = generator.generate({
        'genre': story.genre,
        'character': story.main_character,
        'location': story.location,
        'theme': story.theme,
        'mood': story.mood,
        'length': story.story_length,
    })
    quote = get_random_quote()
    story.title = generated['title']
    story.content = generated['story']
    story.quote = quote.get('quote', '')
    story.quote_author = quote.get('author', '')
    story.save()
    return redirect('story_detail', pk=story.pk)


def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == 'POST':
        story.delete()
        messages.success(request, 'Story deleted successfully.')
        return redirect('story_history')
    return render(request, 'stories/delete_confirm.html', {'story': story})


def story_history(request):
    stories = Story.objects.all()
    return render(request, 'stories/history.html', {'stories': stories})


def about(request):
    return render(request, 'stories/about.html')
