from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cliente

@csrf_exempt  # Desabilitar CSRF para fins de teste (não recomendado em produção).
def receber_dados(request):
    if request.method == 'POST':
        try:
            # Decodifica o JSON recebido
            data = json.loads(request.body)
            
            # Cria e salva um novo Cliente
            cliente = Cliente(
                nome=data['name'],
                email=data['email'],
                telefone=data['telefone'],
                empresa=data['empresa'],
                senha=data['password']  # Apenas salva a senha hashada como veio.
            )
            cliente.save()
            
            return JsonResponse({'status': 'success', 'message': 'Cliente salvo com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)
