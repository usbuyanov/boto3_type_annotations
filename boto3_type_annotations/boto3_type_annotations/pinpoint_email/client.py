from typing import Optional
from botocore.client import BaseClient
from typing import Dict
from typing import Union
from botocore.paginate import Paginator
from datetime import datetime
from botocore.waiter import Waiter
from typing import List


class Client(BaseClient):
    def can_paginate(self, operation_name: str = None):
        pass

    def create_configuration_set(self, ConfigurationSetName: str = None, TrackingOptions: Dict = None, DeliveryOptions: Dict = None, ReputationOptions: Dict = None, SendingOptions: Dict = None, Tags: List = None) -> Dict:
        pass

    def create_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        pass

    def create_dedicated_ip_pool(self, PoolName: str, Tags: List = None) -> Dict:
        pass

    def create_deliverability_test_report(self, FromEmailAddress: str, Content: Dict, ReportName: str = None, Tags: List = None) -> Dict:
        pass

    def create_email_identity(self, EmailIdentity: str, Tags: List = None) -> Dict:
        pass

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict:
        pass

    def delete_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str) -> Dict:
        pass

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict:
        pass

    def delete_email_identity(self, EmailIdentity: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_account(self) -> Dict:
        pass

    def get_blacklist_reports(self, BlacklistItemNames: List) -> Dict:
        pass

    def get_configuration_set(self, ConfigurationSetName: str) -> Dict:
        pass

    def get_configuration_set_event_destinations(self, ConfigurationSetName: str) -> Dict:
        pass

    def get_dedicated_ip(self, Ip: str) -> Dict:
        pass

    def get_dedicated_ips(self, PoolName: str = None, NextToken: str = None, PageSize: int = None) -> Dict:
        pass

    def get_deliverability_dashboard_options(self) -> Dict:
        pass

    def get_deliverability_test_report(self, ReportId: str) -> Dict:
        pass

    def get_domain_statistics_report(self, Domain: str, StartDate: datetime, EndDate: datetime) -> Dict:
        pass

    def get_email_identity(self, EmailIdentity: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> Paginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> Waiter:
        pass

    def list_configuration_sets(self, NextToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_dedicated_ip_pools(self, NextToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_deliverability_test_reports(self, NextToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_email_identities(self, NextToken: str = None, PageSize: int = None) -> Dict:
        pass

    def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    def put_account_dedicated_ip_warmup_attributes(self, AutoWarmupEnabled: bool = None) -> Dict:
        pass

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict:
        pass

    def put_configuration_set_delivery_options(self, ConfigurationSetName: str, SendingPoolName: str = None) -> Dict:
        pass

    def put_configuration_set_reputation_options(self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None) -> Dict:
        pass

    def put_configuration_set_sending_options(self, ConfigurationSetName: str, SendingEnabled: bool = None) -> Dict:
        pass

    def put_configuration_set_tracking_options(self, ConfigurationSetName: str, CustomRedirectDomain: str = None) -> Dict:
        pass

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict:
        pass

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict:
        pass

    def put_deliverability_dashboard_option(self, DashboardEnabled: bool) -> Dict:
        pass

    def put_email_identity_dkim_attributes(self, EmailIdentity: str, SigningEnabled: bool = None) -> Dict:
        pass

    def put_email_identity_feedback_attributes(self, EmailIdentity: str, EmailForwardingEnabled: bool = None) -> Dict:
        pass

    def put_email_identity_mail_from_attributes(self, EmailIdentity: str, MailFromDomain: str = None, BehaviorOnMxFailure: str = None) -> Dict:
        pass

    def send_email(self, Destination: Dict, Content: Dict, FromEmailAddress: str = None, ReplyToAddresses: List = None, FeedbackForwardingEmailAddress: str = None, EmailTags: List = None, ConfigurationSetName: str = None) -> Dict:
        pass

    def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass

    def update_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict) -> Dict:
        pass
