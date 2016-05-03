import time


# TODO: allow either serializer or instance, since view may not use serializer
class BaseMulator():

    def __init__(self, serializer):
        serializer.save()
        self.instance = serializer.instance


class DelayMulator(BaseMulator):

    def __init__(cls, serializer, delay):
        cls.delay = delay
        super(DelayMulator, cls).__init__(serializer)

    def mulate(self):
        self.pre_mulate(self.instance)
        time.sleep(self.delay)
        self.post_mulate(self.instance)
