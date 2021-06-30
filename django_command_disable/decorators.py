from .models import Command
from .utils import getinstance

def command_disable(f):
    def wrapper(command,*args,**options):
        instance = getinstance(command)
        module_name = type(instance).__module__
        try:
            app, name = module_name.split('.')[-4], module_name.split('.')[-1]
        except IndexError:
            raise ValueError('invalid module name - %s' % module_name)
        command, created = Command.objects.get_or_create({'app':app},name=name)
        if command.app!=app:
            Command.objects.filter(name=name).update(app=app)
        if command.is_enabled:
            return f(instance,*args, **options)
    return wrapper if f else None
