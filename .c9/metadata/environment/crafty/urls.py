{"filter":false,"title":"urls.py","tooltip":"/crafty/urls.py","ace":{"folds":[],"scrolltop":110.1875,"scrollleft":0,"selection":{"start":{"row":38,"column":0},"end":{"row":38,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":34,"state":"start","mode":"ace/mode/python"}},"hash":"1929dc0659eabd71460935812794a23530bfc0f5","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":15,"column":0},"end":{"row":37,"column":1},"action":"remove","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from accounts.views import index","from products import urls as urls_products","from find import urls as urls_find","from products.views import get_products, sell_product","from checkout import urls as urls_checkout","from cart import urls as urls_cart","from django.views import static","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', index, name=\"index\"),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^find/', include(urls_find)),","    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),","  ","]"],"id":2},{"start":{"row":15,"column":0},"end":{"row":26,"column":14},"action":"insert","lines":["{% extends \"base.html\" %}","","<h3> Sell</h3>","{% block content %}","<h3> Sell</h3>","","<form method=\"POST\">","    {{ sell_form  }}","    <button type=\"submit\">Sell</button>","</form>","","{% endblock %}"]}]]},"timestamp":1585134135806}