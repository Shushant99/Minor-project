from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('start/<int:classroom_id>/', views.start_attendance, name='start_attendance'),
    path('session/<int:session_id>/', views.take_attendance, name='take_attendance'),
    path('session/<int:session_id>/video/', views.video_feed, name='video_feed'),
    path('session/<int:session_id>/end/', views.end_attendance, name='end_attendance'),
    path('session/<int:session_id>/detail/', views.attendance_detail, name='attendance_detail'),
    path('record/<int:record_id>/update/', views.update_record_status, name='update_record_status'),
    path('session/<int:session_id>/status/', views.session_status, name='session_status'),
    path('reports/', views.session_report_list, name='session_report_list'),
    path('reports/<int:session_id>/', views.session_report_detail, name='session_report_detail'),

]
