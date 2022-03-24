# techtask

Technical Challenge:

Task1: Design of 3 tier environment:
- This 3 tier environment architecture is based on AWS cloud services
- Create separate VPC (Virtual Private Cloud) to isolate all the resources belong to the application.
- Create 3 private subnets to keep web,application and DB instances/VMs/services.
- Create 1 public subnet to for Bastion host(used to ssh to all hosts which are in private subnet) & NAT Gateway for all private instances to 
communicate to Internet for patch upgrade etc.
- Create EC2 (Elastic Cloud Computing) Instances for Web and application tier under Auto Scaling group.
- Create RDS for DB Tier and with Multi Availabitlity Zone configuration for High Availability.
- Configure Route53 DNS service with domain name of the web application and point to Static IP address (Elastic IP) of Elastic Load Balancer(ELB).
- Configure Elastic Load Balancer between Web and Application tier to support scalability of Application tier.


Task2:


Task3:
