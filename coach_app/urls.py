from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.intro, name='intro'),  # Landing page
    path('', views.coach_login, name='coach_login'),
    path('login/', views.coach_login, name='coach_login'),
    path('register/', views.register_coach, name='register_coach'),
    path('logout/', views.coach_logout, name='coach_logout'),

    # App
    path('locations/<int:coach_id>/', views.select_location, name='select_location'),
    path('attendance/<int:location_id>/', views.attendance, name='attendance'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    # CRUD
    path('add_location/<int:coach_id>/', views.add_location, name='add_location'),
    path('edit_location/<int:location_id>/', views.edit_location, name='edit_location'),
    path('delete_location/<int:location_id>/', views.delete_location, name='delete_location'),
    path('add_student/<int:location_id>/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # Reports
    path('history/<int:location_id>/', views.attendance_history, name='attendance_history'),
    path('fees-pdf/<int:location_id>/', views.fees_pdf_report, name='fees_pdf_report'),
]