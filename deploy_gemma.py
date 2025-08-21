import boto3

region = "us-east-1"  
sagemaker = boto3.client("sagemaker", region_name=region)

# 1. Create Model
sagemaker.create_model(
    ModelName="gemma-model",
    PrimaryContainer={
        "Image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/huggingface-pytorch-inference:1.12.1-transformers4.26-gpu-py39-cu116-ubuntu20.04",  ##for  us reagion
        "ModelDataUrl": "s3://gemma-model-bucket/gemma-model.tar.gz"  ##tesgt
    },
    ExecutionRoleArn="arn:aws:iam::<your-account-id>:role/service-role/AmazonSageMaker-ExecutionRole"  ##test
)

# 2. Create Endpoint Config
sagemaker.create_endpoint_config(
    EndpointConfigName="gemma-config",
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": "gemma-model",
        "InitialInstanceCount": 1,
        "InstanceType": "ml.c5.xlarge"
    }]
)

# 3. Create Endpoint
sagemaker.create_endpoint(
    EndpointName="gemma-endpoint",
    EndpointConfigName="gemma-config"
)
