from django.shortcuts import render
from .models import images
from django.http import JsonResponse
from .chat_bot import medical_chatbot

def index(request):
    im=images.objects.filter(name='avatar')
    h={'avatar':im}
    return render(request,'chatbot/index.html',h)

def reply(request):
    h={'hello':'hello what brings you here','how are you':'i am a good what about you if you are not feeling well please tell me your symptoms','i am not feeling well':'ok can you tell me more about your symptoms','your name':'my name is eva','good morning':'a very good morning please tell me about your symptoms','good afternoon':'a very good afternoon please tell me about your symptoms','good evening':'a very good evening please tell me about your symptoms','i am fine':'oh thats good to hear','thank you':'your welcome please let me know if something comes up','thanks':'your welcome please let me know if something comes up','dont haved any problem':'oh thats good to hear','no problem':'oh its good to hear'}
    if request.method == 'GET':
        query=request.GET.get('message')
        for i in h.keys():
            if i in query:
                bot_response=h[i]
                return JsonResponse({'message':bot_response})
        try:
            bot_response=medical_chatbot.chatbot_reply(query=query)
        except Exception:
            bot_response='Sorry but i am unable to understand what you are saying kindly mention your symptoms again.....'       
        return JsonResponse({'message':bot_response})
    else:
        return JsonResponse({'error':'invalid request meathod.'})


