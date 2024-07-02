from .cart import Cart

# lets create context processor so our cart can work on all pages of the site

def cart(request):
    return {'cart': Cart(request)}