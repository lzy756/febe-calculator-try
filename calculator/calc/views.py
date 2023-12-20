from django.http import JsonResponse

def calculate(request):
    operation = request.GET.get('operation')
    x = float(request.GET.get('x', 0))
    y = float(request.GET.get('y', 0))

    result = 0
    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        result = x / y

    return JsonResponse({'result': result})
