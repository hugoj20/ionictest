from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
 
urlpatterns = [ 
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('address/', views.AddressList.as_view()),
    path('address/<int:pk>', views.AddressDetail.as_view()),
    path('email/verification/<token>', views.VerifyEmail.as_view(), name='email_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)