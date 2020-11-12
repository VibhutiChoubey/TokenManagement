from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from apis.models import Token, Client
import uuid, random


@require_http_methods(["GET"])
def generate_token(request):
    key = uuid.uuid4()
    token = Token.objects.create(key=key)
    return JsonResponse({'message': 'Generated successfully!'})


@require_http_methods(["POST"])
@csrf_exempt
def assign_token(request):
    post_data = request.POST
    email = post_data.get('email')
    password = post_data.get('password')
    client, created = Client.objects.get_or_create(email=email, password=password)
    client_token_qs = Token.objects.filter(user=client)
    if not created and client_token_qs:
        return JsonResponse({'token': client_token_qs[0].key}, status=200)

    token_qs = Token.objects.filter(status='AVAILABLE')
    if token_qs:
        token = random.choice(token_qs)
        token.user = client
        token.status = 'BLOCKED'
        token.save()
        return JsonResponse({'token': token.key}, status=200)
    else:
        return JsonResponse({'message': 'Not found'}, status=404)


@require_http_methods(["PUT"])
@csrf_exempt
def unblock_token(request, token):
    try:
        token = Token.objects.get(key=token)
    except Exception:
        return JsonResponse({'message': 'Invalid token'}, status=404)

    try:
        token.user = None
        token.status = 'AVAILABLE'
        token.save()
        return JsonResponse({'message': 'Unblocked'}, status=200)
    except Exception as e:
        return JsonResponse({'message': f'There was some error - {e}'}, status=500)


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_token(request, token):
    try:
        token = Token.objects.get(key=token)
    except Exception:
        return JsonResponse({'message': 'Invalid token'}, status=404)

    try:
        token.delete()
        return JsonResponse({'message': 'Deleted'})
    except Exception as e:
        return JsonResponse({'message': f'There was some error - {e}'}, status=500)


@require_http_methods(["PUT"])
@csrf_exempt
def keep_alive_token(request, token):
    try:
        token = Token.objects.get(key=token)
    except Exception:
        return JsonResponse({'message': 'Invalid token'}, status=404)

    try:
        token.save()
        return JsonResponse({'message': 'Updated'})
    except Exception as e:
        return JsonResponse({'message': f'There was some error - {e}'}, status=500)
