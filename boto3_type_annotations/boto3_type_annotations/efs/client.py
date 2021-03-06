from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_file_system(self, CreationToken: str, PerformanceMode: str = None, Encrypted: bool = None, KmsKeyId: str = None, ThroughputMode: str = None, ProvisionedThroughputInMibps: float = None, Tags: List = None) -> Dict:
        pass

    def create_mount_target(self, FileSystemId: str, SubnetId: str, IpAddress: str = None, SecurityGroups: List = None) -> Dict:
        pass

    def create_tags(self, FileSystemId: str, Tags: List):
        pass

    def delete_file_system(self, FileSystemId: str):
        pass

    def delete_mount_target(self, MountTargetId: str):
        pass

    def delete_tags(self, FileSystemId: str, TagKeys: List):
        pass

    def describe_file_systems(self, MaxItems: int = None, Marker: str = None, CreationToken: str = None, FileSystemId: str = None) -> Dict:
        pass

    def describe_lifecycle_configuration(self, FileSystemId: str) -> Dict:
        pass

    def describe_mount_target_security_groups(self, MountTargetId: str) -> Dict:
        pass

    def describe_mount_targets(self, MaxItems: int = None, Marker: str = None, FileSystemId: str = None, MountTargetId: str = None) -> Dict:
        pass

    def describe_tags(self, FileSystemId: str, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def modify_mount_target_security_groups(self, MountTargetId: str, SecurityGroups: List = None):
        pass

    def put_lifecycle_configuration(self, FileSystemId: str, LifecyclePolicies: List) -> Dict:
        pass

    def update_file_system(self, FileSystemId: str, ThroughputMode: str = None, ProvisionedThroughputInMibps: float = None) -> Dict:
        pass
