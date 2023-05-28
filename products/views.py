import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .emails import send_confirm_mail


from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.views import APIView


#from rest_framework.response import Response
#from rest_framework.decorators import api_view

from .serializers import *




class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


logger = logging.getLogger(__name__)

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializers = Userserializers(data=data)
            if serializers.is_valid():
                print('ok')
                serializers.save()
                send_confirm_mail(serializers.data['email'])
                return Response({
                    'status': 200,
                    'message': 'ok',
                    'data': serializer.data,
                    
                })
                
            return Response({
                'status': 400,
                'message': 'wrong',
                'data': serializer.error,
                    
                
            })  
        except Exception as e:
            print(e)      
        
        
    



# @api_view(['POST'])
# def send_emails(request):
#     email_addresses = request.data.get('email_addresses', [])
#     email_subject = request.data.get('email_subject', '')
#     email_body = request.data.get('email_body', '')

#     if not email_addresses:
#         return Response({'message': 'No email addresses provided.'}, status=400)

#     try:
#         send_custom_mail(request, email_subject, email_body, email_addresses)
#         return Response({'message': 'Emails sent successfully.'}, status=200)
#     except Exception as e:
#         error_message = str(e)
#         logger.error(f"Error sending emails: {error_message}")
#         return Response({'message': 'An error occurred while sending emails.'}, status=500)



# @api_view(['POST'])
# def send_emails(request):
#     email_addresses = request.data.get('email_addresses', [])
#     email_subject = request.data.get('email_subject', '')
#     email_body = request.data.get('email_body', '')

#     if not email_addresses:
#         return Response({'message': 'No email addresses provided.'}, status=400)

#     try:
#         send_mail(
#             email_subject,
#             email_body,
#             settings.DEFAULT_FROM_EMAIL,
#             email_addresses,
#             fail_silently=False,
#         )
#     except Exception as e:
#         return Response({'message': str(e)}, status=500)

#     return Response({'message': 'Emails sent successfully.'}, status=200)