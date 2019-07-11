mongoengine Adapter for PyCasbin 
====

mongoengine Adapter is the [mongoengine](https://github.com/MongoEngine/mongoengine) adapter for [PyCasbin](https://github.com/zhangbailong945/mongodb_adapter). With this library, Casbin can load policy from mongoengine supported database or save policy to it.

Based on [Officially Supported Databases](https://github.com/MongoEngine/mongoengine), The current supported databases are:

- mongodb


## Installation

```
pip install casbin_mongoengine_adapter
```

## Simple Example

```python
import casbin_mongoengine_adapter
import casbin

adapter = Adapter(dbname='casbin_test', host='mongodb://localhost:27017')

e = casbin.Enforcer('path/to/model.conf', adapter, True)

sub = "alice"  # the user that wants to access a resource.
obj = "data1"  # the resource that is going to be accessed.
act = "read"  # the operation that the user performs on the resource.

if e.enforce(sub, obj, act):
    # permit alice to read data1casbin_mongoengine_adapter
    pass
else:
    # deny the request, show an error
    pass
```


### Getting Help

- [PyCasbin](https://github.com/casbin/pycasbin)

### License

This project is licensed under the [Apache 2.0 license](LICENSE).
