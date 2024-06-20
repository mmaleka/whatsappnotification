# todo/todo_api/views.py
from rest_framework.views import APIView
from django.http import JsonResponse
from sendwhatsapp.models import WhatsAppNotification
from .serializers import WhatsAppNotificationSerializer
from rest_framework.response import Response
from rest_framework import status
# Importing the Required Library
import pywhatkit
import pyautogui
import keyboard as k
import time


class SendWhatsappAPIView(APIView):

    lookup_field = 'id'
    serializer_class = WhatsAppNotificationSerializer

    def sendmessage(self, msg):

        # Defining the Phone Number and Message
        phone_number = "+27716431040"


        # Sending the WhatsApp Message
        pywhatkit.sendwhatmsg_instantly(phone_number, msg, 8, 38)
        # pywhatkit.sendwhatmsg(phone_number, "hello", 13, 12, 32)
        pyautogui.click(1050, 950)
        time.sleep(2)
        k.press_and_release('enter')
 
        # Displaying a Success Message
        print("WhatsApp message sent!")
        



        return True
    

    # 1. List all

    def get(self, request, *args, **kwargs):
        '''

        List all the todo items for given requested user
        '''
        todos = WhatsAppNotification.objects.all()
        serializer = WhatsAppNotificationSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    # 2. Create
    def post(self, request, *args, **kwargs):



        '''
        Send a whatsapp notification
        '''
        self.sendmessage(request.data.get('task'))


        '''
        Now update the database:
        if message sent successfully, completed is true else completed is false
        '''
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = WhatsAppNotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
