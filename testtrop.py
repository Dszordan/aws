from troposphere import Ref, Template, Parameter, Output
import troposphere.ec2 as ec2
template = Template()
instance = ec2.Instance('JordansInstance')
instance.ImageId = "ami-ebed508f"
instance.InstanceType = "t2.micro"

keyname_param = template.add_parameter(Parameter(
	"KeyName",
	Description="EC2 Keypair",
	Type="String",
))
instance.KeyName = Ref(keyname_param)
ec2_instance = template.add_resource(instance)
template.add_output([
	Output(
		"InstanceId",
		Description="InstanceID of EC2 instance",
		Value=Ref(ec2_instance)
)])
print(template.to_json())