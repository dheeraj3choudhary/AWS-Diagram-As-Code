# Author :- Dheeraj Choudhary
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Diagram", show= True, direction="TB"):
    ELB("Load_Balancer") >> EC2("Instance") >> RDS("Database")
