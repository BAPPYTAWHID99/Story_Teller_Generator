document.addEventListener('DOMContentLoaded', function () {
    const storyForm = document.getElementById('story-form');
    if (storyForm) {
        const button = storyForm.querySelector('.generate-btn');
        const text = button?.querySelector('.button-text');

        storyForm.addEventListener('submit', function () {
            if (button && text) {
                text.textContent = '✨ Creating your story...';
                button.disabled = true;
                button.style.opacity = '0.85';
                button.style.cursor = 'wait';
            }
        });
    }
});
