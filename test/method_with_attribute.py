# -*- coding: utf-8 -*-
#!/usr/bin/env python
from suds.sax.attribute import Attribute
from suds.plugin import MessagePlugin
from suds.client import Client

class _AttributePlugin(MessagePlugin):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def marshalled(self, context):
        method = context.envelope.getChild('Body')[0]
        for key, item in self.kwargs.items():
            method.attributes.append(Attribute(key, item))

#方法属性
url = ''
client = Client(url)
client.options.plugins = [_AttributePlugin(foo='bar')]
response = client.service.method1()
client.options.plugins = []
response = client.service.method2()
