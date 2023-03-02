#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sentio_common_layer.sentio_common_layer_stack import SentioCommonLayerStack

def init_config():
    environment_id = app.node.try_get_context(key='config')
    # We could have made it code branch specific too. By fetching git branch in code.
    if not environment_id:
        raise LookupError("Context variable missing on CDK Command. Please pass valid config. Pass as '-c config=dev'")
    environments = app.node.try_get_context(key='environments')
    global_params = app.node.try_get_context(key='globals')
    app_config = environments[environment_id]
    return app_config, global_params

app = cdk.App()
# Fetching context params as config
app_config, global_params = init_config()

SentioCommonLayerStack(app, "SentioCommonLayerStack",
    env=cdk.Environment(account=app_config['accountNumber'], region=app_config['region']),
    app_config=app_config,
    global_params=global_params,
    )

app.synth()
