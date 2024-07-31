import nltk
from nltk.tokenize import word_tokenize
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

class ChatbotView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        user_message = request.POST.get('message')
        response = self.generate_response(user_message)
        return render(request, 'home.html', {'user_message': user_message, 'bot_response': response})

    def generate_response(self, message):
        # Example: Echo back the user's message with some modification
        if message.lower() == 'hello':
            return "Hello! How can I assist you today?"
        elif message.lower() == 'how are you?':
            return "I'm just a bot, but I'm here to help!"
        else:
            return f"Sorry, I didn't quite understand '{message}'. Could you rephrase?"

