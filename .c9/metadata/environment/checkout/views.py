{"filter":false,"title":"views.py","tooltip":"/checkout/views.py","ace":{"folds":[],"scrolltop":360,"scrollleft":0,"selection":{"start":{"row":58,"column":145},"end":{"row":58,"column":145},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"hash":"eb12c7f3fbaf7b5980190a073177d081adee2bb7","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":26,"column":27},"end":{"row":26,"column":28},"action":"remove","lines":["y"],"id":2},{"start":{"row":26,"column":26},"end":{"row":26,"column":27},"action":"remove","lines":["t"]},{"start":{"row":26,"column":25},"end":{"row":26,"column":26},"action":"remove","lines":["i"]},{"start":{"row":26,"column":24},"end":{"row":26,"column":25},"action":"remove","lines":["t"]},{"start":{"row":26,"column":23},"end":{"row":26,"column":24},"action":"remove","lines":["n"]},{"start":{"row":26,"column":22},"end":{"row":26,"column":23},"action":"remove","lines":["a"]},{"start":{"row":26,"column":21},"end":{"row":26,"column":22},"action":"remove","lines":["u"]},{"start":{"row":26,"column":20},"end":{"row":26,"column":21},"action":"remove","lines":["q"]},{"start":{"row":26,"column":19},"end":{"row":26,"column":20},"action":"remove","lines":[" "]},{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"remove","lines":[","]}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"remove","lines":["+"],"id":3}],[{"start":{"row":28,"column":22},"end":{"row":28,"column":23},"action":"insert","lines":["="],"id":4}],[{"start":{"row":28,"column":25},"end":{"row":28,"column":35},"action":"remove","lines":["quantity *"],"id":5},{"start":{"row":28,"column":24},"end":{"row":28,"column":25},"action":"remove","lines":[" "]}],[{"start":{"row":32,"column":20},"end":{"row":32,"column":39},"action":"remove","lines":["quantity = quantity"],"id":6},{"start":{"row":32,"column":16},"end":{"row":32,"column":20},"action":"remove","lines":["    "]},{"start":{"row":32,"column":12},"end":{"row":32,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":32,"column":8},"end":{"row":32,"column":12},"action":"remove","lines":["    "],"id":7},{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":38},"end":{"row":32,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"remove","lines":["}"],"id":8},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"remove","lines":["{"]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"remove","lines":[" "]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"remove","lines":[","]}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":[","],"id":9}],[{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":[" "],"id":10}],[{"start":{"row":24,"column":47},"end":{"row":24,"column":49},"action":"insert","lines":["{}"],"id":11}],[{"start":{"row":24,"column":48},"end":{"row":24,"column":49},"action":"remove","lines":["}"],"id":12},{"start":{"row":24,"column":47},"end":{"row":24,"column":48},"action":"remove","lines":["{"]},{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"remove","lines":[" "]},{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"remove","lines":[","]}],[{"start":{"row":24,"column":45},"end":{"row":24,"column":46},"action":"insert","lines":[","],"id":13}],[{"start":{"row":24,"column":46},"end":{"row":24,"column":47},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":24,"column":47},"end":{"row":24,"column":49},"action":"insert","lines":["{}"],"id":15}],[{"start":{"row":13,"column":0},"end":{"row":58,"column":145},"action":"remove","lines":["@login_required()","def checkout(request):","    if request.method==\"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","        ","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save","            ","            cart = request.session.get('cart', {})","            total = 0","            for id in cart.items():","                product = get_object_or_404(Product, pk=id)","                total == product.price","                order_line_item = OrderLineItem(","                    order= order,","                    product = product,)","                order_line_item.save()","                ","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('allproducts'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"],"id":16},{"start":{"row":13,"column":0},"end":{"row":58,"column":145},"action":"insert","lines":["def checkout(request):","    if request.method==\"POST\":","        order_form = OrderForm(request.POST)","        payment_form = MakePaymentForm(request.POST)","        ","        if order_form.is_valid() and payment_form.is_valid():","            order = order_form.save(commit=False)","            order.date = timezone.now()","            order.save","            ","            cart = request.session.get('cart', {})","            total = 0","            for id, quantity in cart.items():","                product = get_object_or_404(Product, pk=id)","                total += quantity * product.price","                order_line_item = OrderLineItem(","                    order= order,","                    product = product,","                    quantity = quantity)","                order_line_item.save()","                ","            ","            try:","                customer = stripe.Charge.create(","                    amount=int(total * 100),","                    currency=\"EUR\",","                    description=request.user.email,","                    card=payment_form.cleaned_data['stripe_id']","                )","            except stripe.error.CardError:","                messages.error(request, \"Your card was declined!\")","            ","            if customer.paid:","                messages.error(request, \"You have successfully paid\")","                request.session['cart'] = {}","                return redirect(reverse('allproducts'))","            else:","                messages.error(request, \"Unable to take payment\")","        else:","            print(payment_form.errors)","            messages.error(request, \"We were unable to take a payment with that card!\")","    else:","        payment_form = MakePaymentForm()","        order_form = OrderForm()","    ","    return render(request, \"checkout.html\", {\"order_form\": order_form, \"payment_form\": payment_form, \"publishable\": settings.STRIPE_PUBLISHABLE})"]}]]},"timestamp":1585413937776}