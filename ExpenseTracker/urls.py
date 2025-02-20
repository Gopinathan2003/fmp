from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expense', views.ExpenseListView.as_view(), name='expenses'),
    path('expense/login', views.login, name='login'),
    path('account/register', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls'))
]