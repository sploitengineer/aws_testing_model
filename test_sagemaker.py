import boto3, json

runtime = boto3.client("sagemaker-runtime", region_name="us-east-1")

response = runtime.invoke_endpoint(
    EndpointName="gemma-endpoint",
    ContentType="application/json",
    Body=json.dumps({
        "prompt": """PROMPT"""
    })
)

print(response["Body"].read().decode("utf-8"))
