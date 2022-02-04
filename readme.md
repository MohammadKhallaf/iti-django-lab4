# API

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

7.Set the required ViewSet
   - queryset => the query of the model
   - serializer_class => __ModelName__Serializer
8.