from troposphere import Ref, Template, Parameter, Output
from troposphere.ec2 import SecurityGroup
import troposphere.ec2 as ec2
template = Template()

keyname_param = template.add_parameter(Parameter(
	"KeyName",
	Description="EC2 Keypair",
	Type="String",
))
securityGroup_param = template.add_parameter(Parameter(
	"SecurityGroup",
	Description="Security Group ID",
	Type="String"
))
ec2_instance = template.add_resource(Instance(
	'JordansInstance',
	ImageId = 'ami-ebed508f',
	InstanceType = 't2.micro',
	KeyName = Ref(keyname_param),
	
))
template.add_output([
	Output(
		"InstanceId",
		Description="InstanceID of EC2 instance",
		Value=Ref(ec2_instance)
)])
print(template.to_json())