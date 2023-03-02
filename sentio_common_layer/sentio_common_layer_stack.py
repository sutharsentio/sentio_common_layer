from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_ssm as ssm,
    # aws_sqs as sqs,
)
from constructs import Construct

class SentioCommonLayerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, app_config, global_params, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app_name = global_params['appName']
        self.app_config = app_config
        env = self.app_config['env_name']

        # Define the layer code
        layer_code = _lambda.Code.from_asset("sentio_common_layer/sentio_layers")
        # Define the layer
        layer = _lambda.LayerVersion(
            self, "layer",
            code=layer_code,
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8, _lambda.Runtime.PYTHON_3_9],
        )

        #layer.add_permission("allow", _lambda.AccountPrincipal(_lambda.AccountPrincipal.AccountId), "lambda:GetLayerVersion")

        # Storing layer information on SSM, So that it can be used in another App's stack
        ssm.StringParameter(self, f"param-{app_name}-layer-{env}",
        type=ssm.ParameterType.STRING,
        tier=ssm.ParameterTier.STANDARD,
        parameter_name=f"{app_name}-layer-{env}",
        description=f"Common util code layer for {env} environment",
        string_value=layer.layer_version_arn)
