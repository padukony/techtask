# techtask

Technical Challenge:

Task1: Design of 3 tier environment:
a) This 3 tier environment architecture is based on AWS cloud services
b) Create separate VPC (Virtual Private Cloud) to isolate all the resources belong to the application.
c) Create 3 private subnets to keep web,application and DB instances/VMs/services.
d) Create 1 public subnet to for Bastion host(used to ssh to all hosts which are in private subnet) & NAT Gateway for all private instances to 
communicate to Internet for patch upgrade etc.
e) Create EC2 (Elastic Cloud Computing) Instances for Web and application tier under Auto Scaling group.
f) Create RDS for DB Tier and with Multi Availabitlity Zone configuration for High Availability.
g) Configure Route53 DNS service with domain name of the web application and point to Static IP address (Elastic IP) of Elastic Load Balancer(ELB).
h) Configure Elastic Load Balancer between Web and Application tier to support scalability of Application tier.


Task2:


Task3:
