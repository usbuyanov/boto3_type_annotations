from typing import Dict
from typing import List
from datetime import datetime
from botocore.paginate import Paginator


class DescribeAutoScalingGroups(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_auto_scaling_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AutoScalingGroups': [
                    {
                        'AutoScalingGroupName': 'string',
                        'AutoScalingGroupARN': 'string',
                        'LaunchConfigurationName': 'string',
                        'LaunchTemplate': {
                            'LaunchTemplateId': 'string',
                            'LaunchTemplateName': 'string',
                            'Version': 'string'
                        },
                        'MixedInstancesPolicy': {
                            'LaunchTemplate': {
                                'LaunchTemplateSpecification': {
                                    'LaunchTemplateId': 'string',
                                    'LaunchTemplateName': 'string',
                                    'Version': 'string'
                                },
                                'Overrides': [
                                    {
                                        'InstanceType': 'string'
                                    },
                                ]
                            },
                            'InstancesDistribution': {
                                'OnDemandAllocationStrategy': 'string',
                                'OnDemandBaseCapacity': 123,
                                'OnDemandPercentageAboveBaseCapacity': 123,
                                'SpotAllocationStrategy': 'string',
                                'SpotInstancePools': 123,
                                'SpotMaxPrice': 'string'
                            }
                        },
                        'MinSize': 123,
                        'MaxSize': 123,
                        'DesiredCapacity': 123,
                        'DefaultCooldown': 123,
                        'AvailabilityZones': [
                            'string',
                        ],
                        'LoadBalancerNames': [
                            'string',
                        ],
                        'TargetGroupARNs': [
                            'string',
                        ],
                        'HealthCheckType': 'string',
                        'HealthCheckGracePeriod': 123,
                        'Instances': [
                            {
                                'InstanceId': 'string',
                                'AvailabilityZone': 'string',
                                'LifecycleState': 'Pending'|'Pending:Wait'|'Pending:Proceed'|'Quarantined'|'InService'|'Terminating'|'Terminating:Wait'|'Terminating:Proceed'|'Terminated'|'Detaching'|'Detached'|'EnteringStandby'|'Standby',
                                'HealthStatus': 'string',
                                'LaunchConfigurationName': 'string',
                                'LaunchTemplate': {
                                    'LaunchTemplateId': 'string',
                                    'LaunchTemplateName': 'string',
                                    'Version': 'string'
                                },
                                'ProtectedFromScaleIn': True|False
                            },
                        ],
                        'CreatedTime': datetime(2015, 1, 1),
                        'SuspendedProcesses': [
                            {
                                'ProcessName': 'string',
                                'SuspensionReason': 'string'
                            },
                        ],
                        'PlacementGroup': 'string',
                        'VPCZoneIdentifier': 'string',
                        'EnabledMetrics': [
                            {
                                'Metric': 'string',
                                'Granularity': 'string'
                            },
                        ],
                        'Status': 'string',
                        'Tags': [
                            {
                                'ResourceId': 'string',
                                'ResourceType': 'string',
                                'Key': 'string',
                                'Value': 'string',
                                'PropagateAtLaunch': True|False
                            },
                        ],
                        'TerminationPolicies': [
                            'string',
                        ],
                        'NewInstancesProtectedFromScaleIn': True|False,
                        'ServiceLinkedRoleARN': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AutoScalingGroups** *(list) --* 
              The groups.
              - *(dict) --* 
                Describes an Auto Scaling group.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group.
                - **AutoScalingGroupARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the Auto Scaling group.
                - **LaunchConfigurationName** *(string) --* 
                  The name of the associated launch configuration.
                - **LaunchTemplate** *(dict) --* 
                  The launch template for the group.
                  - **LaunchTemplateId** *(string) --* 
                    The ID of the launch template. You must specify either a template ID or a template name.
                  - **LaunchTemplateName** *(string) --* 
                    The name of the launch template. You must specify either a template name or a template ID.
                  - **Version** *(string) --* 
                    The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
                - **MixedInstancesPolicy** *(dict) --* 
                  The mixed instances policy for the group. 
                  - **LaunchTemplate** *(dict) --* 
                    The launch template and overrides.
                    This parameter is required when creating an Auto Scaling group with a mixed instances policy, but is not required when updating the group.
                    - **LaunchTemplateSpecification** *(dict) --* 
                      The launch template to use. You must specify either the launch template ID or launch template name in the request. 
                      - **LaunchTemplateId** *(string) --* 
                        The ID of the launch template. You must specify either a template ID or a template name.
                      - **LaunchTemplateName** *(string) --* 
                        The name of the launch template. You must specify either a template name or a template ID.
                      - **Version** *(string) --* 
                        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
                    - **Overrides** *(list) --* 
                      Any parameters that you specify override the same parameters in the launch template. Currently, the only supported override is instance type. 
                      You must specify between 2 and 20 overrides.
                      - *(dict) --* 
                        Describes an override for a launch template. 
                        - **InstanceType** *(string) --* 
                          The instance type. 
                          For information about available instance types, see `Available Instance Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__ in the *Amazon Elastic Compute Cloud User Guide.*  
                  - **InstancesDistribution** *(dict) --* 
                    The instances distribution to use. 
                    If you leave this parameter unspecified when creating the group, the default values are used.
                    - **OnDemandAllocationStrategy** *(string) --* 
                      Indicates how to allocate instance types to fulfill On-Demand capacity. 
                      The only valid value is ``prioritized`` , which is also the default value. This strategy uses the order of instance type overrides for the  LaunchTemplate to define the launch priority of each instance type. The first instance type in the array is prioritized higher than the last. If all your On-Demand capacity cannot be fulfilled using your highest priority instance, then the Auto Scaling groups launches the remaining capacity using the second priority instance type, and so on. 
                    - **OnDemandBaseCapacity** *(integer) --* 
                      The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
                      The default value is ``0`` . If you leave this parameter set to ``0`` , On-Demand Instances are launched as a percentage of the Auto Scaling group's desired capacity, per the ``OnDemandPercentageAboveBaseCapacity`` setting.
                    - **OnDemandPercentageAboveBaseCapacity** *(integer) --* 
                      Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond ``OnDemandBaseCapacity`` .
                      The range is 0–100. The default value is ``100`` . If you leave this parameter set to ``100`` , the percentages are 100% for On-Demand Instances and 0% for Spot Instances. 
                    - **SpotAllocationStrategy** *(string) --* 
                      Indicates how to allocate Spot capacity across Spot pools.
                      The only valid value is ``lowest-price`` , which is also the default value. The Auto Scaling group selects the cheapest Spot pools and evenly allocates your Spot capacity across the number of Spot pools that you specify. 
                    - **SpotInstancePools** *(integer) --* 
                      The number of Spot pools to use to allocate your Spot capacity. The Spot pools are determined from the different instance types in the Overrides array of  LaunchTemplate . 
                      The range is 1–20 and the default is 2. 
                    - **SpotMaxPrice** *(string) --* 
                      The maximum price per unit hour that you are willing to pay for a Spot Instance. If you leave the value of this parameter blank (which is the default), the maximum Spot price is set at the On-Demand price.
                      To remove a value that you previously set, include the parameter but leave the value blank.
                - **MinSize** *(integer) --* 
                  The minimum size of the group.
                - **MaxSize** *(integer) --* 
                  The maximum size of the group.
                - **DesiredCapacity** *(integer) --* 
                  The desired size of the group.
                - **DefaultCooldown** *(integer) --* 
                  The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
                - **AvailabilityZones** *(list) --* 
                  One or more Availability Zones for the group.
                  - *(string) --* 
                - **LoadBalancerNames** *(list) --* 
                  One or more load balancers associated with the group.
                  - *(string) --* 
                - **TargetGroupARNs** *(list) --* 
                  The Amazon Resource Names (ARN) of the target groups for your load balancer.
                  - *(string) --* 
                - **HealthCheckType** *(string) --* 
                  The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.
                - **HealthCheckGracePeriod** *(integer) --* 
                  The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
                - **Instances** *(list) --* 
                  The EC2 instances associated with the group.
                  - *(dict) --* 
                    Describes an EC2 instance.
                    - **InstanceId** *(string) --* 
                      The ID of the instance.
                    - **AvailabilityZone** *(string) --* 
                      The Availability Zone in which the instance is running.
                    - **LifecycleState** *(string) --* 
                      A description of the current lifecycle state. The ``Quarantined`` state is not used.
                    - **HealthStatus** *(string) --* 
                      The last reported health status of the instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.
                    - **LaunchConfigurationName** *(string) --* 
                      The launch configuration associated with the instance.
                    - **LaunchTemplate** *(dict) --* 
                      The launch template for the instance.
                      - **LaunchTemplateId** *(string) --* 
                        The ID of the launch template. You must specify either a template ID or a template name.
                      - **LaunchTemplateName** *(string) --* 
                        The name of the launch template. You must specify either a template name or a template ID.
                      - **Version** *(string) --* 
                        The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
                    - **ProtectedFromScaleIn** *(boolean) --* 
                      Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
                - **CreatedTime** *(datetime) --* 
                  The date and time the group was created.
                - **SuspendedProcesses** *(list) --* 
                  The suspended processes associated with the group.
                  - *(dict) --* 
                    Describes an automatic scaling process that has been suspended. For more information, see  ProcessType .
                    - **ProcessName** *(string) --* 
                      The name of the suspended process.
                    - **SuspensionReason** *(string) --* 
                      The reason that the process was suspended.
                - **PlacementGroup** *(string) --* 
                  The name of the placement group into which to launch your instances, if any.
                - **VPCZoneIdentifier** *(string) --* 
                  One or more subnet IDs, if applicable, separated by commas.
                - **EnabledMetrics** *(list) --* 
                  The metrics enabled for the group.
                  - *(dict) --* 
                    Describes an enabled metric.
                    - **Metric** *(string) --* 
                      One of the following metrics:
                      * ``GroupMinSize``   
                      * ``GroupMaxSize``   
                      * ``GroupDesiredCapacity``   
                      * ``GroupInServiceInstances``   
                      * ``GroupPendingInstances``   
                      * ``GroupStandbyInstances``   
                      * ``GroupTerminatingInstances``   
                      * ``GroupTotalInstances``   
                    - **Granularity** *(string) --* 
                      The granularity of the metric. The only valid value is ``1Minute`` .
                - **Status** *(string) --* 
                  The current state of the group when  DeleteAutoScalingGroup is in progress.
                - **Tags** *(list) --* 
                  The tags for the group.
                  - *(dict) --* 
                    Describes a tag for an Auto Scaling group.
                    - **ResourceId** *(string) --* 
                      The name of the group.
                    - **ResourceType** *(string) --* 
                      The type of resource. The only supported value is ``auto-scaling-group`` .
                    - **Key** *(string) --* 
                      The tag key.
                    - **Value** *(string) --* 
                      The tag value.
                    - **PropagateAtLaunch** *(boolean) --* 
                      Determines whether the tag is added to new instances as they are launched in the group.
                - **TerminationPolicies** *(list) --* 
                  The termination policies for the group.
                  - *(string) --* 
                - **NewInstancesProtectedFromScaleIn** *(boolean) --* 
                  Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.
                - **ServiceLinkedRoleARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames:
          The names of the Auto Scaling groups. Each name can be a maximum of 1600 characters. By default, you can only specify up to 50 names. You can optionally increase this limit using the ``MaxRecords`` parameter.
          If you omit this parameter, all Auto Scaling groups are described.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeAutoScalingInstances(Paginator):
    def paginate(self, InstanceIds: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_auto_scaling_instances`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingInstances>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              InstanceIds=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'AutoScalingInstances': [
                    {
                        'InstanceId': 'string',
                        'AutoScalingGroupName': 'string',
                        'AvailabilityZone': 'string',
                        'LifecycleState': 'string',
                        'HealthStatus': 'string',
                        'LaunchConfigurationName': 'string',
                        'LaunchTemplate': {
                            'LaunchTemplateId': 'string',
                            'LaunchTemplateName': 'string',
                            'Version': 'string'
                        },
                        'ProtectedFromScaleIn': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AutoScalingInstances** *(list) --* 
              The instances.
              - *(dict) --* 
                Describes an EC2 instance associated with an Auto Scaling group.
                - **InstanceId** *(string) --* 
                  The ID of the instance.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group for the instance.
                - **AvailabilityZone** *(string) --* 
                  The Availability Zone for the instance.
                - **LifecycleState** *(string) --* 
                  The lifecycle state for the instance.
                - **HealthStatus** *(string) --* 
                  The last reported health status of this instance. "Healthy" means that the instance is healthy and should remain in service. "Unhealthy" means that the instance is unhealthy and Amazon EC2 Auto Scaling should terminate and replace it.
                - **LaunchConfigurationName** *(string) --* 
                  The launch configuration used to launch the instance. This value is not available if you attached the instance to the Auto Scaling group.
                - **LaunchTemplate** *(dict) --* 
                  The launch template for the instance.
                  - **LaunchTemplateId** *(string) --* 
                    The ID of the launch template. You must specify either a template ID or a template name.
                  - **LaunchTemplateName** *(string) --* 
                    The name of the launch template. You must specify either a template name or a template ID.
                  - **Version** *(string) --* 
                    The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
                - **ProtectedFromScaleIn** *(boolean) --* 
                  Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to ``MaxRecords`` IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeLaunchConfigurations(Paginator):
    def paginate(self, LaunchConfigurationNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_launch_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              LaunchConfigurationNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LaunchConfigurations': [
                    {
                        'LaunchConfigurationName': 'string',
                        'LaunchConfigurationARN': 'string',
                        'ImageId': 'string',
                        'KeyName': 'string',
                        'SecurityGroups': [
                            'string',
                        ],
                        'ClassicLinkVPCId': 'string',
                        'ClassicLinkVPCSecurityGroups': [
                            'string',
                        ],
                        'UserData': 'string',
                        'InstanceType': 'string',
                        'KernelId': 'string',
                        'RamdiskId': 'string',
                        'BlockDeviceMappings': [
                            {
                                'VirtualName': 'string',
                                'DeviceName': 'string',
                                'Ebs': {
                                    'SnapshotId': 'string',
                                    'VolumeSize': 123,
                                    'VolumeType': 'string',
                                    'DeleteOnTermination': True|False,
                                    'Iops': 123,
                                    'Encrypted': True|False
                                },
                                'NoDevice': True|False
                            },
                        ],
                        'InstanceMonitoring': {
                            'Enabled': True|False
                        },
                        'SpotPrice': 'string',
                        'IamInstanceProfile': 'string',
                        'CreatedTime': datetime(2015, 1, 1),
                        'EbsOptimized': True|False,
                        'AssociatePublicIpAddress': True|False,
                        'PlacementTenancy': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LaunchConfigurations** *(list) --* 
              The launch configurations.
              - *(dict) --* 
                Describes a launch configuration.
                - **LaunchConfigurationName** *(string) --* 
                  The name of the launch configuration.
                - **LaunchConfigurationARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the launch configuration.
                - **ImageId** *(string) --* 
                  The ID of the Amazon Machine Image (AMI).
                - **KeyName** *(string) --* 
                  The name of the key pair.
                - **SecurityGroups** *(list) --* 
                  The security groups to associate with the instances.
                  - *(string) --* 
                - **ClassicLinkVPCId** *(string) --* 
                  The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter can only be used if you are launching EC2-Classic instances. For more information, see `ClassicLink <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__ in the *Amazon EC2 Auto Scaling User Guide* .
                - **ClassicLinkVPCSecurityGroups** *(list) --* 
                  The IDs of one or more security groups for the VPC specified in ``ClassicLinkVPCId`` . For more information, see `ClassicLink <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__ in the *Amazon EC2 Auto Scaling User Guide* .
                  Conditional: This parameter is required if you specify a ClassicLink-enabled VPC, and cannot be used otherwise.
                  - *(string) --* 
                - **UserData** *(string) --* 
                  The user data available to the instances.
                - **InstanceType** *(string) --* 
                  The instance type for the instances.
                - **KernelId** *(string) --* 
                  The ID of the kernel associated with the AMI.
                - **RamdiskId** *(string) --* 
                  The ID of the RAM disk associated with the AMI.
                - **BlockDeviceMappings** *(list) --* 
                  A block device mapping, which specifies the block devices for the instance.
                  - *(dict) --* 
                    Describes a block device mapping.
                    - **VirtualName** *(string) --* 
                      The name of the virtual device (for example, ``ephemeral0`` ).
                    - **DeviceName** *(string) --* 
                      The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ). For more information, see `Device Naming on Linux Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
                    - **Ebs** *(dict) --* 
                      The information about the Amazon EBS volume.
                      - **SnapshotId** *(string) --* 
                        The ID of the snapshot. This parameter is optional if you specify a volume size. 
                      - **VolumeSize** *(integer) --* 
                        The volume size, in GiB. 
                        Constraints: 1-1,024 for ``standard`` , 4-16,384 for ``io1`` , 1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
                        Default: If you create a volume from a snapshot and you don't specify a volume size, the default is the snapshot size.
                        .. note::
                          At least one of VolumeSize or SnapshotId is required.
                      - **VolumeType** *(string) --* 
                        The volume type, which can be ``standard`` for Magnetic, ``io1`` for Provisioned IOPS SSD, ``gp2`` for General Purpose SSD, ``st1`` for Throughput Optimized HDD, or ``sc1`` for Cold HDD. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
                        Valid values: ``standard`` | ``io1`` | ``gp2`` | ``st1`` | ``sc1``  
                      - **DeleteOnTermination** *(boolean) --* 
                        Indicates whether the volume is deleted on instance termination. The default value is ``true`` .
                      - **Iops** *(integer) --* 
                        The number of I/O operations per second (IOPS) to provision for the volume. For more information, see `Amazon EBS Volume Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
                        Conditional: This parameter is required when the volume type is ``io1`` . (Not used with ``standard`` , ``gp2`` , ``st1`` , or ``sc1`` volumes.) 
                      - **Encrypted** *(boolean) --* 
                        Specifies whether the volume should be encrypted. Encrypted EBS volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are automatically encrypted. There is no way to create an encrypted volume from an unencrypted snapshot or an unencrypted volume from an encrypted snapshot. If your AMI uses encrypted volumes, you can only launch it on supported instance types. For more information, see `Amazon EBS Encryption <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
                    - **NoDevice** *(boolean) --* 
                      Suppresses a device mapping.
                      If this parameter is true for the root device, the instance might fail the EC2 health check. In that case, Amazon EC2 Auto Scaling launches a replacement instance.
                - **InstanceMonitoring** *(dict) --* 
                  Controls whether instances in this group are launched with detailed (``true`` ) or basic (``false`` ) monitoring.
                  - **Enabled** *(boolean) --* 
                    If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
                - **SpotPrice** *(string) --* 
                  The price to bid when launching Spot Instances.
                - **IamInstanceProfile** *(string) --* 
                  The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.
                - **CreatedTime** *(datetime) --* 
                  The creation date and time for the launch configuration.
                - **EbsOptimized** *(boolean) --* 
                  Controls whether the instance is optimized for EBS I/O (``true`` ) or not (``false`` ).
                - **AssociatePublicIpAddress** *(boolean) --* 
                  [EC2-VPC] Indicates whether to assign a public IP address to each instance.
                - **PlacementTenancy** *(string) --* 
                  The tenancy of the instance, either ``default`` or ``dedicated`` . An instance with ``dedicated`` tenancy runs in an isolated, single-tenant hardware and can only be launched into a VPC.
        :type LaunchConfigurationNames: list
        :param LaunchConfigurationNames:
          The launch configuration names. If you omit this parameter, all launch configurations are described.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeLoadBalancerTargetGroups(Paginator):
    def paginate(self, AutoScalingGroupName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_load_balancer_target_groups`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancerTargetGroups>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LoadBalancerTargetGroups': [
                    {
                        'LoadBalancerTargetGroupARN': 'string',
                        'State': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LoadBalancerTargetGroups** *(list) --* 
              Information about the target groups.
              - *(dict) --* 
                Describes the state of a target group.
                If you attach a target group to an existing Auto Scaling group, the initial state is ``Adding`` . The state transitions to ``Added`` after all Auto Scaling instances are registered with the target group. If Elastic Load Balancing health checks are enabled, the state transitions to ``InService`` after at least one Auto Scaling instance passes the health check. If EC2 health checks are enabled instead, the target group remains in the ``Added`` state.
                - **LoadBalancerTargetGroupARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the target group.
                - **State** *(string) --* 
                  The state of the target group.
                  * ``Adding`` - The Auto Scaling instances are being registered with the target group. 
                  * ``Added`` - All Auto Scaling instances are registered with the target group. 
                  * ``InService`` - At least one Auto Scaling instance passed an ELB health check. 
                  * ``Removing`` - The Auto Scaling instances are being deregistered from the target group. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances. 
                  * ``Removed`` - All Auto Scaling instances are deregistered from the target group. 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeLoadBalancers(Paginator):
    def paginate(self, AutoScalingGroupName: str, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_load_balancers`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancers>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'LoadBalancers': [
                    {
                        'LoadBalancerName': 'string',
                        'State': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LoadBalancers** *(list) --* 
              The load balancers.
              - *(dict) --* 
                Describes the state of a Classic Load Balancer.
                If you specify a load balancer when creating the Auto Scaling group, the state of the load balancer is ``InService`` .
                If you attach a load balancer to an existing Auto Scaling group, the initial state is ``Adding`` . The state transitions to ``Added`` after all instances in the group are registered with the load balancer. If Elastic Load Balancing health checks are enabled for the load balancer, the state transitions to ``InService`` after at least one instance in the group passes the health check. If EC2 health checks are enabled instead, the load balancer remains in the ``Added`` state.
                - **LoadBalancerName** *(string) --* 
                  The name of the load balancer.
                - **State** *(string) --* 
                  One of the following load balancer states:
                  * ``Adding`` - The instances in the group are being registered with the load balancer. 
                  * ``Added`` - All instances in the group are registered with the load balancer. 
                  * ``InService`` - At least one instance in the group passed an ELB health check. 
                  * ``Removing`` - The instances in the group are being deregistered from the load balancer. If connection draining is enabled, Elastic Load Balancing waits for in-flight requests to complete before deregistering the instances. 
                  * ``Removed`` - All instances in the group are deregistered from the load balancer. 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeNotificationConfigurations(Paginator):
    def paginate(self, AutoScalingGroupNames: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_notification_configurations`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeNotificationConfigurations>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'NotificationConfigurations': [
                    {
                        'AutoScalingGroupName': 'string',
                        'TopicARN': 'string',
                        'NotificationType': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **NotificationConfigurations** *(list) --* 
              The notification configurations.
              - *(dict) --* 
                Describes a notification.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group.
                - **TopicARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.
                - **NotificationType** *(string) --* 
                  One of the following event notification types:
                  * ``autoscaling:EC2_INSTANCE_LAUNCH``   
                  * ``autoscaling:EC2_INSTANCE_LAUNCH_ERROR``   
                  * ``autoscaling:EC2_INSTANCE_TERMINATE``   
                  * ``autoscaling:EC2_INSTANCE_TERMINATE_ERROR``   
                  * ``autoscaling:TEST_NOTIFICATION``   
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames:
          The name of the Auto Scaling group.
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribePolicies(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, PolicyNames: List = None, PolicyTypes: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_policies`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribePolicies>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupName='string',
              PolicyNames=[
                  'string',
              ],
              PolicyTypes=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScalingPolicies': [
                    {
                        'AutoScalingGroupName': 'string',
                        'PolicyName': 'string',
                        'PolicyARN': 'string',
                        'PolicyType': 'string',
                        'AdjustmentType': 'string',
                        'MinAdjustmentStep': 123,
                        'MinAdjustmentMagnitude': 123,
                        'ScalingAdjustment': 123,
                        'Cooldown': 123,
                        'StepAdjustments': [
                            {
                                'MetricIntervalLowerBound': 123.0,
                                'MetricIntervalUpperBound': 123.0,
                                'ScalingAdjustment': 123
                            },
                        ],
                        'MetricAggregationType': 'string',
                        'EstimatedInstanceWarmup': 123,
                        'Alarms': [
                            {
                                'AlarmName': 'string',
                                'AlarmARN': 'string'
                            },
                        ],
                        'TargetTrackingConfiguration': {
                            'PredefinedMetricSpecification': {
                                'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
                                'ResourceLabel': 'string'
                            },
                            'CustomizedMetricSpecification': {
                                'MetricName': 'string',
                                'Namespace': 'string',
                                'Dimensions': [
                                    {
                                        'Name': 'string',
                                        'Value': 'string'
                                    },
                                ],
                                'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                                'Unit': 'string'
                            },
                            'TargetValue': 123.0,
                            'DisableScaleIn': True|False
                        }
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ScalingPolicies** *(list) --* 
              The scaling policies.
              - *(dict) --* 
                Describes a scaling policy.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group.
                - **PolicyName** *(string) --* 
                  The name of the scaling policy.
                - **PolicyARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the policy.
                - **PolicyType** *(string) --* 
                  The policy type. The valid values are ``SimpleScaling`` and ``StepScaling`` .
                - **AdjustmentType** *(string) --* 
                  The adjustment type, which specifies how ``ScalingAdjustment`` is interpreted. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .
                - **MinAdjustmentStep** *(integer) --* 
                  Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.
                - **MinAdjustmentMagnitude** *(integer) --* 
                  The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .
                - **ScalingAdjustment** *(integer) --* 
                  The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
                - **Cooldown** *(integer) --* 
                  The amount of time, in seconds, after a scaling activity completes before any further dynamic scaling activities can start.
                - **StepAdjustments** *(list) --* 
                  A set of adjustments that enable you to scale based on the size of the alarm breach.
                  - *(dict) --* 
                    Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you've defined for the alarm. Used in combination with  PutScalingPolicy .
                    For the following examples, suppose that you have an alarm with a breach threshold of 50:
                    * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10. 
                    * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0. 
                    There are a few rules for the step adjustments for your step policy:
                    * The ranges of your step adjustments can't overlap or have a gap. 
                    * At most, one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound. 
                    * At most, one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound. 
                    * The upper and lower bound can't be null in the same step adjustment. 
                    - **MetricIntervalLowerBound** *(float) --* 
                      The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
                    - **MetricIntervalUpperBound** *(float) --* 
                      The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
                      The upper bound must be greater than the lower bound.
                    - **ScalingAdjustment** *(integer) --* 
                      The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
                - **MetricAggregationType** *(string) --* 
                  The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` , ``Maximum`` , and ``Average`` .
                - **EstimatedInstanceWarmup** *(integer) --* 
                  The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.
                - **Alarms** *(list) --* 
                  The CloudWatch alarms related to the policy.
                  - *(dict) --* 
                    Describes an alarm.
                    - **AlarmName** *(string) --* 
                      The name of the alarm.
                    - **AlarmARN** *(string) --* 
                      The Amazon Resource Name (ARN) of the alarm.
                - **TargetTrackingConfiguration** *(dict) --* 
                  A target tracking scaling policy.
                  - **PredefinedMetricSpecification** *(dict) --* 
                    A predefined metric. You can specify either a predefined metric or a customized metric.
                    - **PredefinedMetricType** *(string) --* 
                      The metric type.
                    - **ResourceLabel** *(string) --* 
                      Identifies the resource associated with the metric type. The following predefined metrics are available:
                      * ``ASGAverageCPUUtilization`` - Average CPU utilization of the Auto Scaling group. 
                      * ``ASGAverageNetworkIn`` - Average number of bytes received on all network interfaces by the Auto Scaling group. 
                      * ``ASGAverageNetworkOut`` - Average number of bytes sent out on all network interfaces by the Auto Scaling group. 
                      * ``ALBRequestCountPerTarget`` - Number of requests completed per target in an Application Load Balancer or a Network Load Balancer target group. 
                      For predefined metric types ``ASGAverageCPUUtilization`` , ``ASGAverageNetworkIn`` , and ``ASGAverageNetworkOut`` , the parameter must not be specified as the resource associated with the metric type is the Auto Scaling group. For predefined metric type ``ALBRequestCountPerTarget`` , the parameter must be specified in the format: ``app/*load-balancer-name* /*load-balancer-id* /targetgroup/*target-group-name* /*target-group-id* `` , where ``app/*load-balancer-name* /*load-balancer-id* `` is the final portion of the load balancer ARN, and ``targetgroup/*target-group-name* /*target-group-id* `` is the final portion of the target group ARN. The target group must be attached to the Auto Scaling group.
                  - **CustomizedMetricSpecification** *(dict) --* 
                    A customized metric. You can specify either a predefined metric or a customized metric.
                    - **MetricName** *(string) --* 
                      The name of the metric.
                    - **Namespace** *(string) --* 
                      The namespace of the metric.
                    - **Dimensions** *(list) --* 
                      The dimensions of the metric.
                      Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
                      - *(dict) --* 
                        Describes the dimension of a metric.
                        - **Name** *(string) --* 
                          The name of the dimension.
                        - **Value** *(string) --* 
                          The value of the dimension.
                    - **Statistic** *(string) --* 
                      The statistic of the metric.
                    - **Unit** *(string) --* 
                      The unit of the metric.
                  - **TargetValue** *(float) --* 
                    The target value for the metric.
                  - **DisableScaleIn** *(boolean) --* 
                    Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is disabled.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type PolicyNames: list
        :param PolicyNames:
          The names of one or more policies. If you omit this parameter, all policies are described. If a group name is provided, the results are limited to that group. This list is limited to 50 items. If you specify an unknown policy name, it is ignored with no error.
          - *(string) --*
        :type PolicyTypes: list
        :param PolicyTypes:
          One or more policy types. The valid values are ``SimpleScaling`` , ``StepScaling`` , and ``TargetTrackingScaling`` .
          - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeScalingActivities(Paginator):
    def paginate(self, ActivityIds: List = None, AutoScalingGroupName: str = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_scaling_activities`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingActivities>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              ActivityIds=[
                  'string',
              ],
              AutoScalingGroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Activities': [
                    {
                        'ActivityId': 'string',
                        'AutoScalingGroupName': 'string',
                        'Description': 'string',
                        'Cause': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'StatusCode': 'PendingSpotBidPlacement'|'WaitingForSpotInstanceRequestId'|'WaitingForSpotInstanceId'|'WaitingForInstanceId'|'PreInService'|'InProgress'|'WaitingForELBConnectionDraining'|'MidLifecycleAction'|'WaitingForInstanceWarmup'|'Successful'|'Failed'|'Cancelled',
                        'StatusMessage': 'string',
                        'Progress': 123,
                        'Details': 'string'
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Activities** *(list) --* 
              The scaling activities. Activities are sorted by start time. Activities still in progress are described first.
              - *(dict) --* 
                Describes scaling activity, which is a long-running process that represents a change to your Auto Scaling group, such as changing its size or replacing an instance.
                - **ActivityId** *(string) --* 
                  The ID of the activity.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group.
                - **Description** *(string) --* 
                  A friendly, more verbose description of the activity.
                - **Cause** *(string) --* 
                  The reason the activity began.
                - **StartTime** *(datetime) --* 
                  The start time of the activity.
                - **EndTime** *(datetime) --* 
                  The end time of the activity.
                - **StatusCode** *(string) --* 
                  The current status of the activity.
                - **StatusMessage** *(string) --* 
                  A friendly, more verbose description of the activity status.
                - **Progress** *(integer) --* 
                  A value between 0 and 100 that indicates the progress of the activity.
                - **Details** *(string) --* 
                  The details about the activity.
        :type ActivityIds: list
        :param ActivityIds:
          The activity IDs of the desired scaling activities. You can specify up to 50 IDs. If you omit this parameter, all activities for the past six weeks are described. If unknown activities are requested, they are ignored with no error. If you specify an Auto Scaling group, the results are limited to that group.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeScheduledActions(Paginator):
    def paginate(self, AutoScalingGroupName: str = None, ScheduledActionNames: List = None, StartTime: datetime = None, EndTime: datetime = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_scheduled_actions`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScheduledActions>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              AutoScalingGroupName='string',
              ScheduledActionNames=[
                  'string',
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'ScheduledUpdateGroupActions': [
                    {
                        'AutoScalingGroupName': 'string',
                        'ScheduledActionName': 'string',
                        'ScheduledActionARN': 'string',
                        'Time': datetime(2015, 1, 1),
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'Recurrence': 'string',
                        'MinSize': 123,
                        'MaxSize': 123,
                        'DesiredCapacity': 123
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ScheduledUpdateGroupActions** *(list) --* 
              The scheduled actions.
              - *(dict) --* 
                Describes a scheduled scaling action. Used in response to  DescribeScheduledActions . 
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group.
                - **ScheduledActionName** *(string) --* 
                  The name of the scheduled action.
                - **ScheduledActionARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the scheduled action.
                - **Time** *(datetime) --* 
                  This parameter is deprecated.
                - **StartTime** *(datetime) --* 
                  The date and time that the action is scheduled to begin. 
                  When ``StartTime`` and ``EndTime`` are specified with ``Recurrence`` , they form the boundaries of when the recurring action starts and stops.
                - **EndTime** *(datetime) --* 
                  The date and time that the action is scheduled to end. 
                - **Recurrence** *(string) --* 
                  The recurring schedule for the action.
                - **MinSize** *(integer) --* 
                  The minimum size of the group.
                - **MaxSize** *(integer) --* 
                  The maximum size of the group.
                - **DesiredCapacity** *(integer) --* 
                  The number of instances you prefer to maintain in the group.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type ScheduledActionNames: list
        :param ScheduledActionNames:
          The names of one or more scheduled actions. You can specify up to 50 actions. If you omit this parameter, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.
          - *(string) --*
        :type StartTime: datetime
        :param StartTime:
          The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :type EndTime: datetime
        :param EndTime:
          The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass


class DescribeTags(Paginator):
    def paginate(self, Filters: List = None, PaginationConfig: Dict = None) -> Dict:
        """
        Creates an iterator that will paginate through responses from :py:meth:`AutoScaling.Client.describe_tags`.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTags>`_
        
        **Request Syntax**
        ::
          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        
        **Response Syntax**
        ::
            {
                'Tags': [
                    {
                        'ResourceId': 'string',
                        'ResourceType': 'string',
                        'Key': 'string',
                        'Value': 'string',
                        'PropagateAtLaunch': True|False
                    },
                ],
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Tags** *(list) --* 
              One or more tags.
              - *(dict) --* 
                Describes a tag for an Auto Scaling group.
                - **ResourceId** *(string) --* 
                  The name of the group.
                - **ResourceType** *(string) --* 
                  The type of resource. The only supported value is ``auto-scaling-group`` .
                - **Key** *(string) --* 
                  The tag key.
                - **Value** *(string) --* 
                  The tag value.
                - **PropagateAtLaunch** *(boolean) --* 
                  Determines whether the tag is added to new instances as they are launched in the group.
        :type Filters: list
        :param Filters:
          One or more filters to scope the tags to return. The maximum number of filters per filter type (for example, ``auto-scaling-group`` ) is 1000.
          - *(dict) --*
            Describes a filter.
            - **Name** *(string) --*
              The name of the filter. The valid values are: ``\"auto-scaling-group\"`` , ``\"key\"`` , ``\"value\"`` , and ``\"propagate-at-launch\"`` .
            - **Values** *(list) --*
              The value of the filter.
              - *(string) --*
        :type PaginationConfig: dict
        :param PaginationConfig:
          A dictionary that provides parameters to control pagination.
          - **MaxItems** *(integer) --*
            The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.
          - **PageSize** *(integer) --*
            The size of each page.
          - **StartingToken** *(string) --*
            A token to specify where to start paginating. This is the ``NextToken`` from a previous response.
        :rtype: dict
        :returns:
        """
        pass
