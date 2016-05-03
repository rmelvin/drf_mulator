from functools import wraps

from django.conf import settings
from django_q.tasks import Async


def mulator_delay(delay=0, **kwargs):
    mulator_class = kwargs.get('mulator_class')

    def mulator_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if settings.MULATOR_DELAY_ENABLED:
                serializer = args[1]
                mulator = mulator_class(serializer, delay)

                Async('mulator.tasks.delay_task', mulator,
                      q_options={
                          'hook': 'mulator.tasks.delay_hook',
                      }).run()
            else:
                func(*args, **kwargs)
        return wrapper
    return mulator_decorator
