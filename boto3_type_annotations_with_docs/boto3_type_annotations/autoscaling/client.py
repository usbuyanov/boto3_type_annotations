from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def attach_instances(self, AutoScalingGroupName: str, InstanceIds: List = None):
        """
        Attaches one or more EC2 instances to the specified Auto Scaling group.
        When you attach instances, Amazon EC2 Auto Scaling increases the desired capacity of the group by the number of instances being attached. If the number of instances being attached plus the desired capacity of the group exceeds the maximum size of the group, the operation fails.
        If there is a Classic Load Balancer attached to your Auto Scaling group, the instances are also registered with the load balancer. If there are target groups attached to your Auto Scaling group, the instances are also registered with the target groups.
        For more information, see `Attach EC2 Instances to Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-instance-asg.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachInstances>`_
        
        **Request Syntax**
        ::
          response = client.attach_instances(
              InstanceIds=[
                  'string',
              ],
              AutoScalingGroupName='string'
          )
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to 20 instances.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :returns: None
        """
        pass

    def attach_load_balancer_target_groups(self, AutoScalingGroupName: str, TargetGroupARNs: List) -> Dict:
        """
        Attaches one or more target groups to the specified Auto Scaling group. 
        To describe the target groups for an Auto Scaling group, use  DescribeLoadBalancerTargetGroups . To detach the target group from the Auto Scaling group, use  DetachLoadBalancerTargetGroups .
        With Application Load Balancers and Network Load Balancers, instances are registered as targets with a target group. With Classic Load Balancers, instances are registered with the load balancer. For more information, see `Attaching a Load Balancer to Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachLoadBalancerTargetGroups>`_
        
        **Request Syntax**
        ::
          response = client.attach_load_balancer_target_groups(
              AutoScalingGroupName='string',
              TargetGroupARNs=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type TargetGroupARNs: list
        :param TargetGroupARNs: **[REQUIRED]**
          The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def attach_load_balancers(self, AutoScalingGroupName: str, LoadBalancerNames: List) -> Dict:
        """
        Attaches one or more Classic Load Balancers to the specified Auto Scaling group.
        To attach an Application Load Balancer or a Network Load Balancer instead, see  AttachLoadBalancerTargetGroups .
        To describe the load balancers for an Auto Scaling group, use  DescribeLoadBalancers . To detach the load balancer from the Auto Scaling group, use  DetachLoadBalancers .
        For more information, see `Attaching a Load Balancer to Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/AttachLoadBalancers>`_
        
        **Request Syntax**
        ::
          response = client.attach_load_balancers(
              AutoScalingGroupName='string',
              LoadBalancerNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LoadBalancerNames: list
        :param LoadBalancerNames: **[REQUIRED]**
          The names of the load balancers. You can specify up to 10 load balancers.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionNames: List) -> Dict:
        """
        Deletes one or more scheduled actions for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/BatchDeleteScheduledAction>`_
        
        **Request Syntax**
        ::
          response = client.batch_delete_scheduled_action(
              AutoScalingGroupName='string',
              ScheduledActionNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedScheduledActions': [
                    {
                        'ScheduledActionName': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedScheduledActions** *(list) --* 
              The names of the scheduled actions that could not be deleted, including an error message. 
              - *(dict) --* 
                Describes a scheduled action that could not be created, updated, or deleted.
                - **ScheduledActionName** *(string) --* 
                  The name of the scheduled action.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message accompanying the error code.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScheduledActionNames: list
        :param ScheduledActionNames: **[REQUIRED]**
          The names of the scheduled actions to delete. The maximum number allowed is 50.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def batch_put_scheduled_update_group_action(self, AutoScalingGroupName: str, ScheduledUpdateGroupActions: List) -> Dict:
        """
        Creates or updates one or more scheduled scaling actions for an Auto Scaling group. If you leave a parameter unspecified when updating a scheduled scaling action, the corresponding value remains unchanged.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction>`_
        
        **Request Syntax**
        ::
          response = client.batch_put_scheduled_update_group_action(
              AutoScalingGroupName='string',
              ScheduledUpdateGroupActions=[
                  {
                      'ScheduledActionName': 'string',
                      'StartTime': datetime(2015, 1, 1),
                      'EndTime': datetime(2015, 1, 1),
                      'Recurrence': 'string',
                      'MinSize': 123,
                      'MaxSize': 123,
                      'DesiredCapacity': 123
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedScheduledUpdateGroupActions': [
                    {
                        'ScheduledActionName': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedScheduledUpdateGroupActions** *(list) --* 
              The names of the scheduled actions that could not be created or updated, including an error message.
              - *(dict) --* 
                Describes a scheduled action that could not be created, updated, or deleted.
                - **ScheduledActionName** *(string) --* 
                  The name of the scheduled action.
                - **ErrorCode** *(string) --* 
                  The error code.
                - **ErrorMessage** *(string) --* 
                  The error message accompanying the error code.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScheduledUpdateGroupActions: list
        :param ScheduledUpdateGroupActions: **[REQUIRED]**
          One or more scheduled actions. The maximum number allowed is 50.
          - *(dict) --*
            Describes one or more scheduled scaling action updates for a specified Auto Scaling group. Used in combination with  BatchPutScheduledUpdateGroupAction .
            When updating a scheduled scaling action, all optional parameters are left unchanged if not specified.
            - **ScheduledActionName** *(string) --* **[REQUIRED]**
              The name of the scaling action.
            - **StartTime** *(datetime) --*
              The time for the action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, ``\"2019-06-01T00:00:00Z\"`` ).
              If you specify ``Recurrence`` and ``StartTime`` , Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
              If you try to schedule the action in the past, Amazon EC2 Auto Scaling returns an error message.
            - **EndTime** *(datetime) --*
              The time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform the action after this time.
            - **Recurrence** *(string) --*
              The recurring schedule for the action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, ``\"30 0 1 1,6,12 *\"`` ). For more information about this format, see `Crontab <http://crontab.org>`__ .
            - **MinSize** *(integer) --*
              The minimum size of the group.
            - **MaxSize** *(integer) --*
              The maximum size of the group.
            - **DesiredCapacity** *(integer) --*
              The number of EC2 instances that should be running in the group.
        :rtype: dict
        :returns:
        """
        pass

    def can_paginate(self, operation_name: str = None):
        """
        Check if an operation can be paginated.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """
        pass

    def complete_lifecycle_action(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleActionResult: str, LifecycleActionToken: str = None, InstanceId: str = None) -> Dict:
        """
        Completes the lifecycle action for the specified token or instance with the specified result.
        This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
        * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances. 
        * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target. 
        * Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate. 
        * If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state. 
        * **If you finish before the timeout period ends, complete the lifecycle action.**   
        For more information, see `Amazon EC2 Auto Scaling Lifecycle Hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CompleteLifecycleAction>`_
        
        **Request Syntax**
        ::
          response = client.complete_lifecycle_action(
              LifecycleHookName='string',
              AutoScalingGroupName='string',
              LifecycleActionToken='string',
              LifecycleActionResult='string',
              InstanceId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LifecycleHookName: string
        :param LifecycleHookName: **[REQUIRED]**
          The name of the lifecycle hook.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LifecycleActionToken: string
        :param LifecycleActionToken:
          A universally unique identifier (UUID) that identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target you specified when you created the lifecycle hook.
        :type LifecycleActionResult: string
        :param LifecycleActionResult: **[REQUIRED]**
          The action for the group to take. This parameter can be either ``CONTINUE`` or ``ABANDON`` .
        :type InstanceId: string
        :param InstanceId:
          The ID of the instance.
        :rtype: dict
        :returns:
        """
        pass

    def create_auto_scaling_group(self, AutoScalingGroupName: str, MinSize: int, MaxSize: int, LaunchConfigurationName: str = None, LaunchTemplate: Dict = None, MixedInstancesPolicy: Dict = None, InstanceId: str = None, DesiredCapacity: int = None, DefaultCooldown: int = None, AvailabilityZones: List = None, LoadBalancerNames: List = None, TargetGroupARNs: List = None, HealthCheckType: str = None, HealthCheckGracePeriod: int = None, PlacementGroup: str = None, VPCZoneIdentifier: str = None, TerminationPolicies: List = None, NewInstancesProtectedFromScaleIn: bool = None, LifecycleHookSpecificationList: List = None, Tags: List = None, ServiceLinkedRoleARN: str = None):
        """
        Creates an Auto Scaling group with the specified name and attributes.
        If you exceed your maximum limit of Auto Scaling groups, the call fails. For information about viewing this limit, see  DescribeAccountLimits . For information about updating this limit, see `Amazon EC2 Auto Scaling Limits <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-limits.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateAutoScalingGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_auto_scaling_group(
              AutoScalingGroupName='string',
              LaunchConfigurationName='string',
              LaunchTemplate={
                  'LaunchTemplateId': 'string',
                  'LaunchTemplateName': 'string',
                  'Version': 'string'
              },
              MixedInstancesPolicy={
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
              InstanceId='string',
              MinSize=123,
              MaxSize=123,
              DesiredCapacity=123,
              DefaultCooldown=123,
              AvailabilityZones=[
                  'string',
              ],
              LoadBalancerNames=[
                  'string',
              ],
              TargetGroupARNs=[
                  'string',
              ],
              HealthCheckType='string',
              HealthCheckGracePeriod=123,
              PlacementGroup='string',
              VPCZoneIdentifier='string',
              TerminationPolicies=[
                  'string',
              ],
              NewInstancesProtectedFromScaleIn=True|False,
              LifecycleHookSpecificationList=[
                  {
                      'LifecycleHookName': 'string',
                      'LifecycleTransition': 'string',
                      'NotificationMetadata': 'string',
                      'HeartbeatTimeout': 123,
                      'DefaultResult': 'string',
                      'NotificationTargetARN': 'string',
                      'RoleARN': 'string'
                  },
              ],
              Tags=[
                  {
                      'ResourceId': 'string',
                      'ResourceType': 'string',
                      'Key': 'string',
                      'Value': 'string',
                      'PropagateAtLaunch': True|False
                  },
              ],
              ServiceLinkedRoleARN='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group. This name must be unique within the scope of your AWS account.
        :type LaunchConfigurationName: string
        :param LaunchConfigurationName:
          The name of the launch configuration. This parameter, a launch template, a mixed instances policy, or an EC2 instance must be specified.
          For more information, see `Creating an Auto Scaling Group Using a Launch Configuration <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type LaunchTemplate: dict
        :param LaunchTemplate:
          The launch template to use to launch instances. This parameter, a launch configuration, a mixed instances policy, or an EC2 instance must be specified.
          For more information, see `Creating an Auto Scaling Group Using a Launch Template <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          - **LaunchTemplateId** *(string) --*
            The ID of the launch template. You must specify either a template ID or a template name.
          - **LaunchTemplateName** *(string) --*
            The name of the launch template. You must specify either a template name or a template ID.
          - **Version** *(string) --*
            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
        :type MixedInstancesPolicy: dict
        :param MixedInstancesPolicy:
          The mixed instances policy to use to launch instances. This parameter, a launch template, a launch configuration, or an EC2 instance must be specified.
          For more information, see `Auto Scaling Groups with Multiple Instance Types and Purchase Options <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
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
              The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
              The default value is ``0`` . If you leave this parameter set to ``0`` , On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the ``OnDemandPercentageAboveBaseCapacity`` setting.
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
        :type InstanceId: string
        :param InstanceId:
          The ID of the instance used to create a launch configuration for the group. This parameter, a launch configuration, a launch template, or a mixed instances policy must be specified.
          When you specify an ID of an instance, Amazon EC2 Auto Scaling creates a new launch configuration and associates it with the group. This launch configuration derives its attributes from the specified instance, except for the block device mapping.
          For more information, see `Create an Auto Scaling Group Using an EC2 Instance <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-from-instance.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type MinSize: integer
        :param MinSize: **[REQUIRED]**
          The minimum size of the group.
        :type MaxSize: integer
        :param MaxSize: **[REQUIRED]**
          The maximum size of the group.
        :type DesiredCapacity: integer
        :param DesiredCapacity:
          The number of EC2 instances that should be running in the group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity, the default is the minimum size of the group.
        :type DefaultCooldown: integer
        :param DefaultCooldown:
          The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default value is ``300`` .
          For more information, see `Scaling Cooldowns <https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type AvailabilityZones: list
        :param AvailabilityZones:
          One or more Availability Zones for the group. This parameter is optional if you specify one or more subnets for ``VPCZoneIdentifier`` .
          Conditional: If your account supports EC2-Classic and VPC, this parameter is required to launch instances into EC2-Classic.
          - *(string) --*
        :type LoadBalancerNames: list
        :param LoadBalancerNames:
          One or more Classic Load Balancers. To specify an Application Load Balancer or a Network Load Balancer, use ``TargetGroupARNs`` instead.
          For more information, see `Using a Load Balancer With an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          - *(string) --*
        :type TargetGroupARNs: list
        :param TargetGroupARNs:
          The Amazon Resource Names (ARN) of the target groups.
          - *(string) --*
        :type HealthCheckType: string
        :param HealthCheckType:
          The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . The default value is ``EC2`` . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.
          For more information, see `Health Checks for Auto Scaling Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type HealthCheckGracePeriod: integer
        :param HealthCheckGracePeriod:
          The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service. During this time, any health check failures for the instance are ignored. The default value is ``0`` .
          For more information, see `Health Checks for Auto Scaling Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          Conditional: This parameter is required if you are adding an ``ELB`` health check.
        :type PlacementGroup: string
        :param PlacementGroup:
          The name of the placement group into which to launch your instances, if any. A placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a placement group. For more information, see `Placement Groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
        :type VPCZoneIdentifier: string
        :param VPCZoneIdentifier:
          A comma-separated list of subnet IDs for your virtual private cloud (VPC).
          If you specify ``VPCZoneIdentifier`` with ``AvailabilityZones`` , the subnets that you specify for this parameter must reside in those Availability Zones.
          Conditional: If your account supports EC2-Classic and VPC, this parameter is required to launch instances into a VPC.
        :type TerminationPolicies: list
        :param TerminationPolicies:
          One or more termination policies used to select the instance to terminate. These policies are executed in the order that they are listed.
          For more information, see `Controlling Which Instances Auto Scaling Terminates During Scale In <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          - *(string) --*
        :type NewInstancesProtectedFromScaleIn: boolean
        :param NewInstancesProtectedFromScaleIn:
          Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.
          For more information about preventing instances from terminating on scale in, see `Instance Protection <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type LifecycleHookSpecificationList: list
        :param LifecycleHookSpecificationList:
          One or more lifecycle hooks.
          - *(dict) --*
            Describes a lifecycle hook. Used in combination with  CreateAutoScalingGroup .
            A lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the instance launches (before it is put into service) or as the instance terminates (before it is fully terminated).
            This step is a part of the procedure for creating a lifecycle hook for an Auto Scaling group:
            * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances.
            * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.
            * **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**
            * If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state using using  RecordLifecycleActionHeartbeat .
            * If you finish before the timeout period ends, complete the lifecycle action using  CompleteLifecycleAction .
            For more information, see `Amazon EC2 Auto Scaling Lifecycle Hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
            You can view the lifecycle hooks for an Auto Scaling group using  DescribeLifecycleHooks . You can modify an existing lifecycle hook or create new lifecycle hooks using  PutLifecycleHook . If you are no longer using a lifecycle hook, you can delete it using  DeleteLifecycleHook .
            - **LifecycleHookName** *(string) --* **[REQUIRED]**
              The name of the lifecycle hook.
            - **LifecycleTransition** *(string) --* **[REQUIRED]**
              The state of the EC2 instance to which you want to attach the lifecycle hook. The valid values are:
              * autoscaling:EC2_INSTANCE_LAUNCHING
              * autoscaling:EC2_INSTANCE_TERMINATING
            - **NotificationMetadata** *(string) --*
              Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
            - **HeartbeatTimeout** *(integer) --*
              The maximum time, in seconds, that can elapse before the lifecycle hook times out.
              If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the ``DefaultResult`` parameter. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat .
            - **DefaultResult** *(string) --*
              Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are ``CONTINUE`` and ``ABANDON`` . The default value is ``ABANDON`` .
            - **NotificationTargetARN** *(string) --*
              The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.
            - **RoleARN** *(string) --*
              The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
        :type Tags: list
        :param Tags:
          One or more tags.
          For more information, see `Tagging Auto Scaling Groups and Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          - *(dict) --*
            Describes a tag for an Auto Scaling group.
            - **ResourceId** *(string) --*
              The name of the group.
            - **ResourceType** *(string) --*
              The type of resource. The only supported value is ``auto-scaling-group`` .
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --*
              The tag value.
            - **PropagateAtLaunch** *(boolean) --*
              Determines whether the tag is added to new instances as they are launched in the group.
        :type ServiceLinkedRoleARN: string
        :param ServiceLinkedRoleARN:
          The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named AWSServiceRoleForAutoScaling, which it creates if it does not exist. For more information, see `Service-Linked Roles <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :returns: None
        """
        pass

    def create_launch_configuration(self, LaunchConfigurationName: str, ImageId: str = None, KeyName: str = None, SecurityGroups: List = None, ClassicLinkVPCId: str = None, ClassicLinkVPCSecurityGroups: List = None, UserData: str = None, InstanceId: str = None, InstanceType: str = None, KernelId: str = None, RamdiskId: str = None, BlockDeviceMappings: List = None, InstanceMonitoring: Dict = None, SpotPrice: str = None, IamInstanceProfile: str = None, EbsOptimized: bool = None, AssociatePublicIpAddress: bool = None, PlacementTenancy: str = None):
        """
        Creates a launch configuration.
        If you exceed your maximum limit of launch configurations, the call fails. For information about viewing this limit, see  DescribeAccountLimits . For information about updating this limit, see `Amazon EC2 Auto Scaling Limits <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-limits.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        For more information, see `Launch Configurations <https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateLaunchConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.create_launch_configuration(
              LaunchConfigurationName='string',
              ImageId='string',
              KeyName='string',
              SecurityGroups=[
                  'string',
              ],
              ClassicLinkVPCId='string',
              ClassicLinkVPCSecurityGroups=[
                  'string',
              ],
              UserData='string',
              InstanceId='string',
              InstanceType='string',
              KernelId='string',
              RamdiskId='string',
              BlockDeviceMappings=[
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
              InstanceMonitoring={
                  'Enabled': True|False
              },
              SpotPrice='string',
              IamInstanceProfile='string',
              EbsOptimized=True|False,
              AssociatePublicIpAddress=True|False,
              PlacementTenancy='string'
          )
        :type LaunchConfigurationName: string
        :param LaunchConfigurationName: **[REQUIRED]**
          The name of the launch configuration. This name must be unique within the scope of your AWS account.
        :type ImageId: string
        :param ImageId:
          The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances.
          If you do not specify ``InstanceId`` , you must specify ``ImageId`` .
          For more information, see `Finding an AMI <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
        :type KeyName: string
        :param KeyName:
          The name of the key pair. For more information, see `Amazon EC2 Key Pairs <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
        :type SecurityGroups: list
        :param SecurityGroups:
          One or more security groups with which to associate the instances.
          If your instances are launched in EC2-Classic, you can either specify security group names or the security group IDs. For more information, see `Amazon EC2 Security Groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
          If your instances are launched into a VPC, specify security group IDs. For more information, see `Security Groups for Your VPC <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html>`__ in the *Amazon Virtual Private Cloud User Guide* .
          - *(string) --*
        :type ClassicLinkVPCId: string
        :param ClassicLinkVPCId:
          The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to. This parameter is supported only if you are launching EC2-Classic instances. For more information, see `ClassicLink <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type ClassicLinkVPCSecurityGroups: list
        :param ClassicLinkVPCSecurityGroups:
          The IDs of one or more security groups for the specified ClassicLink-enabled VPC. For more information, see `ClassicLink <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html>`__ in the *Amazon EC2 User Guide for Linux Instances* and `Linking EC2-Classic Instances to a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html#as-ClassicLink>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          Conditional: This parameter is required if you specify a ClassicLink-enabled VPC, and is not supported otherwise.
          - *(string) --*
        :type UserData: string
        :param UserData:
          The user data to make available to the launched EC2 instances. For more information, see `Instance Metadata and User Data <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
            **This value will be base64 encoded automatically. Do not base64 encode this value prior to performing the operation.**
        :type InstanceId: string
        :param InstanceId:
          The ID of the instance to use to create the launch configuration. The new launch configuration derives attributes from the instance, except for the block device mapping.
          If you do not specify ``InstanceId`` , you must specify both ``ImageId`` and ``InstanceType`` .
          To create a launch configuration with a block device mapping or override any other instance attributes, specify them as part of the same request.
          For more information, see `Create a Launch Configuration Using an EC2 Instance <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-lc-with-instanceID.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type InstanceType: string
        :param InstanceType:
          The instance type of the EC2 instance.
          If you do not specify ``InstanceId`` , you must specify ``InstanceType`` .
          For information about available instance types, see `Available Instance Types <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes>`__ in the *Amazon EC2 User Guide for Linux Instances.*
        :type KernelId: string
        :param KernelId:
          The ID of the kernel associated with the AMI.
        :type RamdiskId: string
        :param RamdiskId:
          The ID of the RAM disk associated with the AMI.
        :type BlockDeviceMappings: list
        :param BlockDeviceMappings:
          One or more mappings that specify how block devices are exposed to the instance. For more information, see `Block Device Mapping <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
          - *(dict) --*
            Describes a block device mapping.
            - **VirtualName** *(string) --*
              The name of the virtual device (for example, ``ephemeral0`` ).
            - **DeviceName** *(string) --* **[REQUIRED]**
              The device name exposed to the EC2 instance (for example, ``/dev/sdh`` or ``xvdh`` ). For more information, see `Device Naming on Linux Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
            - **Ebs** *(dict) --*
              The information about the Amazon EBS volume.
              - **SnapshotId** *(string) --*
                The ID of the snapshot. This parameter is optional if you specify a volume size.
              - **VolumeSize** *(integer) --*
                The volume size, in GiB.
                Constraints: 1-1,024 for ``standard`` , 4-16,384 for ``io1`` , 1-16,384 for ``gp2`` , and 500-16,384 for ``st1`` and ``sc1`` . If you specify a snapshot, the volume size must be equal to or larger than the snapshot size.
                Default: If you create a volume from a snapshot and you don\'t specify a volume size, the default is the snapshot size.
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
        :type InstanceMonitoring: dict
        :param InstanceMonitoring:
          Enables detailed monitoring (``true`` ) or basic monitoring (``false`` ) for the Auto Scaling instances. The default value is ``true`` .
          - **Enabled** *(boolean) --*
            If ``true`` , detailed monitoring is enabled. Otherwise, basic monitoring is enabled.
        :type SpotPrice: string
        :param SpotPrice:
          The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. For more information, see `Launching Spot Instances in Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type IamInstanceProfile: string
        :param IamInstanceProfile:
          The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.
          EC2 instances launched with an IAM role automatically have AWS security credentials available. You can use IAM roles with Amazon EC2 Auto Scaling to automatically enable applications running on your EC2 instances to securely access other AWS resources. For more information, see `Use an IAM Role for Applications That Run on Amazon EC2 Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type EbsOptimized: boolean
        :param EbsOptimized:
          Indicates whether the instance is optimized for Amazon EBS I/O. By default, the instance is not optimized for EBS I/O. The optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization is not available with all instance types. Additional usage charges apply. For more information, see `Amazon EBS-Optimized Instances <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
        :type AssociatePublicIpAddress: boolean
        :param AssociatePublicIpAddress:
          Used for groups that launch instances into a virtual private cloud (VPC). Specifies whether to assign a public IP address to each instance. For more information, see `Launching Auto Scaling Instances in a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          If you specify this parameter, be sure to specify at least one subnet when you create your group.
          Default: If the instance is launched into a default subnet, the default is to assign a public IP address. If the instance is launched into a nondefault subnet, the default is not to assign a public IP address.
        :type PlacementTenancy: string
        :param PlacementTenancy:
          The tenancy of the instance. An instance with a tenancy of ``dedicated`` runs on single-tenant hardware and can only be launched into a VPC.
          To launch Dedicated Instances into a shared tenancy VPC (a VPC with the instance placement tenancy attribute set to ``default`` ), you must set the value of this parameter to ``dedicated`` .
          If you specify this parameter, be sure to specify at least one subnet when you create your group.
          For more information, see `Launching Auto Scaling Instances in a VPC <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          Valid values: ``default`` | ``dedicated``
        :returns: None
        """
        pass

    def create_or_update_tags(self, Tags: List):
        """
        Creates or updates tags for the specified Auto Scaling group.
        When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.
        For more information, see `Tagging Auto Scaling Groups and Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/CreateOrUpdateTags>`_
        
        **Request Syntax**
        ::
          response = client.create_or_update_tags(
              Tags=[
                  {
                      'ResourceId': 'string',
                      'ResourceType': 'string',
                      'Key': 'string',
                      'Value': 'string',
                      'PropagateAtLaunch': True|False
                  },
              ]
          )
        :type Tags: list
        :param Tags: **[REQUIRED]**
          One or more tags.
          - *(dict) --*
            Describes a tag for an Auto Scaling group.
            - **ResourceId** *(string) --*
              The name of the group.
            - **ResourceType** *(string) --*
              The type of resource. The only supported value is ``auto-scaling-group`` .
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --*
              The tag value.
            - **PropagateAtLaunch** *(boolean) --*
              Determines whether the tag is added to new instances as they are launched in the group.
        :returns: None
        """
        pass

    def delete_auto_scaling_group(self, AutoScalingGroupName: str, ForceDelete: bool = None):
        """
        Deletes the specified Auto Scaling group.
        If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed.
        If the group has policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.
        To remove instances from the Auto Scaling group before deleting it, call  DetachInstances with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.
        To terminate all instances before deleting the Auto Scaling group, call  UpdateAutoScalingGroup and set the minimum size and desired capacity of the Auto Scaling group to zero.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteAutoScalingGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_auto_scaling_group(
              AutoScalingGroupName='string',
              ForceDelete=True|False
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ForceDelete: boolean
        :param ForceDelete:
          Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This parameter also deletes any lifecycle actions associated with the group.
        :returns: None
        """
        pass

    def delete_launch_configuration(self, LaunchConfigurationName: str):
        """
        Deletes the specified launch configuration.
        The launch configuration must not be attached to an Auto Scaling group. When this call completes, the launch configuration is no longer available for use.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteLaunchConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_launch_configuration(
              LaunchConfigurationName='string'
          )
        :type LaunchConfigurationName: string
        :param LaunchConfigurationName: **[REQUIRED]**
          The name of the launch configuration.
        :returns: None
        """
        pass

    def delete_lifecycle_hook(self, LifecycleHookName: str, AutoScalingGroupName: str) -> Dict:
        """
        Deletes the specified lifecycle hook.
        If there are any outstanding lifecycle actions, they are completed first (``ABANDON`` for launching instances, ``CONTINUE`` for terminating instances).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteLifecycleHook>`_
        
        **Request Syntax**
        ::
          response = client.delete_lifecycle_hook(
              LifecycleHookName='string',
              AutoScalingGroupName='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LifecycleHookName: string
        :param LifecycleHookName: **[REQUIRED]**
          The name of the lifecycle hook.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :rtype: dict
        :returns:
        """
        pass

    def delete_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str):
        """
        Deletes the specified notification.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteNotificationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.delete_notification_configuration(
              AutoScalingGroupName='string',
              TopicARN='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type TopicARN: string
        :param TopicARN: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.
        :returns: None
        """
        pass

    def delete_policy(self, PolicyName: str, AutoScalingGroupName: str = None):
        """
        Deletes the specified scaling policy.
        Deleting a policy deletes the underlying alarm action, but does not delete the alarm, even if it no longer has an associated action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeletePolicy>`_
        
        **Request Syntax**
        ::
          response = client.delete_policy(
              AutoScalingGroupName='string',
              PolicyName='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**
          The name or Amazon Resource Name (ARN) of the policy.
        :returns: None
        """
        pass

    def delete_scheduled_action(self, AutoScalingGroupName: str, ScheduledActionName: str):
        """
        Deletes the specified scheduled action.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteScheduledAction>`_
        
        **Request Syntax**
        ::
          response = client.delete_scheduled_action(
              AutoScalingGroupName='string',
              ScheduledActionName='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScheduledActionName: string
        :param ScheduledActionName: **[REQUIRED]**
          The name of the action to delete.
        :returns: None
        """
        pass

    def delete_tags(self, Tags: List):
        """
        Deletes the specified tags.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DeleteTags>`_
        
        **Request Syntax**
        ::
          response = client.delete_tags(
              Tags=[
                  {
                      'ResourceId': 'string',
                      'ResourceType': 'string',
                      'Key': 'string',
                      'Value': 'string',
                      'PropagateAtLaunch': True|False
                  },
              ]
          )
        :type Tags: list
        :param Tags: **[REQUIRED]**
          One or more tags.
          - *(dict) --*
            Describes a tag for an Auto Scaling group.
            - **ResourceId** *(string) --*
              The name of the group.
            - **ResourceType** *(string) --*
              The type of resource. The only supported value is ``auto-scaling-group`` .
            - **Key** *(string) --* **[REQUIRED]**
              The tag key.
            - **Value** *(string) --*
              The tag value.
            - **PropagateAtLaunch** *(boolean) --*
              Determines whether the tag is added to new instances as they are launched in the group.
        :returns: None
        """
        pass

    def describe_account_limits(self) -> Dict:
        """
        Describes the current Amazon EC2 Auto Scaling resource limits for your AWS account.
        For information about requesting an increase in these limits, see `Amazon EC2 Auto Scaling Limits <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-limits.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAccountLimits>`_
        
        **Request Syntax**
        ::
          response = client.describe_account_limits()
        
        **Response Syntax**
        ::
            {
                'MaxNumberOfAutoScalingGroups': 123,
                'MaxNumberOfLaunchConfigurations': 123,
                'NumberOfAutoScalingGroups': 123,
                'NumberOfLaunchConfigurations': 123
            }
        
        **Response Structure**
          - *(dict) --* 
            - **MaxNumberOfAutoScalingGroups** *(integer) --* 
              The maximum number of groups allowed for your AWS account. The default limit is 200 per region.
            - **MaxNumberOfLaunchConfigurations** *(integer) --* 
              The maximum number of launch configurations allowed for your AWS account. The default limit is 200 per region.
            - **NumberOfAutoScalingGroups** *(integer) --* 
              The current number of groups for your AWS account.
            - **NumberOfLaunchConfigurations** *(integer) --* 
              The current number of launch configurations for your AWS account.
        :rtype: dict
        :returns:
        """
        pass

    def describe_adjustment_types(self) -> Dict:
        """
        Describes the policy adjustment types for use with  PutScalingPolicy .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAdjustmentTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_adjustment_types()
        
        **Response Syntax**
        ::
            {
                'AdjustmentTypes': [
                    {
                        'AdjustmentType': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AdjustmentTypes** *(list) --* 
              The policy adjustment types.
              - *(dict) --* 
                Describes a policy adjustment type.
                - **AdjustmentType** *(string) --* 
                  The policy adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_auto_scaling_groups(self, AutoScalingGroupNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes one or more Auto Scaling groups.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups>`_
        
        **Request Syntax**
        ::
          response = client.describe_auto_scaling_groups(
              AutoScalingGroupNames=[
                  'string',
              ],
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames:
          The names of the Auto Scaling groups. Each name can be a maximum of 1600 characters. By default, you can only specify up to 50 names. You can optionally increase this limit using the ``MaxRecords`` parameter.
          If you omit this parameter, all Auto Scaling groups are described.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_auto_scaling_instances(self, InstanceIds: List = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        """
        Describes one or more Auto Scaling instances.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingInstances>`_
        
        **Request Syntax**
        ::
          response = client.describe_auto_scaling_instances(
              InstanceIds=[
                  'string',
              ],
              MaxRecords=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to ``MaxRecords`` IDs. If you omit this parameter, all Auto Scaling instances are described. If you specify an ID that does not exist, it is ignored with no error.
          - *(string) --*
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``50`` .
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :rtype: dict
        :returns:
        """
        pass

    def describe_auto_scaling_notification_types(self) -> Dict:
        """
        Describes the notification types that are supported by Amazon EC2 Auto Scaling.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_auto_scaling_notification_types()
        
        **Response Syntax**
        ::
            {
                'AutoScalingNotificationTypes': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AutoScalingNotificationTypes** *(list) --* 
              The notification types.
              - *(string) --* 
        :rtype: dict
        :returns:
        """
        pass

    def describe_launch_configurations(self, LaunchConfigurationNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes one or more launch configurations.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLaunchConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.describe_launch_configurations(
              LaunchConfigurationNames=[
                  'string',
              ],
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type LaunchConfigurationNames: list
        :param LaunchConfigurationNames:
          The launch configuration names. If you omit this parameter, all launch configurations are described.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_lifecycle_hook_types(self) -> Dict:
        """
        Describes the available types of lifecycle hooks.
        The following hook types are supported:
        * autoscaling:EC2_INSTANCE_LAUNCHING 
        * autoscaling:EC2_INSTANCE_TERMINATING 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLifecycleHookTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_lifecycle_hook_types()
        
        **Response Syntax**
        ::
            {
                'LifecycleHookTypes': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LifecycleHookTypes** *(list) --* 
              The lifecycle hook types.
              - *(string) --* 
        :rtype: dict
        :returns:
        """
        pass

    def describe_lifecycle_hooks(self, AutoScalingGroupName: str, LifecycleHookNames: List = None) -> Dict:
        """
        Describes the lifecycle hooks for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLifecycleHooks>`_
        
        **Request Syntax**
        ::
          response = client.describe_lifecycle_hooks(
              AutoScalingGroupName='string',
              LifecycleHookNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'LifecycleHooks': [
                    {
                        'LifecycleHookName': 'string',
                        'AutoScalingGroupName': 'string',
                        'LifecycleTransition': 'string',
                        'NotificationTargetARN': 'string',
                        'RoleARN': 'string',
                        'NotificationMetadata': 'string',
                        'HeartbeatTimeout': 123,
                        'GlobalTimeout': 123,
                        'DefaultResult': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **LifecycleHooks** *(list) --* 
              The lifecycle hooks for the specified group.
              - *(dict) --* 
                Describes a lifecycle hook, which tells Amazon EC2 Auto Scaling that you want to perform an action whenever it launches instances or whenever it terminates instances. Used in response to  DescribeLifecycleHooks .
                - **LifecycleHookName** *(string) --* 
                  The name of the lifecycle hook.
                - **AutoScalingGroupName** *(string) --* 
                  The name of the Auto Scaling group for the lifecycle hook.
                - **LifecycleTransition** *(string) --* 
                  The state of the EC2 instance to which to attach the lifecycle hook. The following are possible values:
                  * autoscaling:EC2_INSTANCE_LAUNCHING 
                  * autoscaling:EC2_INSTANCE_TERMINATING 
                - **NotificationTargetARN** *(string) --* 
                  The ARN of the target that Amazon EC2 Auto Scaling sends notifications to when an instance is in the transition state for the lifecycle hook. The notification target can be either an SQS queue or an SNS topic.
                - **RoleARN** *(string) --* 
                  The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
                - **NotificationMetadata** *(string) --* 
                  Additional information that is included any time Amazon EC2 Auto Scaling sends a message to the notification target.
                - **HeartbeatTimeout** *(integer) --* 
                  The maximum time, in seconds, that can elapse before the lifecycle hook times out. If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the ``DefaultResult`` parameter.
                - **GlobalTimeout** *(integer) --* 
                  The maximum time, in seconds, that an instance can remain in a ``Pending:Wait`` or ``Terminating:Wait`` state. The maximum is 172800 seconds (48 hours) or 100 times ``HeartbeatTimeout`` , whichever is smaller.
                - **DefaultResult** *(string) --* 
                  Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The possible values are ``CONTINUE`` and ``ABANDON`` .
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LifecycleHookNames: list
        :param LifecycleHookNames:
          The names of one or more lifecycle hooks. If you omit this parameter, all lifecycle hooks are described.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_load_balancer_target_groups(self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the target groups for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancerTargetGroups>`_
        
        **Request Syntax**
        ::
          response = client.describe_load_balancer_target_groups(
              AutoScalingGroupName='string',
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``100`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_load_balancers(self, AutoScalingGroupName: str, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the load balancers for the specified Auto Scaling group.
        This operation describes only Classic Load Balancers. If you have Application Load Balancers or Network Load Balancers, use  DescribeLoadBalancerTargetGroups instead.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeLoadBalancers>`_
        
        **Request Syntax**
        ::
          response = client.describe_load_balancers(
              AutoScalingGroupName='string',
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``100`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_metric_collection_types(self) -> Dict:
        """
        Describes the available CloudWatch metrics for Amazon EC2 Auto Scaling.
        The ``GroupStandbyInstances`` metric is not returned by default. You must explicitly request this metric when calling  EnableMetricsCollection .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeMetricCollectionTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_metric_collection_types()
        
        **Response Syntax**
        ::
            {
                'Metrics': [
                    {
                        'Metric': 'string'
                    },
                ],
                'Granularities': [
                    {
                        'Granularity': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Metrics** *(list) --* 
              One or more metrics.
              - *(dict) --* 
                Describes a metric.
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
            - **Granularities** *(list) --* 
              The granularities for the metrics.
              - *(dict) --* 
                Describes a granularity of a metric.
                - **Granularity** *(string) --* 
                  The granularity. The only valid value is ``1Minute`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_notification_configurations(self, AutoScalingGroupNames: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the notification actions associated with the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeNotificationConfigurations>`_
        
        **Request Syntax**
        ::
          response = client.describe_notification_configurations(
              AutoScalingGroupNames=[
                  'string',
              ],
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type AutoScalingGroupNames: list
        :param AutoScalingGroupNames:
          The name of the Auto Scaling group.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_policies(self, AutoScalingGroupName: str = None, PolicyNames: List = None, PolicyTypes: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the policies for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribePolicies>`_
        
        **Request Syntax**
        ::
          response = client.describe_policies(
              AutoScalingGroupName='string',
              PolicyNames=[
                  'string',
              ],
              PolicyTypes=[
                  'string',
              ],
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
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
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to be returned with each call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_scaling_activities(self, ActivityIds: List = None, AutoScalingGroupName: str = None, MaxRecords: int = None, NextToken: str = None) -> Dict:
        """
        Describes one or more scaling activities for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingActivities>`_
        
        **Request Syntax**
        ::
          response = client.describe_scaling_activities(
              ActivityIds=[
                  'string',
              ],
              AutoScalingGroupName='string',
              MaxRecords=123,
              NextToken='string'
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
        :type ActivityIds: list
        :param ActivityIds:
          The activity IDs of the desired scaling activities. You can specify up to 50 IDs. If you omit this parameter, all activities for the past six weeks are described. If unknown activities are requested, they are ignored with no error. If you specify an Auto Scaling group, the results are limited to that group.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``100`` and the maximum value is ``100`` .
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :rtype: dict
        :returns:
        """
        pass

    def describe_scaling_process_types(self) -> Dict:
        """
        Describes the scaling process types for use with  ResumeProcesses and  SuspendProcesses .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScalingProcessTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_scaling_process_types()
        
        **Response Syntax**
        ::
            {
                'Processes': [
                    {
                        'ProcessName': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Processes** *(list) --* 
              The names of the process types.
              - *(dict) --* 
                Describes a process type.
                For more information, see `Scaling Processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types>`__ in the *Amazon EC2 Auto Scaling User Guide* .
                - **ProcessName** *(string) --* 
                  One of the following processes:
                  * ``Launch``   
                  * ``Terminate``   
                  * ``AddToLoadBalancer``   
                  * ``AlarmNotification``   
                  * ``AZRebalance``   
                  * ``HealthCheck``   
                  * ``ReplaceUnhealthy``   
                  * ``ScheduledActions``   
        :rtype: dict
        :returns:
        """
        pass

    def describe_scheduled_actions(self, AutoScalingGroupName: str = None, ScheduledActionNames: List = None, StartTime: datetime = None, EndTime: datetime = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the actions scheduled for your Auto Scaling group that haven't run. To describe the actions that have already run, use  DescribeScalingActivities .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeScheduledActions>`_
        
        **Request Syntax**
        ::
          response = client.describe_scheduled_actions(
              AutoScalingGroupName='string',
              ScheduledActionNames=[
                  'string',
              ],
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
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
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_tags(self, Filters: List = None, NextToken: str = None, MaxRecords: int = None) -> Dict:
        """
        Describes the specified tags.
        You can use filters to limit the results. For example, you can query for the tags for a specific Auto Scaling group. You can specify multiple values for a filter. A tag must match at least one of the specified values for it to be included in the results.
        You can also specify multiple filters. The result includes information for a particular tag only if it matches all the filters. If there's no match, no special message is returned.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTags>`_
        
        **Request Syntax**
        ::
          response = client.describe_tags(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              NextToken='string',
              MaxRecords=123
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
                'NextToken': 'string'
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
            - **NextToken** *(string) --* 
              A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the ``NextToken`` value when requesting the next set of items. This value is null when there are no more items to return.
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
        :type NextToken: string
        :param NextToken:
          The token for the next set of items to return. (You received this token from a previous call.)
        :type MaxRecords: integer
        :param MaxRecords:
          The maximum number of items to return with this call. The default value is ``50`` and the maximum value is ``100`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_termination_policy_types(self) -> Dict:
        """
        Describes the termination policies supported by Amazon EC2 Auto Scaling.
        For more information, see `Controlling Which Auto Scaling Instances Terminate During Scale In <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeTerminationPolicyTypes>`_
        
        **Request Syntax**
        ::
          response = client.describe_termination_policy_types()
        
        **Response Syntax**
        ::
            {
                'TerminationPolicyTypes': [
                    'string',
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TerminationPolicyTypes** *(list) --* 
              The termination policies supported by Amazon EC2 Auto Scaling: ``OldestInstance`` , ``OldestLaunchConfiguration`` , ``NewestInstance`` , ``ClosestToNextInstanceHour`` , ``Default`` , ``OldestLaunchTemplate`` , and ``AllocationStrategy`` .
              - *(string) --* 
        :rtype: dict
        :returns:
        """
        pass

    def detach_instances(self, AutoScalingGroupName: str, ShouldDecrementDesiredCapacity: bool, InstanceIds: List = None) -> Dict:
        """
        Removes one or more instances from the specified Auto Scaling group.
        After the instances are detached, you can manage them independent of the Auto Scaling group.
        If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.
        If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.
        For more information, see `Detach EC2 Instances from Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/detach-instance-asg.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachInstances>`_
        
        **Request Syntax**
        ::
          response = client.detach_instances(
              InstanceIds=[
                  'string',
              ],
              AutoScalingGroupName='string',
              ShouldDecrementDesiredCapacity=True|False
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Activities** *(list) --* 
              The activities related to detaching the instances from the Auto Scaling group.
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
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to 20 instances.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ShouldDecrementDesiredCapacity: boolean
        :param ShouldDecrementDesiredCapacity: **[REQUIRED]**
          Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.
        :rtype: dict
        :returns:
        """
        pass

    def detach_load_balancer_target_groups(self, AutoScalingGroupName: str, TargetGroupARNs: List) -> Dict:
        """
        Detaches one or more target groups from the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachLoadBalancerTargetGroups>`_
        
        **Request Syntax**
        ::
          response = client.detach_load_balancer_target_groups(
              AutoScalingGroupName='string',
              TargetGroupARNs=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type TargetGroupARNs: list
        :param TargetGroupARNs: **[REQUIRED]**
          The Amazon Resource Names (ARN) of the target groups. You can specify up to 10 target groups.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def detach_load_balancers(self, AutoScalingGroupName: str, LoadBalancerNames: List) -> Dict:
        """
        Detaches one or more Classic Load Balancers from the specified Auto Scaling group.
        This operation detaches only Classic Load Balancers. If you have Application Load Balancers or Network Load Balancers, use  DetachLoadBalancerTargetGroups instead.
        When you detach a load balancer, it enters the ``Removing`` state while deregistering the instances in the group. When all instances are deregistered, then you can no longer describe the load balancer using  DescribeLoadBalancers . The instances remain running.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DetachLoadBalancers>`_
        
        **Request Syntax**
        ::
          response = client.detach_load_balancers(
              AutoScalingGroupName='string',
              LoadBalancerNames=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LoadBalancerNames: list
        :param LoadBalancerNames: **[REQUIRED]**
          The names of the load balancers. You can specify up to 10 load balancers.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def disable_metrics_collection(self, AutoScalingGroupName: str, Metrics: List = None):
        """
        Disables group metrics for the specified Auto Scaling group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DisableMetricsCollection>`_
        
        **Request Syntax**
        ::
          response = client.disable_metrics_collection(
              AutoScalingGroupName='string',
              Metrics=[
                  'string',
              ]
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type Metrics: list
        :param Metrics:
          One or more of the following metrics. If you omit this parameter, all metrics are disabled.
          * ``GroupMinSize``
          * ``GroupMaxSize``
          * ``GroupDesiredCapacity``
          * ``GroupInServiceInstances``
          * ``GroupPendingInstances``
          * ``GroupStandbyInstances``
          * ``GroupTerminatingInstances``
          * ``GroupTotalInstances``
          - *(string) --*
        :returns: None
        """
        pass

    def enable_metrics_collection(self, AutoScalingGroupName: str, Granularity: str, Metrics: List = None):
        """
        Enables group metrics for the specified Auto Scaling group. For more information, see `Monitoring Your Auto Scaling Groups and Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/EnableMetricsCollection>`_
        
        **Request Syntax**
        ::
          response = client.enable_metrics_collection(
              AutoScalingGroupName='string',
              Metrics=[
                  'string',
              ],
              Granularity='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type Metrics: list
        :param Metrics:
          One or more of the following metrics. If you omit this parameter, all metrics are enabled.
          * ``GroupMinSize``
          * ``GroupMaxSize``
          * ``GroupDesiredCapacity``
          * ``GroupInServiceInstances``
          * ``GroupPendingInstances``
          * ``GroupStandbyInstances``
          * ``GroupTerminatingInstances``
          * ``GroupTotalInstances``
          - *(string) --*
        :type Granularity: string
        :param Granularity: **[REQUIRED]**
          The granularity to associate with the metrics to collect. The only valid value is ``1Minute`` .
        :returns: None
        """
        pass

    def enter_standby(self, AutoScalingGroupName: str, ShouldDecrementDesiredCapacity: bool, InstanceIds: List = None) -> Dict:
        """
        Moves the specified instances into the standby state.
        For more information, see `Temporarily Removing Instances from Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/EnterStandby>`_
        
        **Request Syntax**
        ::
          response = client.enter_standby(
              InstanceIds=[
                  'string',
              ],
              AutoScalingGroupName='string',
              ShouldDecrementDesiredCapacity=True|False
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Activities** *(list) --* 
              The activities related to moving instances into ``Standby`` mode.
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
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to 20 instances.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ShouldDecrementDesiredCapacity: boolean
        :param ShouldDecrementDesiredCapacity: **[REQUIRED]**
          Indicates whether to decrement the desired capacity of the Auto Scaling group by the number of instances moved to ``Standby`` mode.
        :rtype: dict
        :returns:
        """
        pass

    def execute_policy(self, PolicyName: str, AutoScalingGroupName: str = None, HonorCooldown: bool = None, MetricValue: float = None, BreachThreshold: float = None):
        """
        Executes the specified policy.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ExecutePolicy>`_
        
        **Request Syntax**
        ::
          response = client.execute_policy(
              AutoScalingGroupName='string',
              PolicyName='string',
              HonorCooldown=True|False,
              MetricValue=123.0,
              BreachThreshold=123.0
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName:
          The name of the Auto Scaling group.
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**
          The name or ARN of the policy.
        :type HonorCooldown: boolean
        :param HonorCooldown:
          Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before executing the policy.
          This parameter is not supported if the policy type is ``StepScaling`` .
          For more information, see `Scaling Cooldowns <https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type MetricValue: float
        :param MetricValue:
          The metric value to compare to ``BreachThreshold`` . This enables you to execute a policy of type ``StepScaling`` and determine which step adjustment to use. For example, if the breach threshold is 50 and you want to use a step adjustment with a lower bound of 0 and an upper bound of 10, you can set the metric value to 59.
          If you specify a metric value that doesn\'t correspond to a step adjustment for the policy, the call returns an error.
          Conditional: This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.
        :type BreachThreshold: float
        :param BreachThreshold:
          The breach threshold for the alarm.
          Conditional: This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.
        :returns: None
        """
        pass

    def exit_standby(self, AutoScalingGroupName: str, InstanceIds: List = None) -> Dict:
        """
        Moves the specified instances out of the standby state.
        For more information, see `Temporarily Removing Instances from Your Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ExitStandby>`_
        
        **Request Syntax**
        ::
          response = client.exit_standby(
              InstanceIds=[
                  'string',
              ],
              AutoScalingGroupName='string'
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
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Activities** *(list) --* 
              The activities related to moving instances out of ``Standby`` mode.
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
        :type InstanceIds: list
        :param InstanceIds:
          The IDs of the instances. You can specify up to 20 instances.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :rtype: dict
        :returns:
        """
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        """
        Generate a presigned url given a client, its method, and arguments
        :type ClientMethod: string
        :param ClientMethod: The client method to presign for
        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.
        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)
        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method\'s model.
        :returns: The presigned url
        """
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        """
        Create a paginator for an operation.
        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you\'d normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator(\"create_foo\")``.
        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.
        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        """
        Returns an object that can wait for some condition.
        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.
        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """
        pass

    def put_lifecycle_hook(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleTransition: str = None, RoleARN: str = None, NotificationTargetARN: str = None, NotificationMetadata: str = None, HeartbeatTimeout: int = None, DefaultResult: str = None) -> Dict:
        """
        Creates or updates a lifecycle hook for the specified Auto Scaling group.
        A lifecycle hook tells Amazon EC2 Auto Scaling to perform an action on an instance when the instance launches (before it is put into service) or as the instance terminates (before it is fully terminated).
        This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
        * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances. 
        * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target. 
        * **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**   
        * If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state using using  RecordLifecycleActionHeartbeat . 
        * If you finish before the timeout period ends, complete the lifecycle action using  CompleteLifecycleAction . 
        For more information, see `Amazon EC2 Auto Scaling Lifecycle Hooks <https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.
        You can view the lifecycle hooks for an Auto Scaling group using  DescribeLifecycleHooks . If you are no longer using a lifecycle hook, you can delete it using  DeleteLifecycleHook .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutLifecycleHook>`_
        
        **Request Syntax**
        ::
          response = client.put_lifecycle_hook(
              LifecycleHookName='string',
              AutoScalingGroupName='string',
              LifecycleTransition='string',
              RoleARN='string',
              NotificationTargetARN='string',
              NotificationMetadata='string',
              HeartbeatTimeout=123,
              DefaultResult='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LifecycleHookName: string
        :param LifecycleHookName: **[REQUIRED]**
          The name of the lifecycle hook.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LifecycleTransition: string
        :param LifecycleTransition:
          The instance state to which you want to attach the lifecycle hook. The valid values are:
          * autoscaling:EC2_INSTANCE_LAUNCHING
          * autoscaling:EC2_INSTANCE_TERMINATING
          Conditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
        :type RoleARN: string
        :param RoleARN:
          The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target, for example, an Amazon SNS topic or an Amazon SQS queue.
          Conditional: This parameter is required for new lifecycle hooks, but optional when updating existing hooks.
        :type NotificationTargetARN: string
        :param NotificationTargetARN:
          The ARN of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in the transition state for the lifecycle hook. This target can be either an SQS queue or an SNS topic.
          If you specify an empty string, this overrides the current ARN.
          This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.
          When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: ``\"Event\": \"autoscaling:TEST_NOTIFICATION\"`` .
        :type NotificationMetadata: string
        :param NotificationMetadata:
          Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
        :type HeartbeatTimeout: integer
        :param HeartbeatTimeout:
          The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from ``30`` to ``7200`` seconds. The default value is ``3600`` seconds (1 hour).
          If the lifecycle hook times out, Amazon EC2 Auto Scaling performs the action that you specified in the ``DefaultResult`` parameter. You can prevent the lifecycle hook from timing out by calling  RecordLifecycleActionHeartbeat .
        :type DefaultResult: string
        :param DefaultResult:
          Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. This parameter can be either ``CONTINUE`` or ``ABANDON`` . The default value is ``ABANDON`` .
        :rtype: dict
        :returns:
        """
        pass

    def put_notification_configuration(self, AutoScalingGroupName: str, TopicARN: str, NotificationTypes: List):
        """
        Configures an Auto Scaling group to send notifications when specified events take place. Subscribers to the specified topic can have messages delivered to an endpoint such as a web server or an email address.
        This configuration overwrites any existing configuration.
        For more information, see `Getting Amazon SNS Notifications When Your Auto Scaling Group Scales <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutNotificationConfiguration>`_
        
        **Request Syntax**
        ::
          response = client.put_notification_configuration(
              AutoScalingGroupName='string',
              TopicARN='string',
              NotificationTypes=[
                  'string',
              ]
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type TopicARN: string
        :param TopicARN: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (Amazon SNS) topic.
        :type NotificationTypes: list
        :param NotificationTypes: **[REQUIRED]**
          The type of event that causes the notification to be sent. For more information about notification types supported by Amazon EC2 Auto Scaling, see  DescribeAutoScalingNotificationTypes .
          - *(string) --*
        :returns: None
        """
        pass

    def put_scaling_policy(self, AutoScalingGroupName: str, PolicyName: str, PolicyType: str = None, AdjustmentType: str = None, MinAdjustmentStep: int = None, MinAdjustmentMagnitude: int = None, ScalingAdjustment: int = None, Cooldown: int = None, MetricAggregationType: str = None, StepAdjustments: List = None, EstimatedInstanceWarmup: int = None, TargetTrackingConfiguration: Dict = None) -> Dict:
        """
        Creates or updates a policy for an Auto Scaling group. To update an existing policy, use the existing policy name and set the parameters to change. Any existing parameter not changed in an update to an existing policy is not changed in this update request.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutScalingPolicy>`_
        
        **Request Syntax**
        ::
          response = client.put_scaling_policy(
              AutoScalingGroupName='string',
              PolicyName='string',
              PolicyType='string',
              AdjustmentType='string',
              MinAdjustmentStep=123,
              MinAdjustmentMagnitude=123,
              ScalingAdjustment=123,
              Cooldown=123,
              MetricAggregationType='string',
              StepAdjustments=[
                  {
                      'MetricIntervalLowerBound': 123.0,
                      'MetricIntervalUpperBound': 123.0,
                      'ScalingAdjustment': 123
                  },
              ],
              EstimatedInstanceWarmup=123,
              TargetTrackingConfiguration={
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
          )
        
        **Response Syntax**
        ::
            {
                'PolicyARN': 'string',
                'Alarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmARN': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            Contains the output of PutScalingPolicy.
            - **PolicyARN** *(string) --* 
              The Amazon Resource Name (ARN) of the policy.
            - **Alarms** *(list) --* 
              The CloudWatch alarms created for the target tracking scaling policy.
              - *(dict) --* 
                Describes an alarm.
                - **AlarmName** *(string) --* 
                  The name of the alarm.
                - **AlarmARN** *(string) --* 
                  The Amazon Resource Name (ARN) of the alarm.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**
          The name of the policy.
        :type PolicyType: string
        :param PolicyType:
          The policy type. The valid values are ``SimpleScaling`` , ``StepScaling`` , and ``TargetTrackingScaling`` . If the policy type is null, the value is treated as ``SimpleScaling`` .
        :type AdjustmentType: string
        :param AdjustmentType:
          The adjustment type. The valid values are ``ChangeInCapacity`` , ``ExactCapacity`` , and ``PercentChangeInCapacity`` .
          This parameter is supported if the policy type is ``SimpleScaling`` or ``StepScaling`` .
          For more information, see `Dynamic Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type MinAdjustmentStep: integer
        :param MinAdjustmentStep:
          Available for backward compatibility. Use ``MinAdjustmentMagnitude`` instead.
        :type MinAdjustmentMagnitude: integer
        :param MinAdjustmentMagnitude:
          The minimum number of instances to scale. If the value of ``AdjustmentType`` is ``PercentChangeInCapacity`` , the scaling policy changes the ``DesiredCapacity`` of the Auto Scaling group by at least this many instances. Otherwise, the error is ``ValidationError`` .
          This parameter is supported if the policy type is ``SimpleScaling`` or ``StepScaling`` .
        :type ScalingAdjustment: integer
        :param ScalingAdjustment:
          The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
          Conditional: This parameter is required if the policy type is ``SimpleScaling`` and not supported otherwise.
        :type Cooldown: integer
        :param Cooldown:
          The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start. If this parameter is not specified, the default cooldown period for the group applies.
          This parameter is supported if the policy type is ``SimpleScaling`` .
          For more information, see `Scaling Cooldowns <https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type MetricAggregationType: string
        :param MetricAggregationType:
          The aggregation type for the CloudWatch metrics. The valid values are ``Minimum`` , ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as ``Average`` .
          This parameter is supported if the policy type is ``StepScaling`` .
        :type StepAdjustments: list
        :param StepAdjustments:
          A set of adjustments that enable you to scale based on the size of the alarm breach.
          Conditional: This parameter is required if the policy type is ``StepScaling`` and not supported otherwise.
          - *(dict) --*
            Describes an adjustment based on the difference between the value of the aggregated CloudWatch metric and the breach threshold that you\'ve defined for the alarm. Used in combination with  PutScalingPolicy .
            For the following examples, suppose that you have an alarm with a breach threshold of 50:
            * To trigger the adjustment when the metric is greater than or equal to 50 and less than 60, specify a lower bound of 0 and an upper bound of 10.
            * To trigger the adjustment when the metric is greater than 40 and less than or equal to 50, specify a lower bound of -10 and an upper bound of 0.
            There are a few rules for the step adjustments for your step policy:
            * The ranges of your step adjustments can\'t overlap or have a gap.
            * At most, one step adjustment can have a null lower bound. If one step adjustment has a negative lower bound, then there must be a step adjustment with a null lower bound.
            * At most, one step adjustment can have a null upper bound. If one step adjustment has a positive upper bound, then there must be a step adjustment with a null upper bound.
            * The upper and lower bound can\'t be null in the same step adjustment.
            - **MetricIntervalLowerBound** *(float) --*
              The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it is exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.
            - **MetricIntervalUpperBound** *(float) --*
              The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it is inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.
              The upper bound must be greater than the lower bound.
            - **ScalingAdjustment** *(integer) --* **[REQUIRED]**
              The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.
        :type EstimatedInstanceWarmup: integer
        :param EstimatedInstanceWarmup:
          The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. The default is to use the value specified for the default cooldown period for the group.
          This parameter is supported if the policy type is ``StepScaling`` or ``TargetTrackingScaling`` .
        :type TargetTrackingConfiguration: dict
        :param TargetTrackingConfiguration:
          A target tracking scaling policy. Includes support for predefined or customized metrics.
          Conditional: This parameter is required if the policy type is ``TargetTrackingScaling`` and not supported otherwise.
          - **PredefinedMetricSpecification** *(dict) --*
            A predefined metric. You can specify either a predefined metric or a customized metric.
            - **PredefinedMetricType** *(string) --* **[REQUIRED]**
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
            - **MetricName** *(string) --* **[REQUIRED]**
              The name of the metric.
            - **Namespace** *(string) --* **[REQUIRED]**
              The namespace of the metric.
            - **Dimensions** *(list) --*
              The dimensions of the metric.
              Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
              - *(dict) --*
                Describes the dimension of a metric.
                - **Name** *(string) --* **[REQUIRED]**
                  The name of the dimension.
                - **Value** *(string) --* **[REQUIRED]**
                  The value of the dimension.
            - **Statistic** *(string) --* **[REQUIRED]**
              The statistic of the metric.
            - **Unit** *(string) --*
              The unit of the metric.
          - **TargetValue** *(float) --* **[REQUIRED]**
            The target value for the metric.
          - **DisableScaleIn** *(boolean) --*
            Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn\'t remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is disabled.
        :rtype: dict
        :returns:
        """
        pass

    def put_scheduled_update_group_action(self, AutoScalingGroupName: str, ScheduledActionName: str, Time: datetime = None, StartTime: datetime = None, EndTime: datetime = None, Recurrence: str = None, MinSize: int = None, MaxSize: int = None, DesiredCapacity: int = None):
        """
        Creates or updates a scheduled scaling action for an Auto Scaling group. If you leave a parameter unspecified when updating a scheduled scaling action, the corresponding value remains unchanged.
        For more information, see `Scheduled Scaling <https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutScheduledUpdateGroupAction>`_
        
        **Request Syntax**
        ::
          response = client.put_scheduled_update_group_action(
              AutoScalingGroupName='string',
              ScheduledActionName='string',
              Time=datetime(2015, 1, 1),
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Recurrence='string',
              MinSize=123,
              MaxSize=123,
              DesiredCapacity=123
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScheduledActionName: string
        :param ScheduledActionName: **[REQUIRED]**
          The name of this scaling action.
        :type Time: datetime
        :param Time:
          This parameter is deprecated.
        :type StartTime: datetime
        :param StartTime:
          The time for this action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, ``\"2019-06-01T00:00:00Z\"`` ).
          If you specify ``Recurrence`` and ``StartTime`` , Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
          If you try to schedule your action in the past, Amazon EC2 Auto Scaling returns an error message.
        :type EndTime: datetime
        :param EndTime:
          The time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform the action after this time.
        :type Recurrence: string
        :param Recurrence:
          The recurring schedule for this action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, ``\"30 0 1 1,6,12 *\"`` ). For more information about this format, see `Crontab <http://crontab.org>`__ .
        :type MinSize: integer
        :param MinSize:
          The minimum size for the Auto Scaling group.
        :type MaxSize: integer
        :param MaxSize:
          The maximum size for the Auto Scaling group.
        :type DesiredCapacity: integer
        :param DesiredCapacity:
          The number of EC2 instances that should be running in the group.
        :returns: None
        """
        pass

    def record_lifecycle_action_heartbeat(self, LifecycleHookName: str, AutoScalingGroupName: str, LifecycleActionToken: str = None, InstanceId: str = None) -> Dict:
        """
        Records a heartbeat for the lifecycle action associated with the specified token or instance. This extends the timeout by the length of time defined using  PutLifecycleHook .
        This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:
        * (Optional) Create a Lambda function and a rule that allows CloudWatch Events to invoke your Lambda function when Amazon EC2 Auto Scaling launches or terminates instances. 
        * (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target. 
        * Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate. 
        * **If you need more time, record the lifecycle action heartbeat to keep the instance in a pending state.**   
        * If you finish before the timeout period ends, complete the lifecycle action. 
        For more information, see `Auto Scaling Lifecycle <https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/RecordLifecycleActionHeartbeat>`_
        
        **Request Syntax**
        ::
          response = client.record_lifecycle_action_heartbeat(
              LifecycleHookName='string',
              AutoScalingGroupName='string',
              LifecycleActionToken='string',
              InstanceId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type LifecycleHookName: string
        :param LifecycleHookName: **[REQUIRED]**
          The name of the lifecycle hook.
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LifecycleActionToken: string
        :param LifecycleActionToken:
          A token that uniquely identifies a specific lifecycle action associated with an instance. Amazon EC2 Auto Scaling sends this token to the notification target that you specified when you created the lifecycle hook.
        :type InstanceId: string
        :param InstanceId:
          The ID of the instance.
        :rtype: dict
        :returns:
        """
        pass

    def resume_processes(self, AutoScalingGroupName: str, ScalingProcesses: List = None):
        """
        Resumes the specified suspended automatic scaling processes, or all suspended process, for the specified Auto Scaling group.
        For more information, see `Suspending and Resuming Scaling Processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/ResumeProcesses>`_
        
        **Request Syntax**
        ::
          response = client.resume_processes(
              AutoScalingGroupName='string',
              ScalingProcesses=[
                  'string',
              ]
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScalingProcesses: list
        :param ScalingProcesses:
          One or more of the following processes. If you omit this parameter, all processes are specified.
          * ``Launch``
          * ``Terminate``
          * ``HealthCheck``
          * ``ReplaceUnhealthy``
          * ``AZRebalance``
          * ``AlarmNotification``
          * ``ScheduledActions``
          * ``AddToLoadBalancer``
          - *(string) --*
        :returns: None
        """
        pass

    def set_desired_capacity(self, AutoScalingGroupName: str, DesiredCapacity: int, HonorCooldown: bool = None):
        """
        Sets the size of the specified Auto Scaling group.
        For more information about desired capacity, see `What Is Amazon EC2 Auto Scaling? <https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetDesiredCapacity>`_
        
        **Request Syntax**
        ::
          response = client.set_desired_capacity(
              AutoScalingGroupName='string',
              DesiredCapacity=123,
              HonorCooldown=True|False
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type DesiredCapacity: integer
        :param DesiredCapacity: **[REQUIRED]**
          The number of EC2 instances that should be running in the Auto Scaling group.
        :type HonorCooldown: boolean
        :param HonorCooldown:
          Indicates whether Amazon EC2 Auto Scaling waits for the cooldown period to complete before initiating a scaling activity to set your Auto Scaling group to its new capacity. By default, Amazon EC2 Auto Scaling does not honor the cooldown period during manual scaling activities.
        :returns: None
        """
        pass

    def set_instance_health(self, InstanceId: str, HealthStatus: str, ShouldRespectGracePeriod: bool = None):
        """
        Sets the health status of the specified instance.
        For more information, see `Health Checks for Auto Scaling Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetInstanceHealth>`_
        
        **Request Syntax**
        ::
          response = client.set_instance_health(
              InstanceId='string',
              HealthStatus='string',
              ShouldRespectGracePeriod=True|False
          )
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The ID of the instance.
        :type HealthStatus: string
        :param HealthStatus: **[REQUIRED]**
          The health status of the instance. Set to ``Healthy`` to have the instance remain in service. Set to ``Unhealthy`` to have the instance be out of service. Amazon EC2 Auto Scaling terminates and replaces the unhealthy instance.
        :type ShouldRespectGracePeriod: boolean
        :param ShouldRespectGracePeriod:
          If the Auto Scaling group of the specified instance has a ``HealthCheckGracePeriod`` specified for the group, by default, this call respects the grace period. Set this to ``False`` , to have the call not respect the grace period associated with the group.
          For more information about the health check grace period, see  CreateAutoScalingGroup .
        :returns: None
        """
        pass

    def set_instance_protection(self, InstanceIds: List, AutoScalingGroupName: str, ProtectedFromScaleIn: bool) -> Dict:
        """
        Updates the instance protection settings of the specified instances.
        For more information about preventing instances that are part of an Auto Scaling group from terminating on scale in, see `Instance Protection <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SetInstanceProtection>`_
        
        **Request Syntax**
        ::
          response = client.set_instance_protection(
              InstanceIds=[
                  'string',
              ],
              AutoScalingGroupName='string',
              ProtectedFromScaleIn=True|False
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type InstanceIds: list
        :param InstanceIds: **[REQUIRED]**
          One or more instance IDs.
          - *(string) --*
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ProtectedFromScaleIn: boolean
        :param ProtectedFromScaleIn: **[REQUIRED]**
          Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.
        :rtype: dict
        :returns:
        """
        pass

    def suspend_processes(self, AutoScalingGroupName: str, ScalingProcesses: List = None):
        """
        Suspends the specified automatic scaling processes, or all processes, for the specified Auto Scaling group.
        If you suspend either the ``Launch`` or ``Terminate`` process types, it can prevent other process types from functioning properly.
        To resume processes that have been suspended, use  ResumeProcesses .
        For more information, see `Suspending and Resuming Scaling Processes <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/SuspendProcesses>`_
        
        **Request Syntax**
        ::
          response = client.suspend_processes(
              AutoScalingGroupName='string',
              ScalingProcesses=[
                  'string',
              ]
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type ScalingProcesses: list
        :param ScalingProcesses:
          One or more of the following processes. If you omit this parameter, all processes are specified.
          * ``Launch``
          * ``Terminate``
          * ``HealthCheck``
          * ``ReplaceUnhealthy``
          * ``AZRebalance``
          * ``AlarmNotification``
          * ``ScheduledActions``
          * ``AddToLoadBalancer``
          - *(string) --*
        :returns: None
        """
        pass

    def terminate_instance_in_auto_scaling_group(self, InstanceId: str, ShouldDecrementDesiredCapacity: bool) -> Dict:
        """
        Terminates the specified instance and optionally adjusts the desired group size.
        This call simply makes a termination request. The instance is not terminated immediately.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup>`_
        
        **Request Syntax**
        ::
          response = client.terminate_instance_in_auto_scaling_group(
              InstanceId='string',
              ShouldDecrementDesiredCapacity=True|False
          )
        
        **Response Syntax**
        ::
            {
                'Activity': {
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
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Activity** *(dict) --* 
              A scaling activity.
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
        :type InstanceId: string
        :param InstanceId: **[REQUIRED]**
          The ID of the instance.
        :type ShouldDecrementDesiredCapacity: boolean
        :param ShouldDecrementDesiredCapacity: **[REQUIRED]**
          Indicates whether terminating the instance also decrements the size of the Auto Scaling group.
        :rtype: dict
        :returns:
        """
        pass

    def update_auto_scaling_group(self, AutoScalingGroupName: str, LaunchConfigurationName: str = None, LaunchTemplate: Dict = None, MixedInstancesPolicy: Dict = None, MinSize: int = None, MaxSize: int = None, DesiredCapacity: int = None, DefaultCooldown: int = None, AvailabilityZones: List = None, HealthCheckType: str = None, HealthCheckGracePeriod: int = None, PlacementGroup: str = None, VPCZoneIdentifier: str = None, TerminationPolicies: List = None, NewInstancesProtectedFromScaleIn: bool = None, ServiceLinkedRoleARN: str = None):
        """
        Updates the configuration for the specified Auto Scaling group.
        The new settings take effect on any scaling activities after this call returns. Scaling activities that are currently in progress aren't affected.
        To update an Auto Scaling group with a launch configuration with ``InstanceMonitoring`` set to ``false`` , you must first disable the collection of group metrics. Otherwise, you get an error. If you have previously enabled the collection of group metrics, you can disable it using  DisableMetricsCollection .
        Note the following:
        * If you specify a new value for ``MinSize`` without specifying a value for ``DesiredCapacity`` , and the new ``MinSize`` is larger than the current size of the group, we implicitly call  SetDesiredCapacity to set the size of the group to the new value of ``MinSize`` . 
        * If you specify a new value for ``MaxSize`` without specifying a value for ``DesiredCapacity`` , and the new ``MaxSize`` is smaller than the current size of the group, we implicitly call  SetDesiredCapacity to set the size of the group to the new value of ``MaxSize`` . 
        * All other optional parameters are left unchanged if not specified. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/UpdateAutoScalingGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_auto_scaling_group(
              AutoScalingGroupName='string',
              LaunchConfigurationName='string',
              LaunchTemplate={
                  'LaunchTemplateId': 'string',
                  'LaunchTemplateName': 'string',
                  'Version': 'string'
              },
              MixedInstancesPolicy={
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
              MinSize=123,
              MaxSize=123,
              DesiredCapacity=123,
              DefaultCooldown=123,
              AvailabilityZones=[
                  'string',
              ],
              HealthCheckType='string',
              HealthCheckGracePeriod=123,
              PlacementGroup='string',
              VPCZoneIdentifier='string',
              TerminationPolicies=[
                  'string',
              ],
              NewInstancesProtectedFromScaleIn=True|False,
              ServiceLinkedRoleARN='string'
          )
        :type AutoScalingGroupName: string
        :param AutoScalingGroupName: **[REQUIRED]**
          The name of the Auto Scaling group.
        :type LaunchConfigurationName: string
        :param LaunchConfigurationName:
          The name of the launch configuration. If you specify this parameter, you can\'t specify a launch template or a mixed instances policy.
        :type LaunchTemplate: dict
        :param LaunchTemplate:
          The launch template and version to use to specify the updates. If you specify this parameter, you can\'t specify a launch configuration or a mixed instances policy.
          - **LaunchTemplateId** *(string) --*
            The ID of the launch template. You must specify either a template ID or a template name.
          - **LaunchTemplateName** *(string) --*
            The name of the launch template. You must specify either a template name or a template ID.
          - **Version** *(string) --*
            The version number, ``$Latest`` , or ``$Default`` . If the value is ``$Latest`` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is ``$Default`` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is ``$Default`` .
        :type MixedInstancesPolicy: dict
        :param MixedInstancesPolicy:
          The mixed instances policy to use to specify the updates. If you specify this parameter, you can\'t specify a launch configuration or a launch template.
          For more information, see `Auto Scaling Groups with Multiple Instance Types and Purchase Options <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
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
              The minimum amount of the Auto Scaling group\'s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.
              The default value is ``0`` . If you leave this parameter set to ``0`` , On-Demand Instances are launched as a percentage of the Auto Scaling group\'s desired capacity, per the ``OnDemandPercentageAboveBaseCapacity`` setting.
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
        :type MinSize: integer
        :param MinSize:
          The minimum size of the Auto Scaling group.
        :type MaxSize: integer
        :param MaxSize:
          The maximum size of the Auto Scaling group.
        :type DesiredCapacity: integer
        :param DesiredCapacity:
          The number of EC2 instances that should be running in the Auto Scaling group. This number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group.
        :type DefaultCooldown: integer
        :param DefaultCooldown:
          The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. The default value is ``300`` .
          For more information, see `Scaling Cooldowns <https://docs.aws.amazon.com/autoscaling/ec2/userguide/Cooldown.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type AvailabilityZones: list
        :param AvailabilityZones:
          One or more Availability Zones for the group.
          - *(string) --*
        :type HealthCheckType: string
        :param HealthCheckType:
          The service to use for the health checks. The valid values are ``EC2`` and ``ELB`` . If you configure an Auto Scaling group to use ELB health checks, it considers the instance unhealthy if it fails either the EC2 status checks or the load balancer health checks.
        :type HealthCheckGracePeriod: integer
        :param HealthCheckGracePeriod:
          The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service. The default value is ``0`` .
          For more information, see `Health Checks for Auto Scaling Instances <https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          Conditional: This parameter is required if you are adding an ``ELB`` health check.
        :type PlacementGroup: string
        :param PlacementGroup:
          The name of the placement group into which to launch your instances, if any. A placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a placement group. For more information, see `Placement Groups <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html>`__ in the *Amazon EC2 User Guide for Linux Instances* .
        :type VPCZoneIdentifier: string
        :param VPCZoneIdentifier:
          A comma-separated list of subnet IDs, if you are launching into a VPC.
          If you specify ``VPCZoneIdentifier`` with ``AvailabilityZones`` , the subnets that you specify for this parameter must reside in those Availability Zones.
        :type TerminationPolicies: list
        :param TerminationPolicies:
          A standalone termination policy or a list of termination policies used to select the instance to terminate. The policies are executed in the order that they are listed.
          For more information, see `Controlling Which Instances Auto Scaling Terminates During Scale In <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
          - *(string) --*
        :type NewInstancesProtectedFromScaleIn: boolean
        :param NewInstancesProtectedFromScaleIn:
          Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.
          For more information about preventing instances from terminating on scale in, see `Instance Protection <https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :type ServiceLinkedRoleARN: string
        :param ServiceLinkedRoleARN:
          The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf. For more information, see `Service-Linked Roles <https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-service-linked-role.html>`__ in the *Amazon EC2 Auto Scaling User Guide* .
        :returns: None
        """
        pass
