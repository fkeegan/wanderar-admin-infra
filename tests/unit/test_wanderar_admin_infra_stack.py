import aws_cdk as core
import aws_cdk.assertions as assertions

from wanderar_admin_infra.wanderar_admin_infra_stack import WanderarAdminInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in wanderar_admin_infra/wanderar_admin_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WanderarAdminInfraStack(app, "wanderar-admin-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
