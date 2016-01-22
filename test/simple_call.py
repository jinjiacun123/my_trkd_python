# -*- coding: utf-8 -*-
#!/usr/bin/env python
from suds.client import Client
url='http://192.168.1.248:86/LightService.svc?wsdl'
client=Client(url)
result = client.service.Get(1)
print result