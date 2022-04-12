from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get("name")
            lastName = request.POST.get("lastName")
            email = request.POST.get("email")
            content = request.POST.get("content")

            try:
                send_mail(
                    'Prueba app django',
                    'El usuario {} {}, escribe lo siguiente:\n\n {}'.format(name,lastName,content),
                    '{}'.format(email),
                    [''],
                    fail_silently=False,
                )
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?invalid")

    return render(request, "contact/contact.html", {"contactForm": contactForm})
