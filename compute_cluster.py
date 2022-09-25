from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.compute import EC2Instance
from diagrams.aws.compute import EC2Instances
from diagrams.aws.compute import EC2Ami
from diagrams.aws.compute import LambdaFunction
with Diagram("Diagram", direction="TB"):
    with Cluster("Compute Cluster"):
        EC2 = EC2("EC2")
        EC2Instance = EC2Instance("EC2Instance")
        EC2Instances = EC2Instances("EC2Instances")
        EC2Ami = EC2Ami("EC2Ami")
        LambdaFunction = LambdaFunction("LambdaFunction")
