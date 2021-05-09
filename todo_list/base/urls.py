from django.urls import path
from .views import CustomLoginView, RegistrationPage, TaskCreate, TaskList


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('register/', RegistrationPage.as_view(), name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('', TaskList.as_view(), name='tasks'),
]