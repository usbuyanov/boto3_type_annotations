from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
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

    def create_cluster(self, clusterName: str = None, tags: List = None) -> Dict:
        """
        Creates a new Amazon ECS cluster. By default, your account receives a ``default`` cluster when you launch your first container instance. However, you can create your own cluster with a unique name with the ``CreateCluster`` action.
        .. note::
          When you call the  CreateCluster API operation, Amazon ECS attempts to create the service-linked role for your account so that required resources in other AWS services can be managed on your behalf. However, if the IAM user that makes the call does not have permissions to create the service-linked role, it is not created. For more information, see `Using Service-Linked Roles for Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateCluster>`_
        
        **Request Syntax**
        ::
          response = client.create_cluster(
              clusterName='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'cluster': {
                    'clusterArn': 'string',
                    'clusterName': 'string',
                    'status': 'string',
                    'registeredContainerInstancesCount': 123,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'activeServicesCount': 123,
                    'statistics': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cluster** *(dict) --* 
              The full description of your new cluster.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..
              - **clusterName** *(string) --* 
                A user-generated string that you use to identify your cluster.
              - **status** *(string) --* 
                The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.
              - **registeredContainerInstancesCount** *(integer) --* 
                The number of container instances registered into the cluster. This includes container instances in both ``ACTIVE`` and ``DRAINING`` status.
              - **runningTasksCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``RUNNING`` state.
              - **pendingTasksCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``PENDING`` state.
              - **activeServicesCount** *(integer) --* 
                The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .
              - **statistics** *(list) --* 
                Additional information about your clusters that are separated by launch type, including:
                * runningEC2TasksCount 
                * RunningFargateTasksCount 
                * pendingEC2TasksCount 
                * pendingFargateTasksCount 
                * activeEC2ServiceCount 
                * activeFargateServiceCount 
                * drainingEC2ServiceCount 
                * drainingFargateServiceCount 
                - *(dict) --* 
                  A key-value pair object.
                  - **name** *(string) --* 
                    The name of the key-value pair. For environment variables, this is the name of the environment variable.
                  - **value** *(string) --* 
                    The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **tags** *(list) --* 
                The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type clusterName: string
        :param clusterName:
          The name of your cluster. If you do not specify a name for your cluster, you create a cluster named ``default`` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
        :type tags: list
        :param tags:
          The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :rtype: dict
        :returns:
        """
        pass

    def create_service(self, serviceName: str, cluster: str = None, taskDefinition: str = None, loadBalancers: List = None, serviceRegistries: List = None, desiredCount: int = None, clientToken: str = None, launchType: str = None, platformVersion: str = None, role: str = None, deploymentConfiguration: Dict = None, placementConstraints: List = None, placementStrategy: List = None, networkConfiguration: Dict = None, healthCheckGracePeriodSeconds: int = None, schedulingStrategy: str = None, deploymentController: Dict = None, tags: List = None, enableECSManagedTags: bool = None, propagateTags: str = None) -> Dict:
        """
        Runs and maintains a desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the ``desiredCount`` , Amazon ECS spawns another copy of the task in the specified cluster. To update an existing service, see  UpdateService .
        In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind a load balancer. The load balancer distributes traffic across the tasks that are associated with the service. For more information, see `Service Load Balancing <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        Tasks for services that *do not* use a load balancer are considered healthy if they're in the ``RUNNING`` state. Tasks for services that *do* use a load balancer are considered healthy if they're in the ``RUNNING`` state and the container instance that they're hosted on is reported as healthy by the load balancer.
        There are two service scheduler strategies available:
        * ``REPLICA`` - The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see `Service Scheduler Concepts <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ in the *Amazon Elastic Container Service Developer Guide* . 
        * ``DAEMON`` - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see `Service Scheduler Concepts <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ in the *Amazon Elastic Container Service Developer Guide* . 
        You can optionally specify a deployment configuration for your service. The deployment is triggered by changing properties, such as the task definition or the desired count of a service, with an  UpdateService operation. The default value for a replica service for ``minimumHealthyPercent`` is 100%. The default value for a daemon service for ``minimumHealthyPercent`` is 0%.
        If a service is using the ``ECS`` deployment controller, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler might stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they're in the ``RUNNING`` state. Tasks for services that *do* use a load balancer are considered healthy if they're in the ``RUNNING`` state and they're reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
        If a service is using the ``ECS`` deployment controller, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
        If a service is using either the ``CODE_DEPLOY`` or ``EXTERNAL`` deployment controller types and tasks that use the EC2 launch type, the **minimum healthy percent** and **maximum percent** values are used only to define the lower and upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent and maximum percent values aren't used, although they're currently visible when describing your service.
        When creating a service that uses the ``EXTERNAL`` deployment controller, you can specify only parameters that aren't controlled at the task set level. The only required parameter is the service name. You control your services using the  CreateTaskSet operation. For more information, see `Amazon ECS Deployment Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        When the service scheduler launches new tasks, it determines task placement in your cluster using the following logic:
        * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes). 
        * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy) with the ``placementStrategy`` parameter): 
          * Sort the valid container instances, giving priority to instances that have the fewest number of running tasks for this service in their respective Availability Zone. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement. 
          * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateService>`_
        
        **Request Syntax**
        ::
          response = client.create_service(
              cluster='string',
              serviceName='string',
              taskDefinition='string',
              loadBalancers=[
                  {
                      'targetGroupArn': 'string',
                      'loadBalancerName': 'string',
                      'containerName': 'string',
                      'containerPort': 123
                  },
              ],
              serviceRegistries=[
                  {
                      'registryArn': 'string',
                      'port': 123,
                      'containerName': 'string',
                      'containerPort': 123
                  },
              ],
              desiredCount=123,
              clientToken='string',
              launchType='EC2'|'FARGATE',
              platformVersion='string',
              role='string',
              deploymentConfiguration={
                  'maximumPercent': 123,
                  'minimumHealthyPercent': 123
              },
              placementConstraints=[
                  {
                      'type': 'distinctInstance'|'memberOf',
                      'expression': 'string'
                  },
              ],
              placementStrategy=[
                  {
                      'type': 'random'|'spread'|'binpack',
                      'field': 'string'
                  },
              ],
              networkConfiguration={
                  'awsvpcConfiguration': {
                      'subnets': [
                          'string',
                      ],
                      'securityGroups': [
                          'string',
                      ],
                      'assignPublicIp': 'ENABLED'|'DISABLED'
                  }
              },
              healthCheckGracePeriodSeconds=123,
              schedulingStrategy='REPLICA'|'DAEMON',
              deploymentController={
                  'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              enableECSManagedTags=True|False,
              propagateTags='TASK_DEFINITION'|'SERVICE'
          )
        
        **Response Syntax**
        ::
            {
                'service': {
                    'serviceArn': 'string',
                    'serviceName': 'string',
                    'clusterArn': 'string',
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'status': 'string',
                    'desiredCount': 123,
                    'runningCount': 123,
                    'pendingCount': 123,
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'taskDefinition': 'string',
                    'deploymentConfiguration': {
                        'maximumPercent': 123,
                        'minimumHealthyPercent': 123
                    },
                    'taskSets': [
                        {
                            'id': 'string',
                            'taskSetArn': 'string',
                            'serviceArn': 'string',
                            'clusterArn': 'string',
                            'startedBy': 'string',
                            'externalId': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'computedDesiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            },
                            'loadBalancers': [
                                {
                                    'targetGroupArn': 'string',
                                    'loadBalancerName': 'string',
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'serviceRegistries': [
                                {
                                    'registryArn': 'string',
                                    'port': 123,
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'scale': {
                                'value': 123.0,
                                'unit': 'PERCENT'
                            },
                            'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                            'stabilityStatusAt': datetime(2015, 1, 1)
                        },
                    ],
                    'deployments': [
                        {
                            'id': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'desiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            }
                        },
                    ],
                    'roleArn': 'string',
                    'events': [
                        {
                            'id': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'message': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'placementConstraints': [
                        {
                            'type': 'distinctInstance'|'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'placementStrategy': [
                        {
                            'type': 'random'|'spread'|'binpack',
                            'field': 'string'
                        },
                    ],
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'healthCheckGracePeriodSeconds': 123,
                    'schedulingStrategy': 'REPLICA'|'DAEMON',
                    'deploymentController': {
                        'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
                    },
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdBy': 'string',
                    'enableECSManagedTags': True|False,
                    'propagateTags': 'TASK_DEFINITION'|'SERVICE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **service** *(dict) --* 
              The full description of your service following the create call.
              If a service is using the ``ECS`` deployment controller, the ``deploymentController`` and ``taskSets`` parameters will not be returned.
              If the service is using the ``CODE_DEPLOY`` deployment controller, the ``deploymentController`` , ``taskSets`` and ``deployments`` parameters will be returned, however the ``deployments`` parameter will be an empty list.
              - **serviceArn** *(string) --* 
                The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .
              - **serviceName** *(string) --* 
                The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that hosts the service.
              - **loadBalancers** *(list) --* 
                A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.
                Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this service. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **status** *(string) --* 
                The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .
              - **desiredCount** *(integer) --* 
                The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **runningCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``RUNNING`` state.
              - **pendingCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``PENDING`` state.
              - **launchType** *(string) --* 
                The launch type on which your service is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **taskDefinition** *(string) --* 
                The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **deploymentConfiguration** *(dict) --* 
                Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
                - **maximumPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
                - **minimumHealthyPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
              - **taskSets** *(list) --* 
                Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                - *(dict) --* 
                  Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                  - **id** *(string) --* 
                    The ID of the task set.
                  - **taskSetArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task set.
                  - **serviceArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service the task set exists in.
                  - **clusterArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
                  - **startedBy** *(string) --* 
                    The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
                  - **externalId** *(string) --* 
                    The external ID associated with the task set.
                    If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                    If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
                  - **status** *(string) --* 
                    The status of the task set. The following describes each state:
                      PRIMARY  
                    The task set is serving production traffic.
                      ACTIVE  
                    The task set is not serving production traffic.
                      DRAINING  
                    The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
                  - **taskDefinition** *(string) --* 
                    The task definition the task set is using.
                  - **computedDesiredCount** *(integer) --* 
                    The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the task set was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the task set was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The network configuration for the task set.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                  - **loadBalancers** *(list) --* 
                    Details on a load balancer that is used with a task set.
                    - *(dict) --* 
                      Details on a load balancer that is used with a service.
                      If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                      If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                      Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **targetGroupArn** *(string) --* 
                        The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                        .. warning::
                          If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **loadBalancerName** *(string) --* 
                        The name of a load balancer.
                      - **containerName** *(string) --* 
                        The name of the container (as it appears in a container definition) to associate with the load balancer.
                      - **containerPort** *(integer) --* 
                        The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                  - **serviceRegistries** *(list) --* 
                    The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                    - *(dict) --* 
                      Details of the service registry.
                      - **registryArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                      - **port** *(integer) --* 
                        The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                      - **containerName** *(string) --* 
                        The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                      - **containerPort** *(integer) --* 
                        The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **scale** *(dict) --* 
                    A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                    - **value** *(float) --* 
                      The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                    - **unit** *(string) --* 
                      The unit of measure for the scale value.
                  - **stabilityStatus** *(string) --* 
                    The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                    * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                    * The ``pendingCount`` is ``0`` . 
                    * There are no tasks running on container instances in the ``DRAINING`` status. 
                    * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                    If any of those conditions are not met, the stability status returns ``STABILIZING`` .
                  - **stabilityStatusAt** *(datetime) --* 
                    The Unix timestamp for when the task set stability status was retrieved.
              - **deployments** *(list) --* 
                The current state of deployments for the service.
                - *(dict) --* 
                  The details of an Amazon ECS service deployment. This is used only when a service uses the ``ECS`` deployment controller type.
                  - **id** *(string) --* 
                    The ID of the deployment.
                  - **status** *(string) --* 
                    The status of the deployment. The following describes each state:
                      PRIMARY  
                    The most recent deployment of a service.
                      ACTIVE  
                    A service deployment that still has running tasks, but are in the process of being replaced with a new ``PRIMARY`` deployment.
                      INACTIVE  
                    A deployment that has been completely replaced.
                  - **taskDefinition** *(string) --* 
                    The most recent task definition that was specified for the tasks in the service to use.
                  - **desiredCount** *(integer) --* 
                    The most recent desired count of tasks that was specified for the service to deploy or maintain.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``PENDING`` status.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``RUNNING`` status.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the service are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **roleArn** *(string) --* 
                The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
              - **events** *(list) --* 
                The event stream for your service. A maximum of 100 of the latest events are displayed.
                - *(dict) --* 
                  Details on an event associated with a service.
                  - **id** *(string) --* 
                    The ID string of the event.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the event was triggered.
                  - **message** *(string) --* 
                    The event message.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the service was created.
              - **placementConstraints** *(list) --* 
                The placement constraints for the tasks in the service.
                - *(dict) --* 
                  An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **placementStrategy** *(list) --* 
                The placement strategy that determines how tasks for the service are placed.
                - *(dict) --* 
                  The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
                  - **field** *(string) --* 
                    The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
              - **networkConfiguration** *(dict) --* 
                The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **healthCheckGracePeriodSeconds** *(integer) --* 
                The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.
              - **schedulingStrategy** *(string) --* 
                The scheduling strategy to use for the service. For more information, see `Services <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ .
                There are two service scheduler strategies available:
                * ``REPLICA`` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. 
                * ``DAEMON`` -The daemon scheduling strategy deploys exactly one task on each container instance in your cluster. When you are using this strategy, do not specify a desired number of tasks or any task placement strategies. 
                .. note::
                   Fargate tasks do not support the ``DAEMON`` scheduling strategy. 
              - **deploymentController** *(dict) --* 
                The deployment controller type the service is using.
                - **type** *(string) --* 
                  The deployment controller type to use.
                  There are three deployment controller types available:
                    ECS  
                  The rolling update (``ECS`` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
                    CODE_DEPLOY  
                  The blue/green (``CODE_DEPLOY`` ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.
                    EXTERNAL  
                  The external (``EXTERNAL`` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
              - **tags** *(list) --* 
                The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
              - **createdBy** *(string) --* 
                The principal that created the service.
              - **enableECSManagedTags** *(boolean) --* 
                Specifies whether to enable Amazon ECS managed tags for the tasks in the service. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **propagateTags** *(string) --* 
                Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service. If you do not specify a cluster, the default cluster is assumed.
        :type serviceName: string
        :param serviceName: **[REQUIRED]**
          The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
        :type taskDefinition: string
        :param taskDefinition:
          The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run in your service. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.
          A task definition must be specified if the service is using the ``ECS`` deployment controller.
        :type loadBalancers: list
        :param loadBalancers:
          A load balancer object representing the load balancer to use with your service.
          If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
          If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). During a deployment, AWS CodeDeploy determines which task set in your service has the status ``PRIMARY`` and associates one target group with it, and then associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that allows you perform validation tests with Lambda functions before routing production traffic to it.
          After you create a service using the ``ECS`` deployment controller, the load balancer name or target group ARN, container name, and container port specified in the service definition are immutable. If you are using the ``CODE_DEPLOY`` deployment controller, these values can be changed when updating the service.
          For Classic Load Balancers, this object must contain the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance is registered with the load balancer specified here.
          For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name (as it appears in a container definition), and the container port to access from the load balancer. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group specified here.
          Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
          - *(dict) --*
            Details on a load balancer that is used with a service.
            If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
            If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
            Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            - **targetGroupArn** *(string) --*
              The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
              .. warning::
                If your service\'s task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            - **loadBalancerName** *(string) --*
              The name of a load balancer.
            - **containerName** *(string) --*
              The name of the container (as it appears in a container definition) to associate with the load balancer.
            - **containerPort** *(integer) --*
              The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service\'s task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
        :type serviceRegistries: list
        :param serviceRegistries:
          The details of the service discovery registries to assign to this service. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
          .. note::
            Service discovery is supported for Fargate tasks if you are using platform version v1.1.0 or later. For more information, see `AWS Fargate Platform Versions <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ .
          - *(dict) --*
            Details of the service registry.
            - **registryArn** *(string) --*
              The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
            - **port** *(integer) --*
              The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
            - **containerName** *(string) --*
              The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
            - **containerPort** *(integer) --*
              The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
        :type desiredCount: integer
        :param desiredCount:
          The number of instantiations of the specified task definition to place and keep running on your cluster.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.
        :type launchType: string
        :param launchType:
          The launch type on which to run your service. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type platformVersion: string
        :param platformVersion:
          The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn\'t specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type role: string
        :param role:
          The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition does not use the ``awsvpc`` network mode. If you specify the ``role`` parameter, you must also specify a load balancer object with the ``loadBalancers`` parameter.
          .. warning::
            If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here. The service-linked role is required if your task definition uses the ``awsvpc`` network mode, in which case you should not specify a role here. For more information, see `Using Service-Linked Roles for Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          If your specified role has a path other than ``/`` , then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``/foo/`` then you would specify ``/foo/bar`` as the role name. For more information, see `Friendly Names and Paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`__ in the *IAM User Guide* .
        :type deploymentConfiguration: dict
        :param deploymentConfiguration:
          Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
          - **maximumPercent** *(integer) --*
            If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
            If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
          - **minimumHealthyPercent** *(integer) --*
            If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
            If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
        :type placementConstraints: list
        :param placementConstraints:
          An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at runtime).
          - *(dict) --*
            An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **type** *(string) --*
              The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
            - **expression** *(string) --*
              A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type placementStrategy: list
        :param placementStrategy:
          The placement strategy objects to use for tasks in your service. You can specify a maximum of five strategy rules per service.
          - *(dict) --*
            The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **type** *(string) --*
              The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
            - **field** *(string) --*
              The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
        :type networkConfiguration: dict
        :param networkConfiguration:
          The network configuration for the service. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          - **awsvpcConfiguration** *(dict) --*
            The VPC subnets and security groups associated with a task.
            .. note::
              All specified subnets and security groups must be from the same VPC.
            - **subnets** *(list) --* **[REQUIRED]**
              The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified subnets must be from the same VPC.
              - *(string) --*
            - **securityGroups** *(list) --*
              The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified security groups must be from the same VPC.
              - *(string) --*
            - **assignPublicIp** *(string) --*
              Whether the task\'s elastic network interface receives a public IP address. The default value is ``DISABLED`` .
        :type healthCheckGracePeriodSeconds: integer
        :param healthCheckGracePeriodSeconds:
          The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service\'s tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 2,147,483,647 seconds. During that time, the ECS service scheduler ignores health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.
        :type schedulingStrategy: string
        :param schedulingStrategy:
          The scheduling strategy to use for the service. For more information, see `Services <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ .
          There are two service scheduler strategies available:
          * ``REPLICA`` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service is using the ``CODE_DEPLOY`` or ``EXTERNAL`` deployment controller types.
          * ``DAEMON`` -The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. When you\'re using this strategy, you don\'t need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.
          .. note::
             Tasks using the Fargate launch type or the ``CODE_DEPLOY`` or ``EXTERNAL`` deployment controller types don\'t support the ``DAEMON`` scheduling strategy.
        :type deploymentController: dict
        :param deploymentController:
          The deployment controller to use for the service.
          - **type** *(string) --* **[REQUIRED]**
            The deployment controller type to use.
            There are three deployment controller types available:
              ECS
            The rolling update (``ECS`` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
              CODE_DEPLOY
            The blue/green (``CODE_DEPLOY`` ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.
              EXTERNAL
            The external (``EXTERNAL`` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
        :type tags: list
        :param tags:
          The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type enableECSManagedTags: boolean
        :param enableECSManagedTags:
          Specifies whether to enable Amazon ECS managed tags for the tasks within the service. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type propagateTags: string
        :param propagateTags:
          Specifies whether to propagate the tags from the task definition or the service to the tasks in the service. If no value is specified, the tags are not propagated. Tags can only be propagated to the tasks within the service during service creation. To add tags to a task after service creation, use the  TagResource API action.
        :rtype: dict
        :returns:
        """
        pass

    def create_task_set(self, service: str, cluster: str, taskDefinition: str, externalId: str = None, networkConfiguration: Dict = None, loadBalancers: List = None, serviceRegistries: List = None, launchType: str = None, platformVersion: str = None, scale: Dict = None, clientToken: str = None) -> Dict:
        """
        Create a task set in the specified cluster and service. This is used when a service uses the ``EXTERNAL`` deployment controller type. For more information, see `Amazon ECS Deployment Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/CreateTaskSet>`_
        
        **Request Syntax**
        ::
          response = client.create_task_set(
              service='string',
              cluster='string',
              externalId='string',
              taskDefinition='string',
              networkConfiguration={
                  'awsvpcConfiguration': {
                      'subnets': [
                          'string',
                      ],
                      'securityGroups': [
                          'string',
                      ],
                      'assignPublicIp': 'ENABLED'|'DISABLED'
                  }
              },
              loadBalancers=[
                  {
                      'targetGroupArn': 'string',
                      'loadBalancerName': 'string',
                      'containerName': 'string',
                      'containerPort': 123
                  },
              ],
              serviceRegistries=[
                  {
                      'registryArn': 'string',
                      'port': 123,
                      'containerName': 'string',
                      'containerPort': 123
                  },
              ],
              launchType='EC2'|'FARGATE',
              platformVersion='string',
              scale={
                  'value': 123.0,
                  'unit': 'PERCENT'
              },
              clientToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskSet': {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'serviceArn': 'string',
                    'clusterArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskSet** *(dict) --* 
              Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
              - **id** *(string) --* 
                The ID of the task set.
              - **taskSetArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task set.
              - **serviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the service the task set exists in.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
              - **startedBy** *(string) --* 
                The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
              - **externalId** *(string) --* 
                The external ID associated with the task set.
                If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
              - **status** *(string) --* 
                The status of the task set. The following describes each state:
                  PRIMARY  
                The task set is serving production traffic.
                  ACTIVE  
                The task set is not serving production traffic.
                  DRAINING  
                The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
              - **taskDefinition** *(string) --* 
                The task definition the task set is using.
              - **computedDesiredCount** *(integer) --* 
                The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
              - **pendingCount** *(integer) --* 
                The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
              - **runningCount** *(integer) --* 
                The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the task set was created.
              - **updatedAt** *(datetime) --* 
                The Unix timestamp for when the task set was last updated.
              - **launchType** *(string) --* 
                The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **networkConfiguration** *(dict) --* 
                The network configuration for the task set.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **loadBalancers** *(list) --* 
                Details on a load balancer that is used with a task set.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **scale** *(dict) --* 
                A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                - **value** *(float) --* 
                  The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                - **unit** *(string) --* 
                  The unit of measure for the scale value.
              - **stabilityStatus** *(string) --* 
                The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                * The ``pendingCount`` is ``0`` . 
                * There are no tasks running on container instances in the ``DRAINING`` status. 
                * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                If any of those conditions are not met, the stability status returns ``STABILIZING`` .
              - **stabilityStatusAt** *(datetime) --* 
                The Unix timestamp for when the task set stability status was retrieved.
        :type service: string
        :param service: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the service to create the task set in.
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.
        :type externalId: string
        :param externalId:
          An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute set to the provided value.
        :type taskDefinition: string
        :param taskDefinition: **[REQUIRED]**
          The task definition for the tasks in the task set to use.
        :type networkConfiguration: dict
        :param networkConfiguration:
          An object representing the network configuration for a task or service.
          - **awsvpcConfiguration** *(dict) --*
            The VPC subnets and security groups associated with a task.
            .. note::
              All specified subnets and security groups must be from the same VPC.
            - **subnets** *(list) --* **[REQUIRED]**
              The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified subnets must be from the same VPC.
              - *(string) --*
            - **securityGroups** *(list) --*
              The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified security groups must be from the same VPC.
              - *(string) --*
            - **assignPublicIp** *(string) --*
              Whether the task\'s elastic network interface receives a public IP address. The default value is ``DISABLED`` .
        :type loadBalancers: list
        :param loadBalancers:
          A load balancer object representing the load balancer to use with the task set. The supported load balancer types are either an Application Load Balancer or a Network Load Balancer.
          - *(dict) --*
            Details on a load balancer that is used with a service.
            If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
            If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
            Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            - **targetGroupArn** *(string) --*
              The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
              .. warning::
                If your service\'s task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
            - **loadBalancerName** *(string) --*
              The name of a load balancer.
            - **containerName** *(string) --*
              The name of the container (as it appears in a container definition) to associate with the load balancer.
            - **containerPort** *(integer) --*
              The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service\'s task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
        :type serviceRegistries: list
        :param serviceRegistries:
          The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
          - *(dict) --*
            Details of the service registry.
            - **registryArn** *(string) --*
              The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
            - **port** *(integer) --*
              The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
            - **containerName** *(string) --*
              The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
            - **containerPort** *(integer) --*
              The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
        :type launchType: string
        :param launchType:
          The launch type that new tasks in the task set will use. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type platformVersion: string
        :param platformVersion:
          The platform version that the tasks in the task set should use. A platform version is specified only for tasks using the Fargate launch type. If one isn\'t specified, the ``LATEST`` platform version is used by default.
        :type scale: dict
        :param scale:
          A floating-point percentage of the desired number of tasks to place and keep running in the task set.
          - **value** *(float) --*
            The value, specified as a percent total of a service\'s ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
          - **unit** *(string) --*
            The unit of measure for the scale value.
        :type clientToken: string
        :param clientToken:
          Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.
        :rtype: dict
        :returns:
        """
        pass

    def delete_account_setting(self, name: str, principalArn: str = None) -> Dict:
        """
        Modifies the ARN and resource ID format of a resource for a specified IAM user, IAM role, or the root user for an account. You can specify whether the new ARN and resource ID format are disabled for new resources that are created.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteAccountSetting>`_
        
        **Request Syntax**
        ::
          response = client.delete_account_setting(
              name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
              principalArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'setting': {
                    'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
                    'value': 'string',
                    'principalArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **setting** *(dict) --* 
              The account setting for the specified principal ARN.
              - **name** *(string) --* 
                The account resource name.
              - **value** *(string) --* 
                The current account setting for the resource name. If ``enabled`` , the resource receives the new Amazon Resource Name (ARN) and resource identifier (ID) format. If ``disabled`` , the resource receives the old Amazon Resource Name (ARN) and resource identifier (ID) format.
              - **principalArn** *(string) --* 
                The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the authenticated user is assumed.
        :type name: string
        :param name: **[REQUIRED]**
          The resource name for which to disable the new format. If ``serviceLongArnFormat`` is specified, the ARN for your Amazon ECS services is affected. If ``taskLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If ``containerInstanceLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS container instances is affected.
        :type principalArn: string
        :param principalArn:
          The ARN of the principal, which can be an IAM user, IAM role, or the root user. If you specify the root user, it modifies the ARN and resource ID format for all IAM users, IAM roles, and the root user of the account unless an IAM user or role explicitly overrides these settings for themselves. If this field is omitted, the setting are changed only for the authenticated user.
        :rtype: dict
        :returns:
        """
        pass

    def delete_attributes(self, attributes: List, cluster: str = None) -> Dict:
        """
        Deletes one or more custom attributes from an Amazon ECS resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteAttributes>`_
        
        **Request Syntax**
        ::
          response = client.delete_attributes(
              cluster='string',
              attributes=[
                  {
                      'name': 'string',
                      'value': 'string',
                      'targetType': 'container-instance',
                      'targetId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **attributes** *(list) --* 
              A list of attribute objects that were successfully deleted from your resource.
              - *(dict) --* 
                An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **name** *(string) --* 
                  The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                - **value** *(string) --* 
                  The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                - **targetType** *(string) --* 
                  The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                - **targetId** *(string) --* 
                  The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.
        :type attributes: list
        :param attributes: **[REQUIRED]**
          The attributes to delete from your resource. You can specify up to 10 attributes per request. For custom attributes, specify the attribute name and target ID, but do not specify the value. If you specify the target ID using the short form, you must also specify the target type.
          - *(dict) --*
            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **name** *(string) --* **[REQUIRED]**
              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            - **value** *(string) --*
              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            - **targetType** *(string) --*
              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            - **targetId** *(string) --*
              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
        :rtype: dict
        :returns:
        """
        pass

    def delete_cluster(self, cluster: str) -> Dict:
        """
        Deletes the specified cluster. You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with  ListContainerInstances and deregister them with  DeregisterContainerInstance .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteCluster>`_
        
        **Request Syntax**
        ::
          response = client.delete_cluster(
              cluster='string'
          )
        
        **Response Syntax**
        ::
            {
                'cluster': {
                    'clusterArn': 'string',
                    'clusterName': 'string',
                    'status': 'string',
                    'registeredContainerInstancesCount': 123,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'activeServicesCount': 123,
                    'statistics': [
                        {
                            'name': 'string',
                            'value': 'string'
                        },
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **cluster** *(dict) --* 
              The full description of the deleted cluster.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..
              - **clusterName** *(string) --* 
                A user-generated string that you use to identify your cluster.
              - **status** *(string) --* 
                The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.
              - **registeredContainerInstancesCount** *(integer) --* 
                The number of container instances registered into the cluster. This includes container instances in both ``ACTIVE`` and ``DRAINING`` status.
              - **runningTasksCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``RUNNING`` state.
              - **pendingTasksCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``PENDING`` state.
              - **activeServicesCount** *(integer) --* 
                The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .
              - **statistics** *(list) --* 
                Additional information about your clusters that are separated by launch type, including:
                * runningEC2TasksCount 
                * RunningFargateTasksCount 
                * pendingEC2TasksCount 
                * pendingFargateTasksCount 
                * activeEC2ServiceCount 
                * activeFargateServiceCount 
                * drainingEC2ServiceCount 
                * drainingFargateServiceCount 
                - *(dict) --* 
                  A key-value pair object.
                  - **name** *(string) --* 
                    The name of the key-value pair. For environment variables, this is the name of the environment variable.
                  - **value** *(string) --* 
                    The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **tags** *(list) --* 
                The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster to delete.
        :rtype: dict
        :returns:
        """
        pass

    def delete_service(self, service: str, cluster: str = None, force: bool = None) -> Dict:
        """
        Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you cannot delete it, and you must update the service to a desired task count of zero. For more information, see  UpdateService .
        .. note::
          When you delete a service, if there are still running tasks that require cleanup, the service status moves from ``ACTIVE`` to ``DRAINING`` , and the service is no longer visible in the console or in the  ListServices API operation. After the tasks have stopped, then the service status moves from ``DRAINING`` to ``INACTIVE`` . Services in the ``DRAINING`` or ``INACTIVE`` status can still be viewed with the  DescribeServices API operation. However, in the future, ``INACTIVE`` services may be cleaned up and purged from Amazon ECS record keeping, and  DescribeServices calls on those services return a ``ServiceNotFoundException`` error.
        .. warning::
          If you attempt to create a new service with the same name as an existing service in either ``ACTIVE`` or ``DRAINING`` status, you receive an error.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteService>`_
        
        **Request Syntax**
        ::
          response = client.delete_service(
              cluster='string',
              service='string',
              force=True|False
          )
        
        **Response Syntax**
        ::
            {
                'service': {
                    'serviceArn': 'string',
                    'serviceName': 'string',
                    'clusterArn': 'string',
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'status': 'string',
                    'desiredCount': 123,
                    'runningCount': 123,
                    'pendingCount': 123,
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'taskDefinition': 'string',
                    'deploymentConfiguration': {
                        'maximumPercent': 123,
                        'minimumHealthyPercent': 123
                    },
                    'taskSets': [
                        {
                            'id': 'string',
                            'taskSetArn': 'string',
                            'serviceArn': 'string',
                            'clusterArn': 'string',
                            'startedBy': 'string',
                            'externalId': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'computedDesiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            },
                            'loadBalancers': [
                                {
                                    'targetGroupArn': 'string',
                                    'loadBalancerName': 'string',
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'serviceRegistries': [
                                {
                                    'registryArn': 'string',
                                    'port': 123,
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'scale': {
                                'value': 123.0,
                                'unit': 'PERCENT'
                            },
                            'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                            'stabilityStatusAt': datetime(2015, 1, 1)
                        },
                    ],
                    'deployments': [
                        {
                            'id': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'desiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            }
                        },
                    ],
                    'roleArn': 'string',
                    'events': [
                        {
                            'id': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'message': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'placementConstraints': [
                        {
                            'type': 'distinctInstance'|'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'placementStrategy': [
                        {
                            'type': 'random'|'spread'|'binpack',
                            'field': 'string'
                        },
                    ],
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'healthCheckGracePeriodSeconds': 123,
                    'schedulingStrategy': 'REPLICA'|'DAEMON',
                    'deploymentController': {
                        'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
                    },
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdBy': 'string',
                    'enableECSManagedTags': True|False,
                    'propagateTags': 'TASK_DEFINITION'|'SERVICE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **service** *(dict) --* 
              The full description of the deleted service.
              - **serviceArn** *(string) --* 
                The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .
              - **serviceName** *(string) --* 
                The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that hosts the service.
              - **loadBalancers** *(list) --* 
                A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.
                Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this service. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **status** *(string) --* 
                The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .
              - **desiredCount** *(integer) --* 
                The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **runningCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``RUNNING`` state.
              - **pendingCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``PENDING`` state.
              - **launchType** *(string) --* 
                The launch type on which your service is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **taskDefinition** *(string) --* 
                The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **deploymentConfiguration** *(dict) --* 
                Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
                - **maximumPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
                - **minimumHealthyPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
              - **taskSets** *(list) --* 
                Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                - *(dict) --* 
                  Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                  - **id** *(string) --* 
                    The ID of the task set.
                  - **taskSetArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task set.
                  - **serviceArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service the task set exists in.
                  - **clusterArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
                  - **startedBy** *(string) --* 
                    The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
                  - **externalId** *(string) --* 
                    The external ID associated with the task set.
                    If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                    If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
                  - **status** *(string) --* 
                    The status of the task set. The following describes each state:
                      PRIMARY  
                    The task set is serving production traffic.
                      ACTIVE  
                    The task set is not serving production traffic.
                      DRAINING  
                    The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
                  - **taskDefinition** *(string) --* 
                    The task definition the task set is using.
                  - **computedDesiredCount** *(integer) --* 
                    The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the task set was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the task set was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The network configuration for the task set.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                  - **loadBalancers** *(list) --* 
                    Details on a load balancer that is used with a task set.
                    - *(dict) --* 
                      Details on a load balancer that is used with a service.
                      If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                      If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                      Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **targetGroupArn** *(string) --* 
                        The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                        .. warning::
                          If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **loadBalancerName** *(string) --* 
                        The name of a load balancer.
                      - **containerName** *(string) --* 
                        The name of the container (as it appears in a container definition) to associate with the load balancer.
                      - **containerPort** *(integer) --* 
                        The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                  - **serviceRegistries** *(list) --* 
                    The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                    - *(dict) --* 
                      Details of the service registry.
                      - **registryArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                      - **port** *(integer) --* 
                        The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                      - **containerName** *(string) --* 
                        The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                      - **containerPort** *(integer) --* 
                        The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **scale** *(dict) --* 
                    A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                    - **value** *(float) --* 
                      The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                    - **unit** *(string) --* 
                      The unit of measure for the scale value.
                  - **stabilityStatus** *(string) --* 
                    The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                    * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                    * The ``pendingCount`` is ``0`` . 
                    * There are no tasks running on container instances in the ``DRAINING`` status. 
                    * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                    If any of those conditions are not met, the stability status returns ``STABILIZING`` .
                  - **stabilityStatusAt** *(datetime) --* 
                    The Unix timestamp for when the task set stability status was retrieved.
              - **deployments** *(list) --* 
                The current state of deployments for the service.
                - *(dict) --* 
                  The details of an Amazon ECS service deployment. This is used only when a service uses the ``ECS`` deployment controller type.
                  - **id** *(string) --* 
                    The ID of the deployment.
                  - **status** *(string) --* 
                    The status of the deployment. The following describes each state:
                      PRIMARY  
                    The most recent deployment of a service.
                      ACTIVE  
                    A service deployment that still has running tasks, but are in the process of being replaced with a new ``PRIMARY`` deployment.
                      INACTIVE  
                    A deployment that has been completely replaced.
                  - **taskDefinition** *(string) --* 
                    The most recent task definition that was specified for the tasks in the service to use.
                  - **desiredCount** *(integer) --* 
                    The most recent desired count of tasks that was specified for the service to deploy or maintain.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``PENDING`` status.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``RUNNING`` status.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the service are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **roleArn** *(string) --* 
                The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
              - **events** *(list) --* 
                The event stream for your service. A maximum of 100 of the latest events are displayed.
                - *(dict) --* 
                  Details on an event associated with a service.
                  - **id** *(string) --* 
                    The ID string of the event.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the event was triggered.
                  - **message** *(string) --* 
                    The event message.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the service was created.
              - **placementConstraints** *(list) --* 
                The placement constraints for the tasks in the service.
                - *(dict) --* 
                  An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **placementStrategy** *(list) --* 
                The placement strategy that determines how tasks for the service are placed.
                - *(dict) --* 
                  The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
                  - **field** *(string) --* 
                    The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
              - **networkConfiguration** *(dict) --* 
                The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **healthCheckGracePeriodSeconds** *(integer) --* 
                The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.
              - **schedulingStrategy** *(string) --* 
                The scheduling strategy to use for the service. For more information, see `Services <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ .
                There are two service scheduler strategies available:
                * ``REPLICA`` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. 
                * ``DAEMON`` -The daemon scheduling strategy deploys exactly one task on each container instance in your cluster. When you are using this strategy, do not specify a desired number of tasks or any task placement strategies. 
                .. note::
                   Fargate tasks do not support the ``DAEMON`` scheduling strategy. 
              - **deploymentController** *(dict) --* 
                The deployment controller type the service is using.
                - **type** *(string) --* 
                  The deployment controller type to use.
                  There are three deployment controller types available:
                    ECS  
                  The rolling update (``ECS`` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
                    CODE_DEPLOY  
                  The blue/green (``CODE_DEPLOY`` ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.
                    EXTERNAL  
                  The external (``EXTERNAL`` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
              - **tags** *(list) --* 
                The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
              - **createdBy** *(string) --* 
                The principal that created the service.
              - **enableECSManagedTags** *(boolean) --* 
                Specifies whether to enable Amazon ECS managed tags for the tasks in the service. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **propagateTags** *(string) --* 
                Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.
        :type service: string
        :param service: **[REQUIRED]**
          The name of the service to delete.
        :type force: boolean
        :param force:
          If ``true`` , allows you to delete a service even if it has not been scaled down to zero tasks. It is only necessary to use this if the service is using the ``REPLICA`` scheduling strategy.
        :rtype: dict
        :returns:
        """
        pass

    def delete_task_set(self, cluster: str, service: str, taskSet: str, force: bool = None) -> Dict:
        """
        Deletes a specified task set within a service. This is used when a service uses the ``EXTERNAL`` deployment controller type. For more information, see `Amazon ECS Deployment Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeleteTaskSet>`_
        
        **Request Syntax**
        ::
          response = client.delete_task_set(
              cluster='string',
              service='string',
              taskSet='string',
              force=True|False
          )
        
        **Response Syntax**
        ::
            {
                'taskSet': {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'serviceArn': 'string',
                    'clusterArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskSet** *(dict) --* 
              Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
              - **id** *(string) --* 
                The ID of the task set.
              - **taskSetArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task set.
              - **serviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the service the task set exists in.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
              - **startedBy** *(string) --* 
                The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
              - **externalId** *(string) --* 
                The external ID associated with the task set.
                If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
              - **status** *(string) --* 
                The status of the task set. The following describes each state:
                  PRIMARY  
                The task set is serving production traffic.
                  ACTIVE  
                The task set is not serving production traffic.
                  DRAINING  
                The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
              - **taskDefinition** *(string) --* 
                The task definition the task set is using.
              - **computedDesiredCount** *(integer) --* 
                The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
              - **pendingCount** *(integer) --* 
                The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
              - **runningCount** *(integer) --* 
                The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the task set was created.
              - **updatedAt** *(datetime) --* 
                The Unix timestamp for when the task set was last updated.
              - **launchType** *(string) --* 
                The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **networkConfiguration** *(dict) --* 
                The network configuration for the task set.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **loadBalancers** *(list) --* 
                Details on a load balancer that is used with a task set.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **scale** *(dict) --* 
                A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                - **value** *(float) --* 
                  The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                - **unit** *(string) --* 
                  The unit of measure for the scale value.
              - **stabilityStatus** *(string) --* 
                The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                * The ``pendingCount`` is ``0`` . 
                * There are no tasks running on container instances in the ``DRAINING`` status. 
                * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                If any of those conditions are not met, the stability status returns ``STABILIZING`` .
              - **stabilityStatusAt** *(datetime) --* 
                The Unix timestamp for when the task set stability status was retrieved.
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in to delete.
        :type service: string
        :param service: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.
        :type taskSet: string
        :param taskSet: **[REQUIRED]**
          The task set ID or full Amazon Resource Name (ARN) of the task set to delete.
        :type force: boolean
        :param force:
          If ``true`` , this allows you to delete a task set even if it hasn\'t been scaled down to zero.
        :rtype: dict
        :returns:
        """
        pass

    def deregister_container_instance(self, containerInstance: str, cluster: str = None, force: bool = None) -> Dict:
        """
        Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.
        If you intend to use the container instance for some other purpose after deregistration, you should stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.
        Deregistering a container instance removes the instance from a cluster, but it does not terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.
        .. note::
          If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents are not automatically deregistered when terminated).
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeregisterContainerInstance>`_
        
        **Request Syntax**
        ::
          response = client.deregister_container_instance(
              cluster='string',
              containerInstance='string',
              force=True|False
          )
        
        **Response Syntax**
        ::
            {
                'containerInstance': {
                    'containerInstanceArn': 'string',
                    'ec2InstanceId': 'string',
                    'version': 123,
                    'versionInfo': {
                        'agentVersion': 'string',
                        'agentHash': 'string',
                        'dockerVersion': 'string'
                    },
                    'remainingResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'registeredResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'status': 'string',
                    'agentConnected': True|False,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                    'attributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'registeredAt': datetime(2015, 1, 1),
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstance** *(dict) --* 
              The container instance that was deregistered.
              - **containerInstanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
              - **ec2InstanceId** *(string) --* 
                The EC2 instance ID of the container instance.
              - **version** *(integer) --* 
                The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.
              - **versionInfo** *(dict) --* 
                The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
                - **agentVersion** *(string) --* 
                  The version number of the Amazon ECS container agent.
                - **agentHash** *(string) --* 
                  The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
                - **dockerVersion** *(string) --* 
                  The Docker version running on the container instance.
              - **remainingResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the remaining CPU and memory that has not already been allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the ``host`` or ``bridge`` network mode). Any port that is not specified here is available for new tasks.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **registeredResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **status** *(string) --* 
                The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **agentConnected** *(boolean) --* 
                This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Only instances connected to an agent can accept placement requests.
              - **runningTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``RUNNING`` status.
              - **pendingTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``PENDING`` status.
              - **agentUpdateStatus** *(string) --* 
                The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .
              - **attributes** *(list) --* 
                The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **registeredAt** *(datetime) --* 
                The Unix timestamp for when the container instance was registered.
              - **attachments** *(list) --* 
                The elastic network interfaces associated with the container instance.
                - *(dict) --* 
                  An object representing a container instance or task attachment.
                  - **id** *(string) --* 
                    The unique identifier for the attachment.
                  - **type** *(string) --* 
                    The type of the attachment, such as ``ElasticNetworkInterface`` .
                  - **status** *(string) --* 
                    The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                  - **details** *(list) --* 
                    Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **tags** *(list) --* 
                The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.
        :type containerInstance: string
        :param containerInstance: **[REQUIRED]**
          The container instance ID or full ARN of the container instance to deregister. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
        :type force: boolean
        :param force:
          Forces the deregistration of the container instance. If you have tasks running on the container instance when you deregister it with the ``force`` option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they are orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible.
          Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.
        :rtype: dict
        :returns:
        """
        pass

    def deregister_task_definition(self, taskDefinition: str) -> Dict:
        """
        .. _https://docs.docker.com/engine/reference/commandline/run/: https://docs.docker.com/engine/reference/commandline/run/
        .. _https://docs.docker.com/engine/reference/commandline/volume_create/: https://docs.docker.com/engine/reference/commandline/volume_create/
        Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as ``INACTIVE`` . Existing tasks and services that reference an ``INACTIVE`` task definition continue to run without disruption. Existing services that reference an ``INACTIVE`` task definition can still scale up or down by modifying the service's desired count.
        You cannot use an ``INACTIVE`` task definition to run new tasks or create new services, and you cannot update an existing service to reference an ``INACTIVE`` task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.
        .. note::
          At this time, ``INACTIVE`` task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future, so you should not rely on ``INACTIVE`` task definitions persisting beyond the lifecycle of any associated tasks and services.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DeregisterTaskDefinition>`_
        
        **Request Syntax**
        ::
          response = client.deregister_task_definition(
              taskDefinition='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskDefinition': {
                    'taskDefinitionArn': 'string',
                    'containerDefinitions': [
                        {
                            'name': 'string',
                            'image': 'string',
                            'repositoryCredentials': {
                                'credentialsParameter': 'string'
                            },
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123,
                            'links': [
                                'string',
                            ],
                            'portMappings': [
                                {
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'essential': True|False,
                            'entryPoint': [
                                'string',
                            ],
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'mountPoints': [
                                {
                                    'sourceVolume': 'string',
                                    'containerPath': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'volumesFrom': [
                                {
                                    'sourceContainer': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'linuxParameters': {
                                'capabilities': {
                                    'add': [
                                        'string',
                                    ],
                                    'drop': [
                                        'string',
                                    ]
                                },
                                'devices': [
                                    {
                                        'hostPath': 'string',
                                        'containerPath': 'string',
                                        'permissions': [
                                            'read'|'write'|'mknod',
                                        ]
                                    },
                                ],
                                'initProcessEnabled': True|False,
                                'sharedMemorySize': 123,
                                'tmpfs': [
                                    {
                                        'containerPath': 'string',
                                        'size': 123,
                                        'mountOptions': [
                                            'string',
                                        ]
                                    },
                                ]
                            },
                            'secrets': [
                                {
                                    'name': 'string',
                                    'valueFrom': 'string'
                                },
                            ],
                            'dependsOn': [
                                {
                                    'containerName': 'string',
                                    'condition': 'START'|'COMPLETE'|'SUCCESS'|'HEALTHY'
                                },
                            ],
                            'startTimeout': 123,
                            'stopTimeout': 123,
                            'hostname': 'string',
                            'user': 'string',
                            'workingDirectory': 'string',
                            'disableNetworking': True|False,
                            'privileged': True|False,
                            'readonlyRootFilesystem': True|False,
                            'dnsServers': [
                                'string',
                            ],
                            'dnsSearchDomains': [
                                'string',
                            ],
                            'extraHosts': [
                                {
                                    'hostname': 'string',
                                    'ipAddress': 'string'
                                },
                            ],
                            'dockerSecurityOptions': [
                                'string',
                            ],
                            'interactive': True|False,
                            'pseudoTerminal': True|False,
                            'dockerLabels': {
                                'string': 'string'
                            },
                            'ulimits': [
                                {
                                    'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                    'softLimit': 123,
                                    'hardLimit': 123
                                },
                            ],
                            'logConfiguration': {
                                'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                                'options': {
                                    'string': 'string'
                                },
                                'secretOptions': [
                                    {
                                        'name': 'string',
                                        'valueFrom': 'string'
                                    },
                                ]
                            },
                            'healthCheck': {
                                'command': [
                                    'string',
                                ],
                                'interval': 123,
                                'timeout': 123,
                                'retries': 123,
                                'startPeriod': 123
                            },
                            'systemControls': [
                                {
                                    'namespace': 'string',
                                    'value': 'string'
                                },
                            ],
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ]
                        },
                    ],
                    'family': 'string',
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string',
                    'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                    'revision': 123,
                    'volumes': [
                        {
                            'name': 'string',
                            'host': {
                                'sourcePath': 'string'
                            },
                            'dockerVolumeConfiguration': {
                                'scope': 'task'|'shared',
                                'autoprovision': True|False,
                                'driver': 'string',
                                'driverOpts': {
                                    'string': 'string'
                                },
                                'labels': {
                                    'string': 'string'
                                }
                            }
                        },
                    ],
                    'status': 'ACTIVE'|'INACTIVE',
                    'requiresAttributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'placementConstraints': [
                        {
                            'type': 'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'compatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'requiresCompatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'cpu': 'string',
                    'memory': 'string',
                    'pidMode': 'host'|'task',
                    'ipcMode': 'host'|'task'|'none',
                    'proxyConfiguration': {
                        'type': 'APPMESH',
                        'containerName': 'string',
                        'properties': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    }
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskDefinition** *(dict) --* 
              The full description of the deregistered task.
              - **taskDefinitionArn** *(string) --* 
                The full Amazon Resource Name (ARN) of the task definition.
              - **containerDefinitions** *(list) --* 
                A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
                  - **name** *(string) --* 
                    The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 
                  - **image** *(string) --* 
                    The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    * When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks. 
                    * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                    * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                    * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                    * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                  - **repositoryCredentials** *(dict) --* 
                    The private repository authentication credentials to use.
                    - **credentialsParameter** *(string) --* 
                      The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
                      .. note::
                        When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.
                  - **cpu** *(integer) --* 
                    The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.
                    .. note::
                      You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.
                    For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:
                    * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares. 
                    * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                    On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.
                  - **memory** *(integer) --* 
                    The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    If your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.
                    For containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **memoryReservation** *(integer) --* 
                    The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **links** *(list) --* 
                    The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    .. warning::
                      Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.
                    - *(string) --* 
                  - **portMappings** *(list) --* 
                    The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
                    For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                    Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 
                    This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.
                    .. note::
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the ``networkBindings`` section  DescribeTasks responses.
                    - *(dict) --* 
                      Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
                      If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                      - **containerPort** *(integer) --* 
                        The port number on the container that is bound to the user-specified or automatically assigned host port.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see ``hostPort`` . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.
                      - **hostPort** *(integer) --* 
                        The port number on the container instance to reserve for your container.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, the ``hostPort`` can either be left blank or set to the same value as the ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
                        The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.
                        .. note::
                          The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.
                        The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output. A container instance can have up to 100 reserved ports at a time, including the default reserved ports. Automatically assigned ports don't count toward the 100 reserved ports limit.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .
                  - **essential** *(boolean) --* 
                    If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
                    All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **entryPoint** *(list) --* 
                    .. warning::
                      Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.
                    The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .
                    - *(string) --* 
                  - **command** *(list) --* 
                    The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ . If there are multiple arguments, each argument should be a separated string in the array.
                    - *(string) --* 
                  - **environment** *(list) --* 
                    The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. warning::
                      We do not recommend using plaintext environment variables for sensitive information, such as credential data.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
                  - **mountPoints** *(list) --* 
                    The mount points for data volumes in your container.
                    This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
                    - *(dict) --* 
                      Details on a volume mount point that is used in a container definition.
                      - **sourceVolume** *(string) --* 
                        The name of the volume to mount. Must be a volume name referenced in the ``name`` parameter of task definition ``volume`` .
                      - **containerPath** *(string) --* 
                        The path on the container to mount the host volume at.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **volumesFrom** *(list) --* 
                    Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - *(dict) --* 
                      Details on a data volume from another container in the same task definition.
                      - **sourceContainer** *(string) --* 
                        The name of another container within the same task definition from which to mount volumes.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **linuxParameters** *(dict) --* 
                    Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - **capabilities** *(dict) --* 
                      The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
                      .. note::
                        If you are using tasks that use the Fargate launch type, ``capabilities`` is supported but the ``add`` parameter is not supported.
                      - **add** *(list) --* 
                        The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        .. note::
                          If you are using tasks that use the Fargate launch type, the ``add`` parameter is not supported.
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                      - **drop** *(list) --* 
                        The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                    - **devices** *(list) --* 
                      Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``devices`` parameter is not supported.
                      - *(dict) --* 
                        An object representing a container instance host device.
                        - **hostPath** *(string) --* 
                          The path for the device on the host container instance.
                        - **containerPath** *(string) --* 
                          The path inside the container at which to expose the host device.
                        - **permissions** *(list) --* 
                          The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.
                          - *(string) --* 
                    - **initProcessEnabled** *(boolean) --* 
                      Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **sharedMemorySize** *(integer) --* 
                      The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``sharedMemorySize`` parameter is not supported.
                    - **tmpfs** *(list) --* 
                      The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``tmpfs`` parameter is not supported.
                      - *(dict) --* 
                        The container path, mount options, and size of the tmpfs mount.
                        - **containerPath** *(string) --* 
                          The absolute file path where the tmpfs volume is to be mounted.
                        - **size** *(integer) --* 
                          The size (in MiB) of the tmpfs volume.
                        - **mountOptions** *(list) --* 
                          The list of tmpfs volume mount options.
                          Valid values: ``"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"``  
                          - *(string) --* 
                  - **secrets** *(list) --* 
                    The secrets to pass to the container. For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - *(dict) --* 
                      An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                      * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                      * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                      For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      - **name** *(string) --* 
                        The name of the secret.
                      - **valueFrom** *(string) --* 
                        The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                        .. note::
                          If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **dependsOn** *(list) --* 
                    The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    - *(dict) --* 
                      The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                      Your Amazon ECS container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you are using tasks that use the Fargate launch type, container dependency parameters are not supported.
                      - **containerName** *(string) --* 
                        The name of a container.
                      - **condition** *(string) --* 
                        The dependency condition of the container. The following are the available conditions and their behavior:
                        * ``START`` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start. 
                        * ``COMPLETE`` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. 
                        * ``SUCCESS`` - This condition is the same as ``COMPLETE`` , but it also requires that the container exits with a ``zero`` status. 
                        * ``HEALTHY`` - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup. 
                  - **startTimeout** *(integer) --* 
                    Time duration to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a ``COMPLETE`` , ``SUCCESS`` , or ``HEALTHY`` status. If a ``startTimeout`` value is specified for containerB and it does not reach the desired status within that time then containerA will give up and not start. This results in the task transitioning to a ``STOPPED`` state.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                  - **stopTimeout** *(integer) --* 
                    Time duration to wait before the container is forcefully killed if it doesn't exit normally on its own. For tasks using the Fargate launch type, the max ``stopTimeout`` value is 2 minutes. This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    For tasks using the EC2 launch type, the stop timeout value for the container takes precedence over the ``ECS_CONTAINER_STOP_TIMEOUT`` container agent configuration parameter, if used. Container instances require at least version 1.26.0 of the container agent to enable a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **hostname** *(string) --* 
                    The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The ``hostname`` parameter is not supported if you are using the ``awsvpc`` network mode.
                  - **user** *(string) --* 
                    The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You can use the following formats. If specifying a UID or GID, you must specify it as a positive integer.
                    * ``user``   
                    * ``user:group``   
                    * ``uid``   
                    * ``uid:gid``   
                    * ``user:gid``   
                    * ``uid:group``   
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **workingDirectory** *(string) --* 
                    The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **disableNetworking** *(boolean) --* 
                    When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **privileged** *(boolean) --* 
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks using the Fargate launch type.
                  - **readonlyRootFilesystem** *(boolean) --* 
                    When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--read-only`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **dnsServers** *(list) --* 
                    A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **dnsSearchDomains** *(list) --* 
                    A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **extraHosts** *(list) --* 
                    A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks that use the ``awsvpc`` network mode.
                    - *(dict) --* 
                      Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 
                      - **hostname** *(string) --* 
                        The hostname to use in the ``/etc/hosts`` entry.
                      - **ipAddress** *(string) --* 
                        The IP address to use in the ``/etc/hosts`` entry.
                  - **dockerSecurityOptions** *(list) --* 
                    A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
                    This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **interactive** *(boolean) --* 
                    When this parameter is ``true`` , this allows you to deploy containerized applications that require ``stdin`` or a ``tty`` to be allocated. This parameter maps to ``OpenStdin`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--interactive`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **pseudoTerminal** *(boolean) --* 
                    When this parameter is ``true`` , a TTY is allocated. This parameter maps to ``Tty`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--tty`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **dockerLabels** *(dict) --* 
                    A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - *(string) --* 
                      - *(string) --* 
                  - **ulimits** *(list) --* 
                    A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(dict) --* 
                      The ``ulimit`` settings to pass to the container.
                      - **name** *(string) --* 
                        The ``type`` of the ``ulimit`` .
                      - **softLimit** *(integer) --* 
                        The soft limit for the ulimit type.
                      - **hardLimit** *(integer) --* 
                        The hard limit for the ulimit type.
                  - **logConfiguration** *(dict) --* 
                    The log configuration specification for the container.
                    For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                    For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                    This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.
                    .. note::
                      Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
                    This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **logDriver** *(string) --* 
                      The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.
                      For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                      For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                      For more information about using the ``awslogs`` log driver, see `Using the awslogs Log Driver <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.
                      This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **options** *(dict) --* 
                      The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                      - *(string) --* 
                        - *(string) --* 
                    - **secretOptions** *(list) --* 
                      The secrets to pass to the log configuration.
                      - *(dict) --* 
                        An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                        * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                        * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                        For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                        - **name** *(string) --* 
                          The name of the secret.
                        - **valueFrom** *(string) --* 
                          The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                          .. note::
                            If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **healthCheck** *(dict) --* 
                    The health check command and associated configuration parameters for the container. This parameter maps to ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``HEALTHCHECK`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - **command** *(list) --* 
                      A string array representing the command that the container runs to determine if it is healthy. The string array must start with ``CMD`` to execute the command arguments directly, or ``CMD-SHELL`` to run the command with the container's default shell. For example:
                       ``[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]``  
                      An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                      - *(string) --* 
                    - **interval** *(integer) --* 
                      The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.
                    - **timeout** *(integer) --* 
                      The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.
                    - **retries** *(integer) --* 
                      The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.
                    - **startPeriod** *(integer) --* 
                      The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The ``startPeriod`` is disabled by default.
                      .. note::
                        If a health check succeeds within the ``startPeriod`` , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
                  - **systemControls** *(list) --* 
                    A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network modes. For tasks that use the ``awsvpc`` network mode, the container that is started last determines which ``systemControls`` parameters take effect. For tasks that use the ``host`` network mode, it changes the container instance's namespaced kernel parameters as well as the containers.
                    - *(dict) --* 
                      A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network mode for the following reasons:
                      * For tasks that use the ``awsvpc`` network mode, if you set ``systemControls`` for any container, it applies to all containers in the task. If you set different ``systemControls`` for multiple containers in a single task, the container that is started last determines which ``systemControls`` take effect. 
                      * For tasks that use the ``host`` network mode, the ``systemControls`` parameter applies to the container instance's kernel parameter as well as that of all containers of any tasks running on that container instance. 
                      - **namespace** *(string) --* 
                        The namespaced kernel parameter for which to set a ``value`` .
                      - **value** *(string) --* 
                        The value for the namespaced kernel parameter specified in ``namespace`` .
                  - **resourceRequirements** *(list) --* 
                    The type and amount of a resource to assign to a container. The only supported resource is a GPU.
                    - *(dict) --* 
                      The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                      - **value** *(string) --* 
                        The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                      - **type** *(string) --* 
                        The type of resource to assign to a container. The only supported value is ``GPU`` .
              - **family** *(string) --* 
                The family of your task definition, used as the definition name.
              - **taskRoleArn** *(string) --* 
                The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **executionRoleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
              - **networkMode** *(string) --* 
                The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If you are using the Fargate launch type, the ``awsvpc`` network mode is required. If you are using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.
                With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 
                If the network mode is ``awsvpc`` , the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                .. note::
                  Currently, only Amazon ECS-optimized AMIs, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 
                If the network mode is ``host`` , you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
                Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 
                For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .
              - **revision** *(integer) --* 
                The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` . Each time that you register a new revision of a task definition in the same family, the revision value always increases by one, even if you have deregistered previous revisions in this family.
              - **volumes** *(list) --* 
                The list of volumes in a task.
                If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.
                For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  A data volume used in a task definition. For tasks that use a Docker volume, specify a ``DockerVolumeConfiguration`` . For tasks that use a bind mount host volume, specify a ``host`` and optional ``sourcePath`` . For more information, see `Using Data Volumes in Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html>`__ .
                  - **name** *(string) --* 
                    The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
                  - **host** *(dict) --* 
                    This parameter is specified when you are using bind mount host volumes. Bind mount host volumes are supported when you are using either the EC2 or Fargate launch types. The contents of the ``host`` parameter determine whether your bind mount host volume persists on the host container instance and where it is stored. If the ``host`` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .
                    - **sourcePath** *(string) --* 
                      When the ``host`` parameter is used, specify a ``sourcePath`` to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                      If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.
                  - **dockerVolumeConfiguration** *(dict) --* 
                    This parameter is specified when you are using Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the ``local`` driver. To use bind mounts, specify a ``host`` instead.
                    - **scope** *(string) --* 
                      The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a ``task`` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as ``shared`` persist after the task stops.
                    - **autoprovision** *(boolean) --* 
                      If this value is ``true`` , the Docker volume is created if it does not already exist.
                      .. note::
                        This field is only used if the ``scope`` is ``shared`` .
                    - **driver** *(string) --* 
                      The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use ``docker plugin ls`` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see `Docker plugin discovery <https://docs.docker.com/engine/extend/plugin_api/#plugin-discovery>`__ . This parameter maps to ``Driver`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxdriver`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                    - **driverOpts** *(dict) --* 
                      A map of Docker driver-specific options passed through. This parameter maps to ``DriverOpts`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxopt`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
                    - **labels** *(dict) --* 
                      Custom metadata to add to your Docker volume. This parameter maps to ``Labels`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxlabel`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
              - **status** *(string) --* 
                The status of the task definition.
              - **requiresAttributes** *(list) --* 
                The container instance attributes required by your task. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **placementConstraints** *(list) --* 
                An array of placement constraint objects to use for tasks. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An object representing a constraint on task placement in the task definition.
                  If you are using the Fargate launch type, task placement constraints are not supported.
                  For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **compatibilities** *(list) --* 
                The launch type to use with your task. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(string) --* 
              - **requiresCompatibilities** *(list) --* 
                The launch type that the task is using.
                - *(string) --* 
              - **cpu** *(string) --* 
                The number of ``cpu`` units used by the task. If you are using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:
                * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
              - **memory** *(string) --* 
                The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:
                * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
              - **pidMode** *(string) --* 
                The process namespace to use for the containers in the task. The valid values are ``host`` or ``task`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` PID mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace. For more information, see `PID settings <https://docs.docker.com/engine/reference/run/#pid-settings---pid>`__ in the *Docker run reference* .
                If the ``host`` PID mode is used, be aware that there is a heightened risk of undesired process namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **ipcMode** *(string) --* 
                The IPC resource namespace to use for the containers in the task. The valid values are ``host`` , ``task`` , or ``none`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same IPC resources. If ``none`` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see `IPC settings <https://docs.docker.com/engine/reference/run/#ipc-settings---ipc>`__ in the *Docker run reference* .
                If the ``host`` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                If you are setting namespaced kernel parameters using ``systemControls`` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see `System Controls <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                * For tasks that use the ``host`` IPC mode, IPC namespace related ``systemControls`` are not supported. 
                * For tasks that use the ``task`` IPC mode, IPC namespace related ``systemControls`` will apply to all containers within a task. 
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **proxyConfiguration** *(dict) --* 
                The configuration details for the App Mesh proxy.
                Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to enable a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **type** *(string) --* 
                  The proxy type. The only supported value is ``APPMESH`` .
                - **containerName** *(string) --* 
                  The name of the container that will serve as the App Mesh proxy.
                - **properties** *(list) --* 
                  The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.
                  * ``IgnoredUID`` - (Required) The user ID (UID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``IgnoredGID`` - (Required) The group ID (GID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``AppPorts`` - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the ``ProxyIngressPort`` and ``ProxyEgressPort`` . 
                  * ``ProxyIngressPort`` - (Required) Specifies the port that incoming traffic to the ``AppPorts`` is directed to. 
                  * ``ProxyEgressPort`` - (Required) Specifies the port that outgoing traffic from the ``AppPorts`` is directed to. 
                  * ``EgressIgnoredPorts`` - (Required) The egress traffic going to the specified ports is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  * ``EgressIgnoredIPs`` - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  - *(dict) --* 
                    A key-value pair object.
                    - **name** *(string) --* 
                      The name of the key-value pair. For environment variables, this is the name of the environment variable.
                    - **value** *(string) --* 
                      The value of the key-value pair. For environment variables, this is the value of the environment variable.
        :type taskDefinition: string
        :param taskDefinition: **[REQUIRED]**
          The ``family`` and ``revision`` (``family:revision`` ) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a ``revision`` .
        :rtype: dict
        :returns:
        """
        pass

    def describe_clusters(self, clusters: List = None, include: List = None) -> Dict:
        """
        Describes one or more of your clusters.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeClusters>`_
        
        **Request Syntax**
        ::
          response = client.describe_clusters(
              clusters=[
                  'string',
              ],
              include=[
                  'STATISTICS'|'TAGS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'clusters': [
                    {
                        'clusterArn': 'string',
                        'clusterName': 'string',
                        'status': 'string',
                        'registeredContainerInstancesCount': 123,
                        'runningTasksCount': 123,
                        'pendingTasksCount': 123,
                        'activeServicesCount': 123,
                        'statistics': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ],
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **clusters** *(list) --* 
              The list of clusters.
              - *(dict) --* 
                A regional grouping of one or more container instances on which you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.
                - **clusterArn** *(string) --* 
                  The Amazon Resource Name (ARN) that identifies the cluster. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the cluster, the AWS account ID of the cluster owner, the ``cluster`` namespace, and then the cluster name. For example, ``arn:aws:ecs:*region* :*012345678910* :cluster/*test* `` ..
                - **clusterName** *(string) --* 
                  A user-generated string that you use to identify your cluster.
                - **status** *(string) --* 
                  The status of the cluster. The valid values are ``ACTIVE`` or ``INACTIVE`` . ``ACTIVE`` indicates that you can register container instances with the cluster and the associated instances can accept tasks.
                - **registeredContainerInstancesCount** *(integer) --* 
                  The number of container instances registered into the cluster. This includes container instances in both ``ACTIVE`` and ``DRAINING`` status.
                - **runningTasksCount** *(integer) --* 
                  The number of tasks in the cluster that are in the ``RUNNING`` state.
                - **pendingTasksCount** *(integer) --* 
                  The number of tasks in the cluster that are in the ``PENDING`` state.
                - **activeServicesCount** *(integer) --* 
                  The number of services that are running on the cluster in an ``ACTIVE`` state. You can view these services with  ListServices .
                - **statistics** *(list) --* 
                  Additional information about your clusters that are separated by launch type, including:
                  * runningEC2TasksCount 
                  * RunningFargateTasksCount 
                  * pendingEC2TasksCount 
                  * pendingFargateTasksCount 
                  * activeEC2ServiceCount 
                  * activeFargateServiceCount 
                  * drainingEC2ServiceCount 
                  * drainingFargateServiceCount 
                  - *(dict) --* 
                    A key-value pair object.
                    - **name** *(string) --* 
                      The name of the key-value pair. For environment variables, this is the name of the environment variable.
                    - **value** *(string) --* 
                      The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **tags** *(list) --* 
                  The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type clusters: list
        :param clusters:
          A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.
          - *(string) --*
        :type include: list
        :param include:
          Additional information about your clusters to be separated by launch type, including:
          * runningEC2TasksCount
          * runningFargateTasksCount
          * pendingEC2TasksCount
          * pendingFargateTasksCount
          * activeEC2ServiceCount
          * activeFargateServiceCount
          * drainingEC2ServiceCount
          * drainingFargateServiceCount
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_container_instances(self, containerInstances: List, cluster: str = None, include: List = None) -> Dict:
        """
        Describes Amazon Elastic Container Service container instances. Returns metadata about registered and remaining resources on each container instance requested.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeContainerInstances>`_
        
        **Request Syntax**
        ::
          response = client.describe_container_instances(
              cluster='string',
              containerInstances=[
                  'string',
              ],
              include=[
                  'TAGS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'containerInstances': [
                    {
                        'containerInstanceArn': 'string',
                        'ec2InstanceId': 'string',
                        'version': 123,
                        'versionInfo': {
                            'agentVersion': 'string',
                            'agentHash': 'string',
                            'dockerVersion': 'string'
                        },
                        'remainingResources': [
                            {
                                'name': 'string',
                                'type': 'string',
                                'doubleValue': 123.0,
                                'longValue': 123,
                                'integerValue': 123,
                                'stringSetValue': [
                                    'string',
                                ]
                            },
                        ],
                        'registeredResources': [
                            {
                                'name': 'string',
                                'type': 'string',
                                'doubleValue': 123.0,
                                'longValue': 123,
                                'integerValue': 123,
                                'stringSetValue': [
                                    'string',
                                ]
                            },
                        ],
                        'status': 'string',
                        'agentConnected': True|False,
                        'runningTasksCount': 123,
                        'pendingTasksCount': 123,
                        'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                        'attributes': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'targetType': 'container-instance',
                                'targetId': 'string'
                            },
                        ],
                        'registeredAt': datetime(2015, 1, 1),
                        'attachments': [
                            {
                                'id': 'string',
                                'type': 'string',
                                'status': 'string',
                                'details': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ]
                            },
                        ],
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstances** *(list) --* 
              The list of container instances.
              - *(dict) --* 
                An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.
                - **containerInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
                - **ec2InstanceId** *(string) --* 
                  The EC2 instance ID of the container instance.
                - **version** *(integer) --* 
                  The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.
                - **versionInfo** *(dict) --* 
                  The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
                  - **agentVersion** *(string) --* 
                    The version number of the Amazon ECS container agent.
                  - **agentHash** *(string) --* 
                    The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
                  - **dockerVersion** *(string) --* 
                    The Docker version running on the container instance.
                - **remainingResources** *(list) --* 
                  For CPU and memory resource types, this parameter describes the remaining CPU and memory that has not already been allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the ``host`` or ``bridge`` network mode). Any port that is not specified here is available for new tasks.
                  - *(dict) --* 
                    Describes the resources available for a container instance.
                    - **name** *(string) --* 
                      The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                    - **type** *(string) --* 
                      The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                    - **doubleValue** *(float) --* 
                      When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                    - **longValue** *(integer) --* 
                      When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                    - **integerValue** *(integer) --* 
                      When the ``integerValue`` type is set, the value of the resource must be an integer.
                    - **stringSetValue** *(list) --* 
                      When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                      - *(string) --* 
                - **registeredResources** *(list) --* 
                  For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
                  - *(dict) --* 
                    Describes the resources available for a container instance.
                    - **name** *(string) --* 
                      The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                    - **type** *(string) --* 
                      The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                    - **doubleValue** *(float) --* 
                      When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                    - **longValue** *(integer) --* 
                      When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                    - **integerValue** *(integer) --* 
                      When the ``integerValue`` type is set, the value of the resource must be an integer.
                    - **stringSetValue** *(list) --* 
                      When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                      - *(string) --* 
                - **status** *(string) --* 
                  The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **agentConnected** *(boolean) --* 
                  This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Only instances connected to an agent can accept placement requests.
                - **runningTasksCount** *(integer) --* 
                  The number of tasks on the container instance that are in the ``RUNNING`` status.
                - **pendingTasksCount** *(integer) --* 
                  The number of tasks on the container instance that are in the ``PENDING`` status.
                - **agentUpdateStatus** *(string) --* 
                  The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .
                - **attributes** *(list) --* 
                  The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.
                  - *(dict) --* 
                    An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **name** *(string) --* 
                      The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                    - **value** *(string) --* 
                      The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                    - **targetType** *(string) --* 
                      The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                    - **targetId** *(string) --* 
                      The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
                - **registeredAt** *(datetime) --* 
                  The Unix timestamp for when the container instance was registered.
                - **attachments** *(list) --* 
                  The elastic network interfaces associated with the container instance.
                  - *(dict) --* 
                    An object representing a container instance or task attachment.
                    - **id** *(string) --* 
                      The unique identifier for the attachment.
                    - **type** *(string) --* 
                      The type of the attachment, such as ``ElasticNetworkInterface`` .
                    - **status** *(string) --* 
                      The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                    - **details** *(list) --* 
                      Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **tags** *(list) --* 
                  The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed.
        :type containerInstances: list
        :param containerInstances: **[REQUIRED]**
          A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.
          - *(string) --*
        :type include: list
        :param include:
          Specifies whether you want to see the resource tags for the container instance. If ``TAGS`` is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_services(self, services: List, cluster: str = None, include: List = None) -> Dict:
        """
        Describes the specified services running in your cluster.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeServices>`_
        
        **Request Syntax**
        ::
          response = client.describe_services(
              cluster='string',
              services=[
                  'string',
              ],
              include=[
                  'TAGS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'services': [
                    {
                        'serviceArn': 'string',
                        'serviceName': 'string',
                        'clusterArn': 'string',
                        'loadBalancers': [
                            {
                                'targetGroupArn': 'string',
                                'loadBalancerName': 'string',
                                'containerName': 'string',
                                'containerPort': 123
                            },
                        ],
                        'serviceRegistries': [
                            {
                                'registryArn': 'string',
                                'port': 123,
                                'containerName': 'string',
                                'containerPort': 123
                            },
                        ],
                        'status': 'string',
                        'desiredCount': 123,
                        'runningCount': 123,
                        'pendingCount': 123,
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'taskDefinition': 'string',
                        'deploymentConfiguration': {
                            'maximumPercent': 123,
                            'minimumHealthyPercent': 123
                        },
                        'taskSets': [
                            {
                                'id': 'string',
                                'taskSetArn': 'string',
                                'serviceArn': 'string',
                                'clusterArn': 'string',
                                'startedBy': 'string',
                                'externalId': 'string',
                                'status': 'string',
                                'taskDefinition': 'string',
                                'computedDesiredCount': 123,
                                'pendingCount': 123,
                                'runningCount': 123,
                                'createdAt': datetime(2015, 1, 1),
                                'updatedAt': datetime(2015, 1, 1),
                                'launchType': 'EC2'|'FARGATE',
                                'platformVersion': 'string',
                                'networkConfiguration': {
                                    'awsvpcConfiguration': {
                                        'subnets': [
                                            'string',
                                        ],
                                        'securityGroups': [
                                            'string',
                                        ],
                                        'assignPublicIp': 'ENABLED'|'DISABLED'
                                    }
                                },
                                'loadBalancers': [
                                    {
                                        'targetGroupArn': 'string',
                                        'loadBalancerName': 'string',
                                        'containerName': 'string',
                                        'containerPort': 123
                                    },
                                ],
                                'serviceRegistries': [
                                    {
                                        'registryArn': 'string',
                                        'port': 123,
                                        'containerName': 'string',
                                        'containerPort': 123
                                    },
                                ],
                                'scale': {
                                    'value': 123.0,
                                    'unit': 'PERCENT'
                                },
                                'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                                'stabilityStatusAt': datetime(2015, 1, 1)
                            },
                        ],
                        'deployments': [
                            {
                                'id': 'string',
                                'status': 'string',
                                'taskDefinition': 'string',
                                'desiredCount': 123,
                                'pendingCount': 123,
                                'runningCount': 123,
                                'createdAt': datetime(2015, 1, 1),
                                'updatedAt': datetime(2015, 1, 1),
                                'launchType': 'EC2'|'FARGATE',
                                'platformVersion': 'string',
                                'networkConfiguration': {
                                    'awsvpcConfiguration': {
                                        'subnets': [
                                            'string',
                                        ],
                                        'securityGroups': [
                                            'string',
                                        ],
                                        'assignPublicIp': 'ENABLED'|'DISABLED'
                                    }
                                }
                            },
                        ],
                        'roleArn': 'string',
                        'events': [
                            {
                                'id': 'string',
                                'createdAt': datetime(2015, 1, 1),
                                'message': 'string'
                            },
                        ],
                        'createdAt': datetime(2015, 1, 1),
                        'placementConstraints': [
                            {
                                'type': 'distinctInstance'|'memberOf',
                                'expression': 'string'
                            },
                        ],
                        'placementStrategy': [
                            {
                                'type': 'random'|'spread'|'binpack',
                                'field': 'string'
                            },
                        ],
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        },
                        'healthCheckGracePeriodSeconds': 123,
                        'schedulingStrategy': 'REPLICA'|'DAEMON',
                        'deploymentController': {
                            'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
                        },
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'createdBy': 'string',
                        'enableECSManagedTags': True|False,
                        'propagateTags': 'TASK_DEFINITION'|'SERVICE'
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **services** *(list) --* 
              The list of services described.
              - *(dict) --* 
                Details on a service within a cluster
                - **serviceArn** *(string) --* 
                  The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .
                - **serviceName** *(string) --* 
                  The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
                - **clusterArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the cluster that hosts the service.
                - **loadBalancers** *(list) --* 
                  A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - *(dict) --* 
                    Details on a load balancer that is used with a service.
                    If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                    If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                    Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                    - **targetGroupArn** *(string) --* 
                      The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                      .. warning::
                        If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                    - **loadBalancerName** *(string) --* 
                      The name of a load balancer.
                    - **containerName** *(string) --* 
                      The name of the container (as it appears in a container definition) to associate with the load balancer.
                    - **containerPort** *(integer) --* 
                      The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                - **serviceRegistries** *(list) --* 
                  The details of the service discovery registries to assign to this service. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                  - *(dict) --* 
                    Details of the service registry.
                    - **registryArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                    - **port** *(integer) --* 
                      The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                    - **containerName** *(string) --* 
                      The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                    - **containerPort** *(integer) --* 
                      The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                - **status** *(string) --* 
                  The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .
                - **desiredCount** *(integer) --* 
                  The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
                - **runningCount** *(integer) --* 
                  The number of tasks in the cluster that are in the ``RUNNING`` state.
                - **pendingCount** *(integer) --* 
                  The number of tasks in the cluster that are in the ``PENDING`` state.
                - **launchType** *(string) --* 
                  The launch type on which your service is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **platformVersion** *(string) --* 
                  The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **taskDefinition** *(string) --* 
                  The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
                - **deploymentConfiguration** *(dict) --* 
                  Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
                  - **maximumPercent** *(integer) --* 
                    If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
                    If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
                  - **minimumHealthyPercent** *(integer) --* 
                    If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
                    If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
                - **taskSets** *(list) --* 
                  Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                  - *(dict) --* 
                    Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                    - **id** *(string) --* 
                      The ID of the task set.
                    - **taskSetArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the task set.
                    - **serviceArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the service the task set exists in.
                    - **clusterArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
                    - **startedBy** *(string) --* 
                      The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
                    - **externalId** *(string) --* 
                      The external ID associated with the task set.
                      If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                      If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
                    - **status** *(string) --* 
                      The status of the task set. The following describes each state:
                        PRIMARY  
                      The task set is serving production traffic.
                        ACTIVE  
                      The task set is not serving production traffic.
                        DRAINING  
                      The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
                    - **taskDefinition** *(string) --* 
                      The task definition the task set is using.
                    - **computedDesiredCount** *(integer) --* 
                      The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
                    - **pendingCount** *(integer) --* 
                      The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
                    - **runningCount** *(integer) --* 
                      The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
                    - **createdAt** *(datetime) --* 
                      The Unix timestamp for when the task set was created.
                    - **updatedAt** *(datetime) --* 
                      The Unix timestamp for when the task set was last updated.
                    - **launchType** *(string) --* 
                      The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **platformVersion** *(string) --* 
                      The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **networkConfiguration** *(dict) --* 
                      The network configuration for the task set.
                      - **awsvpcConfiguration** *(dict) --* 
                        The VPC subnets and security groups associated with a task.
                        .. note::
                          All specified subnets and security groups must be from the same VPC.
                        - **subnets** *(list) --* 
                          The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                          .. note::
                            All specified subnets must be from the same VPC.
                          - *(string) --* 
                        - **securityGroups** *(list) --* 
                          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                          .. note::
                            All specified security groups must be from the same VPC.
                          - *(string) --* 
                        - **assignPublicIp** *(string) --* 
                          Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                    - **loadBalancers** *(list) --* 
                      Details on a load balancer that is used with a task set.
                      - *(dict) --* 
                        Details on a load balancer that is used with a service.
                        If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                        If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                        Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                        - **targetGroupArn** *(string) --* 
                          The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                          .. warning::
                            If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                        - **loadBalancerName** *(string) --* 
                          The name of a load balancer.
                        - **containerName** *(string) --* 
                          The name of the container (as it appears in a container definition) to associate with the load balancer.
                        - **containerPort** *(integer) --* 
                          The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                    - **serviceRegistries** *(list) --* 
                      The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                      - *(dict) --* 
                        Details of the service registry.
                        - **registryArn** *(string) --* 
                          The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                        - **port** *(integer) --* 
                          The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                        - **containerName** *(string) --* 
                          The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                        - **containerPort** *(integer) --* 
                          The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                    - **scale** *(dict) --* 
                      A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                      - **value** *(float) --* 
                        The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                      - **unit** *(string) --* 
                        The unit of measure for the scale value.
                    - **stabilityStatus** *(string) --* 
                      The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                      * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                      * The ``pendingCount`` is ``0`` . 
                      * There are no tasks running on container instances in the ``DRAINING`` status. 
                      * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                      If any of those conditions are not met, the stability status returns ``STABILIZING`` .
                    - **stabilityStatusAt** *(datetime) --* 
                      The Unix timestamp for when the task set stability status was retrieved.
                - **deployments** *(list) --* 
                  The current state of deployments for the service.
                  - *(dict) --* 
                    The details of an Amazon ECS service deployment. This is used only when a service uses the ``ECS`` deployment controller type.
                    - **id** *(string) --* 
                      The ID of the deployment.
                    - **status** *(string) --* 
                      The status of the deployment. The following describes each state:
                        PRIMARY  
                      The most recent deployment of a service.
                        ACTIVE  
                      A service deployment that still has running tasks, but are in the process of being replaced with a new ``PRIMARY`` deployment.
                        INACTIVE  
                      A deployment that has been completely replaced.
                    - **taskDefinition** *(string) --* 
                      The most recent task definition that was specified for the tasks in the service to use.
                    - **desiredCount** *(integer) --* 
                      The most recent desired count of tasks that was specified for the service to deploy or maintain.
                    - **pendingCount** *(integer) --* 
                      The number of tasks in the deployment that are in the ``PENDING`` status.
                    - **runningCount** *(integer) --* 
                      The number of tasks in the deployment that are in the ``RUNNING`` status.
                    - **createdAt** *(datetime) --* 
                      The Unix timestamp for when the service deployment was created.
                    - **updatedAt** *(datetime) --* 
                      The Unix timestamp for when the service deployment was last updated.
                    - **launchType** *(string) --* 
                      The launch type the tasks in the service are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **platformVersion** *(string) --* 
                      The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **networkConfiguration** *(dict) --* 
                      The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                      - **awsvpcConfiguration** *(dict) --* 
                        The VPC subnets and security groups associated with a task.
                        .. note::
                          All specified subnets and security groups must be from the same VPC.
                        - **subnets** *(list) --* 
                          The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                          .. note::
                            All specified subnets must be from the same VPC.
                          - *(string) --* 
                        - **securityGroups** *(list) --* 
                          The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                          .. note::
                            All specified security groups must be from the same VPC.
                          - *(string) --* 
                        - **assignPublicIp** *(string) --* 
                          Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                - **roleArn** *(string) --* 
                  The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
                - **events** *(list) --* 
                  The event stream for your service. A maximum of 100 of the latest events are displayed.
                  - *(dict) --* 
                    Details on an event associated with a service.
                    - **id** *(string) --* 
                      The ID string of the event.
                    - **createdAt** *(datetime) --* 
                      The Unix timestamp for when the event was triggered.
                    - **message** *(string) --* 
                      The event message.
                - **createdAt** *(datetime) --* 
                  The Unix timestamp for when the service was created.
                - **placementConstraints** *(list) --* 
                  The placement constraints for the tasks in the service.
                  - *(dict) --* 
                    An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **type** *(string) --* 
                      The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
                    - **expression** *(string) --* 
                      A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **placementStrategy** *(list) --* 
                  The placement strategy that determines how tasks for the service are placed.
                  - *(dict) --* 
                    The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **type** *(string) --* 
                      The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
                    - **field** *(string) --* 
                      The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
                - **networkConfiguration** *(dict) --* 
                  The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                  - **awsvpcConfiguration** *(dict) --* 
                    The VPC subnets and security groups associated with a task.
                    .. note::
                      All specified subnets and security groups must be from the same VPC.
                    - **subnets** *(list) --* 
                      The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                      .. note::
                        All specified subnets must be from the same VPC.
                      - *(string) --* 
                    - **securityGroups** *(list) --* 
                      The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                      .. note::
                        All specified security groups must be from the same VPC.
                      - *(string) --* 
                    - **assignPublicIp** *(string) --* 
                      Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                - **healthCheckGracePeriodSeconds** *(integer) --* 
                  The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.
                - **schedulingStrategy** *(string) --* 
                  The scheduling strategy to use for the service. For more information, see `Services <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ .
                  There are two service scheduler strategies available:
                  * ``REPLICA`` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. 
                  * ``DAEMON`` -The daemon scheduling strategy deploys exactly one task on each container instance in your cluster. When you are using this strategy, do not specify a desired number of tasks or any task placement strategies. 
                  .. note::
                     Fargate tasks do not support the ``DAEMON`` scheduling strategy. 
                - **deploymentController** *(dict) --* 
                  The deployment controller type the service is using.
                  - **type** *(string) --* 
                    The deployment controller type to use.
                    There are three deployment controller types available:
                      ECS  
                    The rolling update (``ECS`` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
                      CODE_DEPLOY  
                    The blue/green (``CODE_DEPLOY`` ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.
                      EXTERNAL  
                    The external (``EXTERNAL`` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
                - **tags** *(list) --* 
                  The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
                - **createdBy** *(string) --* 
                  The principal that created the service.
                - **enableECSManagedTags** *(boolean) --* 
                  Specifies whether to enable Amazon ECS managed tags for the tasks in the service. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **propagateTags** *(string) --* 
                  Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed.
        :type services: list
        :param services: **[REQUIRED]**
          A list of services to describe. You may specify up to 10 services to describe in a single operation.
          - *(string) --*
        :type include: list
        :param include:
          Specifies whether you want to see the resource tags for the service. If ``TAGS`` is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_task_definition(self, taskDefinition: str, include: List = None) -> Dict:
        """
        .. _https://docs.docker.com/engine/reference/commandline/run/: https://docs.docker.com/engine/reference/commandline/run/
        .. _https://docs.docker.com/engine/reference/commandline/volume_create/: https://docs.docker.com/engine/reference/commandline/volume_create/
        Describes a task definition. You can specify a ``family`` and ``revision`` to find information about a specific task definition, or you can simply specify the family to find the latest ``ACTIVE`` revision in that family.
        .. note::
          You can only describe ``INACTIVE`` task definitions while an active task or service references them.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTaskDefinition>`_
        
        **Request Syntax**
        ::
          response = client.describe_task_definition(
              taskDefinition='string',
              include=[
                  'TAGS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'taskDefinition': {
                    'taskDefinitionArn': 'string',
                    'containerDefinitions': [
                        {
                            'name': 'string',
                            'image': 'string',
                            'repositoryCredentials': {
                                'credentialsParameter': 'string'
                            },
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123,
                            'links': [
                                'string',
                            ],
                            'portMappings': [
                                {
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'essential': True|False,
                            'entryPoint': [
                                'string',
                            ],
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'mountPoints': [
                                {
                                    'sourceVolume': 'string',
                                    'containerPath': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'volumesFrom': [
                                {
                                    'sourceContainer': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'linuxParameters': {
                                'capabilities': {
                                    'add': [
                                        'string',
                                    ],
                                    'drop': [
                                        'string',
                                    ]
                                },
                                'devices': [
                                    {
                                        'hostPath': 'string',
                                        'containerPath': 'string',
                                        'permissions': [
                                            'read'|'write'|'mknod',
                                        ]
                                    },
                                ],
                                'initProcessEnabled': True|False,
                                'sharedMemorySize': 123,
                                'tmpfs': [
                                    {
                                        'containerPath': 'string',
                                        'size': 123,
                                        'mountOptions': [
                                            'string',
                                        ]
                                    },
                                ]
                            },
                            'secrets': [
                                {
                                    'name': 'string',
                                    'valueFrom': 'string'
                                },
                            ],
                            'dependsOn': [
                                {
                                    'containerName': 'string',
                                    'condition': 'START'|'COMPLETE'|'SUCCESS'|'HEALTHY'
                                },
                            ],
                            'startTimeout': 123,
                            'stopTimeout': 123,
                            'hostname': 'string',
                            'user': 'string',
                            'workingDirectory': 'string',
                            'disableNetworking': True|False,
                            'privileged': True|False,
                            'readonlyRootFilesystem': True|False,
                            'dnsServers': [
                                'string',
                            ],
                            'dnsSearchDomains': [
                                'string',
                            ],
                            'extraHosts': [
                                {
                                    'hostname': 'string',
                                    'ipAddress': 'string'
                                },
                            ],
                            'dockerSecurityOptions': [
                                'string',
                            ],
                            'interactive': True|False,
                            'pseudoTerminal': True|False,
                            'dockerLabels': {
                                'string': 'string'
                            },
                            'ulimits': [
                                {
                                    'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                    'softLimit': 123,
                                    'hardLimit': 123
                                },
                            ],
                            'logConfiguration': {
                                'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                                'options': {
                                    'string': 'string'
                                },
                                'secretOptions': [
                                    {
                                        'name': 'string',
                                        'valueFrom': 'string'
                                    },
                                ]
                            },
                            'healthCheck': {
                                'command': [
                                    'string',
                                ],
                                'interval': 123,
                                'timeout': 123,
                                'retries': 123,
                                'startPeriod': 123
                            },
                            'systemControls': [
                                {
                                    'namespace': 'string',
                                    'value': 'string'
                                },
                            ],
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ]
                        },
                    ],
                    'family': 'string',
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string',
                    'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                    'revision': 123,
                    'volumes': [
                        {
                            'name': 'string',
                            'host': {
                                'sourcePath': 'string'
                            },
                            'dockerVolumeConfiguration': {
                                'scope': 'task'|'shared',
                                'autoprovision': True|False,
                                'driver': 'string',
                                'driverOpts': {
                                    'string': 'string'
                                },
                                'labels': {
                                    'string': 'string'
                                }
                            }
                        },
                    ],
                    'status': 'ACTIVE'|'INACTIVE',
                    'requiresAttributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'placementConstraints': [
                        {
                            'type': 'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'compatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'requiresCompatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'cpu': 'string',
                    'memory': 'string',
                    'pidMode': 'host'|'task',
                    'ipcMode': 'host'|'task'|'none',
                    'proxyConfiguration': {
                        'type': 'APPMESH',
                        'containerName': 'string',
                        'properties': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    }
                },
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskDefinition** *(dict) --* 
              The full task definition description.
              - **taskDefinitionArn** *(string) --* 
                The full Amazon Resource Name (ARN) of the task definition.
              - **containerDefinitions** *(list) --* 
                A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
                  - **name** *(string) --* 
                    The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 
                  - **image** *(string) --* 
                    The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    * When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks. 
                    * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                    * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                    * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                    * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                  - **repositoryCredentials** *(dict) --* 
                    The private repository authentication credentials to use.
                    - **credentialsParameter** *(string) --* 
                      The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
                      .. note::
                        When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.
                  - **cpu** *(integer) --* 
                    The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.
                    .. note::
                      You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.
                    For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:
                    * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares. 
                    * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                    On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.
                  - **memory** *(integer) --* 
                    The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    If your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.
                    For containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **memoryReservation** *(integer) --* 
                    The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **links** *(list) --* 
                    The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    .. warning::
                      Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.
                    - *(string) --* 
                  - **portMappings** *(list) --* 
                    The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
                    For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                    Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 
                    This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.
                    .. note::
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the ``networkBindings`` section  DescribeTasks responses.
                    - *(dict) --* 
                      Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
                      If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                      - **containerPort** *(integer) --* 
                        The port number on the container that is bound to the user-specified or automatically assigned host port.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see ``hostPort`` . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.
                      - **hostPort** *(integer) --* 
                        The port number on the container instance to reserve for your container.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, the ``hostPort`` can either be left blank or set to the same value as the ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
                        The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.
                        .. note::
                          The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.
                        The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output. A container instance can have up to 100 reserved ports at a time, including the default reserved ports. Automatically assigned ports don't count toward the 100 reserved ports limit.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .
                  - **essential** *(boolean) --* 
                    If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
                    All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **entryPoint** *(list) --* 
                    .. warning::
                      Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.
                    The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .
                    - *(string) --* 
                  - **command** *(list) --* 
                    The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ . If there are multiple arguments, each argument should be a separated string in the array.
                    - *(string) --* 
                  - **environment** *(list) --* 
                    The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. warning::
                      We do not recommend using plaintext environment variables for sensitive information, such as credential data.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
                  - **mountPoints** *(list) --* 
                    The mount points for data volumes in your container.
                    This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
                    - *(dict) --* 
                      Details on a volume mount point that is used in a container definition.
                      - **sourceVolume** *(string) --* 
                        The name of the volume to mount. Must be a volume name referenced in the ``name`` parameter of task definition ``volume`` .
                      - **containerPath** *(string) --* 
                        The path on the container to mount the host volume at.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **volumesFrom** *(list) --* 
                    Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - *(dict) --* 
                      Details on a data volume from another container in the same task definition.
                      - **sourceContainer** *(string) --* 
                        The name of another container within the same task definition from which to mount volumes.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **linuxParameters** *(dict) --* 
                    Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - **capabilities** *(dict) --* 
                      The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
                      .. note::
                        If you are using tasks that use the Fargate launch type, ``capabilities`` is supported but the ``add`` parameter is not supported.
                      - **add** *(list) --* 
                        The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        .. note::
                          If you are using tasks that use the Fargate launch type, the ``add`` parameter is not supported.
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                      - **drop** *(list) --* 
                        The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                    - **devices** *(list) --* 
                      Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``devices`` parameter is not supported.
                      - *(dict) --* 
                        An object representing a container instance host device.
                        - **hostPath** *(string) --* 
                          The path for the device on the host container instance.
                        - **containerPath** *(string) --* 
                          The path inside the container at which to expose the host device.
                        - **permissions** *(list) --* 
                          The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.
                          - *(string) --* 
                    - **initProcessEnabled** *(boolean) --* 
                      Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **sharedMemorySize** *(integer) --* 
                      The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``sharedMemorySize`` parameter is not supported.
                    - **tmpfs** *(list) --* 
                      The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``tmpfs`` parameter is not supported.
                      - *(dict) --* 
                        The container path, mount options, and size of the tmpfs mount.
                        - **containerPath** *(string) --* 
                          The absolute file path where the tmpfs volume is to be mounted.
                        - **size** *(integer) --* 
                          The size (in MiB) of the tmpfs volume.
                        - **mountOptions** *(list) --* 
                          The list of tmpfs volume mount options.
                          Valid values: ``"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"``  
                          - *(string) --* 
                  - **secrets** *(list) --* 
                    The secrets to pass to the container. For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - *(dict) --* 
                      An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                      * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                      * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                      For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      - **name** *(string) --* 
                        The name of the secret.
                      - **valueFrom** *(string) --* 
                        The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                        .. note::
                          If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **dependsOn** *(list) --* 
                    The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    - *(dict) --* 
                      The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                      Your Amazon ECS container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you are using tasks that use the Fargate launch type, container dependency parameters are not supported.
                      - **containerName** *(string) --* 
                        The name of a container.
                      - **condition** *(string) --* 
                        The dependency condition of the container. The following are the available conditions and their behavior:
                        * ``START`` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start. 
                        * ``COMPLETE`` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. 
                        * ``SUCCESS`` - This condition is the same as ``COMPLETE`` , but it also requires that the container exits with a ``zero`` status. 
                        * ``HEALTHY`` - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup. 
                  - **startTimeout** *(integer) --* 
                    Time duration to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a ``COMPLETE`` , ``SUCCESS`` , or ``HEALTHY`` status. If a ``startTimeout`` value is specified for containerB and it does not reach the desired status within that time then containerA will give up and not start. This results in the task transitioning to a ``STOPPED`` state.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                  - **stopTimeout** *(integer) --* 
                    Time duration to wait before the container is forcefully killed if it doesn't exit normally on its own. For tasks using the Fargate launch type, the max ``stopTimeout`` value is 2 minutes. This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    For tasks using the EC2 launch type, the stop timeout value for the container takes precedence over the ``ECS_CONTAINER_STOP_TIMEOUT`` container agent configuration parameter, if used. Container instances require at least version 1.26.0 of the container agent to enable a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **hostname** *(string) --* 
                    The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The ``hostname`` parameter is not supported if you are using the ``awsvpc`` network mode.
                  - **user** *(string) --* 
                    The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You can use the following formats. If specifying a UID or GID, you must specify it as a positive integer.
                    * ``user``   
                    * ``user:group``   
                    * ``uid``   
                    * ``uid:gid``   
                    * ``user:gid``   
                    * ``uid:group``   
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **workingDirectory** *(string) --* 
                    The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **disableNetworking** *(boolean) --* 
                    When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **privileged** *(boolean) --* 
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks using the Fargate launch type.
                  - **readonlyRootFilesystem** *(boolean) --* 
                    When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--read-only`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **dnsServers** *(list) --* 
                    A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **dnsSearchDomains** *(list) --* 
                    A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **extraHosts** *(list) --* 
                    A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks that use the ``awsvpc`` network mode.
                    - *(dict) --* 
                      Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 
                      - **hostname** *(string) --* 
                        The hostname to use in the ``/etc/hosts`` entry.
                      - **ipAddress** *(string) --* 
                        The IP address to use in the ``/etc/hosts`` entry.
                  - **dockerSecurityOptions** *(list) --* 
                    A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
                    This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **interactive** *(boolean) --* 
                    When this parameter is ``true`` , this allows you to deploy containerized applications that require ``stdin`` or a ``tty`` to be allocated. This parameter maps to ``OpenStdin`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--interactive`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **pseudoTerminal** *(boolean) --* 
                    When this parameter is ``true`` , a TTY is allocated. This parameter maps to ``Tty`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--tty`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **dockerLabels** *(dict) --* 
                    A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - *(string) --* 
                      - *(string) --* 
                  - **ulimits** *(list) --* 
                    A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(dict) --* 
                      The ``ulimit`` settings to pass to the container.
                      - **name** *(string) --* 
                        The ``type`` of the ``ulimit`` .
                      - **softLimit** *(integer) --* 
                        The soft limit for the ulimit type.
                      - **hardLimit** *(integer) --* 
                        The hard limit for the ulimit type.
                  - **logConfiguration** *(dict) --* 
                    The log configuration specification for the container.
                    For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                    For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                    This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.
                    .. note::
                      Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
                    This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **logDriver** *(string) --* 
                      The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.
                      For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                      For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                      For more information about using the ``awslogs`` log driver, see `Using the awslogs Log Driver <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.
                      This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **options** *(dict) --* 
                      The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                      - *(string) --* 
                        - *(string) --* 
                    - **secretOptions** *(list) --* 
                      The secrets to pass to the log configuration.
                      - *(dict) --* 
                        An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                        * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                        * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                        For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                        - **name** *(string) --* 
                          The name of the secret.
                        - **valueFrom** *(string) --* 
                          The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                          .. note::
                            If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **healthCheck** *(dict) --* 
                    The health check command and associated configuration parameters for the container. This parameter maps to ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``HEALTHCHECK`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - **command** *(list) --* 
                      A string array representing the command that the container runs to determine if it is healthy. The string array must start with ``CMD`` to execute the command arguments directly, or ``CMD-SHELL`` to run the command with the container's default shell. For example:
                       ``[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]``  
                      An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                      - *(string) --* 
                    - **interval** *(integer) --* 
                      The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.
                    - **timeout** *(integer) --* 
                      The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.
                    - **retries** *(integer) --* 
                      The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.
                    - **startPeriod** *(integer) --* 
                      The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The ``startPeriod`` is disabled by default.
                      .. note::
                        If a health check succeeds within the ``startPeriod`` , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
                  - **systemControls** *(list) --* 
                    A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network modes. For tasks that use the ``awsvpc`` network mode, the container that is started last determines which ``systemControls`` parameters take effect. For tasks that use the ``host`` network mode, it changes the container instance's namespaced kernel parameters as well as the containers.
                    - *(dict) --* 
                      A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network mode for the following reasons:
                      * For tasks that use the ``awsvpc`` network mode, if you set ``systemControls`` for any container, it applies to all containers in the task. If you set different ``systemControls`` for multiple containers in a single task, the container that is started last determines which ``systemControls`` take effect. 
                      * For tasks that use the ``host`` network mode, the ``systemControls`` parameter applies to the container instance's kernel parameter as well as that of all containers of any tasks running on that container instance. 
                      - **namespace** *(string) --* 
                        The namespaced kernel parameter for which to set a ``value`` .
                      - **value** *(string) --* 
                        The value for the namespaced kernel parameter specified in ``namespace`` .
                  - **resourceRequirements** *(list) --* 
                    The type and amount of a resource to assign to a container. The only supported resource is a GPU.
                    - *(dict) --* 
                      The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                      - **value** *(string) --* 
                        The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                      - **type** *(string) --* 
                        The type of resource to assign to a container. The only supported value is ``GPU`` .
              - **family** *(string) --* 
                The family of your task definition, used as the definition name.
              - **taskRoleArn** *(string) --* 
                The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **executionRoleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
              - **networkMode** *(string) --* 
                The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If you are using the Fargate launch type, the ``awsvpc`` network mode is required. If you are using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.
                With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 
                If the network mode is ``awsvpc`` , the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                .. note::
                  Currently, only Amazon ECS-optimized AMIs, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 
                If the network mode is ``host`` , you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
                Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 
                For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .
              - **revision** *(integer) --* 
                The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` . Each time that you register a new revision of a task definition in the same family, the revision value always increases by one, even if you have deregistered previous revisions in this family.
              - **volumes** *(list) --* 
                The list of volumes in a task.
                If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.
                For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  A data volume used in a task definition. For tasks that use a Docker volume, specify a ``DockerVolumeConfiguration`` . For tasks that use a bind mount host volume, specify a ``host`` and optional ``sourcePath`` . For more information, see `Using Data Volumes in Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html>`__ .
                  - **name** *(string) --* 
                    The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
                  - **host** *(dict) --* 
                    This parameter is specified when you are using bind mount host volumes. Bind mount host volumes are supported when you are using either the EC2 or Fargate launch types. The contents of the ``host`` parameter determine whether your bind mount host volume persists on the host container instance and where it is stored. If the ``host`` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .
                    - **sourcePath** *(string) --* 
                      When the ``host`` parameter is used, specify a ``sourcePath`` to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                      If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.
                  - **dockerVolumeConfiguration** *(dict) --* 
                    This parameter is specified when you are using Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the ``local`` driver. To use bind mounts, specify a ``host`` instead.
                    - **scope** *(string) --* 
                      The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a ``task`` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as ``shared`` persist after the task stops.
                    - **autoprovision** *(boolean) --* 
                      If this value is ``true`` , the Docker volume is created if it does not already exist.
                      .. note::
                        This field is only used if the ``scope`` is ``shared`` .
                    - **driver** *(string) --* 
                      The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use ``docker plugin ls`` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see `Docker plugin discovery <https://docs.docker.com/engine/extend/plugin_api/#plugin-discovery>`__ . This parameter maps to ``Driver`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxdriver`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                    - **driverOpts** *(dict) --* 
                      A map of Docker driver-specific options passed through. This parameter maps to ``DriverOpts`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxopt`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
                    - **labels** *(dict) --* 
                      Custom metadata to add to your Docker volume. This parameter maps to ``Labels`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxlabel`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
              - **status** *(string) --* 
                The status of the task definition.
              - **requiresAttributes** *(list) --* 
                The container instance attributes required by your task. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **placementConstraints** *(list) --* 
                An array of placement constraint objects to use for tasks. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An object representing a constraint on task placement in the task definition.
                  If you are using the Fargate launch type, task placement constraints are not supported.
                  For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **compatibilities** *(list) --* 
                The launch type to use with your task. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(string) --* 
              - **requiresCompatibilities** *(list) --* 
                The launch type that the task is using.
                - *(string) --* 
              - **cpu** *(string) --* 
                The number of ``cpu`` units used by the task. If you are using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:
                * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
              - **memory** *(string) --* 
                The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:
                * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
              - **pidMode** *(string) --* 
                The process namespace to use for the containers in the task. The valid values are ``host`` or ``task`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` PID mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace. For more information, see `PID settings <https://docs.docker.com/engine/reference/run/#pid-settings---pid>`__ in the *Docker run reference* .
                If the ``host`` PID mode is used, be aware that there is a heightened risk of undesired process namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **ipcMode** *(string) --* 
                The IPC resource namespace to use for the containers in the task. The valid values are ``host`` , ``task`` , or ``none`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same IPC resources. If ``none`` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see `IPC settings <https://docs.docker.com/engine/reference/run/#ipc-settings---ipc>`__ in the *Docker run reference* .
                If the ``host`` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                If you are setting namespaced kernel parameters using ``systemControls`` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see `System Controls <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                * For tasks that use the ``host`` IPC mode, IPC namespace related ``systemControls`` are not supported. 
                * For tasks that use the ``task`` IPC mode, IPC namespace related ``systemControls`` will apply to all containers within a task. 
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **proxyConfiguration** *(dict) --* 
                The configuration details for the App Mesh proxy.
                Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to enable a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **type** *(string) --* 
                  The proxy type. The only supported value is ``APPMESH`` .
                - **containerName** *(string) --* 
                  The name of the container that will serve as the App Mesh proxy.
                - **properties** *(list) --* 
                  The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.
                  * ``IgnoredUID`` - (Required) The user ID (UID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``IgnoredGID`` - (Required) The group ID (GID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``AppPorts`` - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the ``ProxyIngressPort`` and ``ProxyEgressPort`` . 
                  * ``ProxyIngressPort`` - (Required) Specifies the port that incoming traffic to the ``AppPorts`` is directed to. 
                  * ``ProxyEgressPort`` - (Required) Specifies the port that outgoing traffic from the ``AppPorts`` is directed to. 
                  * ``EgressIgnoredPorts`` - (Required) The egress traffic going to the specified ports is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  * ``EgressIgnoredIPs`` - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  - *(dict) --* 
                    A key-value pair object.
                    - **name** *(string) --* 
                      The name of the key-value pair. For environment variables, this is the name of the environment variable.
                    - **value** *(string) --* 
                      The value of the key-value pair. For environment variables, this is the value of the environment variable.
            - **tags** *(list) --* 
              The metadata that is applied to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
              - *(dict) --* 
                The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - **key** *(string) --* 
                  One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                - **value** *(string) --* 
                  The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type taskDefinition: string
        :param taskDefinition: **[REQUIRED]**
          The ``family`` for the latest ``ACTIVE`` revision, ``family`` and ``revision`` (``family:revision`` ) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.
        :type include: list
        :param include:
          Specifies whether to see the resource tags for the task definition. If ``TAGS`` is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_task_sets(self, cluster: str, service: str, taskSets: List = None) -> Dict:
        """
        Describes the task sets in the specified cluster and service. This is used when a service uses the ``EXTERNAL`` deployment controller type. For more information, see `Amazon ECS Deployment Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTaskSets>`_
        
        **Request Syntax**
        ::
          response = client.describe_task_sets(
              cluster='string',
              service='string',
              taskSets=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'taskSets': [
                    {
                        'id': 'string',
                        'taskSetArn': 'string',
                        'serviceArn': 'string',
                        'clusterArn': 'string',
                        'startedBy': 'string',
                        'externalId': 'string',
                        'status': 'string',
                        'taskDefinition': 'string',
                        'computedDesiredCount': 123,
                        'pendingCount': 123,
                        'runningCount': 123,
                        'createdAt': datetime(2015, 1, 1),
                        'updatedAt': datetime(2015, 1, 1),
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'networkConfiguration': {
                            'awsvpcConfiguration': {
                                'subnets': [
                                    'string',
                                ],
                                'securityGroups': [
                                    'string',
                                ],
                                'assignPublicIp': 'ENABLED'|'DISABLED'
                            }
                        },
                        'loadBalancers': [
                            {
                                'targetGroupArn': 'string',
                                'loadBalancerName': 'string',
                                'containerName': 'string',
                                'containerPort': 123
                            },
                        ],
                        'serviceRegistries': [
                            {
                                'registryArn': 'string',
                                'port': 123,
                                'containerName': 'string',
                                'containerPort': 123
                            },
                        ],
                        'scale': {
                            'value': 123.0,
                            'unit': 'PERCENT'
                        },
                        'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                        'stabilityStatusAt': datetime(2015, 1, 1)
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskSets** *(list) --* 
              The list of task sets described.
              - *(dict) --* 
                Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                - **id** *(string) --* 
                  The ID of the task set.
                - **taskSetArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task set.
                - **serviceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the service the task set exists in.
                - **clusterArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
                - **startedBy** *(string) --* 
                  The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
                - **externalId** *(string) --* 
                  The external ID associated with the task set.
                  If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                  If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
                - **status** *(string) --* 
                  The status of the task set. The following describes each state:
                    PRIMARY  
                  The task set is serving production traffic.
                    ACTIVE  
                  The task set is not serving production traffic.
                    DRAINING  
                  The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
                - **taskDefinition** *(string) --* 
                  The task definition the task set is using.
                - **computedDesiredCount** *(integer) --* 
                  The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
                - **pendingCount** *(integer) --* 
                  The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
                - **runningCount** *(integer) --* 
                  The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
                - **createdAt** *(datetime) --* 
                  The Unix timestamp for when the task set was created.
                - **updatedAt** *(datetime) --* 
                  The Unix timestamp for when the task set was last updated.
                - **launchType** *(string) --* 
                  The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **platformVersion** *(string) --* 
                  The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **networkConfiguration** *(dict) --* 
                  The network configuration for the task set.
                  - **awsvpcConfiguration** *(dict) --* 
                    The VPC subnets and security groups associated with a task.
                    .. note::
                      All specified subnets and security groups must be from the same VPC.
                    - **subnets** *(list) --* 
                      The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                      .. note::
                        All specified subnets must be from the same VPC.
                      - *(string) --* 
                    - **securityGroups** *(list) --* 
                      The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                      .. note::
                        All specified security groups must be from the same VPC.
                      - *(string) --* 
                    - **assignPublicIp** *(string) --* 
                      Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                - **loadBalancers** *(list) --* 
                  Details on a load balancer that is used with a task set.
                  - *(dict) --* 
                    Details on a load balancer that is used with a service.
                    If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                    If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                    Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                    - **targetGroupArn** *(string) --* 
                      The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                      .. warning::
                        If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                    - **loadBalancerName** *(string) --* 
                      The name of a load balancer.
                    - **containerName** *(string) --* 
                      The name of the container (as it appears in a container definition) to associate with the load balancer.
                    - **containerPort** *(integer) --* 
                      The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                - **serviceRegistries** *(list) --* 
                  The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                  - *(dict) --* 
                    Details of the service registry.
                    - **registryArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                    - **port** *(integer) --* 
                      The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                    - **containerName** *(string) --* 
                      The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                    - **containerPort** *(integer) --* 
                      The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                - **scale** *(dict) --* 
                  A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                  - **value** *(float) --* 
                    The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                  - **unit** *(string) --* 
                    The unit of measure for the scale value.
                - **stabilityStatus** *(string) --* 
                  The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                  * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                  * The ``pendingCount`` is ``0`` . 
                  * There are no tasks running on container instances in the ``DRAINING`` status. 
                  * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                  If any of those conditions are not met, the stability status returns ``STABILIZING`` .
                - **stabilityStatusAt** *(datetime) --* 
                  The Unix timestamp for when the task set stability status was retrieved.
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.
        :type service: string
        :param service: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.
        :type taskSets: list
        :param taskSets:
          The ID or full Amazon Resource Name (ARN) of task sets to describe.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_tasks(self, tasks: List, cluster: str = None, include: List = None) -> Dict:
        """
        Describes a specified task or tasks.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeTasks>`_
        
        **Request Syntax**
        ::
          response = client.describe_tasks(
              cluster='string',
              tasks=[
                  'string',
              ],
              include=[
                  'TAGS',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'tasks': [
                    {
                        'taskArn': 'string',
                        'clusterArn': 'string',
                        'taskDefinitionArn': 'string',
                        'containerInstanceArn': 'string',
                        'overrides': {
                            'containerOverrides': [
                                {
                                    'name': 'string',
                                    'command': [
                                        'string',
                                    ],
                                    'environment': [
                                        {
                                            'name': 'string',
                                            'value': 'string'
                                        },
                                    ],
                                    'cpu': 123,
                                    'memory': 123,
                                    'memoryReservation': 123,
                                    'resourceRequirements': [
                                        {
                                            'value': 'string',
                                            'type': 'GPU'
                                        },
                                    ]
                                },
                            ],
                            'taskRoleArn': 'string',
                            'executionRoleArn': 'string'
                        },
                        'lastStatus': 'string',
                        'desiredStatus': 'string',
                        'cpu': 'string',
                        'memory': 'string',
                        'containers': [
                            {
                                'containerArn': 'string',
                                'taskArn': 'string',
                                'name': 'string',
                                'lastStatus': 'string',
                                'exitCode': 123,
                                'reason': 'string',
                                'networkBindings': [
                                    {
                                        'bindIP': 'string',
                                        'containerPort': 123,
                                        'hostPort': 123,
                                        'protocol': 'tcp'|'udp'
                                    },
                                ],
                                'networkInterfaces': [
                                    {
                                        'attachmentId': 'string',
                                        'privateIpv4Address': 'string',
                                        'ipv6Address': 'string'
                                    },
                                ],
                                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                                'cpu': 'string',
                                'memory': 'string',
                                'memoryReservation': 'string',
                                'gpuIds': [
                                    'string',
                                ]
                            },
                        ],
                        'startedBy': 'string',
                        'version': 123,
                        'stoppedReason': 'string',
                        'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                        'connectivity': 'CONNECTED'|'DISCONNECTED',
                        'connectivityAt': datetime(2015, 1, 1),
                        'pullStartedAt': datetime(2015, 1, 1),
                        'pullStoppedAt': datetime(2015, 1, 1),
                        'executionStoppedAt': datetime(2015, 1, 1),
                        'createdAt': datetime(2015, 1, 1),
                        'startedAt': datetime(2015, 1, 1),
                        'stoppingAt': datetime(2015, 1, 1),
                        'stoppedAt': datetime(2015, 1, 1),
                        'group': 'string',
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'attachments': [
                            {
                                'id': 'string',
                                'type': 'string',
                                'status': 'string',
                                'details': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ]
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tasks** *(list) --* 
              The list of tasks.
              - *(dict) --* 
                Details on a task in a cluster.
                - **taskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task.
                - **clusterArn** *(string) --* 
                  The ARN of the cluster that hosts the task.
                - **taskDefinitionArn** *(string) --* 
                  The ARN of the task definition that creates the task.
                - **containerInstanceArn** *(string) --* 
                  The ARN of the container instances that host the task.
                - **overrides** *(dict) --* 
                  One or more container overrides.
                  - **containerOverrides** *(list) --* 
                    One or more container overrides sent to a task.
                    - *(dict) --* 
                      The overrides that should be sent to a container.
                      - **name** *(string) --* 
                        The name of the container that receives the override. This parameter is required if any override is specified.
                      - **command** *(list) --* 
                        The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                        - *(string) --* 
                      - **environment** *(list) --* 
                        The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                        - *(dict) --* 
                          A key-value pair object.
                          - **name** *(string) --* 
                            The name of the key-value pair. For environment variables, this is the name of the environment variable.
                          - **value** *(string) --* 
                            The value of the key-value pair. For environment variables, this is the value of the environment variable.
                      - **cpu** *(integer) --* 
                        The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **memory** *(integer) --* 
                        The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
                      - **memoryReservation** *(integer) --* 
                        The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **resourceRequirements** *(list) --* 
                        The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                        - *(dict) --* 
                          The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                          - **value** *(string) --* 
                            The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                          - **type** *(string) --* 
                            The type of resource to assign to a container. The only supported value is ``GPU`` .
                  - **taskRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                  - **executionRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
                - **lastStatus** *(string) --* 
                  The last known status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **desiredStatus** *(string) --* 
                  The desired status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **cpu** *(string) --* 
                  The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units, for example ``1024`` . It can also be expressed as a string using vCPUs, for example ``1 vCPU`` or ``1 vcpu`` . String values are converted to an integer indicating the CPU units when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional. Supported values are between ``128`` CPU units (``0.125`` vCPUs) and ``10240`` CPU units (``10`` vCPUs).
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``memory`` parameter:
                  * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                  * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                  * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                  * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                  * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
                - **memory** *(string) --* 
                  The amount of memory (in MiB) used by the task as expressed in a task definition. It can be expressed as an integer using MiB, for example ``1024`` . It can also be expressed as a string using GB, for example ``1GB`` or ``1 GB`` . String values are converted to an integer indicating the MiB when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional.
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``cpu`` parameter:
                  * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                  * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                  * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                  * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                  * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
                - **containers** *(list) --* 
                  The containers associated with the task.
                  - *(dict) --* 
                    A Docker container that is part of a task.
                    - **containerArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the container.
                    - **taskArn** *(string) --* 
                      The ARN of the task.
                    - **name** *(string) --* 
                      The name of the container.
                    - **lastStatus** *(string) --* 
                      The last known status of the container.
                    - **exitCode** *(integer) --* 
                      The exit code returned from the container.
                    - **reason** *(string) --* 
                      A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
                    - **networkBindings** *(list) --* 
                      The network bindings associated with the container.
                      - *(dict) --* 
                        Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                        - **bindIP** *(string) --* 
                          The IP address that the container is bound to on the container instance.
                        - **containerPort** *(integer) --* 
                          The port number on the container that is used with the network binding.
                        - **hostPort** *(integer) --* 
                          The port number on the host that is used with the network binding.
                        - **protocol** *(string) --* 
                          The protocol used for the network binding.
                    - **networkInterfaces** *(list) --* 
                      The network interfaces associated with the container.
                      - *(dict) --* 
                        An object representing the elastic network interface for tasks that use the ``awsvpc`` network mode.
                        - **attachmentId** *(string) --* 
                          The attachment ID for the network interface.
                        - **privateIpv4Address** *(string) --* 
                          The private IPv4 address for the network interface.
                        - **ipv6Address** *(string) --* 
                          The private IPv6 address for the network interface.
                    - **healthStatus** *(string) --* 
                      The health status of the container. If health checks are not configured for this container in its task definition, then it reports the health status as ``UNKNOWN`` .
                    - **cpu** *(string) --* 
                      The number of CPU units set for the container. The value will be ``0`` if no value was specified in the container definition when the task definition was registered.
                    - **memory** *(string) --* 
                      The hard limit (in MiB) of memory set for the container.
                    - **memoryReservation** *(string) --* 
                      The soft limit (in MiB) of memory set for the container.
                    - **gpuIds** *(list) --* 
                      The IDs of each GPU assigned to the container.
                      - *(string) --* 
                - **startedBy** *(string) --* 
                  The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
                - **version** *(integer) --* 
                  The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actionss with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.
                - **stoppedReason** *(string) --* 
                  The reason that the task was stopped.
                - **stopCode** *(string) --* 
                  The stop code indicating why a task was stopped. The ``stoppedReason`` may contain additional details.
                - **connectivity** *(string) --* 
                  The connectivity status of a task.
                - **connectivityAt** *(datetime) --* 
                  The Unix timestamp for when the task last went into ``CONNECTED`` status.
                - **pullStartedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull began.
                - **pullStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull completed.
                - **executionStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task execution stopped.
                - **createdAt** *(datetime) --* 
                  The Unix timestamp for when the task was created (the task entered the ``PENDING`` state).
                - **startedAt** *(datetime) --* 
                  The Unix timestamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).
                - **stoppingAt** *(datetime) --* 
                  The Unix timestamp for when the task stops (transitions from the ``RUNNING`` state to ``STOPPED`` ).
                - **stoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).
                - **group** *(string) --* 
                  The name of the task group associated with the task.
                - **launchType** *(string) --* 
                  The launch type on which your task is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **platformVersion** *(string) --* 
                  The platform version on which your task is running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **attachments** *(list) --* 
                  The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.
                  - *(dict) --* 
                    An object representing a container instance or task attachment.
                    - **id** *(string) --* 
                      The unique identifier for the attachment.
                    - **type** *(string) --* 
                      The type of the attachment, such as ``ElasticNetworkInterface`` .
                    - **status** *(string) --* 
                      The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                    - **details** *(list) --* 
                      Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **healthStatus** *(string) --* 
                  The health status for the task, which is determined by the health of the essential containers in the task. If all essential containers in the task are reporting as ``HEALTHY`` , then the task status also reports as ``HEALTHY`` . If any essential containers in the task are reporting as ``UNHEALTHY`` or ``UNKNOWN`` , then the task status also reports as ``UNHEALTHY`` or ``UNKNOWN`` , accordingly.
                  .. note::
                    The Amazon ECS container agent does not monitor or report on Docker health checks that are embedded in a container image (such as those specified in a parent image or from the image's Dockerfile) and not specified in the container definition. Health check parameters that are specified in a container definition override any Docker health checks that exist in the container image.
                - **tags** *(list) --* 
                  The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to describe. If you do not specify a cluster, the default cluster is assumed.
        :type tasks: list
        :param tasks: **[REQUIRED]**
          A list of up to 100 task IDs or full ARN entries.
          - *(string) --*
        :type include: list
        :param include:
          Specifies whether you want to see the resource tags for the task. If ``TAGS`` is specified, the tags are included in the response. If this field is omitted, tags are not included in the response.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def discover_poll_endpoint(self, containerInstance: str = None, cluster: str = None) -> Dict:
        """
        .. note::
          This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.
        Returns an endpoint for the Amazon ECS agent to poll for updates.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DiscoverPollEndpoint>`_
        
        **Request Syntax**
        ::
          response = client.discover_poll_endpoint(
              containerInstance='string',
              cluster='string'
          )
        
        **Response Syntax**
        ::
            {
                'endpoint': 'string',
                'telemetryEndpoint': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **endpoint** *(string) --* 
              The endpoint for the Amazon ECS agent to poll.
            - **telemetryEndpoint** *(string) --* 
              The telemetry endpoint for the Amazon ECS agent.
        :type containerInstance: string
        :param containerInstance:
          The container instance ID or full ARN of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster to which the container instance belongs.
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

    def list_account_settings(self, name: str = None, value: str = None, principalArn: str = None, effectiveSettings: bool = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the account settings for an Amazon ECS resource for a specified principal.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListAccountSettings>`_
        
        **Request Syntax**
        ::
          response = client.list_account_settings(
              name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
              value='string',
              principalArn='string',
              effectiveSettings=True|False,
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'settings': [
                    {
                        'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
                        'value': 'string',
                        'principalArn': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **settings** *(list) --* 
              The account settings for the resource.
              - *(dict) --* 
                The current account setting for a resource.
                - **name** *(string) --* 
                  The account resource name.
                - **value** *(string) --* 
                  The current account setting for the resource name. If ``enabled`` , the resource receives the new Amazon Resource Name (ARN) and resource identifier (ID) format. If ``disabled`` , the resource receives the old Amazon Resource Name (ARN) and resource identifier (ID) format.
                - **principalArn** *(string) --* 
                  The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the authenticated user is assumed.
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListAccountSettings`` request. When the results of a ``ListAccountSettings`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type name: string
        :param name:
          The resource name you want to list the account settings for.
        :type value: string
        :param value:
          The value of the account settings with which to filter results. You must also specify an account setting name to use this parameter.
        :type principalArn: string
        :param principalArn:
          The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.
        :type effectiveSettings: boolean
        :param effectiveSettings:
          Specifies whether to return the effective settings. If ``true`` , the account settings for the root user or the default setting for the ``principalArn`` . If ``false`` , the account settings for the ``principalArn`` are returned if they are set. Otherwise, no account settings are returned.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListAccountSettings`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of account setting results returned by ``ListAccountSettings`` in paginated output. When this parameter is used, ``ListAccountSettings`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListAccountSettings`` request with the returned ``nextToken`` value. This value can be between 1 and 10. If this parameter is not used, then ``ListAccountSettings`` returns up to 10 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_attributes(self, targetType: str, cluster: str = None, attributeName: str = None, attributeValue: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, ``ListAttributes`` returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value, for example, to see which container instances in a cluster are running a Linux AMI (``ecs.os-type=linux`` ). 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListAttributes>`_
        
        **Request Syntax**
        ::
          response = client.list_attributes(
              cluster='string',
              targetType='container-instance',
              attributeName='string',
              attributeValue='string',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **attributes** *(list) --* 
              A list of attribute objects that meet the criteria of the request.
              - *(dict) --* 
                An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **name** *(string) --* 
                  The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                - **value** *(string) --* 
                  The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                - **targetType** *(string) --* 
                  The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                - **targetId** *(string) --* 
                  The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListAttributes`` request. When the results of a ``ListAttributes`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.
        :type targetType: string
        :param targetType: **[REQUIRED]**
          The type of the target with which to list attributes.
        :type attributeName: string
        :param attributeName:
          The name of the attribute with which to filter the results.
        :type attributeValue: string
        :param attributeValue:
          The value of the attribute with which to filter results. You must also specify an attribute name to use this parameter.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListAttributes`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of cluster results returned by ``ListAttributes`` in paginated output. When this parameter is used, ``ListAttributes`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListAttributes`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListAttributes`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_clusters(self, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Returns a list of existing clusters.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListClusters>`_
        
        **Request Syntax**
        ::
          response = client.list_clusters(
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'clusterArns': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **clusterArns** *(list) --* 
              The list of full Amazon Resource Name (ARN) entries for each cluster associated with your account.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListClusters`` request. When the results of a ``ListClusters`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListClusters`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of cluster results returned by ``ListClusters`` in paginated output. When this parameter is used, ``ListClusters`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListClusters`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListClusters`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_container_instances(self, cluster: str = None, filter: str = None, nextToken: str = None, maxResults: int = None, status: str = None) -> Dict:
        """
        Returns a list of container instances in a specified cluster. You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements inside the ``filter`` parameter. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListContainerInstances>`_
        
        **Request Syntax**
        ::
          response = client.list_container_instances(
              cluster='string',
              filter='string',
              nextToken='string',
              maxResults=123,
              status='ACTIVE'|'DRAINING'
          )
        
        **Response Syntax**
        ::
            {
                'containerInstanceArns': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstanceArns** *(list) --* 
              The list of container instances with full ARN entries for each container instance associated with the specified cluster.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListContainerInstances`` request. When the results of a ``ListContainerInstances`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.
        :type filter: string
        :param filter:
          You can filter the results of a ``ListContainerInstances`` operation with cluster query language statements. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListContainerInstances`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of container instance results returned by ``ListContainerInstances`` in paginated output. When this parameter is used, ``ListContainerInstances`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListContainerInstances`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListContainerInstances`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type status: string
        :param status:
          Filters the container instances by status. For example, if you specify the ``DRAINING`` status, the results include only container instances that have been set to ``DRAINING`` using  UpdateContainerInstancesState . If you do not specify this parameter, the default is to include container instances set to ``ACTIVE`` and ``DRAINING`` .
        :rtype: dict
        :returns:
        """
        pass

    def list_services(self, cluster: str = None, nextToken: str = None, maxResults: int = None, launchType: str = None, schedulingStrategy: str = None) -> Dict:
        """
        Lists the services that are running in a specified cluster.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListServices>`_
        
        **Request Syntax**
        ::
          response = client.list_services(
              cluster='string',
              nextToken='string',
              maxResults=123,
              launchType='EC2'|'FARGATE',
              schedulingStrategy='REPLICA'|'DAEMON'
          )
        
        **Response Syntax**
        ::
            {
                'serviceArns': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **serviceArns** *(list) --* 
              The list of full ARN entries for each service associated with the specified cluster.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListServices`` request. When the results of a ``ListServices`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the services to list. If you do not specify a cluster, the default cluster is assumed.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListServices`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of service results returned by ``ListServices`` in paginated output. When this parameter is used, ``ListServices`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListServices`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListServices`` returns up to 10 results and a ``nextToken`` value if applicable.
        :type launchType: string
        :param launchType:
          The launch type for the services to list.
        :type schedulingStrategy: string
        :param schedulingStrategy:
          The scheduling strategy for services to list.
        :rtype: dict
        :returns:
        """
        pass

    def list_tags_for_resource(self, resourceArn: str) -> Dict:
        """
        List the tags for an Amazon ECS resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTagsForResource>`_
        
        **Request Syntax**
        ::
          response = client.list_tags_for_resource(
              resourceArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tags** *(list) --* 
              The tags for the resource.
              - *(dict) --* 
                The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - **key** *(string) --* 
                  One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                - **value** *(string) --* 
                  The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
        :rtype: dict
        :returns:
        """
        pass

    def list_task_definition_families(self, familyPrefix: str = None, status: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Returns a list of task definition families that are registered to your account (which may include task definition families that no longer have any ``ACTIVE`` task definition revisions).
        You can filter out task definition families that do not contain any ``ACTIVE`` task definition revisions by setting the ``status`` parameter to ``ACTIVE`` . You can also filter the results with the ``familyPrefix`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitionFamilies>`_
        
        **Request Syntax**
        ::
          response = client.list_task_definition_families(
              familyPrefix='string',
              status='ACTIVE'|'INACTIVE'|'ALL',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'families': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **families** *(list) --* 
              The list of task definition family names that match the ``ListTaskDefinitionFamilies`` request.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListTaskDefinitionFamilies`` request. When the results of a ``ListTaskDefinitionFamilies`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type familyPrefix: string
        :param familyPrefix:
          The ``familyPrefix`` is a string that is used to filter the results of ``ListTaskDefinitionFamilies`` . If you specify a ``familyPrefix`` , only task definition family names that begin with the ``familyPrefix`` string are returned.
        :type status: string
        :param status:
          The task definition family status with which to filter the ``ListTaskDefinitionFamilies`` results. By default, both ``ACTIVE`` and ``INACTIVE`` task definition families are listed. If this parameter is set to ``ACTIVE`` , only task definition families that have an ``ACTIVE`` task definition revision are returned. If this parameter is set to ``INACTIVE`` , only task definition families that do not have any ``ACTIVE`` task definition revisions are returned. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListTaskDefinitionFamilies`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of task definition family results returned by ``ListTaskDefinitionFamilies`` in paginated output. When this parameter is used, ``ListTaskDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTaskDefinitionFamilies`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTaskDefinitionFamilies`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_task_definitions(self, familyPrefix: str = None, status: str = None, sort: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        """
        Returns a list of task definitions that are registered to your account. You can filter the results by family name with the ``familyPrefix`` parameter or by status with the ``status`` parameter.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTaskDefinitions>`_
        
        **Request Syntax**
        ::
          response = client.list_task_definitions(
              familyPrefix='string',
              status='ACTIVE'|'INACTIVE',
              sort='ASC'|'DESC',
              nextToken='string',
              maxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'taskDefinitionArns': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskDefinitionArns** *(list) --* 
              The list of task definition Amazon Resource Name (ARN) entries for the ``ListTaskDefinitions`` request.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListTaskDefinitions`` request. When the results of a ``ListTaskDefinitions`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type familyPrefix: string
        :param familyPrefix:
          The full family name with which to filter the ``ListTaskDefinitions`` results. Specifying a ``familyPrefix`` limits the listed task definitions to task definition revisions that belong to that family.
        :type status: string
        :param status:
          The task definition status with which to filter the ``ListTaskDefinitions`` results. By default, only ``ACTIVE`` task definitions are listed. By setting this parameter to ``INACTIVE`` , you can view task definitions that are ``INACTIVE`` as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the ``status`` value constant in each subsequent request.
        :type sort: string
        :param sort:
          The order in which to sort the results. Valid values are ``ASC`` and ``DESC`` . By default (``ASC`` ), task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to ``DESC`` reverses the sort order on family name and revision so that the newest task definitions in a family are listed first.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListTaskDefinitions`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of task definition results returned by ``ListTaskDefinitions`` in paginated output. When this parameter is used, ``ListTaskDefinitions`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTaskDefinitions`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTaskDefinitions`` returns up to 100 results and a ``nextToken`` value if applicable.
        :rtype: dict
        :returns:
        """
        pass

    def list_tasks(self, cluster: str = None, containerInstance: str = None, family: str = None, nextToken: str = None, maxResults: int = None, startedBy: str = None, serviceName: str = None, desiredStatus: str = None, launchType: str = None) -> Dict:
        """
        Returns a list of tasks for a specified cluster. You can filter the results by family name, by a particular container instance, or by the desired status of the task with the ``family`` , ``containerInstance`` , and ``desiredStatus`` parameters.
        Recently stopped tasks might appear in the returned results. Currently, stopped tasks appear in the returned results for at least one hour. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/ListTasks>`_
        
        **Request Syntax**
        ::
          response = client.list_tasks(
              cluster='string',
              containerInstance='string',
              family='string',
              nextToken='string',
              maxResults=123,
              startedBy='string',
              serviceName='string',
              desiredStatus='RUNNING'|'PENDING'|'STOPPED',
              launchType='EC2'|'FARGATE'
          )
        
        **Response Syntax**
        ::
            {
                'taskArns': [
                    'string',
                ],
                'nextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskArns** *(list) --* 
              The list of task ARN entries for the ``ListTasks`` request.
              - *(string) --* 
            - **nextToken** *(string) --* 
              The ``nextToken`` value to include in a future ``ListTasks`` request. When the results of a ``ListTasks`` request exceed ``maxResults`` , this value can be used to retrieve the next page of results. This value is ``null`` when there are no more results to return.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the tasks to list. If you do not specify a cluster, the default cluster is assumed.
        :type containerInstance: string
        :param containerInstance:
          The container instance ID or full ARN of the container instance with which to filter the ``ListTasks`` results. Specifying a ``containerInstance`` limits the results to tasks that belong to that container instance.
        :type family: string
        :param family:
          The name of the family with which to filter the ``ListTasks`` results. Specifying a ``family`` limits the results to tasks that belong to that family.
        :type nextToken: string
        :param nextToken:
          The ``nextToken`` value returned from a previous paginated ``ListTasks`` request where ``maxResults`` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the ``nextToken`` value.
          .. note::
            This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
        :type maxResults: integer
        :param maxResults:
          The maximum number of task results returned by ``ListTasks`` in paginated output. When this parameter is used, ``ListTasks`` only returns ``maxResults`` results in a single page along with a ``nextToken`` response element. The remaining results of the initial request can be seen by sending another ``ListTasks`` request with the returned ``nextToken`` value. This value can be between 1 and 100. If this parameter is not used, then ``ListTasks`` returns up to 100 results and a ``nextToken`` value if applicable.
        :type startedBy: string
        :param startedBy:
          The ``startedBy`` value with which to filter the task results. Specifying a ``startedBy`` value limits the results to tasks that were started with that value.
        :type serviceName: string
        :param serviceName:
          The name of the service with which to filter the ``ListTasks`` results. Specifying a ``serviceName`` limits the results to tasks that belong to that service.
        :type desiredStatus: string
        :param desiredStatus:
          The task desired status with which to filter the ``ListTasks`` results. Specifying a ``desiredStatus`` of ``STOPPED`` limits the results to tasks that Amazon ECS has set the desired status to ``STOPPED`` . This can be useful for debugging tasks that are not starting properly or have died or finished. The default status filter is ``RUNNING`` , which shows tasks that Amazon ECS has set the desired status to ``RUNNING`` .
          .. note::
            Although you can filter results based on a desired status of ``PENDING`` , this does not return any results. Amazon ECS never sets the desired status of a task to that value (only a task\'s ``lastStatus`` may have a value of ``PENDING`` ).
        :type launchType: string
        :param launchType:
          The launch type for services to list.
        :rtype: dict
        :returns:
        """
        pass

    def put_account_setting(self, name: str, value: str, principalArn: str = None) -> Dict:
        """
        Modifies the ARN and resource ID format of a resource type for a specified IAM user, IAM role, or the root user for an account. If the account setting for the root user is changed, it sets the default setting for all of the IAM users and roles for which no individual account setting has been set. The opt-in and opt-out account setting can be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource will be defined by the opt-in status of the IAM user or role that created the resource. Enabling this setting is required to use new Amazon ECS features such as resource tagging. For more information, see `Amazon Resource Names (ARNs) and IDs <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-resource-ids.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/PutAccountSetting>`_
        
        **Request Syntax**
        ::
          response = client.put_account_setting(
              name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
              value='string',
              principalArn='string'
          )
        
        **Response Syntax**
        ::
            {
                'setting': {
                    'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
                    'value': 'string',
                    'principalArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **setting** *(dict) --* 
              The current account setting for a resource.
              - **name** *(string) --* 
                The account resource name.
              - **value** *(string) --* 
                The current account setting for the resource name. If ``enabled`` , the resource receives the new Amazon Resource Name (ARN) and resource identifier (ID) format. If ``disabled`` , the resource receives the old Amazon Resource Name (ARN) and resource identifier (ID) format.
              - **principalArn** *(string) --* 
                The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the authenticated user is assumed.
        :type name: string
        :param name: **[REQUIRED]**
          The resource name for which to enable the new format. If ``serviceLongArnFormat`` is specified, the ARN for your Amazon ECS services is affected. If ``taskLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If ``containerInstanceLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS container instances is affected.
        :type value: string
        :param value: **[REQUIRED]**
          The account setting value for the specified principal ARN. Accepted values are ``enabled`` and ``disabled`` .
        :type principalArn: string
        :param principalArn:
          The ARN of the principal, which can be an IAM user, IAM role, or the root user. If you specify the root user, it modifies the ARN and resource ID format for all IAM users, IAM roles, and the root user of the account unless an IAM user or role explicitly overrides these settings for themselves. If this field is omitted, the settings are changed only for the authenticated user.
        :rtype: dict
        :returns:
        """
        pass

    def put_account_setting_default(self, name: str, value: str) -> Dict:
        """
        Modifies the ARN and resource ID format of a resource type for all IAM users on an account for which no individual account setting has been set. Enabling this setting is required to use new Amazon ECS features such as resource tagging.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/PutAccountSettingDefault>`_
        
        **Request Syntax**
        ::
          response = client.put_account_setting_default(
              name='serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
              value='string'
          )
        
        **Response Syntax**
        ::
            {
                'setting': {
                    'name': 'serviceLongArnFormat'|'taskLongArnFormat'|'containerInstanceLongArnFormat',
                    'value': 'string',
                    'principalArn': 'string'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **setting** *(dict) --* 
              The current account setting for a resource.
              - **name** *(string) --* 
                The account resource name.
              - **value** *(string) --* 
                The current account setting for the resource name. If ``enabled`` , the resource receives the new Amazon Resource Name (ARN) and resource identifier (ID) format. If ``disabled`` , the resource receives the old Amazon Resource Name (ARN) and resource identifier (ID) format.
              - **principalArn** *(string) --* 
                The ARN of the principal, which can be an IAM user, IAM role, or the root user. If this field is omitted, the authenticated user is assumed.
        :type name: string
        :param name: **[REQUIRED]**
          The resource type to enable the new format for. If ``serviceLongArnFormat`` is specified, the ARN for your Amazon ECS services is affected. If ``taskLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS tasks are affected. If ``containerInstanceLongArnFormat`` is specified, the ARN and resource ID for your Amazon ECS container instances are affected.
        :type value: string
        :param value: **[REQUIRED]**
          The account setting value for the specified principal ARN. Accepted values are ``enabled`` and ``disabled`` .
        :rtype: dict
        :returns:
        """
        pass

    def put_attributes(self, attributes: List, cluster: str = None) -> Dict:
        """
        Create or update an attribute on an Amazon ECS resource. If the attribute does not exist, it is created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use  DeleteAttributes . For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/PutAttributes>`_
        
        **Request Syntax**
        ::
          response = client.put_attributes(
              cluster='string',
              attributes=[
                  {
                      'name': 'string',
                      'value': 'string',
                      'targetType': 'container-instance',
                      'targetId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'attributes': [
                    {
                        'name': 'string',
                        'value': 'string',
                        'targetType': 'container-instance',
                        'targetId': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **attributes** *(list) --* 
              The attributes applied to your resource.
              - *(dict) --* 
                An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **name** *(string) --* 
                  The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                - **value** *(string) --* 
                  The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                - **targetType** *(string) --* 
                  The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                - **targetId** *(string) --* 
                  The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to apply attributes. If you do not specify a cluster, the default cluster is assumed.
        :type attributes: list
        :param attributes: **[REQUIRED]**
          The attributes to apply to your resource. You can specify up to 10 custom attributes per resource. You can specify up to 10 attributes in a single call.
          - *(dict) --*
            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **name** *(string) --* **[REQUIRED]**
              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            - **value** *(string) --*
              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            - **targetType** *(string) --*
              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            - **targetId** *(string) --*
              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
        :rtype: dict
        :returns:
        """
        pass

    def register_container_instance(self, cluster: str = None, instanceIdentityDocument: str = None, instanceIdentityDocumentSignature: str = None, totalResources: List = None, versionInfo: Dict = None, containerInstanceArn: str = None, attributes: List = None, platformDevices: List = None, tags: List = None) -> Dict:
        """
        .. note::
          This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.
        Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RegisterContainerInstance>`_
        
        **Request Syntax**
        ::
          response = client.register_container_instance(
              cluster='string',
              instanceIdentityDocument='string',
              instanceIdentityDocumentSignature='string',
              totalResources=[
                  {
                      'name': 'string',
                      'type': 'string',
                      'doubleValue': 123.0,
                      'longValue': 123,
                      'integerValue': 123,
                      'stringSetValue': [
                          'string',
                      ]
                  },
              ],
              versionInfo={
                  'agentVersion': 'string',
                  'agentHash': 'string',
                  'dockerVersion': 'string'
              },
              containerInstanceArn='string',
              attributes=[
                  {
                      'name': 'string',
                      'value': 'string',
                      'targetType': 'container-instance',
                      'targetId': 'string'
                  },
              ],
              platformDevices=[
                  {
                      'id': 'string',
                      'type': 'GPU'
                  },
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'containerInstance': {
                    'containerInstanceArn': 'string',
                    'ec2InstanceId': 'string',
                    'version': 123,
                    'versionInfo': {
                        'agentVersion': 'string',
                        'agentHash': 'string',
                        'dockerVersion': 'string'
                    },
                    'remainingResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'registeredResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'status': 'string',
                    'agentConnected': True|False,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                    'attributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'registeredAt': datetime(2015, 1, 1),
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstance** *(dict) --* 
              The container instance that was registered.
              - **containerInstanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
              - **ec2InstanceId** *(string) --* 
                The EC2 instance ID of the container instance.
              - **version** *(integer) --* 
                The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.
              - **versionInfo** *(dict) --* 
                The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
                - **agentVersion** *(string) --* 
                  The version number of the Amazon ECS container agent.
                - **agentHash** *(string) --* 
                  The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
                - **dockerVersion** *(string) --* 
                  The Docker version running on the container instance.
              - **remainingResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the remaining CPU and memory that has not already been allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the ``host`` or ``bridge`` network mode). Any port that is not specified here is available for new tasks.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **registeredResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **status** *(string) --* 
                The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **agentConnected** *(boolean) --* 
                This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Only instances connected to an agent can accept placement requests.
              - **runningTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``RUNNING`` status.
              - **pendingTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``PENDING`` status.
              - **agentUpdateStatus** *(string) --* 
                The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .
              - **attributes** *(list) --* 
                The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **registeredAt** *(datetime) --* 
                The Unix timestamp for when the container instance was registered.
              - **attachments** *(list) --* 
                The elastic network interfaces associated with the container instance.
                - *(dict) --* 
                  An object representing a container instance or task attachment.
                  - **id** *(string) --* 
                    The unique identifier for the attachment.
                  - **type** *(string) --* 
                    The type of the attachment, such as ``ElasticNetworkInterface`` .
                  - **status** *(string) --* 
                    The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                  - **details** *(list) --* 
                    Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **tags** *(list) --* 
                The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster with which to register your container instance. If you do not specify a cluster, the default cluster is assumed.
        :type instanceIdentityDocument: string
        :param instanceIdentityDocument:
          The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: ``curl http://169.254.169.254/latest/dynamic/instance-identity/document/``
        :type instanceIdentityDocumentSignature: string
        :param instanceIdentityDocumentSignature:
          The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: ``curl http://169.254.169.254/latest/dynamic/instance-identity/signature/``
        :type totalResources: list
        :param totalResources:
          The resources available on the instance.
          - *(dict) --*
            Describes the resources available for a container instance.
            - **name** *(string) --*
              The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
            - **type** *(string) --*
              The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
            - **doubleValue** *(float) --*
              When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
            - **longValue** *(integer) --*
              When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
            - **integerValue** *(integer) --*
              When the ``integerValue`` type is set, the value of the resource must be an integer.
            - **stringSetValue** *(list) --*
              When the ``stringSetValue`` type is set, the value of the resource must be a string type.
              - *(string) --*
        :type versionInfo: dict
        :param versionInfo:
          The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
          - **agentVersion** *(string) --*
            The version number of the Amazon ECS container agent.
          - **agentHash** *(string) --*
            The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
          - **dockerVersion** *(string) --*
            The Docker version running on the container instance.
        :type containerInstanceArn: string
        :param containerInstanceArn:
          The ARN of the container instance (if it was previously registered).
        :type attributes: list
        :param attributes:
          The container instance attributes that this container instance supports.
          - *(dict) --*
            An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **name** *(string) --* **[REQUIRED]**
              The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
            - **value** *(string) --*
              The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
            - **targetType** *(string) --*
              The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
            - **targetId** *(string) --*
              The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
        :type platformDevices: list
        :param platformDevices:
          The devices that are available on the container instance. The only supported device type is a GPU.
          - *(dict) --*
            The devices that are available on the container instance. The only supported device type is a GPU.
            - **id** *(string) --* **[REQUIRED]**
              The ID for the GPU(s) on the container instance. The available GPU IDs can also be obtained on the container instance in the ``/var/lib/ecs/gpu/nvidia_gpu_info.json`` file.
            - **type** *(string) --* **[REQUIRED]**
              The type of device that is available on the container instance. The only supported value is ``GPU`` .
        :type tags: list
        :param tags:
          The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :rtype: dict
        :returns:
        """
        pass

    def register_task_definition(self, family: str, containerDefinitions: List, taskRoleArn: str = None, executionRoleArn: str = None, networkMode: str = None, volumes: List = None, placementConstraints: List = None, requiresCompatibilities: List = None, cpu: str = None, memory: str = None, tags: List = None, pidMode: str = None, ipcMode: str = None, proxyConfiguration: Dict = None) -> Dict:
        """
        .. _https://docs.docker.com/engine/reference/commandline/run/: https://docs.docker.com/engine/reference/commandline/run/
        .. _https://docs.docker.com/engine/reference/commandline/volume_create/: https://docs.docker.com/engine/reference/commandline/volume_create/
        Registers a new task definition from the supplied ``family`` and ``containerDefinitions`` . Optionally, you can add data volumes to your containers with the ``volumes`` parameter. For more information about task definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        You can specify an IAM role for your task with the ``taskRoleArn`` parameter. When you specify an IAM role for a task, its containers can then use the latest versions of the AWS CLI or SDKs to make API requests to the AWS services that are specified in the IAM policy associated with the role. For more information, see `IAM Roles for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        You can specify a Docker networking mode for the containers in your task definition with the ``networkMode`` parameter. The available network modes correspond to those described in `Network settings <https://docs.docker.com/engine/reference/run/#/network-settings>`__ in the Docker run reference. If you specify the ``awsvpc`` network mode, the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RegisterTaskDefinition>`_
        
        **Request Syntax**
        ::
          response = client.register_task_definition(
              family='string',
              taskRoleArn='string',
              executionRoleArn='string',
              networkMode='bridge'|'host'|'awsvpc'|'none',
              containerDefinitions=[
                  {
                      'name': 'string',
                      'image': 'string',
                      'repositoryCredentials': {
                          'credentialsParameter': 'string'
                      },
                      'cpu': 123,
                      'memory': 123,
                      'memoryReservation': 123,
                      'links': [
                          'string',
                      ],
                      'portMappings': [
                          {
                              'containerPort': 123,
                              'hostPort': 123,
                              'protocol': 'tcp'|'udp'
                          },
                      ],
                      'essential': True|False,
                      'entryPoint': [
                          'string',
                      ],
                      'command': [
                          'string',
                      ],
                      'environment': [
                          {
                              'name': 'string',
                              'value': 'string'
                          },
                      ],
                      'mountPoints': [
                          {
                              'sourceVolume': 'string',
                              'containerPath': 'string',
                              'readOnly': True|False
                          },
                      ],
                      'volumesFrom': [
                          {
                              'sourceContainer': 'string',
                              'readOnly': True|False
                          },
                      ],
                      'linuxParameters': {
                          'capabilities': {
                              'add': [
                                  'string',
                              ],
                              'drop': [
                                  'string',
                              ]
                          },
                          'devices': [
                              {
                                  'hostPath': 'string',
                                  'containerPath': 'string',
                                  'permissions': [
                                      'read'|'write'|'mknod',
                                  ]
                              },
                          ],
                          'initProcessEnabled': True|False,
                          'sharedMemorySize': 123,
                          'tmpfs': [
                              {
                                  'containerPath': 'string',
                                  'size': 123,
                                  'mountOptions': [
                                      'string',
                                  ]
                              },
                          ]
                      },
                      'secrets': [
                          {
                              'name': 'string',
                              'valueFrom': 'string'
                          },
                      ],
                      'dependsOn': [
                          {
                              'containerName': 'string',
                              'condition': 'START'|'COMPLETE'|'SUCCESS'|'HEALTHY'
                          },
                      ],
                      'startTimeout': 123,
                      'stopTimeout': 123,
                      'hostname': 'string',
                      'user': 'string',
                      'workingDirectory': 'string',
                      'disableNetworking': True|False,
                      'privileged': True|False,
                      'readonlyRootFilesystem': True|False,
                      'dnsServers': [
                          'string',
                      ],
                      'dnsSearchDomains': [
                          'string',
                      ],
                      'extraHosts': [
                          {
                              'hostname': 'string',
                              'ipAddress': 'string'
                          },
                      ],
                      'dockerSecurityOptions': [
                          'string',
                      ],
                      'interactive': True|False,
                      'pseudoTerminal': True|False,
                      'dockerLabels': {
                          'string': 'string'
                      },
                      'ulimits': [
                          {
                              'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                              'softLimit': 123,
                              'hardLimit': 123
                          },
                      ],
                      'logConfiguration': {
                          'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                          'options': {
                              'string': 'string'
                          },
                          'secretOptions': [
                              {
                                  'name': 'string',
                                  'valueFrom': 'string'
                              },
                          ]
                      },
                      'healthCheck': {
                          'command': [
                              'string',
                          ],
                          'interval': 123,
                          'timeout': 123,
                          'retries': 123,
                          'startPeriod': 123
                      },
                      'systemControls': [
                          {
                              'namespace': 'string',
                              'value': 'string'
                          },
                      ],
                      'resourceRequirements': [
                          {
                              'value': 'string',
                              'type': 'GPU'
                          },
                      ]
                  },
              ],
              volumes=[
                  {
                      'name': 'string',
                      'host': {
                          'sourcePath': 'string'
                      },
                      'dockerVolumeConfiguration': {
                          'scope': 'task'|'shared',
                          'autoprovision': True|False,
                          'driver': 'string',
                          'driverOpts': {
                              'string': 'string'
                          },
                          'labels': {
                              'string': 'string'
                          }
                      }
                  },
              ],
              placementConstraints=[
                  {
                      'type': 'memberOf',
                      'expression': 'string'
                  },
              ],
              requiresCompatibilities=[
                  'EC2'|'FARGATE',
              ],
              cpu='string',
              memory='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              pidMode='host'|'task',
              ipcMode='host'|'task'|'none',
              proxyConfiguration={
                  'type': 'APPMESH',
                  'containerName': 'string',
                  'properties': [
                      {
                          'name': 'string',
                          'value': 'string'
                      },
                  ]
              }
          )
        
        **Response Syntax**
        ::
            {
                'taskDefinition': {
                    'taskDefinitionArn': 'string',
                    'containerDefinitions': [
                        {
                            'name': 'string',
                            'image': 'string',
                            'repositoryCredentials': {
                                'credentialsParameter': 'string'
                            },
                            'cpu': 123,
                            'memory': 123,
                            'memoryReservation': 123,
                            'links': [
                                'string',
                            ],
                            'portMappings': [
                                {
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'essential': True|False,
                            'entryPoint': [
                                'string',
                            ],
                            'command': [
                                'string',
                            ],
                            'environment': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ],
                            'mountPoints': [
                                {
                                    'sourceVolume': 'string',
                                    'containerPath': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'volumesFrom': [
                                {
                                    'sourceContainer': 'string',
                                    'readOnly': True|False
                                },
                            ],
                            'linuxParameters': {
                                'capabilities': {
                                    'add': [
                                        'string',
                                    ],
                                    'drop': [
                                        'string',
                                    ]
                                },
                                'devices': [
                                    {
                                        'hostPath': 'string',
                                        'containerPath': 'string',
                                        'permissions': [
                                            'read'|'write'|'mknod',
                                        ]
                                    },
                                ],
                                'initProcessEnabled': True|False,
                                'sharedMemorySize': 123,
                                'tmpfs': [
                                    {
                                        'containerPath': 'string',
                                        'size': 123,
                                        'mountOptions': [
                                            'string',
                                        ]
                                    },
                                ]
                            },
                            'secrets': [
                                {
                                    'name': 'string',
                                    'valueFrom': 'string'
                                },
                            ],
                            'dependsOn': [
                                {
                                    'containerName': 'string',
                                    'condition': 'START'|'COMPLETE'|'SUCCESS'|'HEALTHY'
                                },
                            ],
                            'startTimeout': 123,
                            'stopTimeout': 123,
                            'hostname': 'string',
                            'user': 'string',
                            'workingDirectory': 'string',
                            'disableNetworking': True|False,
                            'privileged': True|False,
                            'readonlyRootFilesystem': True|False,
                            'dnsServers': [
                                'string',
                            ],
                            'dnsSearchDomains': [
                                'string',
                            ],
                            'extraHosts': [
                                {
                                    'hostname': 'string',
                                    'ipAddress': 'string'
                                },
                            ],
                            'dockerSecurityOptions': [
                                'string',
                            ],
                            'interactive': True|False,
                            'pseudoTerminal': True|False,
                            'dockerLabels': {
                                'string': 'string'
                            },
                            'ulimits': [
                                {
                                    'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
                                    'softLimit': 123,
                                    'hardLimit': 123
                                },
                            ],
                            'logConfiguration': {
                                'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk',
                                'options': {
                                    'string': 'string'
                                },
                                'secretOptions': [
                                    {
                                        'name': 'string',
                                        'valueFrom': 'string'
                                    },
                                ]
                            },
                            'healthCheck': {
                                'command': [
                                    'string',
                                ],
                                'interval': 123,
                                'timeout': 123,
                                'retries': 123,
                                'startPeriod': 123
                            },
                            'systemControls': [
                                {
                                    'namespace': 'string',
                                    'value': 'string'
                                },
                            ],
                            'resourceRequirements': [
                                {
                                    'value': 'string',
                                    'type': 'GPU'
                                },
                            ]
                        },
                    ],
                    'family': 'string',
                    'taskRoleArn': 'string',
                    'executionRoleArn': 'string',
                    'networkMode': 'bridge'|'host'|'awsvpc'|'none',
                    'revision': 123,
                    'volumes': [
                        {
                            'name': 'string',
                            'host': {
                                'sourcePath': 'string'
                            },
                            'dockerVolumeConfiguration': {
                                'scope': 'task'|'shared',
                                'autoprovision': True|False,
                                'driver': 'string',
                                'driverOpts': {
                                    'string': 'string'
                                },
                                'labels': {
                                    'string': 'string'
                                }
                            }
                        },
                    ],
                    'status': 'ACTIVE'|'INACTIVE',
                    'requiresAttributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'placementConstraints': [
                        {
                            'type': 'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'compatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'requiresCompatibilities': [
                        'EC2'|'FARGATE',
                    ],
                    'cpu': 'string',
                    'memory': 'string',
                    'pidMode': 'host'|'task',
                    'ipcMode': 'host'|'task'|'none',
                    'proxyConfiguration': {
                        'type': 'APPMESH',
                        'containerName': 'string',
                        'properties': [
                            {
                                'name': 'string',
                                'value': 'string'
                            },
                        ]
                    }
                },
                'tags': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskDefinition** *(dict) --* 
              The full description of the registered task definition.
              - **taskDefinitionArn** *(string) --* 
                The full Amazon Resource Name (ARN) of the task definition.
              - **containerDefinitions** *(list) --* 
                A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
                  - **name** *(string) --* 
                    The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . 
                  - **image** *(string) --* 
                    The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    * When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks. 
                    * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .  
                    * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ). 
                    * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ). 
                    * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ). 
                  - **repositoryCredentials** *(dict) --* 
                    The private repository authentication credentials to use.
                    - **credentialsParameter** *(string) --* 
                      The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
                      .. note::
                        When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.
                  - **cpu** *(integer) --* 
                    The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.
                    .. note::
                      You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.
                    For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
                    On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:
                    * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares. 
                    * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2. 
                    On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.
                  - **memory** *(integer) --* 
                    The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    If your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.
                    For containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **memoryReservation** *(integer) --* 
                    The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
                    For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
                    The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers. 
                  - **links** *(list) --* 
                    The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    .. warning::
                      Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.
                    - *(string) --* 
                  - **portMappings** *(list) --* 
                    The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
                    For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                    Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container's mapped port from the host itself. 
                    This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can't specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.
                    .. note::
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the ``networkBindings`` section  DescribeTasks responses.
                    - *(dict) --* 
                      Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
                      If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                      After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                      - **containerPort** *(integer) --* 
                        The port number on the container that is bound to the user-specified or automatically assigned host port.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see ``hostPort`` . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.
                      - **hostPort** *(integer) --* 
                        The port number on the container instance to reserve for your container.
                        If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, the ``hostPort`` can either be left blank or set to the same value as the ``containerPort`` .
                        If you are using containers in a task with the ``bridge`` network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
                        The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.
                        .. note::
                          The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.
                        The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output. A container instance can have up to 100 reserved ports at a time, including the default reserved ports. Automatically assigned ports don't count toward the 100 reserved ports limit.
                      - **protocol** *(string) --* 
                        The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .
                  - **essential** *(boolean) --* 
                    If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
                    All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **entryPoint** *(list) --* 
                    .. warning::
                      Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.
                    The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .
                    - *(string) --* 
                  - **command** *(list) --* 
                    The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ . If there are multiple arguments, each argument should be a separated string in the array.
                    - *(string) --* 
                  - **environment** *(list) --* 
                    The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. warning::
                      We do not recommend using plaintext environment variables for sensitive information, such as credential data.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
                  - **mountPoints** *(list) --* 
                    The mount points for data volumes in your container.
                    This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
                    - *(dict) --* 
                      Details on a volume mount point that is used in a container definition.
                      - **sourceVolume** *(string) --* 
                        The name of the volume to mount. Must be a volume name referenced in the ``name`` parameter of task definition ``volume`` .
                      - **containerPath** *(string) --* 
                        The path on the container to mount the host volume at.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **volumesFrom** *(list) --* 
                    Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - *(dict) --* 
                      Details on a data volume from another container in the same task definition.
                      - **sourceContainer** *(string) --* 
                        The name of another container within the same task definition from which to mount volumes.
                      - **readOnly** *(boolean) --* 
                        If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
                  - **linuxParameters** *(dict) --* 
                    Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - **capabilities** *(dict) --* 
                      The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
                      .. note::
                        If you are using tasks that use the Fargate launch type, ``capabilities`` is supported but the ``add`` parameter is not supported.
                      - **add** *(list) --* 
                        The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        .. note::
                          If you are using tasks that use the Fargate launch type, the ``add`` parameter is not supported.
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                      - **drop** *(list) --* 
                        The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                        Valid values: ``"ALL" | "AUDIT_CONTROL" | "AUDIT_WRITE" | "BLOCK_SUSPEND" | "CHOWN" | "DAC_OVERRIDE" | "DAC_READ_SEARCH" | "FOWNER" | "FSETID" | "IPC_LOCK" | "IPC_OWNER" | "KILL" | "LEASE" | "LINUX_IMMUTABLE" | "MAC_ADMIN" | "MAC_OVERRIDE" | "MKNOD" | "NET_ADMIN" | "NET_BIND_SERVICE" | "NET_BROADCAST" | "NET_RAW" | "SETFCAP" | "SETGID" | "SETPCAP" | "SETUID" | "SYS_ADMIN" | "SYS_BOOT" | "SYS_CHROOT" | "SYS_MODULE" | "SYS_NICE" | "SYS_PACCT" | "SYS_PTRACE" | "SYS_RAWIO" | "SYS_RESOURCE" | "SYS_TIME" | "SYS_TTY_CONFIG" | "SYSLOG" | "WAKE_ALARM"``  
                        - *(string) --* 
                    - **devices** *(list) --* 
                      Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``devices`` parameter is not supported.
                      - *(dict) --* 
                        An object representing a container instance host device.
                        - **hostPath** *(string) --* 
                          The path for the device on the host container instance.
                        - **containerPath** *(string) --* 
                          The path inside the container at which to expose the host device.
                        - **permissions** *(list) --* 
                          The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.
                          - *(string) --* 
                    - **initProcessEnabled** *(boolean) --* 
                      Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **sharedMemorySize** *(integer) --* 
                      The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``sharedMemorySize`` parameter is not supported.
                    - **tmpfs** *(list) --* 
                      The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      .. note::
                        If you are using tasks that use the Fargate launch type, the ``tmpfs`` parameter is not supported.
                      - *(dict) --* 
                        The container path, mount options, and size of the tmpfs mount.
                        - **containerPath** *(string) --* 
                          The absolute file path where the tmpfs volume is to be mounted.
                        - **size** *(integer) --* 
                          The size (in MiB) of the tmpfs volume.
                        - **mountOptions** *(list) --* 
                          The list of tmpfs volume mount options.
                          Valid values: ``"defaults" | "ro" | "rw" | "suid" | "nosuid" | "dev" | "nodev" | "exec" | "noexec" | "sync" | "async" | "dirsync" | "remount" | "mand" | "nomand" | "atime" | "noatime" | "diratime" | "nodiratime" | "bind" | "rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime" | "norelatime" | "strictatime" | "nostrictatime" | "mode" | "uid" | "gid" | "nr_inodes" | "nr_blocks" | "mpol"``  
                          - *(string) --* 
                  - **secrets** *(list) --* 
                    The secrets to pass to the container. For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - *(dict) --* 
                      An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                      * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                      * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                      For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      - **name** *(string) --* 
                        The name of the secret.
                      - **valueFrom** *(string) --* 
                        The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                        .. note::
                          If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **dependsOn** *(list) --* 
                    The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    - *(dict) --* 
                      The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                      Your Amazon ECS container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you are using tasks that use the Fargate launch type, container dependency parameters are not supported.
                      - **containerName** *(string) --* 
                        The name of a container.
                      - **condition** *(string) --* 
                        The dependency condition of the container. The following are the available conditions and their behavior:
                        * ``START`` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start. 
                        * ``COMPLETE`` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. 
                        * ``SUCCESS`` - This condition is the same as ``COMPLETE`` , but it also requires that the container exits with a ``zero`` status. 
                        * ``HEALTHY`` - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup. 
                  - **startTimeout** *(integer) --* 
                    Time duration to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a ``COMPLETE`` , ``SUCCESS`` , or ``HEALTHY`` status. If a ``startTimeout`` value is specified for containerB and it does not reach the desired status within that time then containerA will give up and not start. This results in the task transitioning to a ``STOPPED`` state.
                    For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                  - **stopTimeout** *(integer) --* 
                    Time duration to wait before the container is forcefully killed if it doesn't exit normally on its own. For tasks using the Fargate launch type, the max ``stopTimeout`` value is 2 minutes. This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
                    For tasks using the EC2 launch type, the stop timeout value for the container takes precedence over the ``ECS_CONTAINER_STOP_TIMEOUT`` container agent configuration parameter, if used. Container instances require at least version 1.26.0 of the container agent to enable a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **hostname** *(string) --* 
                    The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The ``hostname`` parameter is not supported if you are using the ``awsvpc`` network mode.
                  - **user** *(string) --* 
                    The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    You can use the following formats. If specifying a UID or GID, you must specify it as a positive integer.
                    * ``user``   
                    * ``user:group``   
                    * ``uid``   
                    * ``uid:gid``   
                    * ``user:gid``   
                    * ``uid:group``   
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **workingDirectory** *(string) --* 
                    The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **disableNetworking** *(boolean) --* 
                    When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **privileged** *(boolean) --* 
                    When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks using the Fargate launch type.
                  - **readonlyRootFilesystem** *(boolean) --* 
                    When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--read-only`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                  - **dnsServers** *(list) --* 
                    A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **dnsSearchDomains** *(list) --* 
                    A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **extraHosts** *(list) --* 
                    A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      This parameter is not supported for Windows containers or tasks that use the ``awsvpc`` network mode.
                    - *(dict) --* 
                      Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition . 
                      - **hostname** *(string) --* 
                        The hostname to use in the ``/etc/hosts`` entry.
                      - **ipAddress** *(string) --* 
                        The IP address to use in the ``/etc/hosts`` entry.
                  - **dockerSecurityOptions** *(list) --* 
                    A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
                    This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      This parameter is not supported for Windows containers.
                    - *(string) --* 
                  - **interactive** *(boolean) --* 
                    When this parameter is ``true`` , this allows you to deploy containerized applications that require ``stdin`` or a ``tty`` to be allocated. This parameter maps to ``OpenStdin`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--interactive`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **pseudoTerminal** *(boolean) --* 
                    When this parameter is ``true`` , a TTY is allocated. This parameter maps to ``Tty`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--tty`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  - **dockerLabels** *(dict) --* 
                    A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - *(string) --* 
                      - *(string) --* 
                  - **ulimits** *(list) --* 
                    A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      This parameter is not supported for Windows containers.
                    - *(dict) --* 
                      The ``ulimit`` settings to pass to the container.
                      - **name** *(string) --* 
                        The ``type`` of the ``ulimit`` .
                      - **softLimit** *(integer) --* 
                        The soft limit for the ulimit type.
                      - **hardLimit** *(integer) --* 
                        The hard limit for the ulimit type.
                  - **logConfiguration** *(dict) --* 
                    The log configuration specification for the container.
                    For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                    For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                    This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.
                    .. note::
                      Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
                    This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    .. note::
                      The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **logDriver** *(string) --* 
                      The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.
                      For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                      For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                      For more information about using the ``awslogs`` log driver, see `Using the awslogs Log Driver <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                      .. note::
                        If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.
                      This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                    - **options** *(dict) --* 
                      The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format '{{.Server.APIVersion}}'``  
                      - *(string) --* 
                        - *(string) --* 
                    - **secretOptions** *(list) --* 
                      The secrets to pass to the log configuration.
                      - *(dict) --* 
                        An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                        * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter. 
                        * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter. 
                        For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                        - **name** *(string) --* 
                          The name of the secret.
                        - **valueFrom** *(string) --* 
                          The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                          .. note::
                            If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
                  - **healthCheck** *(dict) --* 
                    The health check command and associated configuration parameters for the container. This parameter maps to ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``HEALTHCHECK`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    - **command** *(list) --* 
                      A string array representing the command that the container runs to determine if it is healthy. The string array must start with ``CMD`` to execute the command arguments directly, or ``CMD-SHELL`` to run the command with the container's default shell. For example:
                       ``[ "CMD-SHELL", "curl -f http://localhost/ || exit 1" ]``  
                      An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                      - *(string) --* 
                    - **interval** *(integer) --* 
                      The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.
                    - **timeout** *(integer) --* 
                      The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.
                    - **retries** *(integer) --* 
                      The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.
                    - **startPeriod** *(integer) --* 
                      The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The ``startPeriod`` is disabled by default.
                      .. note::
                        If a health check succeeds within the ``startPeriod`` , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
                  - **systemControls** *(list) --* 
                    A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                    .. note::
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network modes. For tasks that use the ``awsvpc`` network mode, the container that is started last determines which ``systemControls`` parameters take effect. For tasks that use the ``host`` network mode, it changes the container instance's namespaced kernel parameters as well as the containers.
                    - *(dict) --* 
                      A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                      It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network mode for the following reasons:
                      * For tasks that use the ``awsvpc`` network mode, if you set ``systemControls`` for any container, it applies to all containers in the task. If you set different ``systemControls`` for multiple containers in a single task, the container that is started last determines which ``systemControls`` take effect. 
                      * For tasks that use the ``host`` network mode, the ``systemControls`` parameter applies to the container instance's kernel parameter as well as that of all containers of any tasks running on that container instance. 
                      - **namespace** *(string) --* 
                        The namespaced kernel parameter for which to set a ``value`` .
                      - **value** *(string) --* 
                        The value for the namespaced kernel parameter specified in ``namespace`` .
                  - **resourceRequirements** *(list) --* 
                    The type and amount of a resource to assign to a container. The only supported resource is a GPU.
                    - *(dict) --* 
                      The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                      - **value** *(string) --* 
                        The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                      - **type** *(string) --* 
                        The type of resource to assign to a container. The only supported value is ``GPU`` .
              - **family** *(string) --* 
                The family of your task definition, used as the definition name.
              - **taskRoleArn** *(string) --* 
                The ARN of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code in order to take advantage of the feature. For more information, see `Windows IAM Roles for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **executionRoleArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
              - **networkMode** *(string) --* 
                The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If you are using the Fargate launch type, the ``awsvpc`` network mode is required. If you are using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.
                With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. 
                If the network mode is ``awsvpc`` , the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                .. note::
                  Currently, only Amazon ECS-optimized AMIs, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode. 
                If the network mode is ``host`` , you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
                Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object. 
                For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .
              - **revision** *(integer) --* 
                The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is ``1`` . Each time that you register a new revision of a task definition in the same family, the revision value always increases by one, even if you have deregistered previous revisions in this family.
              - **volumes** *(list) --* 
                The list of volumes in a task.
                If you are using the Fargate launch type, the ``host`` and ``sourcePath`` parameters are not supported.
                For more information about volume definition parameters and defaults, see `Amazon ECS Task Definitions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(dict) --* 
                  A data volume used in a task definition. For tasks that use a Docker volume, specify a ``DockerVolumeConfiguration`` . For tasks that use a bind mount host volume, specify a ``host`` and optional ``sourcePath`` . For more information, see `Using Data Volumes in Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html>`__ .
                  - **name** *(string) --* 
                    The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
                  - **host** *(dict) --* 
                    This parameter is specified when you are using bind mount host volumes. Bind mount host volumes are supported when you are using either the EC2 or Fargate launch types. The contents of the ``host`` parameter determine whether your bind mount host volume persists on the host container instance and where it is stored. If the ``host`` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
                    Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .
                    - **sourcePath** *(string) --* 
                      When the ``host`` parameter is used, specify a ``sourcePath`` to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                      If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.
                  - **dockerVolumeConfiguration** *(dict) --* 
                    This parameter is specified when you are using Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the ``local`` driver. To use bind mounts, specify a ``host`` instead.
                    - **scope** *(string) --* 
                      The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a ``task`` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as ``shared`` persist after the task stops.
                    - **autoprovision** *(boolean) --* 
                      If this value is ``true`` , the Docker volume is created if it does not already exist.
                      .. note::
                        This field is only used if the ``scope`` is ``shared`` .
                    - **driver** *(string) --* 
                      The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use ``docker plugin ls`` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see `Docker plugin discovery <https://docs.docker.com/engine/extend/plugin_api/#plugin-discovery>`__ . This parameter maps to ``Driver`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxdriver`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                    - **driverOpts** *(dict) --* 
                      A map of Docker driver-specific options passed through. This parameter maps to ``DriverOpts`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxopt`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
                    - **labels** *(dict) --* 
                      Custom metadata to add to your Docker volume. This parameter maps to ``Labels`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxlabel`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                      - *(string) --* 
                        - *(string) --* 
              - **status** *(string) --* 
                The status of the task definition.
              - **requiresAttributes** *(list) --* 
                The container instance attributes required by your task. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **placementConstraints** *(list) --* 
                An array of placement constraint objects to use for tasks. This field is not valid if you are using the Fargate launch type for your task.
                - *(dict) --* 
                  An object representing a constraint on task placement in the task definition.
                  If you are using the Fargate launch type, task placement constraints are not supported.
                  For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **compatibilities** *(list) --* 
                The launch type to use with your task. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - *(string) --* 
              - **requiresCompatibilities** *(list) --* 
                The launch type that the task is using.
                - *(string) --* 
              - **cpu** *(string) --* 
                The number of ``cpu`` units used by the task. If you are using the EC2 launch type, this field is optional and any value can be used. If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``memory`` parameter:
                * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
              - **memory** *(string) --* 
                The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the ``cpu`` parameter:
                * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
              - **pidMode** *(string) --* 
                The process namespace to use for the containers in the task. The valid values are ``host`` or ``task`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` PID mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace. For more information, see `PID settings <https://docs.docker.com/engine/reference/run/#pid-settings---pid>`__ in the *Docker run reference* .
                If the ``host`` PID mode is used, be aware that there is a heightened risk of undesired process namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **ipcMode** *(string) --* 
                The IPC resource namespace to use for the containers in the task. The valid values are ``host`` , ``task`` , or ``none`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same IPC resources. If ``none`` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see `IPC settings <https://docs.docker.com/engine/reference/run/#ipc-settings---ipc>`__ in the *Docker run reference* .
                If the ``host`` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
                If you are setting namespaced kernel parameters using ``systemControls`` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see `System Controls <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                * For tasks that use the ``host`` IPC mode, IPC namespace related ``systemControls`` are not supported. 
                * For tasks that use the ``task`` IPC mode, IPC namespace related ``systemControls`` will apply to all containers within a task. 
                .. note::
                  This parameter is not supported for Windows containers or tasks using the Fargate launch type.
              - **proxyConfiguration** *(dict) --* 
                The configuration details for the App Mesh proxy.
                Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to enable a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **type** *(string) --* 
                  The proxy type. The only supported value is ``APPMESH`` .
                - **containerName** *(string) --* 
                  The name of the container that will serve as the App Mesh proxy.
                - **properties** *(list) --* 
                  The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.
                  * ``IgnoredUID`` - (Required) The user ID (UID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``IgnoredGID`` - (Required) The group ID (GID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty. 
                  * ``AppPorts`` - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the ``ProxyIngressPort`` and ``ProxyEgressPort`` . 
                  * ``ProxyIngressPort`` - (Required) Specifies the port that incoming traffic to the ``AppPorts`` is directed to. 
                  * ``ProxyEgressPort`` - (Required) Specifies the port that outgoing traffic from the ``AppPorts`` is directed to. 
                  * ``EgressIgnoredPorts`` - (Required) The egress traffic going to the specified ports is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  * ``EgressIgnoredIPs`` - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list. 
                  - *(dict) --* 
                    A key-value pair object.
                    - **name** *(string) --* 
                      The name of the key-value pair. For environment variables, this is the name of the environment variable.
                    - **value** *(string) --* 
                      The value of the key-value pair. For environment variables, this is the value of the environment variable.
            - **tags** *(list) --* 
              The list of tags associated with the task definition.
              - *(dict) --* 
                The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - **key** *(string) --* 
                  One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                - **value** *(string) --* 
                  The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type family: string
        :param family: **[REQUIRED]**
          You must specify a ``family`` for a task definition, which allows you to track multiple versions of the same task definition. The ``family`` is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
        :type taskRoleArn: string
        :param taskRoleArn:
          The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see `IAM Roles for Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type executionRoleArn: string
        :param executionRoleArn:
          The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
        :type networkMode: string
        :param networkMode:
          The Docker networking mode to use for the containers in the task. The valid values are ``none`` , ``bridge`` , ``awsvpc`` , and ``host`` . The default Docker network mode is ``bridge`` . If you are using the Fargate launch type, the ``awsvpc`` network mode is required. If you are using the EC2 launch type, any network mode can be used. If the network mode is set to ``none`` , you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.
          With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings.
          If the network mode is ``awsvpc`` , the task is allocated an elastic network interface, and you must specify a  NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          .. note::
            Currently, only Amazon ECS-optimized AMIs, other Amazon Linux variants with the ``ecs-init`` package, or AWS Fargate infrastructure support the ``awsvpc`` network mode.
          If the network mode is ``host`` , you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.
          Docker for Windows uses different network modes than Docker for Linux. When you register a task definition with Windows containers, you must not specify a network mode. If you use the console to register a task definition with Windows containers, you must choose the ``<default>`` network mode object.
          For more information, see `Network settings <https://docs.docker.com/engine/reference/run/#network-settings>`__ in the *Docker run reference* .
        :type containerDefinitions: list
        :param containerDefinitions: **[REQUIRED]**
          A list of container definitions in JSON format that describe the different containers that make up your task.
          - *(dict) --*
            Container definitions are used in task definitions to describe the different containers that are launched as part of a task.
            - **name** *(string) --*
              The name of a container. If you are linking multiple containers together in a task definition, the ``name`` of one container can be entered in the ``links`` of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This parameter maps to ``name`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--name`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
            - **image** *(string) --*
              The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with either `` *repository-url* /*image* :*tag* `` or `` *repository-url* /*image* @*digest* `` . Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to ``Image`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``IMAGE`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              * When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image are not propagated to already running tasks.
              * Images in Amazon ECR repositories can be specified by either using the full ``registry/repository:tag`` or ``registry/repository@digest`` . For example, ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>:latest`` or ``012345678910.dkr.ecr.<region-name>.amazonaws.com/<repository-name>@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE`` .
              * Images in official repositories on Docker Hub use a single name (for example, ``ubuntu`` or ``mongo`` ).
              * Images in other repositories on Docker Hub are qualified with an organization name (for example, ``amazon/amazon-ecs-agent`` ).
              * Images in other online repositories are qualified further by a domain name (for example, ``quay.io/assemblyline/ubuntu`` ).
            - **repositoryCredentials** *(dict) --*
              The private repository authentication credentials to use.
              - **credentialsParameter** *(string) --* **[REQUIRED]**
                The Amazon Resource Name (ARN) of the secret containing the private repository credentials.
                .. note::
                  When you are using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same Region as the task that you are launching then you can use either the full ARN or the name of the secret. When you are using the AWS Management Console, you must specify the full ARN of the secret.
            - **cpu** *(integer) --*
              The number of ``cpu`` units reserved for the container. This parameter maps to ``CpuShares`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cpu-shares`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level ``cpu`` value.
              .. note::
                You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the `Amazon EC2 Instances <http://aws.amazon.com/ec2/instance-types/>`__ detail page by 1,024.
              For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
              Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that is the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task would be guaranteed a minimum of 512 CPU units when needed, and each container could float to higher CPU usage if the other container was not using it, but if both tasks were 100% active all of the time, they would be limited to 512 CPU units.
              On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. For more information, see `CPU share constraint <https://docs.docker.com/engine/reference/run/#cpu-share-constraint>`__ in the Docker documentation. The minimum valid CPU share value that the Linux kernel allows is 2. However, the CPU parameter is not required, and you can use CPU values below 2 in your container definitions. For CPU values below 2 (including null), the behavior varies based on your Amazon ECS container agent version:
              * **Agent versions less than or equal to 1.1.0:** Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares.
              * **Agent versions greater than or equal to 1.2.0:** Null, zero, and CPU values of 1 are passed to Docker as 2.
              On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that is described in the task definition.
            - **memory** *(integer) --*
              The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to ``Memory`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              If your containers are part of a task using the Fargate launch type, this field is optional and the only requirement is that the total amount of memory reserved for all containers within a task be lower than the task ``memory`` value.
              For containers that are part of a task using the EC2 launch type, you must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
              The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.
            - **memoryReservation** *(integer) --*
              The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the ``memory`` parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to ``MemoryReservation`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--memory-reservation`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              You must specify a non-zero integer for one or both of ``memory`` or ``memoryReservation`` in container definitions. If you specify both, ``memory`` must be greater than ``memoryReservation`` . If you specify ``memoryReservation`` , then that value is subtracted from the available memory resources for the container instance on which the container is placed. Otherwise, the value of ``memory`` is used.
              For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a ``memoryReservation`` of 128 MiB, and a ``memory`` hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.
              The Docker daemon reserves a minimum of 4 MiB of memory for a container, so you should not specify fewer than 4 MiB of memory for your containers.
            - **links** *(list) --*
              The ``link`` parameter allows containers to communicate with each other without the need for port mappings. Only supported if the network mode of a task definition is set to ``bridge`` . The ``name:internalName`` construct is analogous to ``name:alias`` in Docker links. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. For more information about linking Docker containers, go to `https\://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/ <https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/>`__ . This parameter maps to ``Links`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--link`` option to ` ``docker run`` https://docs.docker.com/engine/reference/commandline/run/`__ .
              .. note::
                This parameter is not supported for Windows containers.
              .. warning::
                Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.
              - *(string) --*
            - **portMappings** *(list) --*
              The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.
              For task definitions that use the ``awsvpc`` network mode, you should only specify the ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
              Port mappings on Windows use the ``NetNAT`` gateway address rather than ``localhost`` . There is no loopback for port mappings on Windows, so you cannot access a container\'s mapped port from the host itself.
              This parameter maps to ``PortBindings`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--publish`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . If the network mode of a task definition is set to ``none`` , then you can\'t specify port mappings. If the network mode of a task definition is set to ``host`` , then host ports must either be undefined or they must match the container port in the port mapping.
              .. note::
                After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the **Network Bindings** section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the ``networkBindings`` section  DescribeTasks responses.
              - *(dict) --*
                Port mappings allow containers to access ports on the host container instance to send or receive traffic. Port mappings are specified as part of the container definition.
                If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` . The ``hostPort`` can be left blank or it must be the same value as the ``containerPort`` .
                After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                - **containerPort** *(integer) --*
                  The port number on the container that is bound to the user-specified or automatically assigned host port.
                  If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, exposed ports should be specified using ``containerPort`` .
                  If you are using containers in a task with the ``bridge`` network mode and you specify a container port and not a host port, your container automatically receives a host port in the ephemeral port range. For more information, see ``hostPort`` . Port mappings that are automatically assigned in this way do not count toward the 100 reserved ports limit of a container instance.
                - **hostPort** *(integer) --*
                  The port number on the container instance to reserve for your container.
                  If you are using containers in a task with the ``awsvpc`` or ``host`` network mode, the ``hostPort`` can either be left blank or set to the same value as the ``containerPort`` .
                  If you are using containers in a task with the ``bridge`` network mode, you can specify a non-reserved host port for your container port mapping, or you can omit the ``hostPort`` (or set it to ``0`` ) while specifying a ``containerPort`` and your container automatically receives a port in the ephemeral port range for your container instance operating system and Docker version.
                  The default ephemeral port range for Docker version 1.6.0 and later is listed on the instance under ``/proc/sys/net/ipv4/ip_local_port_range`` . If this kernel parameter is unavailable, the default ephemeral port range from 49153 through 65535 is used. Do not attempt to specify a host port in the ephemeral port range as these are reserved for automatic assignment. In general, ports below 32768 are outside of the ephemeral port range.
                  .. note::
                    The default ephemeral port range from 49153 through 65535 is always used for Docker versions before 1.6.0.
                  The default reserved ports are 22 for SSH, the Docker ports 2375 and 2376, and the Amazon ECS container agent ports 51678-51680. Any host port that was previously specified in a running task is also reserved while the task is running (after a task stops, the host port is released). The current reserved ports are displayed in the ``remainingResources`` of  DescribeContainerInstances output. A container instance can have up to 100 reserved ports at a time, including the default reserved ports. Automatically assigned ports don\'t count toward the 100 reserved ports limit.
                - **protocol** *(string) --*
                  The protocol used for the port mapping. Valid values are ``tcp`` and ``udp`` . The default is ``tcp`` .
            - **essential** *(boolean) --*
              If the ``essential`` parameter of a container is marked as ``true`` , and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the ``essential`` parameter of a container is marked as ``false`` , then its failure does not affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.
              All tasks must have at least one essential container. If you have an application that is composed of multiple containers, you should group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see `Application Architecture <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **entryPoint** *(list) --*
              .. warning::
                Early versions of the Amazon ECS container agent do not properly handle ``entryPoint`` parameters. If you have problems using ``entryPoint`` , update your container agent or enter your commands and arguments as ``command`` array items instead.
              The entry point that is passed to the container. This parameter maps to ``Entrypoint`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--entrypoint`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#entrypoint <https://docs.docker.com/engine/reference/builder/#entrypoint>`__ .
              - *(string) --*
            - **command** *(list) --*
              The command that is passed to the container. This parameter maps to ``Cmd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``COMMAND`` parameter to `docker run <https://docs.docker.com/engine/reference/run/>`__ . For more information, see `https\://docs.docker.com/engine/reference/builder/#cmd <https://docs.docker.com/engine/reference/builder/#cmd>`__ . If there are multiple arguments, each argument should be a separated string in the array.
              - *(string) --*
            - **environment** *(list) --*
              The environment variables to pass to a container. This parameter maps to ``Env`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--env`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. warning::
                We do not recommend using plaintext environment variables for sensitive information, such as credential data.
              - *(dict) --*
                A key-value pair object.
                - **name** *(string) --*
                  The name of the key-value pair. For environment variables, this is the name of the environment variable.
                - **value** *(string) --*
                  The value of the key-value pair. For environment variables, this is the value of the environment variable.
            - **mountPoints** *(list) --*
              The mount points for data volumes in your container.
              This parameter maps to ``Volumes`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volume`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives.
              - *(dict) --*
                Details on a volume mount point that is used in a container definition.
                - **sourceVolume** *(string) --*
                  The name of the volume to mount. Must be a volume name referenced in the ``name`` parameter of task definition ``volume`` .
                - **containerPath** *(string) --*
                  The path on the container to mount the host volume at.
                - **readOnly** *(boolean) --*
                  If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
            - **volumesFrom** *(list) --*
              Data volumes to mount from another container. This parameter maps to ``VolumesFrom`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--volumes-from`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              - *(dict) --*
                Details on a data volume from another container in the same task definition.
                - **sourceContainer** *(string) --*
                  The name of another container within the same task definition from which to mount volumes.
                - **readOnly** *(boolean) --*
                  If this value is ``true`` , the container has read-only access to the volume. If this value is ``false`` , then the container can write to the volume. The default value is ``false`` .
            - **linuxParameters** *(dict) --*
              Linux-specific modifications that are applied to the container, such as Linux  KernelCapabilities .
              .. note::
                This parameter is not supported for Windows containers.
              - **capabilities** *(dict) --*
                The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
                .. note::
                  If you are using tasks that use the Fargate launch type, ``capabilities`` is supported but the ``add`` parameter is not supported.
                - **add** *(list) --*
                  The Linux capabilities for the container that have been added to the default configuration provided by Docker. This parameter maps to ``CapAdd`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-add`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  .. note::
                    If you are using tasks that use the Fargate launch type, the ``add`` parameter is not supported.
                  Valid values: ``\"ALL\" | \"AUDIT_CONTROL\" | \"AUDIT_WRITE\" | \"BLOCK_SUSPEND\" | \"CHOWN\" | \"DAC_OVERRIDE\" | \"DAC_READ_SEARCH\" | \"FOWNER\" | \"FSETID\" | \"IPC_LOCK\" | \"IPC_OWNER\" | \"KILL\" | \"LEASE\" | \"LINUX_IMMUTABLE\" | \"MAC_ADMIN\" | \"MAC_OVERRIDE\" | \"MKNOD\" | \"NET_ADMIN\" | \"NET_BIND_SERVICE\" | \"NET_BROADCAST\" | \"NET_RAW\" | \"SETFCAP\" | \"SETGID\" | \"SETPCAP\" | \"SETUID\" | \"SYS_ADMIN\" | \"SYS_BOOT\" | \"SYS_CHROOT\" | \"SYS_MODULE\" | \"SYS_NICE\" | \"SYS_PACCT\" | \"SYS_PTRACE\" | \"SYS_RAWIO\" | \"SYS_RESOURCE\" | \"SYS_TIME\" | \"SYS_TTY_CONFIG\" | \"SYSLOG\" | \"WAKE_ALARM\"``
                  - *(string) --*
                - **drop** *(list) --*
                  The Linux capabilities for the container that have been removed from the default configuration provided by Docker. This parameter maps to ``CapDrop`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--cap-drop`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                  Valid values: ``\"ALL\" | \"AUDIT_CONTROL\" | \"AUDIT_WRITE\" | \"BLOCK_SUSPEND\" | \"CHOWN\" | \"DAC_OVERRIDE\" | \"DAC_READ_SEARCH\" | \"FOWNER\" | \"FSETID\" | \"IPC_LOCK\" | \"IPC_OWNER\" | \"KILL\" | \"LEASE\" | \"LINUX_IMMUTABLE\" | \"MAC_ADMIN\" | \"MAC_OVERRIDE\" | \"MKNOD\" | \"NET_ADMIN\" | \"NET_BIND_SERVICE\" | \"NET_BROADCAST\" | \"NET_RAW\" | \"SETFCAP\" | \"SETGID\" | \"SETPCAP\" | \"SETUID\" | \"SYS_ADMIN\" | \"SYS_BOOT\" | \"SYS_CHROOT\" | \"SYS_MODULE\" | \"SYS_NICE\" | \"SYS_PACCT\" | \"SYS_PTRACE\" | \"SYS_RAWIO\" | \"SYS_RESOURCE\" | \"SYS_TIME\" | \"SYS_TTY_CONFIG\" | \"SYSLOG\" | \"WAKE_ALARM\"``
                  - *(string) --*
              - **devices** *(list) --*
                Any host devices to expose to the container. This parameter maps to ``Devices`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--device`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                .. note::
                  If you are using tasks that use the Fargate launch type, the ``devices`` parameter is not supported.
                - *(dict) --*
                  An object representing a container instance host device.
                  - **hostPath** *(string) --* **[REQUIRED]**
                    The path for the device on the host container instance.
                  - **containerPath** *(string) --*
                    The path inside the container at which to expose the host device.
                  - **permissions** *(list) --*
                    The explicit permissions to provide to the container for the device. By default, the container has permissions for ``read`` , ``write`` , and ``mknod`` for the device.
                    - *(string) --*
              - **initProcessEnabled** *(boolean) --*
                Run an ``init`` process inside the container that forwards signals and reaps processes. This parameter maps to the ``--init`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
              - **sharedMemorySize** *(integer) --*
                The value for the size (in MiB) of the ``/dev/shm`` volume. This parameter maps to the ``--shm-size`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                .. note::
                  If you are using tasks that use the Fargate launch type, the ``sharedMemorySize`` parameter is not supported.
              - **tmpfs** *(list) --*
                The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the ``--tmpfs`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                .. note::
                  If you are using tasks that use the Fargate launch type, the ``tmpfs`` parameter is not supported.
                - *(dict) --*
                  The container path, mount options, and size of the tmpfs mount.
                  - **containerPath** *(string) --* **[REQUIRED]**
                    The absolute file path where the tmpfs volume is to be mounted.
                  - **size** *(integer) --* **[REQUIRED]**
                    The size (in MiB) of the tmpfs volume.
                  - **mountOptions** *(list) --*
                    The list of tmpfs volume mount options.
                    Valid values: ``\"defaults\" | \"ro\" | \"rw\" | \"suid\" | \"nosuid\" | \"dev\" | \"nodev\" | \"exec\" | \"noexec\" | \"sync\" | \"async\" | \"dirsync\" | \"remount\" | \"mand\" | \"nomand\" | \"atime\" | \"noatime\" | \"diratime\" | \"nodiratime\" | \"bind\" | \"rbind\" | \"unbindable\" | \"runbindable\" | \"private\" | \"rprivate\" | \"shared\" | \"rshared\" | \"slave\" | \"rslave\" | \"relatime\" | \"norelatime\" | \"strictatime\" | \"nostrictatime\" | \"mode\" | \"uid\" | \"gid\" | \"nr_inodes\" | \"nr_blocks\" | \"mpol\"``
                    - *(string) --*
            - **secrets** *(list) --*
              The secrets to pass to the container. For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - *(dict) --*
                An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter.
                * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter.
                For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **name** *(string) --* **[REQUIRED]**
                  The name of the secret.
                - **valueFrom** *(string) --* **[REQUIRED]**
                  The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                  .. note::
                    If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
            - **dependsOn** *(list) --*
              The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
              For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
              - *(dict) --*
                The dependencies defined for container startup and shutdown. A container can contain multiple dependencies. When a dependency is defined for container startup, for container shutdown it is reversed.
                Your Amazon ECS container instances require at least version 1.26.0 of the container agent to enable container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                .. note::
                  If you are using tasks that use the Fargate launch type, container dependency parameters are not supported.
                - **containerName** *(string) --* **[REQUIRED]**
                  The name of a container.
                - **condition** *(string) --* **[REQUIRED]**
                  The dependency condition of the container. The following are the available conditions and their behavior:
                  * ``START`` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.
                  * ``COMPLETE`` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit.
                  * ``SUCCESS`` - This condition is the same as ``COMPLETE`` , but it also requires that the container exits with a ``zero`` status.
                  * ``HEALTHY`` - This condition validates that the dependent container passes its Docker health check before permitting other containers to start. This requires that the dependent container has health checks configured. This condition is confirmed only at task startup.
            - **startTimeout** *(integer) --*
              Time duration to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a ``COMPLETE`` , ``SUCCESS`` , or ``HEALTHY`` status. If a ``startTimeout`` value is specified for containerB and it does not reach the desired status within that time then containerA will give up and not start. This results in the task transitioning to a ``STOPPED`` state.
              For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to enable a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
            - **stopTimeout** *(integer) --*
              Time duration to wait before the container is forcefully killed if it doesn\'t exit normally on its own. For tasks using the Fargate launch type, the max ``stopTimeout`` value is 2 minutes. This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
              For tasks using the EC2 launch type, the stop timeout value for the container takes precedence over the ``ECS_CONTAINER_STOP_TIMEOUT`` container agent configuration parameter, if used. Container instances require at least version 1.26.0 of the container agent to enable a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see `Updating the Amazon ECS Container Agent <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html>`__ in the *Amazon Elastic Container Service Developer Guide* . If you are using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the ``ecs-init`` package. If your container instances are launched from version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **hostname** *(string) --*
              The hostname to use for your container. This parameter maps to ``Hostname`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--hostname`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                The ``hostname`` parameter is not supported if you are using the ``awsvpc`` network mode.
            - **user** *(string) --*
              The user name to use inside the container. This parameter maps to ``User`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--user`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              You can use the following formats. If specifying a UID or GID, you must specify it as a positive integer.
              * ``user``
              * ``user:group``
              * ``uid``
              * ``uid:gid``
              * ``user:gid``
              * ``uid:group``
              .. note::
                This parameter is not supported for Windows containers.
            - **workingDirectory** *(string) --*
              The working directory in which to run commands inside the container. This parameter maps to ``WorkingDir`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--workdir`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
            - **disableNetworking** *(boolean) --*
              When this parameter is true, networking is disabled within the container. This parameter maps to ``NetworkDisabled`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
              .. note::
                This parameter is not supported for Windows containers.
            - **privileged** *(boolean) --*
              When this parameter is true, the container is given elevated privileges on the host container instance (similar to the ``root`` user). This parameter maps to ``Privileged`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--privileged`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                This parameter is not supported for Windows containers or tasks using the Fargate launch type.
            - **readonlyRootFilesystem** *(boolean) --*
              When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ``ReadonlyRootfs`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--read-only`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                This parameter is not supported for Windows containers.
            - **dnsServers** *(list) --*
              A list of DNS servers that are presented to the container. This parameter maps to ``Dns`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                This parameter is not supported for Windows containers.
              - *(string) --*
            - **dnsSearchDomains** *(list) --*
              A list of DNS search domains that are presented to the container. This parameter maps to ``DnsSearch`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--dns-search`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                This parameter is not supported for Windows containers.
              - *(string) --*
            - **extraHosts** *(list) --*
              A list of hostnames and IP address mappings to append to the ``/etc/hosts`` file on the container. This parameter maps to ``ExtraHosts`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--add-host`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                This parameter is not supported for Windows containers or tasks that use the ``awsvpc`` network mode.
              - *(dict) --*
                Hostnames and IP address entries that are added to the ``/etc/hosts`` file of a container via the ``extraHosts`` parameter of its  ContainerDefinition .
                - **hostname** *(string) --* **[REQUIRED]**
                  The hostname to use in the ``/etc/hosts`` entry.
                - **ipAddress** *(string) --* **[REQUIRED]**
                  The IP address to use in the ``/etc/hosts`` entry.
            - **dockerSecurityOptions** *(list) --*
              A list of strings to provide custom labels for SELinux and AppArmor multi-level security systems. This field is not valid for containers in tasks using the Fargate launch type.
              This parameter maps to ``SecurityOpt`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--security-opt`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                The Amazon ECS container agent running on a container instance must register with the ``ECS_SELINUX_CAPABLE=true`` or ``ECS_APPARMOR_CAPABLE=true`` environment variables before containers placed on that instance can use these security options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                This parameter is not supported for Windows containers.
              - *(string) --*
            - **interactive** *(boolean) --*
              When this parameter is ``true`` , this allows you to deploy containerized applications that require ``stdin`` or a ``tty`` to be allocated. This parameter maps to ``OpenStdin`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--interactive`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
            - **pseudoTerminal** *(boolean) --*
              When this parameter is ``true`` , a TTY is allocated. This parameter maps to ``Tty`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--tty`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
            - **dockerLabels** *(dict) --*
              A key/value map of labels to add to the container. This parameter maps to ``Labels`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--label`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
              - *(string) --*
                - *(string) --*
            - **ulimits** *(list) --*
              A list of ``ulimits`` to set in the container. This parameter maps to ``Ulimits`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--ulimit`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . Valid naming values are displayed in the  Ulimit data type. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
              .. note::
                This parameter is not supported for Windows containers.
              - *(dict) --*
                The ``ulimit`` settings to pass to the container.
                - **name** *(string) --* **[REQUIRED]**
                  The ``type`` of the ``ulimit`` .
                - **softLimit** *(integer) --* **[REQUIRED]**
                  The soft limit for the ulimit type.
                - **hardLimit** *(integer) --* **[REQUIRED]**
                  The hard limit for the ulimit type.
            - **logConfiguration** *(dict) --*
              The log configuration specification for the container.
              For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
              For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
              This parameter maps to ``LogConfig`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--log-driver`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ . By default, containers use the same logging driver that the Docker daemon uses. However the container may use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). For more information on the options for different supported log drivers, see `Configure logging drivers <https://docs.docker.com/engine/admin/logging/overview/>`__ in the Docker documentation.
              .. note::
                Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the  LogConfiguration data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.
              This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
              .. note::
                The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the ``ECS_AVAILABLE_LOGGING_DRIVERS`` environment variable before containers placed on that instance can use these log configuration options. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **logDriver** *(string) --* **[REQUIRED]**
                The log driver to use for the container. The valid values listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.
                For tasks using the Fargate launch type, the supported log drivers are ``awslogs`` and ``splunk`` .
                For tasks using the EC2 launch type, the supported log drivers are ``awslogs`` , ``syslog`` , ``gelf`` , ``fluentd`` , ``splunk`` , ``journald`` , and ``json-file`` .
                For more information about using the ``awslogs`` log driver, see `Using the awslogs Log Driver <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                .. note::
                  If you have a custom driver that is not listed above that you would like to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that is `available on GitHub <https://github.com/aws/amazon-ecs-agent>`__ and customize it to work with that driver. We encourage you to submit pull requests for changes that you would like to have included. However, Amazon Web Services does not currently support running modified copies of this software.
                This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
              - **options** *(dict) --*
                The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: ``sudo docker version --format \'{{.Server.APIVersion}}\'``
                - *(string) --*
                  - *(string) --*
              - **secretOptions** *(list) --*
                The secrets to pass to the log configuration.
                - *(dict) --*
                  An object representing the secret to expose to your container. Secrets can be exposed to a container in the following ways:
                  * To inject sensitive data into your containers as environment variables, use the ``secrets`` container definition parameter.
                  * To reference sensitive information in the log configuration of a container, use the ``secretOptions`` container definition parameter.
                  For more information, see `Specifying Sensitive Data <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* **[REQUIRED]**
                    The name of the secret.
                  - **valueFrom** *(string) --* **[REQUIRED]**
                    The secret to expose to the container. The supported values are either the full ARN of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
                    .. note::
                      If the AWS Systems Manager Parameter Store parameter exists in the same Region as the task you are launching, then you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
            - **healthCheck** *(dict) --*
              The health check command and associated configuration parameters for the container. This parameter maps to ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``HEALTHCHECK`` parameter of `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              - **command** *(list) --* **[REQUIRED]**
                A string array representing the command that the container runs to determine if it is healthy. The string array must start with ``CMD`` to execute the command arguments directly, or ``CMD-SHELL`` to run the command with the container\'s default shell. For example:
                 ``[ \"CMD-SHELL\", \"curl -f http://localhost/ || exit 1\" ]``
                An exit code of 0 indicates success, and non-zero exit code indicates failure. For more information, see ``HealthCheck`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ .
                - *(string) --*
              - **interval** *(integer) --*
                The time period in seconds between each health check execution. You may specify between 5 and 300 seconds. The default value is 30 seconds.
              - **timeout** *(integer) --*
                The time period in seconds to wait for a health check to succeed before it is considered a failure. You may specify between 2 and 60 seconds. The default value is 5.
              - **retries** *(integer) --*
                The number of times to retry a failed health check before the container is considered unhealthy. You may specify between 1 and 10 retries. The default value is 3.
              - **startPeriod** *(integer) --*
                The optional grace period within which to provide containers time to bootstrap before failed health checks count towards the maximum number of retries. You may specify between 0 and 300 seconds. The ``startPeriod`` is disabled by default.
                .. note::
                  If a health check succeeds within the ``startPeriod`` , then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
            - **systemControls** *(list) --*
              A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
              .. note::
                It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network modes. For tasks that use the ``awsvpc`` network mode, the container that is started last determines which ``systemControls`` parameters take effect. For tasks that use the ``host`` network mode, it changes the container instance\'s namespaced kernel parameters as well as the containers.
              - *(dict) --*
                A list of namespaced kernel parameters to set in the container. This parameter maps to ``Sysctls`` in the `Create a container <https://docs.docker.com/engine/api/v1.35/#operation/ContainerCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``--sysctl`` option to `docker run <https://docs.docker.com/engine/reference/run/>`__ .
                It is not recommended that you specify network-related ``systemControls`` parameters for multiple containers in a single task that also uses either the ``awsvpc`` or ``host`` network mode for the following reasons:
                * For tasks that use the ``awsvpc`` network mode, if you set ``systemControls`` for any container, it applies to all containers in the task. If you set different ``systemControls`` for multiple containers in a single task, the container that is started last determines which ``systemControls`` take effect.
                * For tasks that use the ``host`` network mode, the ``systemControls`` parameter applies to the container instance\'s kernel parameter as well as that of all containers of any tasks running on that container instance.
                - **namespace** *(string) --*
                  The namespaced kernel parameter for which to set a ``value`` .
                - **value** *(string) --*
                  The value for the namespaced kernel parameter specified in ``namespace`` .
            - **resourceRequirements** *(list) --*
              The type and amount of a resource to assign to a container. The only supported resource is a GPU.
              - *(dict) --*
                The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*
                - **value** *(string) --* **[REQUIRED]**
                  The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                - **type** *(string) --* **[REQUIRED]**
                  The type of resource to assign to a container. The only supported value is ``GPU`` .
        :type volumes: list
        :param volumes:
          A list of volume definitions in JSON format that containers in your task may use.
          - *(dict) --*
            A data volume used in a task definition. For tasks that use a Docker volume, specify a ``DockerVolumeConfiguration`` . For tasks that use a bind mount host volume, specify a ``host`` and optional ``sourcePath`` . For more information, see `Using Data Volumes in Tasks <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html>`__ .
            - **name** *(string) --*
              The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the ``sourceVolume`` parameter of container definition ``mountPoints`` .
            - **host** *(dict) --*
              This parameter is specified when you are using bind mount host volumes. Bind mount host volumes are supported when you are using either the EC2 or Fargate launch types. The contents of the ``host`` parameter determine whether your bind mount host volume persists on the host container instance and where it is stored. If the ``host`` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data is not guaranteed to persist after the containers associated with it stop running.
              Windows containers can mount whole directories on the same drive as ``$env:ProgramData`` . Windows containers cannot mount directories on a different drive, and mount point cannot be across drives. For example, you can mount ``C:\my\path:C:\my\path`` and ``D:\:D:\`` , but not ``D:\my\path:C:\my\path`` or ``D:\:C:\my\path`` .
              - **sourcePath** *(string) --*
                When the ``host`` parameter is used, specify a ``sourcePath`` to declare the path on the host container instance that is presented to the container. If this parameter is empty, then the Docker daemon has assigned a host path for you. If the ``host`` parameter contains a ``sourcePath`` file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the ``sourcePath`` value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.
                If you are using the Fargate launch type, the ``sourcePath`` parameter is not supported.
            - **dockerVolumeConfiguration** *(dict) --*
              This parameter is specified when you are using Docker volumes. Docker volumes are only supported when you are using the EC2 launch type. Windows containers only support the use of the ``local`` driver. To use bind mounts, specify a ``host`` instead.
              - **scope** *(string) --*
                The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a ``task`` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as ``shared`` persist after the task stops.
              - **autoprovision** *(boolean) --*
                If this value is ``true`` , the Docker volume is created if it does not already exist.
                .. note::
                  This field is only used if the ``scope`` is ``shared`` .
              - **driver** *(string) --*
                The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use ``docker plugin ls`` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. For more information, see `Docker plugin discovery <https://docs.docker.com/engine/extend/plugin_api/#plugin-discovery>`__ . This parameter maps to ``Driver`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxdriver`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
              - **driverOpts** *(dict) --*
                A map of Docker driver-specific options passed through. This parameter maps to ``DriverOpts`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxopt`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                - *(string) --*
                  - *(string) --*
              - **labels** *(dict) --*
                Custom metadata to add to your Docker volume. This parameter maps to ``Labels`` in the `Create a volume <https://docs.docker.com/engine/api/v1.35/#operation/VolumeCreate>`__ section of the `Docker Remote API <https://docs.docker.com/engine/api/v1.35/>`__ and the ``xxlabel`` option to ` ``docker volume create`` https://docs.docker.com/engine/reference/commandline/volume_create/`__ .
                - *(string) --*
                  - *(string) --*
        :type placementConstraints: list
        :param placementConstraints:
          An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints per task (this limit includes constraints in the task definition and those specified at runtime).
          - *(dict) --*
            An object representing a constraint on task placement in the task definition.
            If you are using the Fargate launch type, task placement constraints are not supported.
            For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **type** *(string) --*
              The type of constraint. The ``DistinctInstance`` constraint ensures that each task in a particular group is running on a different container instance. The ``MemberOf`` constraint restricts selection to be from a group of valid candidates.
            - **expression** *(string) --*
              A cluster query language expression to apply to the constraint. For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type requiresCompatibilities: list
        :param requiresCompatibilities:
          The launch type required by the task. If no value is specified, it defaults to ``EC2`` .
          - *(string) --*
        :type cpu: string
        :param cpu:
          The number of CPU units used by the task. It can be expressed as an integer using CPU units, for example ``1024`` , or as a string using vCPUs, for example ``1 vCPU`` or ``1 vcpu`` , in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.
          .. note::
            Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
          If you are using the EC2 launch type, this field is optional. Supported values are between ``128`` CPU units (``0.125`` vCPUs) and ``10240`` CPU units (``10`` vCPUs).
          If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``memory`` parameter:
          * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)
          * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)
          * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)
          * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)
          * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)
        :type memory: string
        :param memory:
          The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB, for example ``1024`` , or as a string using GB, for example ``1GB`` or ``1 GB`` , in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.
          .. note::
            Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.
          If using the EC2 launch type, this field is optional.
          If using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``cpu`` parameter:
          * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU)
          * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU)
          * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU)
          * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU)
          * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU)
        :type tags: list
        :param tags:
          The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type pidMode: string
        :param pidMode:
          The process namespace to use for the containers in the task. The valid values are ``host`` or ``task`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` PID mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace. For more information, see `PID settings <https://docs.docker.com/engine/reference/run/#pid-settings---pid>`__ in the *Docker run reference* .
          If the ``host`` PID mode is used, be aware that there is a heightened risk of undesired process namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
          .. note::
            This parameter is not supported for Windows containers or tasks using the Fargate launch type.
        :type ipcMode: string
        :param ipcMode:
          The IPC resource namespace to use for the containers in the task. The valid values are ``host`` , ``task`` , or ``none`` . If ``host`` is specified, then all containers within the tasks that specified the ``host`` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same IPC resources. If ``none`` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see `IPC settings <https://docs.docker.com/engine/reference/run/#ipc-settings---ipc>`__ in the *Docker run reference* .
          If the ``host`` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see `Docker security <https://docs.docker.com/engine/security/security/>`__ .
          If you are setting namespaced kernel parameters using ``systemControls`` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see `System Controls <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          * For tasks that use the ``host`` IPC mode, IPC namespace related ``systemControls`` are not supported.
          * For tasks that use the ``task`` IPC mode, IPC namespace related ``systemControls`` will apply to all containers within a task.
          .. note::
            This parameter is not supported for Windows containers or tasks using the Fargate launch type.
        :type proxyConfiguration: dict
        :param proxyConfiguration:
          The configuration details for the App Mesh proxy.
          For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to enable a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version ``20190301`` or later, then they contain the required versions of the container agent and ``ecs-init`` . For more information, see `Amazon ECS-optimized Linux AMI <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          This parameter is available for tasks using the Fargate launch type in the Ohio (us-east-2) region only and the task or service requires platform version 1.3.0 or later.
          - **type** *(string) --*
            The proxy type. The only supported value is ``APPMESH`` .
          - **containerName** *(string) --* **[REQUIRED]**
            The name of the container that will serve as the App Mesh proxy.
          - **properties** *(list) --*
            The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified as key-value pairs.
            * ``IgnoredUID`` - (Required) The user ID (UID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty.
            * ``IgnoredGID`` - (Required) The group ID (GID) of the proxy container as defined by the ``user`` parameter in a container definition. This is used to ensure the proxy ignores its own traffic. If ``IgnoredGID`` is specified, this field can be empty.
            * ``AppPorts`` - (Required) The list of ports that the application uses. Network traffic to these ports is forwarded to the ``ProxyIngressPort`` and ``ProxyEgressPort`` .
            * ``ProxyIngressPort`` - (Required) Specifies the port that incoming traffic to the ``AppPorts`` is directed to.
            * ``ProxyEgressPort`` - (Required) Specifies the port that outgoing traffic from the ``AppPorts`` is directed to.
            * ``EgressIgnoredPorts`` - (Required) The egress traffic going to the specified ports is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list.
            * ``EgressIgnoredIPs`` - (Required) The egress traffic going to the specified IP addresses is ignored and not redirected to the ``ProxyEgressPort`` . It can be an empty list.
            - *(dict) --*
              A key-value pair object.
              - **name** *(string) --*
                The name of the key-value pair. For environment variables, this is the name of the environment variable.
              - **value** *(string) --*
                The value of the key-value pair. For environment variables, this is the value of the environment variable.
        :rtype: dict
        :returns:
        """
        pass

    def run_task(self, taskDefinition: str, cluster: str = None, overrides: Dict = None, count: int = None, startedBy: str = None, group: str = None, placementConstraints: List = None, placementStrategy: List = None, launchType: str = None, platformVersion: str = None, networkConfiguration: Dict = None, tags: List = None, enableECSManagedTags: bool = None, propagateTags: str = None) -> Dict:
        """
        Starts a new task using the specified task definition.
        You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see `Scheduling Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        Alternatively, you can use  StartTask to use your own scheduler or place tasks manually on specific container instances.
        The Amazon ECS API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.
        To manage eventual consistency, you can do the following:
        * Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time. 
        * Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RunTask>`_
        
        **Request Syntax**
        ::
          response = client.run_task(
              cluster='string',
              taskDefinition='string',
              overrides={
                  'containerOverrides': [
                      {
                          'name': 'string',
                          'command': [
                              'string',
                          ],
                          'environment': [
                              {
                                  'name': 'string',
                                  'value': 'string'
                              },
                          ],
                          'cpu': 123,
                          'memory': 123,
                          'memoryReservation': 123,
                          'resourceRequirements': [
                              {
                                  'value': 'string',
                                  'type': 'GPU'
                              },
                          ]
                      },
                  ],
                  'taskRoleArn': 'string',
                  'executionRoleArn': 'string'
              },
              count=123,
              startedBy='string',
              group='string',
              placementConstraints=[
                  {
                      'type': 'distinctInstance'|'memberOf',
                      'expression': 'string'
                  },
              ],
              placementStrategy=[
                  {
                      'type': 'random'|'spread'|'binpack',
                      'field': 'string'
                  },
              ],
              launchType='EC2'|'FARGATE',
              platformVersion='string',
              networkConfiguration={
                  'awsvpcConfiguration': {
                      'subnets': [
                          'string',
                      ],
                      'securityGroups': [
                          'string',
                      ],
                      'assignPublicIp': 'ENABLED'|'DISABLED'
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              enableECSManagedTags=True|False,
              propagateTags='TASK_DEFINITION'|'SERVICE'
          )
        
        **Response Syntax**
        ::
            {
                'tasks': [
                    {
                        'taskArn': 'string',
                        'clusterArn': 'string',
                        'taskDefinitionArn': 'string',
                        'containerInstanceArn': 'string',
                        'overrides': {
                            'containerOverrides': [
                                {
                                    'name': 'string',
                                    'command': [
                                        'string',
                                    ],
                                    'environment': [
                                        {
                                            'name': 'string',
                                            'value': 'string'
                                        },
                                    ],
                                    'cpu': 123,
                                    'memory': 123,
                                    'memoryReservation': 123,
                                    'resourceRequirements': [
                                        {
                                            'value': 'string',
                                            'type': 'GPU'
                                        },
                                    ]
                                },
                            ],
                            'taskRoleArn': 'string',
                            'executionRoleArn': 'string'
                        },
                        'lastStatus': 'string',
                        'desiredStatus': 'string',
                        'cpu': 'string',
                        'memory': 'string',
                        'containers': [
                            {
                                'containerArn': 'string',
                                'taskArn': 'string',
                                'name': 'string',
                                'lastStatus': 'string',
                                'exitCode': 123,
                                'reason': 'string',
                                'networkBindings': [
                                    {
                                        'bindIP': 'string',
                                        'containerPort': 123,
                                        'hostPort': 123,
                                        'protocol': 'tcp'|'udp'
                                    },
                                ],
                                'networkInterfaces': [
                                    {
                                        'attachmentId': 'string',
                                        'privateIpv4Address': 'string',
                                        'ipv6Address': 'string'
                                    },
                                ],
                                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                                'cpu': 'string',
                                'memory': 'string',
                                'memoryReservation': 'string',
                                'gpuIds': [
                                    'string',
                                ]
                            },
                        ],
                        'startedBy': 'string',
                        'version': 123,
                        'stoppedReason': 'string',
                        'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                        'connectivity': 'CONNECTED'|'DISCONNECTED',
                        'connectivityAt': datetime(2015, 1, 1),
                        'pullStartedAt': datetime(2015, 1, 1),
                        'pullStoppedAt': datetime(2015, 1, 1),
                        'executionStoppedAt': datetime(2015, 1, 1),
                        'createdAt': datetime(2015, 1, 1),
                        'startedAt': datetime(2015, 1, 1),
                        'stoppingAt': datetime(2015, 1, 1),
                        'stoppedAt': datetime(2015, 1, 1),
                        'group': 'string',
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'attachments': [
                            {
                                'id': 'string',
                                'type': 'string',
                                'status': 'string',
                                'details': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ]
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tasks** *(list) --* 
              A full description of the tasks that were run. The tasks that were successfully placed on your cluster are described here.
              - *(dict) --* 
                Details on a task in a cluster.
                - **taskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task.
                - **clusterArn** *(string) --* 
                  The ARN of the cluster that hosts the task.
                - **taskDefinitionArn** *(string) --* 
                  The ARN of the task definition that creates the task.
                - **containerInstanceArn** *(string) --* 
                  The ARN of the container instances that host the task.
                - **overrides** *(dict) --* 
                  One or more container overrides.
                  - **containerOverrides** *(list) --* 
                    One or more container overrides sent to a task.
                    - *(dict) --* 
                      The overrides that should be sent to a container.
                      - **name** *(string) --* 
                        The name of the container that receives the override. This parameter is required if any override is specified.
                      - **command** *(list) --* 
                        The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                        - *(string) --* 
                      - **environment** *(list) --* 
                        The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                        - *(dict) --* 
                          A key-value pair object.
                          - **name** *(string) --* 
                            The name of the key-value pair. For environment variables, this is the name of the environment variable.
                          - **value** *(string) --* 
                            The value of the key-value pair. For environment variables, this is the value of the environment variable.
                      - **cpu** *(integer) --* 
                        The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **memory** *(integer) --* 
                        The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
                      - **memoryReservation** *(integer) --* 
                        The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **resourceRequirements** *(list) --* 
                        The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                        - *(dict) --* 
                          The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                          - **value** *(string) --* 
                            The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                          - **type** *(string) --* 
                            The type of resource to assign to a container. The only supported value is ``GPU`` .
                  - **taskRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                  - **executionRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
                - **lastStatus** *(string) --* 
                  The last known status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **desiredStatus** *(string) --* 
                  The desired status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **cpu** *(string) --* 
                  The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units, for example ``1024`` . It can also be expressed as a string using vCPUs, for example ``1 vCPU`` or ``1 vcpu`` . String values are converted to an integer indicating the CPU units when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional. Supported values are between ``128`` CPU units (``0.125`` vCPUs) and ``10240`` CPU units (``10`` vCPUs).
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``memory`` parameter:
                  * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                  * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                  * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                  * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                  * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
                - **memory** *(string) --* 
                  The amount of memory (in MiB) used by the task as expressed in a task definition. It can be expressed as an integer using MiB, for example ``1024`` . It can also be expressed as a string using GB, for example ``1GB`` or ``1 GB`` . String values are converted to an integer indicating the MiB when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional.
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``cpu`` parameter:
                  * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                  * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                  * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                  * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                  * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
                - **containers** *(list) --* 
                  The containers associated with the task.
                  - *(dict) --* 
                    A Docker container that is part of a task.
                    - **containerArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the container.
                    - **taskArn** *(string) --* 
                      The ARN of the task.
                    - **name** *(string) --* 
                      The name of the container.
                    - **lastStatus** *(string) --* 
                      The last known status of the container.
                    - **exitCode** *(integer) --* 
                      The exit code returned from the container.
                    - **reason** *(string) --* 
                      A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
                    - **networkBindings** *(list) --* 
                      The network bindings associated with the container.
                      - *(dict) --* 
                        Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                        - **bindIP** *(string) --* 
                          The IP address that the container is bound to on the container instance.
                        - **containerPort** *(integer) --* 
                          The port number on the container that is used with the network binding.
                        - **hostPort** *(integer) --* 
                          The port number on the host that is used with the network binding.
                        - **protocol** *(string) --* 
                          The protocol used for the network binding.
                    - **networkInterfaces** *(list) --* 
                      The network interfaces associated with the container.
                      - *(dict) --* 
                        An object representing the elastic network interface for tasks that use the ``awsvpc`` network mode.
                        - **attachmentId** *(string) --* 
                          The attachment ID for the network interface.
                        - **privateIpv4Address** *(string) --* 
                          The private IPv4 address for the network interface.
                        - **ipv6Address** *(string) --* 
                          The private IPv6 address for the network interface.
                    - **healthStatus** *(string) --* 
                      The health status of the container. If health checks are not configured for this container in its task definition, then it reports the health status as ``UNKNOWN`` .
                    - **cpu** *(string) --* 
                      The number of CPU units set for the container. The value will be ``0`` if no value was specified in the container definition when the task definition was registered.
                    - **memory** *(string) --* 
                      The hard limit (in MiB) of memory set for the container.
                    - **memoryReservation** *(string) --* 
                      The soft limit (in MiB) of memory set for the container.
                    - **gpuIds** *(list) --* 
                      The IDs of each GPU assigned to the container.
                      - *(string) --* 
                - **startedBy** *(string) --* 
                  The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
                - **version** *(integer) --* 
                  The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actionss with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.
                - **stoppedReason** *(string) --* 
                  The reason that the task was stopped.
                - **stopCode** *(string) --* 
                  The stop code indicating why a task was stopped. The ``stoppedReason`` may contain additional details.
                - **connectivity** *(string) --* 
                  The connectivity status of a task.
                - **connectivityAt** *(datetime) --* 
                  The Unix timestamp for when the task last went into ``CONNECTED`` status.
                - **pullStartedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull began.
                - **pullStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull completed.
                - **executionStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task execution stopped.
                - **createdAt** *(datetime) --* 
                  The Unix timestamp for when the task was created (the task entered the ``PENDING`` state).
                - **startedAt** *(datetime) --* 
                  The Unix timestamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).
                - **stoppingAt** *(datetime) --* 
                  The Unix timestamp for when the task stops (transitions from the ``RUNNING`` state to ``STOPPED`` ).
                - **stoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).
                - **group** *(string) --* 
                  The name of the task group associated with the task.
                - **launchType** *(string) --* 
                  The launch type on which your task is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **platformVersion** *(string) --* 
                  The platform version on which your task is running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **attachments** *(list) --* 
                  The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.
                  - *(dict) --* 
                    An object representing a container instance or task attachment.
                    - **id** *(string) --* 
                      The unique identifier for the attachment.
                    - **type** *(string) --* 
                      The type of the attachment, such as ``ElasticNetworkInterface`` .
                    - **status** *(string) --* 
                      The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                    - **details** *(list) --* 
                      Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **healthStatus** *(string) --* 
                  The health status for the task, which is determined by the health of the essential containers in the task. If all essential containers in the task are reporting as ``HEALTHY`` , then the task status also reports as ``HEALTHY`` . If any essential containers in the task are reporting as ``UNHEALTHY`` or ``UNKNOWN`` , then the task status also reports as ``UNHEALTHY`` or ``UNKNOWN`` , accordingly.
                  .. note::
                    The Amazon ECS container agent does not monitor or report on Docker health checks that are embedded in a container image (such as those specified in a parent image or from the image's Dockerfile) and not specified in the container definition. Health check parameters that are specified in a container definition override any Docker health checks that exist in the container image.
                - **tags** *(list) --* 
                  The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster on which to run your task. If you do not specify a cluster, the default cluster is assumed.
        :type taskDefinition: string
        :param taskDefinition: **[REQUIRED]**
          The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.
        :type overrides: dict
        :param overrides:
          A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.
          .. note::
            A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
          - **containerOverrides** *(list) --*
            One or more container overrides sent to a task.
            - *(dict) --*
              The overrides that should be sent to a container.
              - **name** *(string) --*
                The name of the container that receives the override. This parameter is required if any override is specified.
              - **command** *(list) --*
                The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                - *(string) --*
              - **environment** *(list) --*
                The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                - *(dict) --*
                  A key-value pair object.
                  - **name** *(string) --*
                    The name of the key-value pair. For environment variables, this is the name of the environment variable.
                  - **value** *(string) --*
                    The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **cpu** *(integer) --*
                The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
              - **memory** *(integer) --*
                The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
              - **memoryReservation** *(integer) --*
                The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
              - **resourceRequirements** *(list) --*
                The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                - *(dict) --*
                  The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*
                  - **value** *(string) --* **[REQUIRED]**
                    The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                  - **type** *(string) --* **[REQUIRED]**
                    The type of resource to assign to a container. The only supported value is ``GPU`` .
          - **taskRoleArn** *(string) --*
            The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
          - **executionRoleArn** *(string) --*
            The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
        :type count: integer
        :param count:
          The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks per call.
        :type startedBy: string
        :param startedBy:
          An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the ``startedBy`` parameter. You can then identify which tasks belong to that job by filtering the results of a  ListTasks call with the ``startedBy`` value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
          If a task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
        :type group: string
        :param group:
          The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).
        :type placementConstraints: list
        :param placementConstraints:
          An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
          - *(dict) --*
            An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **type** *(string) --*
              The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
            - **expression** *(string) --*
              A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type placementStrategy: list
        :param placementStrategy:
          The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task.
          - *(dict) --*
            The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
            - **type** *(string) --*
              The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
            - **field** *(string) --*
              The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
        :type launchType: string
        :param launchType:
          The launch type on which to run your task. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type platformVersion: string
        :param platformVersion:
          The platform version the task should run. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type networkConfiguration: dict
        :param networkConfiguration:
          The network configuration for the task. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          - **awsvpcConfiguration** *(dict) --*
            The VPC subnets and security groups associated with a task.
            .. note::
              All specified subnets and security groups must be from the same VPC.
            - **subnets** *(list) --* **[REQUIRED]**
              The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified subnets must be from the same VPC.
              - *(string) --*
            - **securityGroups** *(list) --*
              The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified security groups must be from the same VPC.
              - *(string) --*
            - **assignPublicIp** *(string) --*
              Whether the task\'s elastic network interface receives a public IP address. The default value is ``DISABLED`` .
        :type tags: list
        :param tags:
          The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type enableECSManagedTags: boolean
        :param enableECSManagedTags:
          Specifies whether to enable Amazon ECS managed tags for the task. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type propagateTags: string
        :param propagateTags:
          Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the  TagResource API action.
          .. note::
            An error will be received if you specify the ``SERVICE`` option when running a task.
        :rtype: dict
        :returns:
        """
        pass

    def start_task(self, taskDefinition: str, containerInstances: List, cluster: str = None, overrides: Dict = None, startedBy: str = None, group: str = None, networkConfiguration: Dict = None, tags: List = None, enableECSManagedTags: bool = None, propagateTags: str = None) -> Dict:
        """
        Starts a new task from the specified task definition on the specified container instance or instances.
        Alternatively, you can use  RunTask to place tasks for you. For more information, see `Scheduling Tasks <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/StartTask>`_
        
        **Request Syntax**
        ::
          response = client.start_task(
              cluster='string',
              taskDefinition='string',
              overrides={
                  'containerOverrides': [
                      {
                          'name': 'string',
                          'command': [
                              'string',
                          ],
                          'environment': [
                              {
                                  'name': 'string',
                                  'value': 'string'
                              },
                          ],
                          'cpu': 123,
                          'memory': 123,
                          'memoryReservation': 123,
                          'resourceRequirements': [
                              {
                                  'value': 'string',
                                  'type': 'GPU'
                              },
                          ]
                      },
                  ],
                  'taskRoleArn': 'string',
                  'executionRoleArn': 'string'
              },
              containerInstances=[
                  'string',
              ],
              startedBy='string',
              group='string',
              networkConfiguration={
                  'awsvpcConfiguration': {
                      'subnets': [
                          'string',
                      ],
                      'securityGroups': [
                          'string',
                      ],
                      'assignPublicIp': 'ENABLED'|'DISABLED'
                  }
              },
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              enableECSManagedTags=True|False,
              propagateTags='TASK_DEFINITION'|'SERVICE'
          )
        
        **Response Syntax**
        ::
            {
                'tasks': [
                    {
                        'taskArn': 'string',
                        'clusterArn': 'string',
                        'taskDefinitionArn': 'string',
                        'containerInstanceArn': 'string',
                        'overrides': {
                            'containerOverrides': [
                                {
                                    'name': 'string',
                                    'command': [
                                        'string',
                                    ],
                                    'environment': [
                                        {
                                            'name': 'string',
                                            'value': 'string'
                                        },
                                    ],
                                    'cpu': 123,
                                    'memory': 123,
                                    'memoryReservation': 123,
                                    'resourceRequirements': [
                                        {
                                            'value': 'string',
                                            'type': 'GPU'
                                        },
                                    ]
                                },
                            ],
                            'taskRoleArn': 'string',
                            'executionRoleArn': 'string'
                        },
                        'lastStatus': 'string',
                        'desiredStatus': 'string',
                        'cpu': 'string',
                        'memory': 'string',
                        'containers': [
                            {
                                'containerArn': 'string',
                                'taskArn': 'string',
                                'name': 'string',
                                'lastStatus': 'string',
                                'exitCode': 123,
                                'reason': 'string',
                                'networkBindings': [
                                    {
                                        'bindIP': 'string',
                                        'containerPort': 123,
                                        'hostPort': 123,
                                        'protocol': 'tcp'|'udp'
                                    },
                                ],
                                'networkInterfaces': [
                                    {
                                        'attachmentId': 'string',
                                        'privateIpv4Address': 'string',
                                        'ipv6Address': 'string'
                                    },
                                ],
                                'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                                'cpu': 'string',
                                'memory': 'string',
                                'memoryReservation': 'string',
                                'gpuIds': [
                                    'string',
                                ]
                            },
                        ],
                        'startedBy': 'string',
                        'version': 123,
                        'stoppedReason': 'string',
                        'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                        'connectivity': 'CONNECTED'|'DISCONNECTED',
                        'connectivityAt': datetime(2015, 1, 1),
                        'pullStartedAt': datetime(2015, 1, 1),
                        'pullStoppedAt': datetime(2015, 1, 1),
                        'executionStoppedAt': datetime(2015, 1, 1),
                        'createdAt': datetime(2015, 1, 1),
                        'startedAt': datetime(2015, 1, 1),
                        'stoppingAt': datetime(2015, 1, 1),
                        'stoppedAt': datetime(2015, 1, 1),
                        'group': 'string',
                        'launchType': 'EC2'|'FARGATE',
                        'platformVersion': 'string',
                        'attachments': [
                            {
                                'id': 'string',
                                'type': 'string',
                                'status': 'string',
                                'details': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ]
                            },
                        ],
                        'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **tasks** *(list) --* 
              A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.
              - *(dict) --* 
                Details on a task in a cluster.
                - **taskArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task.
                - **clusterArn** *(string) --* 
                  The ARN of the cluster that hosts the task.
                - **taskDefinitionArn** *(string) --* 
                  The ARN of the task definition that creates the task.
                - **containerInstanceArn** *(string) --* 
                  The ARN of the container instances that host the task.
                - **overrides** *(dict) --* 
                  One or more container overrides.
                  - **containerOverrides** *(list) --* 
                    One or more container overrides sent to a task.
                    - *(dict) --* 
                      The overrides that should be sent to a container.
                      - **name** *(string) --* 
                        The name of the container that receives the override. This parameter is required if any override is specified.
                      - **command** *(list) --* 
                        The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                        - *(string) --* 
                      - **environment** *(list) --* 
                        The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                        - *(dict) --* 
                          A key-value pair object.
                          - **name** *(string) --* 
                            The name of the key-value pair. For environment variables, this is the name of the environment variable.
                          - **value** *(string) --* 
                            The value of the key-value pair. For environment variables, this is the value of the environment variable.
                      - **cpu** *(integer) --* 
                        The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **memory** *(integer) --* 
                        The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
                      - **memoryReservation** *(integer) --* 
                        The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
                      - **resourceRequirements** *(list) --* 
                        The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                        - *(dict) --* 
                          The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                          - **value** *(string) --* 
                            The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                          - **type** *(string) --* 
                            The type of resource to assign to a container. The only supported value is ``GPU`` .
                  - **taskRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                  - **executionRoleArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
                - **lastStatus** *(string) --* 
                  The last known status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **desiredStatus** *(string) --* 
                  The desired status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
                - **cpu** *(string) --* 
                  The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units, for example ``1024`` . It can also be expressed as a string using vCPUs, for example ``1 vCPU`` or ``1 vcpu`` . String values are converted to an integer indicating the CPU units when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional. Supported values are between ``128`` CPU units (``0.125`` vCPUs) and ``10240`` CPU units (``10`` vCPUs).
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``memory`` parameter:
                  * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                  * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                  * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                  * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                  * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
                - **memory** *(string) --* 
                  The amount of memory (in MiB) used by the task as expressed in a task definition. It can be expressed as an integer using MiB, for example ``1024`` . It can also be expressed as a string using GB, for example ``1GB`` or ``1 GB`` . String values are converted to an integer indicating the MiB when the task definition is registered.
                  If you are using the EC2 launch type, this field is optional.
                  If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``cpu`` parameter:
                  * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                  * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                  * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                  * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                  * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
                - **containers** *(list) --* 
                  The containers associated with the task.
                  - *(dict) --* 
                    A Docker container that is part of a task.
                    - **containerArn** *(string) --* 
                      The Amazon Resource Name (ARN) of the container.
                    - **taskArn** *(string) --* 
                      The ARN of the task.
                    - **name** *(string) --* 
                      The name of the container.
                    - **lastStatus** *(string) --* 
                      The last known status of the container.
                    - **exitCode** *(integer) --* 
                      The exit code returned from the container.
                    - **reason** *(string) --* 
                      A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
                    - **networkBindings** *(list) --* 
                      The network bindings associated with the container.
                      - *(dict) --* 
                        Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                        - **bindIP** *(string) --* 
                          The IP address that the container is bound to on the container instance.
                        - **containerPort** *(integer) --* 
                          The port number on the container that is used with the network binding.
                        - **hostPort** *(integer) --* 
                          The port number on the host that is used with the network binding.
                        - **protocol** *(string) --* 
                          The protocol used for the network binding.
                    - **networkInterfaces** *(list) --* 
                      The network interfaces associated with the container.
                      - *(dict) --* 
                        An object representing the elastic network interface for tasks that use the ``awsvpc`` network mode.
                        - **attachmentId** *(string) --* 
                          The attachment ID for the network interface.
                        - **privateIpv4Address** *(string) --* 
                          The private IPv4 address for the network interface.
                        - **ipv6Address** *(string) --* 
                          The private IPv6 address for the network interface.
                    - **healthStatus** *(string) --* 
                      The health status of the container. If health checks are not configured for this container in its task definition, then it reports the health status as ``UNKNOWN`` .
                    - **cpu** *(string) --* 
                      The number of CPU units set for the container. The value will be ``0`` if no value was specified in the container definition when the task definition was registered.
                    - **memory** *(string) --* 
                      The hard limit (in MiB) of memory set for the container.
                    - **memoryReservation** *(string) --* 
                      The soft limit (in MiB) of memory set for the container.
                    - **gpuIds** *(list) --* 
                      The IDs of each GPU assigned to the container.
                      - *(string) --* 
                - **startedBy** *(string) --* 
                  The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
                - **version** *(integer) --* 
                  The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actionss with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.
                - **stoppedReason** *(string) --* 
                  The reason that the task was stopped.
                - **stopCode** *(string) --* 
                  The stop code indicating why a task was stopped. The ``stoppedReason`` may contain additional details.
                - **connectivity** *(string) --* 
                  The connectivity status of a task.
                - **connectivityAt** *(datetime) --* 
                  The Unix timestamp for when the task last went into ``CONNECTED`` status.
                - **pullStartedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull began.
                - **pullStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the container image pull completed.
                - **executionStoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task execution stopped.
                - **createdAt** *(datetime) --* 
                  The Unix timestamp for when the task was created (the task entered the ``PENDING`` state).
                - **startedAt** *(datetime) --* 
                  The Unix timestamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).
                - **stoppingAt** *(datetime) --* 
                  The Unix timestamp for when the task stops (transitions from the ``RUNNING`` state to ``STOPPED`` ).
                - **stoppedAt** *(datetime) --* 
                  The Unix timestamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).
                - **group** *(string) --* 
                  The name of the task group associated with the task.
                - **launchType** *(string) --* 
                  The launch type on which your task is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **platformVersion** *(string) --* 
                  The platform version on which your task is running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **attachments** *(list) --* 
                  The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.
                  - *(dict) --* 
                    An object representing a container instance or task attachment.
                    - **id** *(string) --* 
                      The unique identifier for the attachment.
                    - **type** *(string) --* 
                      The type of the attachment, such as ``ElasticNetworkInterface`` .
                    - **status** *(string) --* 
                      The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                    - **details** *(list) --* 
                      Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **healthStatus** *(string) --* 
                  The health status for the task, which is determined by the health of the essential containers in the task. If all essential containers in the task are reporting as ``HEALTHY`` , then the task status also reports as ``HEALTHY`` . If any essential containers in the task are reporting as ``UNHEALTHY`` or ``UNKNOWN`` , then the task status also reports as ``UNHEALTHY`` or ``UNKNOWN`` , accordingly.
                  .. note::
                    The Amazon ECS container agent does not monitor or report on Docker health checks that are embedded in a container image (such as those specified in a parent image or from the image's Dockerfile) and not specified in the container definition. Health check parameters that are specified in a container definition override any Docker health checks that exist in the container image.
                - **tags** *(list) --* 
                  The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster on which to start your task. If you do not specify a cluster, the default cluster is assumed.
        :type taskDefinition: string
        :param taskDefinition: **[REQUIRED]**
          The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to start. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used.
        :type overrides: dict
        :param overrides:
          A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that is specified in the task definition or Docker image) with a ``command`` override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an ``environment`` override.
          .. note::
            A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.
          - **containerOverrides** *(list) --*
            One or more container overrides sent to a task.
            - *(dict) --*
              The overrides that should be sent to a container.
              - **name** *(string) --*
                The name of the container that receives the override. This parameter is required if any override is specified.
              - **command** *(list) --*
                The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                - *(string) --*
              - **environment** *(list) --*
                The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                - *(dict) --*
                  A key-value pair object.
                  - **name** *(string) --*
                    The name of the key-value pair. For environment variables, this is the name of the environment variable.
                  - **value** *(string) --*
                    The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **cpu** *(integer) --*
                The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
              - **memory** *(integer) --*
                The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
              - **memoryReservation** *(integer) --*
                The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
              - **resourceRequirements** *(list) --*
                The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                - *(dict) --*
                  The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*
                  - **value** *(string) --* **[REQUIRED]**
                    The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                  - **type** *(string) --* **[REQUIRED]**
                    The type of resource to assign to a container. The only supported value is ``GPU`` .
          - **taskRoleArn** *(string) --*
            The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
          - **executionRoleArn** *(string) --*
            The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
        :type containerInstances: list
        :param containerInstances: **[REQUIRED]**
          The container instance IDs or full ARN entries for the container instances on which you would like to place your task. You can specify up to 10 container instances.
          - *(string) --*
        :type startedBy: string
        :param startedBy:
          An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the ``startedBy`` parameter. You can then identify which tasks belong to that job by filtering the results of a  ListTasks call with the ``startedBy`` value. Up to 36 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.
          If a task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
        :type group: string
        :param group:
          The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).
        :type networkConfiguration: dict
        :param networkConfiguration:
          The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
          - **awsvpcConfiguration** *(dict) --*
            The VPC subnets and security groups associated with a task.
            .. note::
              All specified subnets and security groups must be from the same VPC.
            - **subnets** *(list) --* **[REQUIRED]**
              The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified subnets must be from the same VPC.
              - *(string) --*
            - **securityGroups** *(list) --*
              The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified security groups must be from the same VPC.
              - *(string) --*
            - **assignPublicIp** *(string) --*
              Whether the task\'s elastic network interface receives a public IP address. The default value is ``DISABLED`` .
        :type tags: list
        :param tags:
          The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type enableECSManagedTags: boolean
        :param enableECSManagedTags:
          Specifies whether to enable Amazon ECS managed tags for the task. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type propagateTags: string
        :param propagateTags:
          Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
        :rtype: dict
        :returns:
        """
        pass

    def stop_task(self, task: str, cluster: str = None, reason: str = None) -> Dict:
        """
        Stops a running task. Any tags associated with the task will be deleted.
        When  StopTask is called on a task, the equivalent of ``docker stop`` is issued to the containers running in the task. This results in a ``SIGTERM`` value and a default 30-second timeout, after which the ``SIGKILL`` value is sent and the containers are forcibly stopped. If the container handles the ``SIGTERM`` value gracefully and exits within 30 seconds from receiving it, no ``SIGKILL`` value is sent.
        .. note::
          The default 30-second timeout can be configured on the Amazon ECS container agent with the ``ECS_CONTAINER_STOP_TIMEOUT`` variable. For more information, see `Amazon ECS Container Agent Configuration <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/StopTask>`_
        
        **Request Syntax**
        ::
          response = client.stop_task(
              cluster='string',
              task='string',
              reason='string'
          )
        
        **Response Syntax**
        ::
            {
                'task': {
                    'taskArn': 'string',
                    'clusterArn': 'string',
                    'taskDefinitionArn': 'string',
                    'containerInstanceArn': 'string',
                    'overrides': {
                        'containerOverrides': [
                            {
                                'name': 'string',
                                'command': [
                                    'string',
                                ],
                                'environment': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ],
                                'cpu': 123,
                                'memory': 123,
                                'memoryReservation': 123,
                                'resourceRequirements': [
                                    {
                                        'value': 'string',
                                        'type': 'GPU'
                                    },
                                ]
                            },
                        ],
                        'taskRoleArn': 'string',
                        'executionRoleArn': 'string'
                    },
                    'lastStatus': 'string',
                    'desiredStatus': 'string',
                    'cpu': 'string',
                    'memory': 'string',
                    'containers': [
                        {
                            'containerArn': 'string',
                            'taskArn': 'string',
                            'name': 'string',
                            'lastStatus': 'string',
                            'exitCode': 123,
                            'reason': 'string',
                            'networkBindings': [
                                {
                                    'bindIP': 'string',
                                    'containerPort': 123,
                                    'hostPort': 123,
                                    'protocol': 'tcp'|'udp'
                                },
                            ],
                            'networkInterfaces': [
                                {
                                    'attachmentId': 'string',
                                    'privateIpv4Address': 'string',
                                    'ipv6Address': 'string'
                                },
                            ],
                            'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                            'cpu': 'string',
                            'memory': 'string',
                            'memoryReservation': 'string',
                            'gpuIds': [
                                'string',
                            ]
                        },
                    ],
                    'startedBy': 'string',
                    'version': 123,
                    'stoppedReason': 'string',
                    'stopCode': 'TaskFailedToStart'|'EssentialContainerExited'|'UserInitiated',
                    'connectivity': 'CONNECTED'|'DISCONNECTED',
                    'connectivityAt': datetime(2015, 1, 1),
                    'pullStartedAt': datetime(2015, 1, 1),
                    'pullStoppedAt': datetime(2015, 1, 1),
                    'executionStoppedAt': datetime(2015, 1, 1),
                    'createdAt': datetime(2015, 1, 1),
                    'startedAt': datetime(2015, 1, 1),
                    'stoppingAt': datetime(2015, 1, 1),
                    'stoppedAt': datetime(2015, 1, 1),
                    'group': 'string',
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ],
                    'healthStatus': 'HEALTHY'|'UNHEALTHY'|'UNKNOWN',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **task** *(dict) --* 
              The task that was stopped.
              - **taskArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task.
              - **clusterArn** *(string) --* 
                The ARN of the cluster that hosts the task.
              - **taskDefinitionArn** *(string) --* 
                The ARN of the task definition that creates the task.
              - **containerInstanceArn** *(string) --* 
                The ARN of the container instances that host the task.
              - **overrides** *(dict) --* 
                One or more container overrides.
                - **containerOverrides** *(list) --* 
                  One or more container overrides sent to a task.
                  - *(dict) --* 
                    The overrides that should be sent to a container.
                    - **name** *(string) --* 
                      The name of the container that receives the override. This parameter is required if any override is specified.
                    - **command** *(list) --* 
                      The command to send to the container that overrides the default command from the Docker image or the task definition. You must also specify a container name.
                      - *(string) --* 
                    - **environment** *(list) --* 
                      The environment variables to send to the container. You can add new environment variables, which are added to the container at launch, or you can override the existing environment variables from the Docker image or the task definition. You must also specify a container name.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                    - **cpu** *(integer) --* 
                      The number of ``cpu`` units reserved for the container, instead of the default value from the task definition. You must also specify a container name.
                    - **memory** *(integer) --* 
                      The hard limit (in MiB) of memory to present to the container, instead of the default value from the task definition. If your container attempts to exceed the memory specified here, the container is killed. You must also specify a container name.
                    - **memoryReservation** *(integer) --* 
                      The soft limit (in MiB) of memory to reserve for the container, instead of the default value from the task definition. You must also specify a container name.
                    - **resourceRequirements** *(list) --* 
                      The type and amount of a resource to assign to a container, instead of the default value from the task definition. The only supported resource is a GPU.
                      - *(dict) --* 
                        The type and amount of a resource to assign to a container. The only supported resource is a GPU. For more information, see `Working with GPUs on Amazon ECS <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html>`__ in the *Amazon Elastic Container Service Developer Guide*  
                        - **value** *(string) --* 
                          The number of physical ``GPUs`` the Amazon ECS container agent will reserve for the container. The number of GPUs reserved for all containers in a task should not exceed the number of available GPUs on the container instance the task is launched on.
                        - **type** *(string) --* 
                          The type of resource to assign to a container. The only supported value is ``GPU`` .
                - **taskRoleArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.
                - **executionRoleArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
              - **lastStatus** *(string) --* 
                The last known status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
              - **desiredStatus** *(string) --* 
                The desired status of the task. For more information, see `Task Lifecycle <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_life_cycle.html>`__ .
              - **cpu** *(string) --* 
                The number of CPU units used by the task as expressed in a task definition. It can be expressed as an integer using CPU units, for example ``1024`` . It can also be expressed as a string using vCPUs, for example ``1 vCPU`` or ``1 vcpu`` . String values are converted to an integer indicating the CPU units when the task definition is registered.
                If you are using the EC2 launch type, this field is optional. Supported values are between ``128`` CPU units (``0.125`` vCPUs) and ``10240`` CPU units (``10`` vCPUs).
                If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``memory`` parameter:
                * 256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 
                * 512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 
                * 1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 
                * 2048 (2 vCPU) - Available ``memory`` values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 
                * 4096 (4 vCPU) - Available ``memory`` values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) 
              - **memory** *(string) --* 
                The amount of memory (in MiB) used by the task as expressed in a task definition. It can be expressed as an integer using MiB, for example ``1024`` . It can also be expressed as a string using GB, for example ``1GB`` or ``1 GB`` . String values are converted to an integer indicating the MiB when the task definition is registered.
                If you are using the EC2 launch type, this field is optional.
                If you are using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of supported values for the ``cpu`` parameter:
                * 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU) 
                * 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU) 
                * 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU) 
                * Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU) 
                * Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU) 
              - **containers** *(list) --* 
                The containers associated with the task.
                - *(dict) --* 
                  A Docker container that is part of a task.
                  - **containerArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the container.
                  - **taskArn** *(string) --* 
                    The ARN of the task.
                  - **name** *(string) --* 
                    The name of the container.
                  - **lastStatus** *(string) --* 
                    The last known status of the container.
                  - **exitCode** *(integer) --* 
                    The exit code returned from the container.
                  - **reason** *(string) --* 
                    A short (255 max characters) human-readable string to provide additional details about a running or stopped container.
                  - **networkBindings** *(list) --* 
                    The network bindings associated with the container.
                    - *(dict) --* 
                      Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                      - **bindIP** *(string) --* 
                        The IP address that the container is bound to on the container instance.
                      - **containerPort** *(integer) --* 
                        The port number on the container that is used with the network binding.
                      - **hostPort** *(integer) --* 
                        The port number on the host that is used with the network binding.
                      - **protocol** *(string) --* 
                        The protocol used for the network binding.
                  - **networkInterfaces** *(list) --* 
                    The network interfaces associated with the container.
                    - *(dict) --* 
                      An object representing the elastic network interface for tasks that use the ``awsvpc`` network mode.
                      - **attachmentId** *(string) --* 
                        The attachment ID for the network interface.
                      - **privateIpv4Address** *(string) --* 
                        The private IPv4 address for the network interface.
                      - **ipv6Address** *(string) --* 
                        The private IPv6 address for the network interface.
                  - **healthStatus** *(string) --* 
                    The health status of the container. If health checks are not configured for this container in its task definition, then it reports the health status as ``UNKNOWN`` .
                  - **cpu** *(string) --* 
                    The number of CPU units set for the container. The value will be ``0`` if no value was specified in the container definition when the task definition was registered.
                  - **memory** *(string) --* 
                    The hard limit (in MiB) of memory set for the container.
                  - **memoryReservation** *(string) --* 
                    The soft limit (in MiB) of memory set for the container.
                  - **gpuIds** *(list) --* 
                    The IDs of each GPU assigned to the container.
                    - *(string) --* 
              - **startedBy** *(string) --* 
                The tag specified when a task is started. If the task is started by an Amazon ECS service, then the ``startedBy`` parameter contains the deployment ID of the service that starts it.
              - **version** *(integer) --* 
                The version counter for the task. Every time a task experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS task state with CloudWatch Events, you can compare the version of a task reported by the Amazon ECS API actionss with the version reported in CloudWatch Events for the task (inside the ``detail`` object) to verify that the version in your event stream is current.
              - **stoppedReason** *(string) --* 
                The reason that the task was stopped.
              - **stopCode** *(string) --* 
                The stop code indicating why a task was stopped. The ``stoppedReason`` may contain additional details.
              - **connectivity** *(string) --* 
                The connectivity status of a task.
              - **connectivityAt** *(datetime) --* 
                The Unix timestamp for when the task last went into ``CONNECTED`` status.
              - **pullStartedAt** *(datetime) --* 
                The Unix timestamp for when the container image pull began.
              - **pullStoppedAt** *(datetime) --* 
                The Unix timestamp for when the container image pull completed.
              - **executionStoppedAt** *(datetime) --* 
                The Unix timestamp for when the task execution stopped.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the task was created (the task entered the ``PENDING`` state).
              - **startedAt** *(datetime) --* 
                The Unix timestamp for when the task started (the task transitioned from the ``PENDING`` state to the ``RUNNING`` state).
              - **stoppingAt** *(datetime) --* 
                The Unix timestamp for when the task stops (transitions from the ``RUNNING`` state to ``STOPPED`` ).
              - **stoppedAt** *(datetime) --* 
                The Unix timestamp for when the task was stopped (the task transitioned from the ``RUNNING`` state to the ``STOPPED`` state).
              - **group** *(string) --* 
                The name of the task group associated with the task.
              - **launchType** *(string) --* 
                The launch type on which your task is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which your task is running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **attachments** *(list) --* 
                The Elastic Network Adapter associated with the task if the task uses the ``awsvpc`` network mode.
                - *(dict) --* 
                  An object representing a container instance or task attachment.
                  - **id** *(string) --* 
                    The unique identifier for the attachment.
                  - **type** *(string) --* 
                    The type of the attachment, such as ``ElasticNetworkInterface`` .
                  - **status** *(string) --* 
                    The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                  - **details** *(list) --* 
                    Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **healthStatus** *(string) --* 
                The health status for the task, which is determined by the health of the essential containers in the task. If all essential containers in the task are reporting as ``HEALTHY`` , then the task status also reports as ``HEALTHY`` . If any essential containers in the task are reporting as ``UNHEALTHY`` or ``UNKNOWN`` , then the task status also reports as ``UNHEALTHY`` or ``UNKNOWN`` , accordingly.
                .. note::
                  The Amazon ECS container agent does not monitor or report on Docker health checks that are embedded in a container image (such as those specified in a parent image or from the image's Dockerfile) and not specified in the container definition. Health check parameters that are specified in a container definition override any Docker health checks that exist in the container image.
              - **tags** *(list) --* 
                The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.
        :type task: string
        :param task: **[REQUIRED]**
          The task ID or full Amazon Resource Name (ARN) of the task to stop.
        :type reason: string
        :param reason:
          An optional message specified when a task is stopped. For example, if you are using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent  DescribeTasks API operations on this task. Up to 255 characters are allowed in this message.
        :rtype: dict
        :returns:
        """
        pass

    def submit_container_state_change(self, cluster: str = None, task: str = None, containerName: str = None, status: str = None, exitCode: int = None, reason: str = None, networkBindings: List = None) -> Dict:
        """
        .. note::
          This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.
        Sent to acknowledge that a container changed states.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/SubmitContainerStateChange>`_
        
        **Request Syntax**
        ::
          response = client.submit_container_state_change(
              cluster='string',
              task='string',
              containerName='string',
              status='string',
              exitCode=123,
              reason='string',
              networkBindings=[
                  {
                      'bindIP': 'string',
                      'containerPort': 123,
                      'hostPort': 123,
                      'protocol': 'tcp'|'udp'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'acknowledgment': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **acknowledgment** *(string) --* 
              Acknowledgement of the state change.
        :type cluster: string
        :param cluster:
          The short name or full ARN of the cluster that hosts the container.
        :type task: string
        :param task:
          The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.
        :type containerName: string
        :param containerName:
          The name of the container.
        :type status: string
        :param status:
          The status of the state change request.
        :type exitCode: integer
        :param exitCode:
          The exit code returned for the state change request.
        :type reason: string
        :param reason:
          The reason for the state change request.
        :type networkBindings: list
        :param networkBindings:
          The network bindings of the container.
          - *(dict) --*
            Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
            - **bindIP** *(string) --*
              The IP address that the container is bound to on the container instance.
            - **containerPort** *(integer) --*
              The port number on the container that is used with the network binding.
            - **hostPort** *(integer) --*
              The port number on the host that is used with the network binding.
            - **protocol** *(string) --*
              The protocol used for the network binding.
        :rtype: dict
        :returns:
        """
        pass

    def submit_task_state_change(self, cluster: str = None, task: str = None, status: str = None, reason: str = None, containers: List = None, attachments: List = None, pullStartedAt: datetime = None, pullStoppedAt: datetime = None, executionStoppedAt: datetime = None) -> Dict:
        """
        .. note::
          This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.
        Sent to acknowledge that a task changed states.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/SubmitTaskStateChange>`_
        
        **Request Syntax**
        ::
          response = client.submit_task_state_change(
              cluster='string',
              task='string',
              status='string',
              reason='string',
              containers=[
                  {
                      'containerName': 'string',
                      'exitCode': 123,
                      'networkBindings': [
                          {
                              'bindIP': 'string',
                              'containerPort': 123,
                              'hostPort': 123,
                              'protocol': 'tcp'|'udp'
                          },
                      ],
                      'reason': 'string',
                      'status': 'string'
                  },
              ],
              attachments=[
                  {
                      'attachmentArn': 'string',
                      'status': 'string'
                  },
              ],
              pullStartedAt=datetime(2015, 1, 1),
              pullStoppedAt=datetime(2015, 1, 1),
              executionStoppedAt=datetime(2015, 1, 1)
          )
        
        **Response Syntax**
        ::
            {
                'acknowledgment': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **acknowledgment** *(string) --* 
              Acknowledgement of the state change.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.
        :type task: string
        :param task:
          The task ID or full ARN of the task in the state change request.
        :type status: string
        :param status:
          The status of the state change request.
        :type reason: string
        :param reason:
          The reason for the state change request.
        :type containers: list
        :param containers:
          Any containers associated with the state change request.
          - *(dict) --*
            An object representing a change in state for a container.
            - **containerName** *(string) --*
              The name of the container.
            - **exitCode** *(integer) --*
              The exit code for the container, if the state change is a result of the container exiting.
            - **networkBindings** *(list) --*
              Any network bindings associated with the container.
              - *(dict) --*
                Details on the network bindings between a container and its host container instance. After a task reaches the ``RUNNING`` status, manual and automatic host and container port assignments are visible in the ``networkBindings`` section of  DescribeTasks API responses.
                - **bindIP** *(string) --*
                  The IP address that the container is bound to on the container instance.
                - **containerPort** *(integer) --*
                  The port number on the container that is used with the network binding.
                - **hostPort** *(integer) --*
                  The port number on the host that is used with the network binding.
                - **protocol** *(string) --*
                  The protocol used for the network binding.
            - **reason** *(string) --*
              The reason for the state change.
            - **status** *(string) --*
              The status of the container.
        :type attachments: list
        :param attachments:
          Any attachments associated with the state change request.
          - *(dict) --*
            An object representing a change in state for a task attachment.
            - **attachmentArn** *(string) --* **[REQUIRED]**
              The Amazon Resource Name (ARN) of the attachment.
            - **status** *(string) --* **[REQUIRED]**
              The status of the attachment.
        :type pullStartedAt: datetime
        :param pullStartedAt:
          The Unix timestamp for when the container image pull began.
        :type pullStoppedAt: datetime
        :param pullStoppedAt:
          The Unix timestamp for when the container image pull completed.
        :type executionStoppedAt: datetime
        :param executionStoppedAt:
          The Unix timestamp for when the task execution stopped.
        :rtype: dict
        :returns:
        """
        pass

    def tag_resource(self, resourceArn: str, tags: List) -> Dict:
        """
        Associates the specified tags to a resource with the specified ``resourceArn`` . If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/TagResource>`_
        
        **Request Syntax**
        ::
          response = client.tag_resource(
              resourceArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource to which to add tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
        :type tags: list
        :param tags: **[REQUIRED]**
          The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
          - *(dict) --*
            The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
            - **key** *(string) --*
              One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
            - **value** *(string) --*
              The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :rtype: dict
        :returns:
        """
        pass

    def untag_resource(self, resourceArn: str, tagKeys: List) -> Dict:
        """
        Deletes specified tags from a resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UntagResource>`_
        
        **Request Syntax**
        ::
          response = client.untag_resource(
              resourceArn='string',
              tagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type resourceArn: string
        :param resourceArn: **[REQUIRED]**
          The Amazon Resource Name (ARN) of the resource from which to delete tags. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.
        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**
          The keys of the tags to be removed.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def update_container_agent(self, containerInstance: str, cluster: str = None) -> Dict:
        """
        Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent does not interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.
         ``UpdateContainerAgent`` requires the Amazon ECS-optimized AMI or Amazon Linux with the ``ecs-init`` service installed and running. For help updating the Amazon ECS container agent on other operating systems, see `Manually Updating the Amazon ECS Container Agent <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateContainerAgent>`_
        
        **Request Syntax**
        ::
          response = client.update_container_agent(
              cluster='string',
              containerInstance='string'
          )
        
        **Response Syntax**
        ::
            {
                'containerInstance': {
                    'containerInstanceArn': 'string',
                    'ec2InstanceId': 'string',
                    'version': 123,
                    'versionInfo': {
                        'agentVersion': 'string',
                        'agentHash': 'string',
                        'dockerVersion': 'string'
                    },
                    'remainingResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'registeredResources': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'doubleValue': 123.0,
                            'longValue': 123,
                            'integerValue': 123,
                            'stringSetValue': [
                                'string',
                            ]
                        },
                    ],
                    'status': 'string',
                    'agentConnected': True|False,
                    'runningTasksCount': 123,
                    'pendingTasksCount': 123,
                    'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                    'attributes': [
                        {
                            'name': 'string',
                            'value': 'string',
                            'targetType': 'container-instance',
                            'targetId': 'string'
                        },
                    ],
                    'registeredAt': datetime(2015, 1, 1),
                    'attachments': [
                        {
                            'id': 'string',
                            'type': 'string',
                            'status': 'string',
                            'details': [
                                {
                                    'name': 'string',
                                    'value': 'string'
                                },
                            ]
                        },
                    ],
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ]
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstance** *(dict) --* 
              The container instance for which the container agent was updated.
              - **containerInstanceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
              - **ec2InstanceId** *(string) --* 
                The EC2 instance ID of the container instance.
              - **version** *(integer) --* 
                The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.
              - **versionInfo** *(dict) --* 
                The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
                - **agentVersion** *(string) --* 
                  The version number of the Amazon ECS container agent.
                - **agentHash** *(string) --* 
                  The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
                - **dockerVersion** *(string) --* 
                  The Docker version running on the container instance.
              - **remainingResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the remaining CPU and memory that has not already been allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the ``host`` or ``bridge`` network mode). Any port that is not specified here is available for new tasks.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **registeredResources** *(list) --* 
                For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
                - *(dict) --* 
                  Describes the resources available for a container instance.
                  - **name** *(string) --* 
                    The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                  - **type** *(string) --* 
                    The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                  - **doubleValue** *(float) --* 
                    When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                  - **longValue** *(integer) --* 
                    When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                  - **integerValue** *(integer) --* 
                    When the ``integerValue`` type is set, the value of the resource must be an integer.
                  - **stringSetValue** *(list) --* 
                    When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                    - *(string) --* 
              - **status** *(string) --* 
                The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **agentConnected** *(boolean) --* 
                This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Only instances connected to an agent can accept placement requests.
              - **runningTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``RUNNING`` status.
              - **pendingTasksCount** *(integer) --* 
                The number of tasks on the container instance that are in the ``PENDING`` status.
              - **agentUpdateStatus** *(string) --* 
                The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .
              - **attributes** *(list) --* 
                The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.
                - *(dict) --* 
                  An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **name** *(string) --* 
                    The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                  - **value** *(string) --* 
                    The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                  - **targetType** *(string) --* 
                    The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                  - **targetId** *(string) --* 
                    The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
              - **registeredAt** *(datetime) --* 
                The Unix timestamp for when the container instance was registered.
              - **attachments** *(list) --* 
                The elastic network interfaces associated with the container instance.
                - *(dict) --* 
                  An object representing a container instance or task attachment.
                  - **id** *(string) --* 
                    The unique identifier for the attachment.
                  - **type** *(string) --* 
                    The type of the attachment, such as ``ElasticNetworkInterface`` .
                  - **status** *(string) --* 
                    The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                  - **details** *(list) --* 
                    Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                    - *(dict) --* 
                      A key-value pair object.
                      - **name** *(string) --* 
                        The name of the key-value pair. For environment variables, this is the name of the environment variable.
                      - **value** *(string) --* 
                        The value of the key-value pair. For environment variables, this is the value of the environment variable.
              - **tags** *(list) --* 
                The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.
        :type containerInstance: string
        :param containerInstance: **[REQUIRED]**
          The container instance ID or full ARN entries for the container instance on which you would like to update the Amazon ECS container agent.
        :rtype: dict
        :returns:
        """
        pass

    def update_container_instances_state(self, containerInstances: List, status: str, cluster: str = None) -> Dict:
        """
        Modifies the status of an Amazon ECS container instance.
        You can change the status of a container instance to ``DRAINING`` to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size. 
        When you set a container instance to ``DRAINING`` , Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the ``PENDING`` state are stopped immediately.
        Service tasks on the container instance that are in the ``RUNNING`` state are stopped and replaced according to the service's deployment configuration parameters, ``minimumHealthyPercent`` and ``maximumPercent`` . You can change the deployment configuration of your service using  UpdateService .
        * If ``minimumHealthyPercent`` is below 100%, the scheduler can ignore ``desiredCount`` temporarily during task replacement. For example, ``desiredCount`` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can't remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they are in the ``RUNNING`` state. Tasks for services that use a load balancer are considered healthy if they are in the ``RUNNING`` state and the container instance they are hosted on is reported as healthy by the load balancer. 
        * The ``maximumPercent`` parameter represents an upper limit on the number of running tasks during task replacement, which enables you to define the replacement batch size. For example, if ``desiredCount`` is four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained, provided that the cluster resources required to do this are available. If the maximum is 100%, then replacement tasks can't start until the draining tasks have stopped. 
        Any ``PENDING`` or ``RUNNING`` tasks that do not belong to a service are not affected. You must wait for them to finish or stop them manually.
        A container instance has completed draining when it has no more ``RUNNING`` tasks. You can verify this using  ListTasks .
        When you set a container instance to ``ACTIVE`` , the Amazon ECS scheduler can begin scheduling tasks on the instance again.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateContainerInstancesState>`_
        
        **Request Syntax**
        ::
          response = client.update_container_instances_state(
              cluster='string',
              containerInstances=[
                  'string',
              ],
              status='ACTIVE'|'DRAINING'
          )
        
        **Response Syntax**
        ::
            {
                'containerInstances': [
                    {
                        'containerInstanceArn': 'string',
                        'ec2InstanceId': 'string',
                        'version': 123,
                        'versionInfo': {
                            'agentVersion': 'string',
                            'agentHash': 'string',
                            'dockerVersion': 'string'
                        },
                        'remainingResources': [
                            {
                                'name': 'string',
                                'type': 'string',
                                'doubleValue': 123.0,
                                'longValue': 123,
                                'integerValue': 123,
                                'stringSetValue': [
                                    'string',
                                ]
                            },
                        ],
                        'registeredResources': [
                            {
                                'name': 'string',
                                'type': 'string',
                                'doubleValue': 123.0,
                                'longValue': 123,
                                'integerValue': 123,
                                'stringSetValue': [
                                    'string',
                                ]
                            },
                        ],
                        'status': 'string',
                        'agentConnected': True|False,
                        'runningTasksCount': 123,
                        'pendingTasksCount': 123,
                        'agentUpdateStatus': 'PENDING'|'STAGING'|'STAGED'|'UPDATING'|'UPDATED'|'FAILED',
                        'attributes': [
                            {
                                'name': 'string',
                                'value': 'string',
                                'targetType': 'container-instance',
                                'targetId': 'string'
                            },
                        ],
                        'registeredAt': datetime(2015, 1, 1),
                        'attachments': [
                            {
                                'id': 'string',
                                'type': 'string',
                                'status': 'string',
                                'details': [
                                    {
                                        'name': 'string',
                                        'value': 'string'
                                    },
                                ]
                            },
                        ],
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ]
                    },
                ],
                'failures': [
                    {
                        'arn': 'string',
                        'reason': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **containerInstances** *(list) --* 
              The list of container instances.
              - *(dict) --* 
                An EC2 instance that is running the Amazon ECS agent and has been registered with a cluster.
                - **containerInstanceArn** *(string) --* 
                  The Amazon Resource Name (ARN) of the container instance. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the container instance, the AWS account ID of the container instance owner, the ``container-instance`` namespace, and then the container instance ID. For example, ``arn:aws:ecs:*region* :*aws_account_id* :container-instance/*container_instance_ID* `` .
                - **ec2InstanceId** *(string) --* 
                  The EC2 instance ID of the container instance.
                - **version** *(integer) --* 
                  The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you are replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the ``detail`` object) to verify that the version in your event stream is current.
                - **versionInfo** *(dict) --* 
                  The version information for the Amazon ECS container agent and Docker daemon running on the container instance.
                  - **agentVersion** *(string) --* 
                    The version number of the Amazon ECS container agent.
                  - **agentHash** *(string) --* 
                    The Git commit hash for the Amazon ECS container agent build on the `amazon-ecs-agent <https://github.com/aws/amazon-ecs-agent/commits/master>`__ GitHub repository.
                  - **dockerVersion** *(string) --* 
                    The Docker version running on the container instance.
                - **remainingResources** *(list) --* 
                  For CPU and memory resource types, this parameter describes the remaining CPU and memory that has not already been allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the ``host`` or ``bridge`` network mode). Any port that is not specified here is available for new tasks.
                  - *(dict) --* 
                    Describes the resources available for a container instance.
                    - **name** *(string) --* 
                      The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                    - **type** *(string) --* 
                      The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                    - **doubleValue** *(float) --* 
                      When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                    - **longValue** *(integer) --* 
                      When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                    - **integerValue** *(integer) --* 
                      When the ``integerValue`` type is set, the value of the resource must be an integer.
                    - **stringSetValue** *(list) --* 
                      When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                      - *(string) --* 
                - **registeredResources** *(list) --* 
                  For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.
                  - *(dict) --* 
                    Describes the resources available for a container instance.
                    - **name** *(string) --* 
                      The name of the resource, such as ``CPU`` , ``MEMORY`` , ``PORTS`` , ``PORTS_UDP`` , or a user-defined resource.
                    - **type** *(string) --* 
                      The type of the resource, such as ``INTEGER`` , ``DOUBLE`` , ``LONG`` , or ``STRINGSET`` .
                    - **doubleValue** *(float) --* 
                      When the ``doubleValue`` type is set, the value of the resource must be a double precision floating-point type.
                    - **longValue** *(integer) --* 
                      When the ``longValue`` type is set, the value of the resource must be an extended precision floating-point type.
                    - **integerValue** *(integer) --* 
                      When the ``integerValue`` type is set, the value of the resource must be an integer.
                    - **stringSetValue** *(list) --* 
                      When the ``stringSetValue`` type is set, the value of the resource must be a string type.
                      - *(string) --* 
                - **status** *(string) --* 
                  The status of the container instance. The valid values are ``ACTIVE`` , ``INACTIVE`` , or ``DRAINING`` . ``ACTIVE`` indicates that the container instance can accept tasks. ``DRAINING`` indicates that new tasks are not placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see `Container Instance Draining <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                - **agentConnected** *(boolean) --* 
                  This parameter returns ``true`` if the agent is connected to Amazon ECS. Registered instances with an agent that may be unhealthy or stopped return ``false`` . Only instances connected to an agent can accept placement requests.
                - **runningTasksCount** *(integer) --* 
                  The number of tasks on the container instance that are in the ``RUNNING`` status.
                - **pendingTasksCount** *(integer) --* 
                  The number of tasks on the container instance that are in the ``PENDING`` status.
                - **agentUpdateStatus** *(string) --* 
                  The status of the most recent agent update. If an update has never been requested, this value is ``NULL`` .
                - **attributes** *(list) --* 
                  The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the  PutAttributes operation.
                  - *(dict) --* 
                    An attribute is a name-value pair associated with an Amazon ECS object. Attributes enable you to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see `Attributes <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes>`__ in the *Amazon Elastic Container Service Developer Guide* .
                    - **name** *(string) --* 
                      The name of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, and periods are allowed.
                    - **value** *(string) --* 
                      The value of the attribute. Up to 128 letters (uppercase and lowercase), numbers, hyphens, underscores, periods, at signs (@), forward slashes, colons, and spaces are allowed.
                    - **targetType** *(string) --* 
                      The type of the target with which to attach the attribute. This parameter is required if you use the short form ID for a resource instead of the full ARN.
                    - **targetId** *(string) --* 
                      The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).
                - **registeredAt** *(datetime) --* 
                  The Unix timestamp for when the container instance was registered.
                - **attachments** *(list) --* 
                  The elastic network interfaces associated with the container instance.
                  - *(dict) --* 
                    An object representing a container instance or task attachment.
                    - **id** *(string) --* 
                      The unique identifier for the attachment.
                    - **type** *(string) --* 
                      The type of the attachment, such as ``ElasticNetworkInterface`` .
                    - **status** *(string) --* 
                      The status of the attachment. Valid values are ``PRECREATED`` , ``CREATED`` , ``ATTACHING`` , ``ATTACHED`` , ``DETACHING`` , ``DETACHED`` , and ``DELETED`` .
                    - **details** *(list) --* 
                      Details of the attachment. For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.
                      - *(dict) --* 
                        A key-value pair object.
                        - **name** *(string) --* 
                          The name of the key-value pair. For environment variables, this is the name of the environment variable.
                        - **value** *(string) --* 
                          The value of the key-value pair. For environment variables, this is the value of the environment variable.
                - **tags** *(list) --* 
                  The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - *(dict) --* 
                    The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                    - **key** *(string) --* 
                      One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                    - **value** *(string) --* 
                      The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
            - **failures** *(list) --* 
              Any failures associated with the call.
              - *(dict) --* 
                A failed resource.
                - **arn** *(string) --* 
                  The Amazon Resource Name (ARN) of the failed resource.
                - **reason** *(string) --* 
                  The reason for the failure.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to update. If you do not specify a cluster, the default cluster is assumed.
        :type containerInstances: list
        :param containerInstances: **[REQUIRED]**
          A list of container instance IDs or full ARN entries.
          - *(string) --*
        :type status: string
        :param status: **[REQUIRED]**
          The container instance state with which to update the container instance.
        :rtype: dict
        :returns:
        """
        pass

    def update_service(self, service: str, cluster: str = None, desiredCount: int = None, taskDefinition: str = None, deploymentConfiguration: Dict = None, networkConfiguration: Dict = None, platformVersion: str = None, forceNewDeployment: bool = None, healthCheckGracePeriodSeconds: int = None) -> Dict:
        """
        Modifies the parameters of a service.
        For services using the rolling update (``ECS`` ) deployment controller, the desired count, deployment configuration, network configuration, or task definition used can be updated.
        For services using the blue/green (``CODE_DEPLOY`` ) deployment controller, only the desired count, deployment configuration, and health check grace period can be updated using this API. If the network configuration, platform version, or task definition need to be updated, a new AWS CodeDeploy deployment should be created. For more information, see `CreateDeployment <https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html>`__ in the *AWS CodeDeploy API Reference* .
        For services using an external deployment controller, you can update only the desired count and health check grace period using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, you should create a new task set. For more information, see  CreateTaskSet .
        You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new ``desiredCount`` parameter.
        If you have updated the Docker image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.
        .. note::
          If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, ``my_image:latest`` ), you do not need to create a new revision of your task definition. You can update the service using the ``forceNewDeployment`` option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.
        You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, ``minimumHealthyPercent`` and ``maximumPercent`` , to determine the deployment strategy.
        * If ``minimumHealthyPercent`` is below 100%, the scheduler can ignore ``desiredCount`` temporarily during a deployment. For example, if ``desiredCount`` is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that do not use a load balancer are considered healthy if they are in the ``RUNNING`` state. Tasks for services that use a load balancer are considered healthy if they are in the ``RUNNING`` state and the container instance they are hosted on is reported as healthy by the load balancer. 
        * The ``maximumPercent`` parameter represents an upper limit on the number of running tasks during a deployment, which enables you to define the deployment batch size. For example, if ``desiredCount`` is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). 
        When  UpdateService stops a task during a deployment, the equivalent of ``docker stop`` is issued to the containers running in the task. This results in a ``SIGTERM`` and a 30-second timeout, after which ``SIGKILL`` is sent and the containers are forcibly stopped. If the container handles the ``SIGTERM`` gracefully and exits within 30 seconds from receiving it, no ``SIGKILL`` is sent.
        When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic:
        * Determine which of the container instances in your cluster can support your service's task definition (for example, they have the required CPU, memory, ports, and container instance attributes). 
        * By default, the service scheduler attempts to balance tasks across Availability Zones in this manner (although you can choose a different placement strategy): 
          * Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement. 
          * Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service. 
        When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: 
        * Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination. 
        * Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateService>`_
        
        **Request Syntax**
        ::
          response = client.update_service(
              cluster='string',
              service='string',
              desiredCount=123,
              taskDefinition='string',
              deploymentConfiguration={
                  'maximumPercent': 123,
                  'minimumHealthyPercent': 123
              },
              networkConfiguration={
                  'awsvpcConfiguration': {
                      'subnets': [
                          'string',
                      ],
                      'securityGroups': [
                          'string',
                      ],
                      'assignPublicIp': 'ENABLED'|'DISABLED'
                  }
              },
              platformVersion='string',
              forceNewDeployment=True|False,
              healthCheckGracePeriodSeconds=123
          )
        
        **Response Syntax**
        ::
            {
                'service': {
                    'serviceArn': 'string',
                    'serviceName': 'string',
                    'clusterArn': 'string',
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'status': 'string',
                    'desiredCount': 123,
                    'runningCount': 123,
                    'pendingCount': 123,
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'taskDefinition': 'string',
                    'deploymentConfiguration': {
                        'maximumPercent': 123,
                        'minimumHealthyPercent': 123
                    },
                    'taskSets': [
                        {
                            'id': 'string',
                            'taskSetArn': 'string',
                            'serviceArn': 'string',
                            'clusterArn': 'string',
                            'startedBy': 'string',
                            'externalId': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'computedDesiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            },
                            'loadBalancers': [
                                {
                                    'targetGroupArn': 'string',
                                    'loadBalancerName': 'string',
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'serviceRegistries': [
                                {
                                    'registryArn': 'string',
                                    'port': 123,
                                    'containerName': 'string',
                                    'containerPort': 123
                                },
                            ],
                            'scale': {
                                'value': 123.0,
                                'unit': 'PERCENT'
                            },
                            'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                            'stabilityStatusAt': datetime(2015, 1, 1)
                        },
                    ],
                    'deployments': [
                        {
                            'id': 'string',
                            'status': 'string',
                            'taskDefinition': 'string',
                            'desiredCount': 123,
                            'pendingCount': 123,
                            'runningCount': 123,
                            'createdAt': datetime(2015, 1, 1),
                            'updatedAt': datetime(2015, 1, 1),
                            'launchType': 'EC2'|'FARGATE',
                            'platformVersion': 'string',
                            'networkConfiguration': {
                                'awsvpcConfiguration': {
                                    'subnets': [
                                        'string',
                                    ],
                                    'securityGroups': [
                                        'string',
                                    ],
                                    'assignPublicIp': 'ENABLED'|'DISABLED'
                                }
                            }
                        },
                    ],
                    'roleArn': 'string',
                    'events': [
                        {
                            'id': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'message': 'string'
                        },
                    ],
                    'createdAt': datetime(2015, 1, 1),
                    'placementConstraints': [
                        {
                            'type': 'distinctInstance'|'memberOf',
                            'expression': 'string'
                        },
                    ],
                    'placementStrategy': [
                        {
                            'type': 'random'|'spread'|'binpack',
                            'field': 'string'
                        },
                    ],
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'healthCheckGracePeriodSeconds': 123,
                    'schedulingStrategy': 'REPLICA'|'DAEMON',
                    'deploymentController': {
                        'type': 'ECS'|'CODE_DEPLOY'|'EXTERNAL'
                    },
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'createdBy': 'string',
                    'enableECSManagedTags': True|False,
                    'propagateTags': 'TASK_DEFINITION'|'SERVICE'
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **service** *(dict) --* 
              The full description of your service following the update call.
              - **serviceArn** *(string) --* 
                The ARN that identifies the service. The ARN contains the ``arn:aws:ecs`` namespace, followed by the Region of the service, the AWS account ID of the service owner, the ``service`` namespace, and then the service name. For example, ``arn:aws:ecs:*region* :*012345678910* :service/*my-service* `` .
              - **serviceName** *(string) --* 
                The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that hosts the service.
              - **loadBalancers** *(list) --* 
                A list of Elastic Load Balancing load balancer objects, containing the load balancer name, the container name (as it appears in a container definition), and the container port to access from the load balancer.
                Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this service. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **status** *(string) --* 
                The status of the service. The valid values are ``ACTIVE`` , ``DRAINING`` , or ``INACTIVE`` .
              - **desiredCount** *(integer) --* 
                The desired number of instantiations of the task definition to keep running on the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **runningCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``RUNNING`` state.
              - **pendingCount** *(integer) --* 
                The number of tasks in the cluster that are in the ``PENDING`` state.
              - **launchType** *(string) --* 
                The launch type on which your service is running. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **taskDefinition** *(string) --* 
                The task definition to use for tasks in the service. This value is specified when the service is created with  CreateService , and it can be modified with  UpdateService .
              - **deploymentConfiguration** *(dict) --* 
                Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
                - **maximumPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
                - **minimumHealthyPercent** *(integer) --* 
                  If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
                  If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
              - **taskSets** *(list) --* 
                Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                - *(dict) --* 
                  Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
                  - **id** *(string) --* 
                    The ID of the task set.
                  - **taskSetArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the task set.
                  - **serviceArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service the task set exists in.
                  - **clusterArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
                  - **startedBy** *(string) --* 
                    The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
                  - **externalId** *(string) --* 
                    The external ID associated with the task set.
                    If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                    If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
                  - **status** *(string) --* 
                    The status of the task set. The following describes each state:
                      PRIMARY  
                    The task set is serving production traffic.
                      ACTIVE  
                    The task set is not serving production traffic.
                      DRAINING  
                    The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
                  - **taskDefinition** *(string) --* 
                    The task definition the task set is using.
                  - **computedDesiredCount** *(integer) --* 
                    The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the task set was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the task set was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The network configuration for the task set.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
                  - **loadBalancers** *(list) --* 
                    Details on a load balancer that is used with a task set.
                    - *(dict) --* 
                      Details on a load balancer that is used with a service.
                      If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                      If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                      Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **targetGroupArn** *(string) --* 
                        The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                        .. warning::
                          If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                      - **loadBalancerName** *(string) --* 
                        The name of a load balancer.
                      - **containerName** *(string) --* 
                        The name of the container (as it appears in a container definition) to associate with the load balancer.
                      - **containerPort** *(integer) --* 
                        The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
                  - **serviceRegistries** *(list) --* 
                    The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                    - *(dict) --* 
                      Details of the service registry.
                      - **registryArn** *(string) --* 
                        The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                      - **port** *(integer) --* 
                        The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                      - **containerName** *(string) --* 
                        The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                      - **containerPort** *(integer) --* 
                        The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **scale** *(dict) --* 
                    A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                    - **value** *(float) --* 
                      The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                    - **unit** *(string) --* 
                      The unit of measure for the scale value.
                  - **stabilityStatus** *(string) --* 
                    The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                    * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                    * The ``pendingCount`` is ``0`` . 
                    * There are no tasks running on container instances in the ``DRAINING`` status. 
                    * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                    If any of those conditions are not met, the stability status returns ``STABILIZING`` .
                  - **stabilityStatusAt** *(datetime) --* 
                    The Unix timestamp for when the task set stability status was retrieved.
              - **deployments** *(list) --* 
                The current state of deployments for the service.
                - *(dict) --* 
                  The details of an Amazon ECS service deployment. This is used only when a service uses the ``ECS`` deployment controller type.
                  - **id** *(string) --* 
                    The ID of the deployment.
                  - **status** *(string) --* 
                    The status of the deployment. The following describes each state:
                      PRIMARY  
                    The most recent deployment of a service.
                      ACTIVE  
                    A service deployment that still has running tasks, but are in the process of being replaced with a new ``PRIMARY`` deployment.
                      INACTIVE  
                    A deployment that has been completely replaced.
                  - **taskDefinition** *(string) --* 
                    The most recent task definition that was specified for the tasks in the service to use.
                  - **desiredCount** *(integer) --* 
                    The most recent desired count of tasks that was specified for the service to deploy or maintain.
                  - **pendingCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``PENDING`` status.
                  - **runningCount** *(integer) --* 
                    The number of tasks in the deployment that are in the ``RUNNING`` status.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was created.
                  - **updatedAt** *(datetime) --* 
                    The Unix timestamp for when the service deployment was last updated.
                  - **launchType** *(string) --* 
                    The launch type the tasks in the service are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **platformVersion** *(string) --* 
                    The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **networkConfiguration** *(dict) --* 
                    The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                    - **awsvpcConfiguration** *(dict) --* 
                      The VPC subnets and security groups associated with a task.
                      .. note::
                        All specified subnets and security groups must be from the same VPC.
                      - **subnets** *(list) --* 
                        The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified subnets must be from the same VPC.
                        - *(string) --* 
                      - **securityGroups** *(list) --* 
                        The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                        .. note::
                          All specified security groups must be from the same VPC.
                        - *(string) --* 
                      - **assignPublicIp** *(string) --* 
                        Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **roleArn** *(string) --* 
                The ARN of the IAM role associated with the service that allows the Amazon ECS container agent to register container instances with an Elastic Load Balancing load balancer.
              - **events** *(list) --* 
                The event stream for your service. A maximum of 100 of the latest events are displayed.
                - *(dict) --* 
                  Details on an event associated with a service.
                  - **id** *(string) --* 
                    The ID string of the event.
                  - **createdAt** *(datetime) --* 
                    The Unix timestamp for when the event was triggered.
                  - **message** *(string) --* 
                    The event message.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the service was created.
              - **placementConstraints** *(list) --* 
                The placement constraints for the tasks in the service.
                - *(dict) --* 
                  An object representing a constraint on task placement. For more information, see `Task Placement Constraints <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates. The value ``distinctInstance`` is not supported in task definitions.
                  - **expression** *(string) --* 
                    A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster Query Language <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **placementStrategy** *(list) --* 
                The placement strategy that determines how tasks for the service are placed.
                - *(dict) --* 
                  The task placement strategy for a task or service. For more information, see `Task Placement Strategies <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
                  - **type** *(string) --* 
                    The type of placement strategy. The ``random`` placement strategy randomly places tasks on available candidates. The ``spread`` placement strategy spreads placement across available candidates evenly based on the ``field`` parameter. The ``binpack`` strategy places tasks on available candidates that have the least available amount of the resource that is specified with the ``field`` parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
                  - **field** *(string) --* 
                    The field to apply the placement strategy against. For the ``spread`` placement strategy, valid values are ``instanceId`` (or ``host`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the ``binpack`` placement strategy, valid values are ``cpu`` and ``memory`` . For the ``random`` placement strategy, this field is not used.
              - **networkConfiguration** *(dict) --* 
                The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the ``awsvpc`` networking mode.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **healthCheckGracePeriodSeconds** *(integer) --* 
                The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.
              - **schedulingStrategy** *(string) --* 
                The scheduling strategy to use for the service. For more information, see `Services <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html>`__ .
                There are two service scheduler strategies available:
                * ``REPLICA`` -The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. 
                * ``DAEMON`` -The daemon scheduling strategy deploys exactly one task on each container instance in your cluster. When you are using this strategy, do not specify a desired number of tasks or any task placement strategies. 
                .. note::
                   Fargate tasks do not support the ``DAEMON`` scheduling strategy. 
              - **deploymentController** *(dict) --* 
                The deployment controller type the service is using.
                - **type** *(string) --* 
                  The deployment controller type to use.
                  There are three deployment controller types available:
                    ECS  
                  The rolling update (``ECS`` ) deployment type involves replacing the current running version of the container with the latest version. The number of containers Amazon ECS adds or removes from the service during a rolling update is controlled by adjusting the minimum and maximum number of healthy tasks allowed during a service deployment, as specified in the  DeploymentConfiguration .
                    CODE_DEPLOY  
                  The blue/green (``CODE_DEPLOY`` ) deployment type uses the blue/green deployment model powered by AWS CodeDeploy, which allows you to verify a new deployment of a service before sending production traffic to it.
                    EXTERNAL  
                  The external (``EXTERNAL`` ) deployment type enables you to use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
              - **tags** *(list) --* 
                The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                - *(dict) --* 
                  The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
                  - **key** *(string) --* 
                    One part of a key-value pair that make up a tag. A ``key`` is a general label that acts like a category for more specific tag values.
                  - **value** *(string) --* 
                    The optional part of a key-value pair that make up a tag. A ``value`` acts as a descriptor within a tag category (key).
              - **createdBy** *(string) --* 
                The principal that created the service.
              - **enableECSManagedTags** *(boolean) --* 
                Specifies whether to enable Amazon ECS managed tags for the tasks in the service. For more information, see `Tagging Your Amazon ECS Resources <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **propagateTags** *(string) --* 
                Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags are not propagated.
        :type cluster: string
        :param cluster:
          The short name or full Amazon Resource Name (ARN) of the cluster that your service is running on. If you do not specify a cluster, the default cluster is assumed.
        :type service: string
        :param service: **[REQUIRED]**
          The name of the service to update.
        :type desiredCount: integer
        :param desiredCount:
          The number of instantiations of the task to place and keep running in your service.
        :type taskDefinition: string
        :param taskDefinition:
          The ``family`` and ``revision`` (``family:revision`` ) or full ARN of the task definition to run in your service. If a ``revision`` is not specified, the latest ``ACTIVE`` revision is used. If you modify the task definition with ``UpdateService`` , Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.
        :type deploymentConfiguration: dict
        :param deploymentConfiguration:
          Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
          - **maximumPercent** *(integer) --*
            If a service is using the rolling update (``ECS`` ) deployment type, the **maximum percent** parameter represents an upper limit on the number of tasks in a service that are allowed in the ``RUNNING`` or ``PENDING`` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.
            If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **maximum percent** value is set to the default value and is used to define the upper limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the maximum percent value is not used, although it is returned when describing your service.
          - **minimumHealthyPercent** *(integer) --*
            If a service is using the rolling update (``ECS`` ) deployment type, the **minimum healthy percent** represents a lower limit on the number of tasks in a service that must remain in the ``RUNNING`` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer), and while any container instances are in the ``DRAINING`` state if the service contains tasks using the EC2 launch type. This parameter enables you to deploy without using additional cluster capacity. For example, if your service has a desired number of four tasks and a minimum healthy percent of 50%, the scheduler may stop two existing tasks to free up cluster capacity before starting two new tasks. Tasks for services that *do not* use a load balancer are considered healthy if they are in the ``RUNNING`` state; tasks for services that *do* use a load balancer are considered healthy if they are in the ``RUNNING`` state and they are reported as healthy by the load balancer. The default value for minimum healthy percent is 100%.
            If a service is using the blue/green (``CODE_DEPLOY`` ) or ``EXTERNAL`` deployment types and tasks that use the EC2 launch type, the **minimum healthy percent** value is set to the default value and is used to define the lower limit on the number of the tasks in the service that remain in the ``RUNNING`` state while the container instances are in the ``DRAINING`` state. If the tasks in the service use the Fargate launch type, the minimum healthy percent value is not used, although it is returned when describing your service.
        :type networkConfiguration: dict
        :param networkConfiguration:
          The network configuration for the service. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see `Task Networking <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
          .. note::
            Updating a service to add a subnet to a list of existing subnets does not trigger a service deployment. For example, if your network configuration change is to keep the existing subnets and simply add another subnet to the network configuration, this does not trigger a new service deployment.
          - **awsvpcConfiguration** *(dict) --*
            The VPC subnets and security groups associated with a task.
            .. note::
              All specified subnets and security groups must be from the same VPC.
            - **subnets** *(list) --* **[REQUIRED]**
              The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified subnets must be from the same VPC.
              - *(string) --*
            - **securityGroups** *(list) --*
              The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
              .. note::
                All specified security groups must be from the same VPC.
              - *(string) --*
            - **assignPublicIp** *(string) --*
              Whether the task\'s elastic network interface receives a public IP address. The default value is ``DISABLED`` .
        :type platformVersion: string
        :param platformVersion:
          The platform version on which your tasks in the service are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        :type forceNewDeployment: boolean
        :param forceNewDeployment:
          Whether to force a new deployment of the service. Deployments are not forced by default. You can use this option to trigger a new deployment with no service definition changes. For example, you can update a service\'s tasks to use a newer Docker image with the same image/tag combination (``my_image:latest`` ) or to roll Fargate tasks onto a newer platform version.
        :type healthCheckGracePeriodSeconds: integer
        :param healthCheckGracePeriodSeconds:
          The period of time, in seconds, that the Amazon ECS service scheduler should ignore unhealthy Elastic Load Balancing target health checks after a task has first started. This is only valid if your service is configured to use a load balancer. If your service\'s tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 1,800 seconds. During that time, the ECS service scheduler ignores the Elastic Load Balancing health check status. This grace period can prevent the ECS service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.
        :rtype: dict
        :returns:
        """
        pass

    def update_service_primary_task_set(self, cluster: str, service: str, primaryTaskSet: str) -> Dict:
        """
        Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the ``EXTERNAL`` deployment controller type. For more information, see `Amazon ECS Deployment Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateServicePrimaryTaskSet>`_
        
        **Request Syntax**
        ::
          response = client.update_service_primary_task_set(
              cluster='string',
              service='string',
              primaryTaskSet='string'
          )
        
        **Response Syntax**
        ::
            {
                'taskSet': {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'serviceArn': 'string',
                    'clusterArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskSet** *(dict) --* 
              Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
              - **id** *(string) --* 
                The ID of the task set.
              - **taskSetArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task set.
              - **serviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the service the task set exists in.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
              - **startedBy** *(string) --* 
                The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
              - **externalId** *(string) --* 
                The external ID associated with the task set.
                If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
              - **status** *(string) --* 
                The status of the task set. The following describes each state:
                  PRIMARY  
                The task set is serving production traffic.
                  ACTIVE  
                The task set is not serving production traffic.
                  DRAINING  
                The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
              - **taskDefinition** *(string) --* 
                The task definition the task set is using.
              - **computedDesiredCount** *(integer) --* 
                The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
              - **pendingCount** *(integer) --* 
                The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
              - **runningCount** *(integer) --* 
                The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the task set was created.
              - **updatedAt** *(datetime) --* 
                The Unix timestamp for when the task set was last updated.
              - **launchType** *(string) --* 
                The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **networkConfiguration** *(dict) --* 
                The network configuration for the task set.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **loadBalancers** *(list) --* 
                Details on a load balancer that is used with a task set.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **scale** *(dict) --* 
                A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                - **value** *(float) --* 
                  The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                - **unit** *(string) --* 
                  The unit of measure for the scale value.
              - **stabilityStatus** *(string) --* 
                The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                * The ``pendingCount`` is ``0`` . 
                * There are no tasks running on container instances in the ``DRAINING`` status. 
                * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                If any of those conditions are not met, the stability status returns ``STABILIZING`` .
              - **stabilityStatusAt** *(datetime) --* 
                The Unix timestamp for when the task set stability status was retrieved.
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.
        :type service: string
        :param service: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.
        :type primaryTaskSet: string
        :param primaryTaskSet: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.
        :rtype: dict
        :returns:
        """
        pass

    def update_task_set(self, cluster: str, service: str, taskSet: str, scale: Dict) -> Dict:
        """
        Modifies a task set. This is used when a service uses the ``EXTERNAL`` deployment controller type. For more information, see `Amazon ECS Deployment Types <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/UpdateTaskSet>`_
        
        **Request Syntax**
        ::
          response = client.update_task_set(
              cluster='string',
              service='string',
              taskSet='string',
              scale={
                  'value': 123.0,
                  'unit': 'PERCENT'
              }
          )
        
        **Response Syntax**
        ::
            {
                'taskSet': {
                    'id': 'string',
                    'taskSetArn': 'string',
                    'serviceArn': 'string',
                    'clusterArn': 'string',
                    'startedBy': 'string',
                    'externalId': 'string',
                    'status': 'string',
                    'taskDefinition': 'string',
                    'computedDesiredCount': 123,
                    'pendingCount': 123,
                    'runningCount': 123,
                    'createdAt': datetime(2015, 1, 1),
                    'updatedAt': datetime(2015, 1, 1),
                    'launchType': 'EC2'|'FARGATE',
                    'platformVersion': 'string',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'subnets': [
                                'string',
                            ],
                            'securityGroups': [
                                'string',
                            ],
                            'assignPublicIp': 'ENABLED'|'DISABLED'
                        }
                    },
                    'loadBalancers': [
                        {
                            'targetGroupArn': 'string',
                            'loadBalancerName': 'string',
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'serviceRegistries': [
                        {
                            'registryArn': 'string',
                            'port': 123,
                            'containerName': 'string',
                            'containerPort': 123
                        },
                    ],
                    'scale': {
                        'value': 123.0,
                        'unit': 'PERCENT'
                    },
                    'stabilityStatus': 'STEADY_STATE'|'STABILIZING',
                    'stabilityStatusAt': datetime(2015, 1, 1)
                }
            }
        
        **Response Structure**
          - *(dict) --* 
            - **taskSet** *(dict) --* 
              Information about a set of Amazon ECS tasks in either an AWS CodeDeploy or an ``EXTERNAL`` deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic.
              - **id** *(string) --* 
                The ID of the task set.
              - **taskSetArn** *(string) --* 
                The Amazon Resource Name (ARN) of the task set.
              - **serviceArn** *(string) --* 
                The Amazon Resource Name (ARN) of the service the task set exists in.
              - **clusterArn** *(string) --* 
                The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.
              - **startedBy** *(string) --* 
                The tag specified when a task set is started. If the task set is created by an AWS CodeDeploy deployment, the ``startedBy`` parameter is ``CODE_DEPLOY`` . For a task set created for an external deployment, the startedBy field isn't used.
              - **externalId** *(string) --* 
                The external ID associated with the task set.
                If a task set is created by an AWS CodeDeploy deployment, the ``externalId`` parameter contains the AWS CodeDeploy deployment ID.
                If a task set is created for an external deployment and is associated with a service discovery registry, the ``externalId`` parameter contains the ``ECS_TASK_SET_EXTERNAL_ID`` AWS Cloud Map attribute.
              - **status** *(string) --* 
                The status of the task set. The following describes each state:
                  PRIMARY  
                The task set is serving production traffic.
                  ACTIVE  
                The task set is not serving production traffic.
                  DRAINING  
                The tasks in the task set are being stopped and their corresponding targets are being deregistered from their target group.
              - **taskDefinition** *(string) --* 
                The task definition the task set is using.
              - **computedDesiredCount** *(integer) --* 
                The computed desired count for the task set. This is calculated by multiplying the service's ``desiredCount`` by the task set's ``scale`` percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.
              - **pendingCount** *(integer) --* 
                The number of tasks in the task set that are in the ``PENDING`` status during a deployment. A task in the ``PENDING`` state is preparing to enter the ``RUNNING`` state. A task set enters the ``PENDING`` status when it launches for the first time or when it is restarted after being in the ``STOPPED`` state.
              - **runningCount** *(integer) --* 
                The number of tasks in the task set that are in the ``RUNNING`` status during a deployment. A task in the ``RUNNING`` state is running and ready for use.
              - **createdAt** *(datetime) --* 
                The Unix timestamp for when the task set was created.
              - **updatedAt** *(datetime) --* 
                The Unix timestamp for when the task set was last updated.
              - **launchType** *(string) --* 
                The launch type the tasks in the task set are using. For more information, see `Amazon ECS Launch Types <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **platformVersion** *(string) --* 
                The platform version on which the tasks in the task set are running. A platform version is only specified for tasks using the Fargate launch type. If one is not specified, the ``LATEST`` platform version is used by default. For more information, see `AWS Fargate Platform Versions <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html>`__ in the *Amazon Elastic Container Service Developer Guide* .
              - **networkConfiguration** *(dict) --* 
                The network configuration for the task set.
                - **awsvpcConfiguration** *(dict) --* 
                  The VPC subnets and security groups associated with a task.
                  .. note::
                    All specified subnets and security groups must be from the same VPC.
                  - **subnets** *(list) --* 
                    The subnets associated with the task or service. There is a limit of 16 subnets that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified subnets must be from the same VPC.
                    - *(string) --* 
                  - **securityGroups** *(list) --* 
                    The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used. There is a limit of 5 security groups that can be specified per ``AwsVpcConfiguration`` .
                    .. note::
                      All specified security groups must be from the same VPC.
                    - *(string) --* 
                  - **assignPublicIp** *(string) --* 
                    Whether the task's elastic network interface receives a public IP address. The default value is ``DISABLED`` .
              - **loadBalancers** *(list) --* 
                Details on a load balancer that is used with a task set.
                - *(dict) --* 
                  Details on a load balancer that is used with a service.
                  If the service is using the ``ECS`` deployment controller, you are limited to one load balancer or target group.
                  If the service is using the ``CODE_DEPLOY`` deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When you are creating an AWS CodeDeploy deployment group, you specify two target groups (referred to as a ``targetGroupPair`` ). Each target group binds to a separate task set in the deployment. The load balancer can also have up to two listeners, a required listener for production traffic and an optional listener that allows you to test new revisions of the service before routing production traffic to it.
                  Services with tasks that use the ``awsvpc`` network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers are not supported. Also, when you create any target groups for these services, you must choose ``ip`` as the target type, not ``instance`` . Tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **targetGroupArn** *(string) --* 
                    The full Amazon Resource Name (ARN) of the Elastic Load Balancing target group or groups associated with a service. For services using the ``ECS`` deployment controller, you are limited to one target group. For services using the ``CODE_DEPLOY`` deployment controller, you are required to define two target groups for the load balancer.
                    .. warning::
                      If your service's task definition uses the ``awsvpc`` network mode (which is required for the Fargate launch type), you must choose ``ip`` as the target type, not ``instance`` , because tasks that use the ``awsvpc`` network mode are associated with an elastic network interface, not an Amazon EC2 instance.
                  - **loadBalancerName** *(string) --* 
                    The name of a load balancer.
                  - **containerName** *(string) --* 
                    The name of the container (as it appears in a container definition) to associate with the load balancer.
                  - **containerPort** *(integer) --* 
                    The port on the container to associate with the load balancer. This port must correspond to a ``containerPort`` in the service's task definition. Your container instances must allow ingress traffic on the ``hostPort`` of the port mapping.
              - **serviceRegistries** *(list) --* 
                The details of the service discovery registries to assign to this task set. For more information, see `Service Discovery <http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html>`__ .
                - *(dict) --* 
                  Details of the service registry.
                  - **registryArn** *(string) --* 
                    The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is AWS Cloud Map. For more information, see `CreateService <https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html>`__ .
                  - **port** *(integer) --* 
                    The port value used if your service discovery service specified an SRV record. This field may be used if both the ``awsvpc`` network mode and SRV records are used.
                  - **containerName** *(string) --* 
                    The container name value, already specified in the task definition, to be used for your service discovery service. If the task definition that your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition that your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
                  - **containerPort** *(integer) --* 
                    The port value, already specified in the task definition, to be used for your service discovery service. If the task definition your service task specifies uses the ``bridge`` or ``host`` network mode, you must specify a ``containerName`` and ``containerPort`` combination from the task definition. If the task definition your service task specifies uses the ``awsvpc`` network mode and a type SRV DNS record is used, you must specify either a ``containerName`` and ``containerPort`` combination or a ``port`` value, but not both.
              - **scale** *(dict) --* 
                A floating-point percentage of the desired number of tasks to place and keep running in the task set.
                - **value** *(float) --* 
                  The value, specified as a percent total of a service's ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
                - **unit** *(string) --* 
                  The unit of measure for the scale value.
              - **stabilityStatus** *(string) --* 
                The stability status, which indicates whether the task set has reached a steady state. If the following conditions are met, the task set will be in ``STEADY_STATE`` :
                * The task ``runningCount`` is equal to the ``computedDesiredCount`` . 
                * The ``pendingCount`` is ``0`` . 
                * There are no tasks running on container instances in the ``DRAINING`` status. 
                * All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks. 
                If any of those conditions are not met, the stability status returns ``STABILIZING`` .
              - **stabilityStatusAt** *(datetime) --* 
                The Unix timestamp for when the task set stability status was retrieved.
        :type cluster: string
        :param cluster: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.
        :type service: string
        :param service: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.
        :type taskSet: string
        :param taskSet: **[REQUIRED]**
          The short name or full Amazon Resource Name (ARN) of the task set to update.
        :type scale: dict
        :param scale: **[REQUIRED]**
          A floating-point percentage of the desired number of tasks to place and keep running in the task set.
          - **value** *(float) --*
            The value, specified as a percent total of a service\'s ``desiredCount`` , to scale the task set. Accepted values are numbers between 0 and 100.
          - **unit** *(string) --*
            The unit of measure for the scale value.
        :rtype: dict
        :returns:
        """
        pass
