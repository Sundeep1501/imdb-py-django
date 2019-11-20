from django.urls import path
from .views import IndexView, QueryAView, QueryBView, QueryCView, QueryDView, QueryEView, QueryFView, QueryGView, QueryHView, QueryIView 

urlpatterns = [
	path('', IndexView.as_view(), name='index'),

	path('querya', QueryAView.as_view(), name='querya'),
	path('queryb', QueryBView.as_view(), name='querya'),
	path('queryc', QueryCView.as_view(), name='querya'),
	path('queryd', QueryDView.as_view(), name='querya'),
	path('querye', QueryEView.as_view(), name='querya'),
	path('queryf', QueryFView.as_view(), name='querya'),
	path('queryg', QueryGView.as_view(), name='querya'),
	path('queryh', QueryHView.as_view(), name='querya'),
	path('queryi', QueryIView.as_view(), name='querya'),
]
