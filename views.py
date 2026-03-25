from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get("num1", 0))
            num2 = float(request.POST.get("num2", 0))
            op = request.POST.get("operation")

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            elif op == '^':
                result = num1 ** num2
            elif op == '%':
                result = (num1 * num2) / 100  # percentage calculation
        except:
            result = "Error"

    return render(request, "calculator.html", {"result": result})