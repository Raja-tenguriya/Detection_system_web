from django.urls import path
from . import views
from .views import upload_and_blur_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('run-mask/', views.run_mask_detection, name='run_mask'), 
    path('change_col/', views.run_change_col, name='change_col'),  
    path('upload_blur/', views.upload_and_blur_image, name='upload_and_blur'),
    path('upload_color/', views.upload_and_color_image, name='upload_and_color'),
    path('upload_gray/', views.upload_and_gray_image, name='upload_and_gray'),
    path('choose_filter/', views.choose_filter, name='choose_filter'),
    path('productpage/', views.product_page, name='product_pg'), 
    path('carrierpage/', views.carrier_page, name='carrier_pg'),
    path('notespage/', views.notes_page, name='notes_pg'), 
    path('supportpage/', views.support_page, name='support_pg'), 
    path('aboutuspage/', views.aboutus_page, name='aboutus_pg'), 
    path('feedbackpage/', views.feedback_page, name='feedback_pg'), 
    path('accountspage/', views.accounts_page, name='accounts_pg'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)