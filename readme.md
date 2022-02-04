# STUDENT CRUD django project 

## Creating an API to the project

1. set up an app (create - register in settings)
3. setup a superuser
4. create a model to manage & migrate...
5. set up the django REST framework (and register in settings)
    - create serializable.py
    - create urls.py -> link to project urls.py
6. Serialize the model
    - import the model
    - import the serializer
    - link both in serializer group:

```python
   class __ModelName__Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = __ModelName__
        fields = ['_field1_', '_field2_', '...']
```
6. Set the required ViewSet
   - queryset => the query of the model
   - serializer_class => __ModelName__Serializer
7. Link the urls of the api to the project api
```python
from django.urls import path, include
from rest_framework import routers
from myapiapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# to register each model to a router => regex
router.register(r'path_name', views.__ModelName__ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

```
8. Check all settings are set properly and run the server :)


## Technologies used:
### Languages
- python
### Frameworks
- django
- REST (django REST)
## Tools
- pyCharm
- postman

## Testing
you can find testing screenshots in **testingShots** folder