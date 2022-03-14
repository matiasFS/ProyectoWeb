from .cart import Cart


def total_amount_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + ((float(value["price"]))*value["quantity"])
    return {"total_amount_cart": total}
