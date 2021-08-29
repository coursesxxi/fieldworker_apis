from django.urls import path,include
from . import views

# serialize
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'fieldworker', views.FieldworkerViewSet)

urlpatterns = [
    path('', views.fieldworker_form,name='fieldworker_insert'), # get and post req. for insert operation
    path('<int:id>/', views.fieldworker_form,name='fieldworker_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.fieldworker_delete,name='fieldworker_delete'),
    path('list/',views.fieldworker_list,name='fieldworker_list'), # get req. to retrieve and display all records

    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='fieldworker')),
	]
