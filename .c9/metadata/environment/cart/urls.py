{"filter":false,"title":"urls.py","tooltip":"/cart/urls.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":1},"end":{"row":7,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"088683e10f32385107b83cf421c2135ce3d84560","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":6,"column":4},"end":{"row":6,"column":65},"action":"remove","lines":["url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),"],"id":2}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":54},"action":"remove","lines":[", adjust_cart"],"id":3}],[{"start":{"row":5,"column":62},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":65},"action":"insert","lines":["url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),"],"id":5}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[","],"id":6}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":[" "],"id":7},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["a"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["d"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["j"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["u"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["s"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["t"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["_"]},{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":["c"]},{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":["a"]}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["r"],"id":8},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["from django.conf.urls import url","from .views import view_cart, add_to_cart, adjust_cart","","urlpatterns = [","    url(r'^$', view_cart, name='view_cart'),","    url(r'^add/(?P<id>\\d+)', add_to_cart, name='add_to_cart'),","    url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),","    ","]"],"id":9},{"start":{"row":0,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["from django.conf.urls import url","from .views import view_cart, add_to_cart, adjust_cart","","urlpatterns = [","    url(r'^$', view_cart, name='view_cart'),","    url(r'^add/(?P<id>\\d+)', add_to_cart, name='add_to_cart'),","    url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),","]"]}]]},"timestamp":1585415440829}