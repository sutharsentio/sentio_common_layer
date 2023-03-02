import aws_cdk as core
import aws_cdk.assertions as assertions

from sentio_common_layer.sentio_common_layer_stack import SentioCommonLayerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sentio_common_layer/sentio_common_layer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SentioCommonLayerStack(app, "sentio-common-layer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
