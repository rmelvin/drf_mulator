# drf_mulator

#### In your api views.py,
##### Define imports
```
from drf_mulator.decorators import mulator_delay
from drf_mulator.mulators import DelayMulator
```
##### Subclass the mulator class DelayMulator and define these funcs
```
class ProductCreateMulator(DelayMulator):

    def pre_mulate(self, instance):
        instance.status_id = Product.SETUP_PENDING
        instance.save()
        return True

    def post_mulate(self, instance):
        instance.status_id = Product.ACTIVE
        instance.save()
        return True
```

##### Attach decorator to a viewset view
```
class ProductViewSet(viewsets.ModelViewSet):

    @mulator_delay(10, mulator_class=ProductCreateMulator)
    def perform_create(self, serializer):

```

#### In your settings.py, add the following setting to turn on the feature:
```
MULATOR_DELAY_ENABLED = True
```

##### Until this package gets added to pypi, add the following to your app's requirements.txt to install this package into your env:
```
git+https://github.com/rmelvin/drf_mulator#egg=drf-mulator
```
