[![](https://img.shields.io/badge/released-2021.6.17-green.svg?longCache=True)](https://pypi.org/project/django-command-disable/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-command-disable
```

### How it works
+   multiple implementations:
    +   `DisableCommand` management command class
    +   `@command_disable` decorator
+   admin interface

#### `settings.py`
```python
INSTALLED_APPS+=['django_command_disable']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Examples
`BaseCommand`
```python
from django_command_disable.management.base import DisableCommand

class Command(DisableCommand):
    def handle(self,*args,**options):
        # your code
```

`@command_disable`
```python
from django_command_disable.decorators import command_disable

class Command(BaseCommand):
    @command_disable
    def handle(self,*args,**kwargs):
        ...
```
```python
class BaseCommand(BaseCommand):
    def execute(self,*args,**kwargs):
        return command_disable(self.handle)(self,*args,**kwargs)
```

`call_command`
```python
from django.core.management import call_command

command_disable(call_command)(name,*args,**options)
```

