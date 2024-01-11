<!-- Start SDK Example Usage [usage] -->
```python
import example
from example.models import shared

s = example.Example()

req = shared.Pet(
    id=596804,
    name='string',
)

res = s.pets.create_pets(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->