from django.shortcuts import render, redirect
from .models import User, Payment, Order
from .forms import FormulariPagament

def main(request):
    return render(request, 'main.html')

def login(request):
    if 'user_id' in request.session:
        return redirect('main')

    error_message = ""

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)

            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('main')  
            else:
                error_message = 'Contraseña incorrecta'

        except User.DoesNotExist:
            error_message = 'No existeix el usuari'

    return render(request, 'login.html' , {'error_message': error_message})

def logout(request):
    request.session.flush()
    return redirect('login')

def payment(request, order_id):
    if 'user_id' not in request.session:
        return redirect('login')

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return redirect('main')

    user_id = request.session.get('user_id')
    if order.user.id != user_id:
        return redirect('main')
    
    if order.status == 'pagat':
        return redirect('main')

    error_message = None

    if request.method == 'POST':
        form = FormulariPagament(request.POST)
        if form.is_valid():
            card_number = request.POST['card_number']
            cvc = request.POST['cvc']
            expiration_date = request.POST['expiration_date']

            if len(card_number) != 16 or len(cvc) != 3:
                error_message = 'Datos incorrectos'

            if not error_message:
                payment_exists = Payment.objects.filter(card_number=card_number).exists()

                if payment_exists:
                    order.status = 'pagat' 
                    order.save() 

                    return redirect('main')
                else:
                    payment = Payment(
                        card_number=card_number,
                        cvc=cvc,
                        expiration_date=expiration_date
                    )

                    payment.save()
                    
                    order.status = 'pagat'
                    order.save()  

                    return redirect('main')

        else:
            error_message = 'Datos incorrectos'
    
    form = FormulariPagament()

    return render(request, 'payment.html', {'form': form, 'error_message': error_message, 'order': order})
