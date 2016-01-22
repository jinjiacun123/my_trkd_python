# -*- coding: utf-8 -*-
#!/usr/bin/env python
from suds.plugin import MessagePlugin

class MyPlugin(MessagePlugin):
    def marshalled(self, context):
        body = context.envelope.getChild('Body')
        params = body.getChild('fix_this_path').getChild('Param')
        foo = params[0]
        foo.set('name','name1')

client = Client(url, plugins=[MyPlugin()])
params =client.factory.create("Payment.Params")
params.param = "val1"