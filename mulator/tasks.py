

def delay_task(*args, **kwargs):
    mulator = kwargs.get('mulator', args[0])
    mulator.mulate()
    return True


def delay_hook(task):
    pass
#    instance = task.args[0]
#    instance.status_id = task.args[2]
#    instance.save()
