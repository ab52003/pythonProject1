import inspect

def introspection_info(obj):
    l = {}
    l.update({'type': type(obj)})
    l.update({'attributes and methods': dir(obj)})
    l.update({'module': inspect.getmodule(obj)})
    return l


number_info = introspection_info('42')

print(number_info)