from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import Union
from typing import List


class Client(BaseClient):
    def associate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        """
        Associates the specified IP access control group with the specified directory.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/AssociateIpGroups>`_
        
        **Request Syntax**
        ::
          response = client.associate_ip_groups(
              DirectoryId='string',
              GroupIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]**
          The identifier of the directory.
        :type GroupIds: list
        :param GroupIds: **[REQUIRED]**
          The identifiers of one or more IP access control groups.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def authorize_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        """
        Adds one or more rules to the specified IP access control group.
        This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/AuthorizeIpRules>`_
        
        **Request Syntax**
        ::
          response = client.authorize_ip_rules(
              GroupId='string',
              UserRules=[
                  {
                      'ipRule': 'string',
                      'ruleDesc': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type GroupId: string
        :param GroupId: **[REQUIRED]**
          The identifier of the group.
        :type UserRules: list
        :param UserRules: **[REQUIRED]**
          The rules to add to the group.
          - *(dict) --*
            Describes a rule for an IP access control group.
            - **ipRule** *(string) --*
              The IP address range, in CIDR notation.
            - **ruleDesc** *(string) --*
              The description.
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

    def create_ip_group(self, GroupName: str, GroupDesc: str = None, UserRules: List = None, Tags: List = None) -> Dict:
        """
        Creates an IP access control group.
        An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using  AuthorizeIpRules .
        There is a default IP access control group associated with your directory. If you don't associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateIpGroup>`_
        
        **Request Syntax**
        ::
          response = client.create_ip_group(
              GroupName='string',
              GroupDesc='string',
              UserRules=[
                  {
                      'ipRule': 'string',
                      'ruleDesc': 'string'
                  },
              ],
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'GroupId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **GroupId** *(string) --* 
              The identifier of the group.
        :type GroupName: string
        :param GroupName: **[REQUIRED]**
          The name of the group.
        :type GroupDesc: string
        :param GroupDesc:
          The description of the group.
        :type UserRules: list
        :param UserRules:
          The rules to add to the group.
          - *(dict) --*
            Describes a rule for an IP access control group.
            - **ipRule** *(string) --*
              The IP address range, in CIDR notation.
            - **ruleDesc** *(string) --*
              The description.
        :type Tags: list
        :param Tags:
          The tags. Each WorkSpaces resource can have a maximum of 50 tags.
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The key of the tag.
            - **Value** *(string) --*
              The value of the tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_tags(self, ResourceId: str, Tags: List) -> Dict:
        """
        Creates the specified tags for the specified WorkSpaces resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateTags>`_
        
        **Request Syntax**
        ::
          response = client.create_tags(
              ResourceId='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.
        :type Tags: list
        :param Tags: **[REQUIRED]**
          The tags. Each WorkSpaces resource can have a maximum of 50 tags.
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The key of the tag.
            - **Value** *(string) --*
              The value of the tag.
        :rtype: dict
        :returns:
        """
        pass

    def create_workspaces(self, Workspaces: List) -> Dict:
        """
        Creates one or more WorkSpaces.
        This operation is asynchronous and returns before the WorkSpaces are created.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/CreateWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.create_workspaces(
              Workspaces=[
                  {
                      'DirectoryId': 'string',
                      'UserName': 'string',
                      'BundleId': 'string',
                      'VolumeEncryptionKey': 'string',
                      'UserVolumeEncryptionEnabled': True|False,
                      'RootVolumeEncryptionEnabled': True|False,
                      'WorkspaceProperties': {
                          'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                          'RunningModeAutoStopTimeoutInMinutes': 123,
                          'RootVolumeSizeGib': 123,
                          'UserVolumeSizeGib': 123,
                          'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                      },
                      'Tags': [
                          {
                              'Key': 'string',
                              'Value': 'string'
                          },
                      ]
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceRequest': {
                            'DirectoryId': 'string',
                            'UserName': 'string',
                            'BundleId': 'string',
                            'VolumeEncryptionKey': 'string',
                            'UserVolumeEncryptionEnabled': True|False,
                            'RootVolumeEncryptionEnabled': True|False,
                            'WorkspaceProperties': {
                                'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                                'RunningModeAutoStopTimeoutInMinutes': 123,
                                'RootVolumeSizeGib': 123,
                                'UserVolumeSizeGib': 123,
                                'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                            },
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ],
                'PendingRequests': [
                    {
                        'WorkspaceId': 'string',
                        'DirectoryId': 'string',
                        'UserName': 'string',
                        'IpAddress': 'string',
                        'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                        'BundleId': 'string',
                        'SubnetId': 'string',
                        'ErrorMessage': 'string',
                        'ErrorCode': 'string',
                        'ComputerName': 'string',
                        'VolumeEncryptionKey': 'string',
                        'UserVolumeEncryptionEnabled': True|False,
                        'RootVolumeEncryptionEnabled': True|False,
                        'WorkspaceProperties': {
                            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                            'RunningModeAutoStopTimeoutInMinutes': 123,
                            'RootVolumeSizeGib': 123,
                            'UserVolumeSizeGib': 123,
                            'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                        },
                        'ModificationStates': [
                            {
                                'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                                'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                            },
                        ]
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpaces that could not be created.
              - *(dict) --* 
                Describes a WorkSpace that cannot be created.
                - **WorkspaceRequest** *(dict) --* 
                  Information about the WorkSpace.
                  - **DirectoryId** *(string) --* 
                    The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.
                  - **UserName** *(string) --* 
                    The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
                  - **BundleId** *(string) --* 
                    The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.
                  - **VolumeEncryptionKey** *(string) --* 
                    The KMS key used to encrypt data stored on your WorkSpace.
                  - **UserVolumeEncryptionEnabled** *(boolean) --* 
                    Indicates whether the data stored on the user volume is encrypted.
                  - **RootVolumeEncryptionEnabled** *(boolean) --* 
                    Indicates whether the data stored on the root volume is encrypted.
                  - **WorkspaceProperties** *(dict) --* 
                    The WorkSpace properties.
                    - **RunningMode** *(string) --* 
                      The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
                    - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 
                      The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
                    - **RootVolumeSizeGib** *(integer) --* 
                      The size of the root volume.
                    - **UserVolumeSizeGib** *(integer) --* 
                      The size of the user storage.
                    - **ComputeTypeName** *(string) --* 
                      The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
                  - **Tags** *(list) --* 
                    The tags for the WorkSpace.
                    - *(dict) --* 
                      Describes a tag.
                      - **Key** *(string) --* 
                        The key of the tag.
                      - **Value** *(string) --* 
                        The value of the tag.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be created.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be created.
            - **PendingRequests** *(list) --* 
              Information about the WorkSpaces that were created.
              Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call  DescribeWorkspaces before the WorkSpace is created, the information returned can be incomplete.
              - *(dict) --* 
                Describes a WorkSpace.
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **DirectoryId** *(string) --* 
                  The identifier of the AWS Directory Service directory for the WorkSpace.
                - **UserName** *(string) --* 
                  The user for the WorkSpace.
                - **IpAddress** *(string) --* 
                  The IP address of the WorkSpace.
                - **State** *(string) --* 
                  The operational state of the WorkSpace.
                - **BundleId** *(string) --* 
                  The identifier of the bundle used to create the WorkSpace.
                - **SubnetId** *(string) --* 
                  The identifier of the subnet for the WorkSpace.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be created.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be created.
                - **ComputerName** *(string) --* 
                  The name of the WorkSpace, as seen by the operating system.
                - **VolumeEncryptionKey** *(string) --* 
                  The KMS key used to encrypt data stored on your WorkSpace.
                - **UserVolumeEncryptionEnabled** *(boolean) --* 
                  Indicates whether the data stored on the user volume is encrypted.
                - **RootVolumeEncryptionEnabled** *(boolean) --* 
                  Indicates whether the data stored on the root volume is encrypted.
                - **WorkspaceProperties** *(dict) --* 
                  The properties of the WorkSpace.
                  - **RunningMode** *(string) --* 
                    The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
                  - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 
                    The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
                  - **RootVolumeSizeGib** *(integer) --* 
                    The size of the root volume.
                  - **UserVolumeSizeGib** *(integer) --* 
                    The size of the user storage.
                  - **ComputeTypeName** *(string) --* 
                    The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
                - **ModificationStates** *(list) --* 
                  The modification states of the WorkSpace.
                  - *(dict) --* 
                    Describes a WorkSpace modification.
                    - **Resource** *(string) --* 
                      The resource.
                    - **State** *(string) --* 
                      The modification state.
        :type Workspaces: list
        :param Workspaces: **[REQUIRED]**
          The WorkSpaces to create. You can specify up to 25 WorkSpaces.
          - *(dict) --*
            Describes the information used to create a WorkSpace.
            - **DirectoryId** *(string) --* **[REQUIRED]**
              The identifier of the AWS Directory Service directory for the WorkSpace. You can use  DescribeWorkspaceDirectories to list the available directories.
            - **UserName** *(string) --* **[REQUIRED]**
              The username of the user for the WorkSpace. This username must exist in the AWS Directory Service directory for the WorkSpace.
            - **BundleId** *(string) --* **[REQUIRED]**
              The identifier of the bundle for the WorkSpace. You can use  DescribeWorkspaceBundles to list the available bundles.
            - **VolumeEncryptionKey** *(string) --*
              The KMS key used to encrypt data stored on your WorkSpace.
            - **UserVolumeEncryptionEnabled** *(boolean) --*
              Indicates whether the data stored on the user volume is encrypted.
            - **RootVolumeEncryptionEnabled** *(boolean) --*
              Indicates whether the data stored on the root volume is encrypted.
            - **WorkspaceProperties** *(dict) --*
              The WorkSpace properties.
              - **RunningMode** *(string) --*
                The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
              - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*
                The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
              - **RootVolumeSizeGib** *(integer) --*
                The size of the root volume.
              - **UserVolumeSizeGib** *(integer) --*
                The size of the user storage.
              - **ComputeTypeName** *(string) --*
                The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
            - **Tags** *(list) --*
              The tags for the WorkSpace.
              - *(dict) --*
                Describes a tag.
                - **Key** *(string) --* **[REQUIRED]**
                  The key of the tag.
                - **Value** *(string) --*
                  The value of the tag.
        :rtype: dict
        :returns:
        """
        pass

    def delete_ip_group(self, GroupId: str) -> Dict:
        """
        Deletes the specified IP access control group.
        You cannot delete an IP access control group that is associated with a directory.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteIpGroup>`_
        
        **Request Syntax**
        ::
          response = client.delete_ip_group(
              GroupId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type GroupId: string
        :param GroupId: **[REQUIRED]**
          The identifier of the IP access control group.
        :rtype: dict
        :returns:
        """
        pass

    def delete_tags(self, ResourceId: str, TagKeys: List) -> Dict:
        """
        Deletes the specified tags from the specified WorkSpaces resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteTags>`_
        
        **Request Syntax**
        ::
          response = client.delete_tags(
              ResourceId='string',
              TagKeys=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.
        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**
          The tag keys.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def delete_workspace_image(self, ImageId: str) -> Dict:
        """
        Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DeleteWorkspaceImage>`_
        
        **Request Syntax**
        ::
          response = client.delete_workspace_image(
              ImageId='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ImageId: string
        :param ImageId: **[REQUIRED]**
          The identifier of the image.
        :rtype: dict
        :returns:
        """
        pass

    def describe_account(self) -> Dict:
        """
        Retrieves a list that describes the configuration of bring your own license (BYOL) for the specified account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeAccount>`_
        
        **Request Syntax**
        ::
          response = client.describe_account()
        
        **Response Syntax**
        ::
            {
                'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
                'DedicatedTenancyManagementCidrRange': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **DedicatedTenancySupport** *(string) --* 
              The status of BYOL (whether BYOL is enabled or disabled).
            - **DedicatedTenancyManagementCidrRange** *(string) --* 
              The IP address range, specified as an IPv4 CIDR block, used for the management network interface.
              The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
        :rtype: dict
        :returns:
        """
        pass

    def describe_account_modifications(self, NextToken: str = None) -> Dict:
        """
        Retrieves a list that describes modifications to the configuration of bring your own license (BYOL) for the specified account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeAccountModifications>`_
        
        **Request Syntax**
        ::
          response = client.describe_account_modifications(
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'AccountModifications': [
                    {
                        'ModificationState': 'PENDING'|'COMPLETED'|'FAILED',
                        'DedicatedTenancySupport': 'ENABLED'|'DISABLED',
                        'DedicatedTenancyManagementCidrRange': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **AccountModifications** *(list) --* 
              The list of modifications to the configuration of BYOL.
              - *(dict) --* 
                Describes a modification to the configuration of bring your own license (BYOL) for the specified account. 
                - **ModificationState** *(string) --* 
                  The state of the modification to the configuration of BYOL.
                - **DedicatedTenancySupport** *(string) --* 
                  The status of BYOL (whether BYOL is being enabled or disabled).
                - **DedicatedTenancyManagementCidrRange** *(string) --* 
                  The IP address range, specified as an IPv4 CIDR block, for the management network interface used for the account.
                - **StartTime** *(datetime) --* 
                  The timestamp when the modification of the BYOL configuration was started.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the configuration of BYOL cannot be modified.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the configuration of BYOL cannot be modified.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def describe_client_properties(self, ResourceIds: List) -> Dict:
        """
        Retrieves a list that describes one or more specified Amazon WorkSpaces clients.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeClientProperties>`_
        
        **Request Syntax**
        ::
          response = client.describe_client_properties(
              ResourceIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ClientPropertiesList': [
                    {
                        'ResourceId': 'string',
                        'ClientProperties': {
                            'ReconnectEnabled': 'ENABLED'|'DISABLED'
                        }
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ClientPropertiesList** *(list) --* 
              Information about the specified Amazon WorkSpaces clients.
              - *(dict) --* 
                Information about the Amazon WorkSpaces client.
                - **ResourceId** *(string) --* 
                  The resource identifier, in the form of a directory ID.
                - **ClientProperties** *(dict) --* 
                  Information about the Amazon WorkSpaces client.
                  - **ReconnectEnabled** *(string) --* 
                    Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials. 
        :type ResourceIds: list
        :param ResourceIds: **[REQUIRED]**
          The resource identifier, in the form of directory IDs.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def describe_ip_groups(self, GroupIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Describes one or more of your IP access control groups.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeIpGroups>`_
        
        **Request Syntax**
        ::
          response = client.describe_ip_groups(
              GroupIds=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Result': [
                    {
                        'groupId': 'string',
                        'groupName': 'string',
                        'groupDesc': 'string',
                        'userRules': [
                            {
                                'ipRule': 'string',
                                'ruleDesc': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Result** *(list) --* 
              Information about the IP access control groups.
              - *(dict) --* 
                Describes an IP access control group.
                - **groupId** *(string) --* 
                  The identifier of the group.
                - **groupName** *(string) --* 
                  The name of the group.
                - **groupDesc** *(string) --* 
                  The description of the group.
                - **userRules** *(list) --* 
                  The rules.
                  - *(dict) --* 
                    Describes a rule for an IP access control group.
                    - **ipRule** *(string) --* 
                      The IP address range, in CIDR notation.
                    - **ruleDesc** *(string) --* 
                      The description.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type GroupIds: list
        :param GroupIds:
          The identifiers of one or more IP access control groups.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to return.
        :rtype: dict
        :returns:
        """
        pass

    def describe_tags(self, ResourceId: str) -> Dict:
        """
        Describes the specified tags for the specified WorkSpaces resource.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeTags>`_
        
        **Request Syntax**
        ::
          response = client.describe_tags(
              ResourceId='string'
          )
        
        **Response Syntax**
        ::
            {
                'TagList': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **TagList** *(list) --* 
              The tags.
              - *(dict) --* 
                Describes a tag.
                - **Key** *(string) --* 
                  The key of the tag.
                - **Value** *(string) --* 
                  The value of the tag.
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, and IP access control groups.
        :rtype: dict
        :returns:
        """
        pass

    def describe_workspace_bundles(self, BundleIds: List = None, Owner: str = None, NextToken: str = None) -> Dict:
        """
        Retrieves a list that describes the available WorkSpace bundles.
        You can filter the results using either bundle ID or owner, but not both.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceBundles>`_
        
        **Request Syntax**
        ::
          response = client.describe_workspace_bundles(
              BundleIds=[
                  'string',
              ],
              Owner='string',
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Bundles': [
                    {
                        'BundleId': 'string',
                        'Name': 'string',
                        'Owner': 'string',
                        'Description': 'string',
                        'RootStorage': {
                            'Capacity': 'string'
                        },
                        'UserStorage': {
                            'Capacity': 'string'
                        },
                        'ComputeType': {
                            'Name': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                        }
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Bundles** *(list) --* 
              Information about the bundles.
              - *(dict) --* 
                Describes a WorkSpace bundle.
                - **BundleId** *(string) --* 
                  The bundle identifier.
                - **Name** *(string) --* 
                  The name of the bundle.
                - **Owner** *(string) --* 
                  The owner of the bundle. This is the account identifier of the owner, or ``AMAZON`` if the bundle is provided by AWS.
                - **Description** *(string) --* 
                  A description.
                - **RootStorage** *(dict) --* 
                  The size of the root volume.
                  - **Capacity** *(string) --* 
                    The size of the root volume.
                - **UserStorage** *(dict) --* 
                  The size of the user storage.
                  - **Capacity** *(string) --* 
                    The size of the user storage.
                - **ComputeType** *(dict) --* 
                  The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
                  - **Name** *(string) --* 
                    The compute type.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if there are no more results available. This token is valid for one day and must be used within that time frame.
        :type BundleIds: list
        :param BundleIds:
          The identifiers of the bundles. You cannot combine this parameter with any other filter.
          - *(string) --*
        :type Owner: string
        :param Owner:
          The owner of the bundles. You cannot combine this parameter with any other filter.
          Specify ``AMAZON`` to describe the bundles provided by AWS or null to describe the bundles that belong to your account.
        :type NextToken: string
        :param NextToken:
          The token for the next set of results. (You received this token from a previous call.)
        :rtype: dict
        :returns:
        """
        pass

    def describe_workspace_directories(self, DirectoryIds: List = None, NextToken: str = None) -> Dict:
        """
        Describes the available AWS Directory Service directories that are registered with Amazon WorkSpaces.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceDirectories>`_
        
        **Request Syntax**
        ::
          response = client.describe_workspace_directories(
              DirectoryIds=[
                  'string',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Directories': [
                    {
                        'DirectoryId': 'string',
                        'Alias': 'string',
                        'DirectoryName': 'string',
                        'RegistrationCode': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'DnsIpAddresses': [
                            'string',
                        ],
                        'CustomerUserName': 'string',
                        'IamRoleId': 'string',
                        'DirectoryType': 'SIMPLE_AD'|'AD_CONNECTOR',
                        'WorkspaceSecurityGroupId': 'string',
                        'State': 'REGISTERING'|'REGISTERED'|'DEREGISTERING'|'DEREGISTERED'|'ERROR',
                        'WorkspaceCreationProperties': {
                            'EnableWorkDocs': True|False,
                            'EnableInternetAccess': True|False,
                            'DefaultOu': 'string',
                            'CustomSecurityGroupId': 'string',
                            'UserEnabledAsLocalAdministrator': True|False
                        },
                        'ipGroupIds': [
                            'string',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Directories** *(list) --* 
              Information about the directories.
              - *(dict) --* 
                Describes an AWS Directory Service directory that is used with Amazon WorkSpaces.
                - **DirectoryId** *(string) --* 
                  The directory identifier.
                - **Alias** *(string) --* 
                  The directory alias.
                - **DirectoryName** *(string) --* 
                  The name of the directory.
                - **RegistrationCode** *(string) --* 
                  The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
                - **SubnetIds** *(list) --* 
                  The identifiers of the subnets used with the directory.
                  - *(string) --* 
                - **DnsIpAddresses** *(list) --* 
                  The IP addresses of the DNS servers for the directory.
                  - *(string) --* 
                - **CustomerUserName** *(string) --* 
                  The user name for the service account.
                - **IamRoleId** *(string) --* 
                  The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
                - **DirectoryType** *(string) --* 
                  The directory type.
                - **WorkspaceSecurityGroupId** *(string) --* 
                  The identifier of the security group that is assigned to new WorkSpaces.
                - **State** *(string) --* 
                  The state of the directory's registration with Amazon WorkSpaces
                - **WorkspaceCreationProperties** *(dict) --* 
                  The default creation properties for all WorkSpaces in the directory.
                  - **EnableWorkDocs** *(boolean) --* 
                    Specifies whether the directory is enabled for Amazon WorkDocs.
                  - **EnableInternetAccess** *(boolean) --* 
                    The public IP address to attach to all WorkSpaces that are created or rebuilt.
                  - **DefaultOu** *(string) --* 
                    The organizational unit (OU) in the directory for the WorkSpace machine accounts.
                  - **CustomSecurityGroupId** *(string) --* 
                    The identifier of any security groups to apply to WorkSpaces when they are created.
                  - **UserEnabledAsLocalAdministrator** *(boolean) --* 
                    Specifies whether the WorkSpace user is an administrator on the WorkSpace.
                - **ipGroupIds** *(list) --* 
                  The identifiers of the IP access control groups associated with the directory.
                  - *(string) --* 
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type DirectoryIds: list
        :param DirectoryIds:
          The identifiers of the directories. If the value is null, all directories are retrieved.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def describe_workspace_images(self, ImageIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        """
        Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaceImages>`_
        
        **Request Syntax**
        ::
          response = client.describe_workspace_images(
              ImageIds=[
                  'string',
              ],
              NextToken='string',
              MaxResults=123
          )
        
        **Response Syntax**
        ::
            {
                'Images': [
                    {
                        'ImageId': 'string',
                        'Name': 'string',
                        'Description': 'string',
                        'OperatingSystem': {
                            'Type': 'WINDOWS'|'LINUX'
                        },
                        'State': 'AVAILABLE'|'PENDING'|'ERROR',
                        'RequiredTenancy': 'DEFAULT'|'DEDICATED',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Images** *(list) --* 
              Information about the images.
              - *(dict) --* 
                Describes a WorkSpace image.
                - **ImageId** *(string) --* 
                  The identifier of the image.
                - **Name** *(string) --* 
                  The name of the image.
                - **Description** *(string) --* 
                  The description of the image.
                - **OperatingSystem** *(dict) --* 
                  The operating system that the image is running. 
                  - **Type** *(string) --* 
                    The operating system.
                - **State** *(string) --* 
                  The status of the image.
                - **RequiredTenancy** *(string) --* 
                  Specifies whether the image is running on dedicated hardware. When bring your own license (BYOL) is enabled, this value is set to DEDICATED. 
                - **ErrorCode** *(string) --* 
                  The error code that is returned for the image.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned for the image.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type ImageIds: list
        :param ImageIds:
          The identifier of the image.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to return.
        :rtype: dict
        :returns:
        """
        pass

    def describe_workspaces(self, WorkspaceIds: List = None, DirectoryId: str = None, UserName: str = None, BundleId: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        """
        Describes the specified WorkSpaces.
        You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.describe_workspaces(
              WorkspaceIds=[
                  'string',
              ],
              DirectoryId='string',
              UserName='string',
              BundleId='string',
              Limit=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'Workspaces': [
                    {
                        'WorkspaceId': 'string',
                        'DirectoryId': 'string',
                        'UserName': 'string',
                        'IpAddress': 'string',
                        'State': 'PENDING'|'AVAILABLE'|'IMPAIRED'|'UNHEALTHY'|'REBOOTING'|'STARTING'|'REBUILDING'|'MAINTENANCE'|'ADMIN_MAINTENANCE'|'TERMINATING'|'TERMINATED'|'SUSPENDED'|'UPDATING'|'STOPPING'|'STOPPED'|'ERROR',
                        'BundleId': 'string',
                        'SubnetId': 'string',
                        'ErrorMessage': 'string',
                        'ErrorCode': 'string',
                        'ComputerName': 'string',
                        'VolumeEncryptionKey': 'string',
                        'UserVolumeEncryptionEnabled': True|False,
                        'RootVolumeEncryptionEnabled': True|False,
                        'WorkspaceProperties': {
                            'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                            'RunningModeAutoStopTimeoutInMinutes': 123,
                            'RootVolumeSizeGib': 123,
                            'UserVolumeSizeGib': 123,
                            'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
                        },
                        'ModificationStates': [
                            {
                                'Resource': 'ROOT_VOLUME'|'USER_VOLUME'|'COMPUTE_TYPE',
                                'State': 'UPDATE_INITIATED'|'UPDATE_IN_PROGRESS'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **Workspaces** *(list) --* 
              Information about the WorkSpaces.
              Because  CreateWorkspaces is an asynchronous operation, some of the returned information could be incomplete.
              - *(dict) --* 
                Describes a WorkSpace.
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **DirectoryId** *(string) --* 
                  The identifier of the AWS Directory Service directory for the WorkSpace.
                - **UserName** *(string) --* 
                  The user for the WorkSpace.
                - **IpAddress** *(string) --* 
                  The IP address of the WorkSpace.
                - **State** *(string) --* 
                  The operational state of the WorkSpace.
                - **BundleId** *(string) --* 
                  The identifier of the bundle used to create the WorkSpace.
                - **SubnetId** *(string) --* 
                  The identifier of the subnet for the WorkSpace.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be created.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be created.
                - **ComputerName** *(string) --* 
                  The name of the WorkSpace, as seen by the operating system.
                - **VolumeEncryptionKey** *(string) --* 
                  The KMS key used to encrypt data stored on your WorkSpace.
                - **UserVolumeEncryptionEnabled** *(boolean) --* 
                  Indicates whether the data stored on the user volume is encrypted.
                - **RootVolumeEncryptionEnabled** *(boolean) --* 
                  Indicates whether the data stored on the root volume is encrypted.
                - **WorkspaceProperties** *(dict) --* 
                  The properties of the WorkSpace.
                  - **RunningMode** *(string) --* 
                    The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
                  - **RunningModeAutoStopTimeoutInMinutes** *(integer) --* 
                    The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
                  - **RootVolumeSizeGib** *(integer) --* 
                    The size of the root volume.
                  - **UserVolumeSizeGib** *(integer) --* 
                    The size of the user storage.
                  - **ComputeTypeName** *(string) --* 
                    The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
                - **ModificationStates** *(list) --* 
                  The modification states of the WorkSpace.
                  - *(dict) --* 
                    Describes a WorkSpace modification.
                    - **Resource** *(string) --* 
                      The resource.
                    - **State** *(string) --* 
                      The modification state.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type WorkspaceIds: list
        :param WorkspaceIds:
          The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.
          Because the  CreateWorkspaces operation is asynchronous, the identifier it returns is not immediately available. If you immediately call  DescribeWorkspaces with this identifier, no information is returned.
          - *(string) --*
        :type DirectoryId: string
        :param DirectoryId:
          The identifier of the directory. In addition, you can optionally specify a specific directory user (see ``UserName`` ). You cannot combine this parameter with any other filter.
        :type UserName: string
        :param UserName:
          The name of the directory user. You must specify this parameter with ``DirectoryId`` .
        :type BundleId: string
        :param BundleId:
          The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.
        :type Limit: integer
        :param Limit:
          The maximum number of items to return.
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def describe_workspaces_connection_status(self, WorkspaceIds: List = None, NextToken: str = None) -> Dict:
        """
        Describes the connection status of the specified WorkSpaces.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeWorkspacesConnectionStatus>`_
        
        **Request Syntax**
        ::
          response = client.describe_workspaces_connection_status(
              WorkspaceIds=[
                  'string',
              ],
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'WorkspacesConnectionStatus': [
                    {
                        'WorkspaceId': 'string',
                        'ConnectionState': 'CONNECTED'|'DISCONNECTED'|'UNKNOWN',
                        'ConnectionStateCheckTimestamp': datetime(2015, 1, 1),
                        'LastKnownUserConnectionTimestamp': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **WorkspacesConnectionStatus** *(list) --* 
              Information about the connection status of the WorkSpace.
              - *(dict) --* 
                Describes the connection status of a WorkSpace.
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ConnectionState** *(string) --* 
                  The connection state of the WorkSpace. The connection state is unknown if the WorkSpace is stopped.
                - **ConnectionStateCheckTimestamp** *(datetime) --* 
                  The timestamp of the connection status check.
                - **LastKnownUserConnectionTimestamp** *(datetime) --* 
                  The timestamp of the last known user connection.
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type WorkspaceIds: list
        :param WorkspaceIds:
          The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.
          - *(string) --*
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def disassociate_ip_groups(self, DirectoryId: str, GroupIds: List) -> Dict:
        """
        Disassociates the specified IP access control group from the specified directory.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DisassociateIpGroups>`_
        
        **Request Syntax**
        ::
          response = client.disassociate_ip_groups(
              DirectoryId='string',
              GroupIds=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type DirectoryId: string
        :param DirectoryId: **[REQUIRED]**
          The identifier of the directory.
        :type GroupIds: list
        :param GroupIds: **[REQUIRED]**
          The identifiers of one or more IP access control groups.
          - *(string) --*
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

    def import_workspace_image(self, Ec2ImageId: str, IngestionProcess: str, ImageName: str, ImageDescription: str, Tags: List = None) -> Dict:
        """
        Imports the specified Windows 7 or Windows 10 bring your own license (BYOL) image into Amazon WorkSpaces. The image must be an already licensed EC2 image that is in your AWS account, and you must own the image. 
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ImportWorkspaceImage>`_
        
        **Request Syntax**
        ::
          response = client.import_workspace_image(
              Ec2ImageId='string',
              IngestionProcess='BYOL_REGULAR'|'BYOL_GRAPHICS'|'BYOL_GRAPHICSPRO',
              ImageName='string',
              ImageDescription='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'ImageId': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ImageId** *(string) --* 
              The identifier of the WorkSpace image.
        :type Ec2ImageId: string
        :param Ec2ImageId: **[REQUIRED]**
          The identifier of the EC2 image.
        :type IngestionProcess: string
        :param IngestionProcess: **[REQUIRED]**
          The ingestion process to be used when importing the image.
        :type ImageName: string
        :param ImageName: **[REQUIRED]**
          The name of the WorkSpace image.
        :type ImageDescription: string
        :param ImageDescription: **[REQUIRED]**
          The description of the WorkSpace image.
        :type Tags: list
        :param Tags:
          The tags. Each WorkSpaces resource can have a maximum of 50 tags.
          - *(dict) --*
            Describes a tag.
            - **Key** *(string) --* **[REQUIRED]**
              The key of the tag.
            - **Value** *(string) --*
              The value of the tag.
        :rtype: dict
        :returns:
        """
        pass

    def list_available_management_cidr_ranges(self, ManagementCidrRangeConstraint: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        """
        Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable bring your own license (BYOL). 
        The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ListAvailableManagementCidrRanges>`_
        
        **Request Syntax**
        ::
          response = client.list_available_management_cidr_ranges(
              ManagementCidrRangeConstraint='string',
              MaxResults=123,
              NextToken='string'
          )
        
        **Response Syntax**
        ::
            {
                'ManagementCidrRanges': [
                    'string',
                ],
                'NextToken': 'string'
            }
        
        **Response Structure**
          - *(dict) --* 
            - **ManagementCidrRanges** *(list) --* 
              The list of available IP address ranges, specified as IPv4 CIDR blocks.
              - *(string) --* 
            - **NextToken** *(string) --* 
              The token to use to retrieve the next set of results, or null if no more results are available.
        :type ManagementCidrRangeConstraint: string
        :param ManagementCidrRangeConstraint: **[REQUIRED]**
          The IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).
        :type MaxResults: integer
        :param MaxResults:
          The maximum number of items to return.
        :type NextToken: string
        :param NextToken:
          If you received a ``NextToken`` from a previous call that was paginated, provide this token to receive the next set of results.
        :rtype: dict
        :returns:
        """
        pass

    def modify_account(self, DedicatedTenancySupport: str = None, DedicatedTenancyManagementCidrRange: str = None) -> Dict:
        """
        Modifies the configuration of bring your own license (BYOL) for the specified account.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyAccount>`_
        
        **Request Syntax**
        ::
          response = client.modify_account(
              DedicatedTenancySupport='ENABLED',
              DedicatedTenancyManagementCidrRange='string'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type DedicatedTenancySupport: string
        :param DedicatedTenancySupport:
          The status of BYOL.
        :type DedicatedTenancyManagementCidrRange: string
        :param DedicatedTenancyManagementCidrRange:
          The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the ``ListAvailableManagementCidrRanges`` operation.
        :rtype: dict
        :returns:
        """
        pass

    def modify_client_properties(self, ResourceId: str, ClientProperties: Dict) -> Dict:
        """
        Modifies the properties of the specified Amazon WorkSpaces clients.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyClientProperties>`_
        
        **Request Syntax**
        ::
          response = client.modify_client_properties(
              ResourceId='string',
              ClientProperties={
                  'ReconnectEnabled': 'ENABLED'|'DISABLED'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**
          The resource identifiers, in the form of directory IDs.
        :type ClientProperties: dict
        :param ClientProperties: **[REQUIRED]**
          Information about the Amazon WorkSpaces client.
          - **ReconnectEnabled** *(string) --*
            Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials.
        :rtype: dict
        :returns:
        """
        pass

    def modify_workspace_properties(self, WorkspaceId: str, WorkspaceProperties: Dict) -> Dict:
        """
        Modifies the specified WorkSpace properties.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceProperties>`_
        
        **Request Syntax**
        ::
          response = client.modify_workspace_properties(
              WorkspaceId='string',
              WorkspaceProperties={
                  'RunningMode': 'AUTO_STOP'|'ALWAYS_ON',
                  'RunningModeAutoStopTimeoutInMinutes': 123,
                  'RootVolumeSizeGib': 123,
                  'UserVolumeSizeGib': 123,
                  'ComputeTypeName': 'VALUE'|'STANDARD'|'PERFORMANCE'|'POWER'|'GRAPHICS'|'POWERPRO'|'GRAPHICSPRO'
              }
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type WorkspaceId: string
        :param WorkspaceId: **[REQUIRED]**
          The identifier of the WorkSpace.
        :type WorkspaceProperties: dict
        :param WorkspaceProperties: **[REQUIRED]**
          The properties of the WorkSpace.
          - **RunningMode** *(string) --*
            The running mode. For more information, see `Manage the WorkSpace Running Mode <https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html>`__ .
          - **RunningModeAutoStopTimeoutInMinutes** *(integer) --*
            The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60 minute intervals.
          - **RootVolumeSizeGib** *(integer) --*
            The size of the root volume.
          - **UserVolumeSizeGib** *(integer) --*
            The size of the user storage.
          - **ComputeTypeName** *(string) --*
            The compute type. For more information, see `Amazon WorkSpaces Bundles <http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles>`__ .
        :rtype: dict
        :returns:
        """
        pass

    def modify_workspace_state(self, WorkspaceId: str, WorkspaceState: str) -> Dict:
        """
        Sets the state of the specified WorkSpace.
        To maintain a WorkSpace without being interrupted, set the WorkSpace state to ``ADMIN_MAINTENANCE`` . WorkSpaces in this state do not respond to requests to reboot, stop, start, or rebuild. An AutoStop WorkSpace in this state is not stopped. Users can log into a WorkSpace in the ``ADMIN_MAINTENANCE`` state.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/ModifyWorkspaceState>`_
        
        **Request Syntax**
        ::
          response = client.modify_workspace_state(
              WorkspaceId='string',
              WorkspaceState='AVAILABLE'|'ADMIN_MAINTENANCE'
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type WorkspaceId: string
        :param WorkspaceId: **[REQUIRED]**
          The identifier of the WorkSpace.
        :type WorkspaceState: string
        :param WorkspaceState: **[REQUIRED]**
          The WorkSpace state.
        :rtype: dict
        :returns:
        """
        pass

    def reboot_workspaces(self, RebootWorkspaceRequests: List) -> Dict:
        """
        Reboots the specified WorkSpaces.
        You cannot reboot a WorkSpace unless its state is ``AVAILABLE`` or ``UNHEALTHY`` .
        This operation is asynchronous and returns before the WorkSpaces have rebooted.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebootWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.reboot_workspaces(
              RebootWorkspaceRequests=[
                  {
                      'WorkspaceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceId': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpaces that could not be rebooted.
              - *(dict) --* 
                Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be rebooted.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be rebooted.
        :type RebootWorkspaceRequests: list
        :param RebootWorkspaceRequests: **[REQUIRED]**
          The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.
          - *(dict) --*
            Describes the information used to reboot a WorkSpace.
            - **WorkspaceId** *(string) --* **[REQUIRED]**
              The identifier of the WorkSpace.
        :rtype: dict
        :returns:
        """
        pass

    def rebuild_workspaces(self, RebuildWorkspaceRequests: List, AdditionalInfo: str = None) -> Dict:
        """
        Rebuilds the specified WorkSpace.
        You cannot rebuild a WorkSpace unless its state is ``AVAILABLE`` , ``ERROR`` , or ``UNHEALTHY`` .
        Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see `Rebuild a WorkSpace <https://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html>`__ .
        This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RebuildWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.rebuild_workspaces(
              RebuildWorkspaceRequests=[
                  {
                      'WorkspaceId': 'string'
                  },
              ],
              AdditionalInfo='string'
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceId': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpace that could not be rebuilt.
              - *(dict) --* 
                Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be rebooted.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be rebooted.
        :type RebuildWorkspaceRequests: list
        :param RebuildWorkspaceRequests: **[REQUIRED]**
          The WorkSpace to rebuild. You can specify a single WorkSpace.
          - *(dict) --*
            Describes the information used to rebuild a WorkSpace.
            - **WorkspaceId** *(string) --* **[REQUIRED]**
              The identifier of the WorkSpace.
        :type AdditionalInfo: string
        :param AdditionalInfo:
          Reserved.
        :rtype: dict
        :returns:
        """
        pass

    def revoke_ip_rules(self, GroupId: str, UserRules: List) -> Dict:
        """
        Removes one or more rules from the specified IP access control group.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/RevokeIpRules>`_
        
        **Request Syntax**
        ::
          response = client.revoke_ip_rules(
              GroupId='string',
              UserRules=[
                  'string',
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type GroupId: string
        :param GroupId: **[REQUIRED]**
          The identifier of the group.
        :type UserRules: list
        :param UserRules: **[REQUIRED]**
          The rules to remove from the group.
          - *(string) --*
        :rtype: dict
        :returns:
        """
        pass

    def start_workspaces(self, StartWorkspaceRequests: List) -> Dict:
        """
        Starts the specified WorkSpaces.
        You cannot start a WorkSpace unless it has a running mode of ``AutoStop`` and a state of ``STOPPED`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StartWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.start_workspaces(
              StartWorkspaceRequests=[
                  {
                      'WorkspaceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceId': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpaces that could not be started.
              - *(dict) --* 
                Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be rebooted.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be rebooted.
        :type StartWorkspaceRequests: list
        :param StartWorkspaceRequests: **[REQUIRED]**
          The WorkSpaces to start. You can specify up to 25 WorkSpaces.
          - *(dict) --*
            Information used to start a WorkSpace.
            - **WorkspaceId** *(string) --*
              The identifier of the WorkSpace.
        :rtype: dict
        :returns:
        """
        pass

    def stop_workspaces(self, StopWorkspaceRequests: List) -> Dict:
        """
        Stops the specified WorkSpaces.
        You cannot stop a WorkSpace unless it has a running mode of ``AutoStop`` and a state of ``AVAILABLE`` , ``IMPAIRED`` , ``UNHEALTHY`` , or ``ERROR`` .
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/StopWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.stop_workspaces(
              StopWorkspaceRequests=[
                  {
                      'WorkspaceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceId': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpaces that could not be stopped.
              - *(dict) --* 
                Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be rebooted.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be rebooted.
        :type StopWorkspaceRequests: list
        :param StopWorkspaceRequests: **[REQUIRED]**
          The WorkSpaces to stop. You can specify up to 25 WorkSpaces.
          - *(dict) --*
            Describes the information used to stop a WorkSpace.
            - **WorkspaceId** *(string) --*
              The identifier of the WorkSpace.
        :rtype: dict
        :returns:
        """
        pass

    def terminate_workspaces(self, TerminateWorkspaceRequests: List) -> Dict:
        """
        Terminates the specified WorkSpaces.
        Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is destroyed. If you need to archive any user data, contact Amazon Web Services before terminating the WorkSpace.
        You can terminate a WorkSpace that is in any state except ``SUSPENDED`` .
        This operation is asynchronous and returns before the WorkSpaces have been completely terminated.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/TerminateWorkspaces>`_
        
        **Request Syntax**
        ::
          response = client.terminate_workspaces(
              TerminateWorkspaceRequests=[
                  {
                      'WorkspaceId': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {
                'FailedRequests': [
                    {
                        'WorkspaceId': 'string',
                        'ErrorCode': 'string',
                        'ErrorMessage': 'string'
                    },
                ]
            }
        
        **Response Structure**
          - *(dict) --* 
            - **FailedRequests** *(list) --* 
              Information about the WorkSpaces that could not be terminated.
              - *(dict) --* 
                Describes a WorkSpace that could not be rebooted. ( RebootWorkspaces ), rebuilt ( RebuildWorkspaces ), terminated ( TerminateWorkspaces ), started ( StartWorkspaces ), or stopped ( StopWorkspaces ).
                - **WorkspaceId** *(string) --* 
                  The identifier of the WorkSpace.
                - **ErrorCode** *(string) --* 
                  The error code that is returned if the WorkSpace cannot be rebooted.
                - **ErrorMessage** *(string) --* 
                  The text of the error message that is returned if the WorkSpace cannot be rebooted.
        :type TerminateWorkspaceRequests: list
        :param TerminateWorkspaceRequests: **[REQUIRED]**
          The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.
          - *(dict) --*
            Describes the information used to terminate a WorkSpace.
            - **WorkspaceId** *(string) --* **[REQUIRED]**
              The identifier of the WorkSpace.
        :rtype: dict
        :returns:
        """
        pass

    def update_rules_of_ip_group(self, GroupId: str, UserRules: List) -> Dict:
        """
        Replaces the current rules of the specified IP access control group with the specified rules.
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/UpdateRulesOfIpGroup>`_
        
        **Request Syntax**
        ::
          response = client.update_rules_of_ip_group(
              GroupId='string',
              UserRules=[
                  {
                      'ipRule': 'string',
                      'ruleDesc': 'string'
                  },
              ]
          )
        
        **Response Syntax**
        ::
            {}
        
        **Response Structure**
          - *(dict) --* 
        :type GroupId: string
        :param GroupId: **[REQUIRED]**
          The identifier of the group.
        :type UserRules: list
        :param UserRules: **[REQUIRED]**
          One or more rules.
          - *(dict) --*
            Describes a rule for an IP access control group.
            - **ipRule** *(string) --*
              The IP address range, in CIDR notation.
            - **ruleDesc** *(string) --*
              The description.
        :rtype: dict
        :returns:
        """
        pass
