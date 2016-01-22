# -*- coding: utf-8 -*-
#!/usr/bin/env python
from suds.client import Client
url='http://api.trkd.thomsonreuters.com/schemas/wsdl/TokenManagement/TokenManagement_1_HttpsAndAnonymous.wsdl'
client=Client(url)
#myheaders = dict(=, , )
#client.set_options(soapheaders=myheaders)

#print client

param = dict(ApplicationID='trkddemoappwm', Username='trkd-demo-wm@thomsonreuters.com', Password='t7c9k32db')
result = client.service.CreateServiceToken_1(params)
print result
