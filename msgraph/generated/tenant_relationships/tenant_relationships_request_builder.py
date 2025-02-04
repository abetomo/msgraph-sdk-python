from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

tenant_relationship = lazy_import('msgraph.generated.models.tenant_relationship')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
delegated_admin_customers_request_builder = lazy_import('msgraph.generated.tenant_relationships.delegated_admin_customers.delegated_admin_customers_request_builder')
delegated_admin_customer_item_request_builder = lazy_import('msgraph.generated.tenant_relationships.delegated_admin_customers.item.delegated_admin_customer_item_request_builder')
delegated_admin_relationships_request_builder = lazy_import('msgraph.generated.tenant_relationships.delegated_admin_relationships.delegated_admin_relationships_request_builder')
delegated_admin_relationship_item_request_builder = lazy_import('msgraph.generated.tenant_relationships.delegated_admin_relationships.item.delegated_admin_relationship_item_request_builder')

class TenantRelationshipsRequestBuilder():
    """
    Provides operations to manage the tenantRelationship singleton.
    """
    @property
    def delegated_admin_customers(self) -> delegated_admin_customers_request_builder.DelegatedAdminCustomersRequestBuilder:
        """
        Provides operations to manage the delegatedAdminCustomers property of the microsoft.graph.tenantRelationship entity.
        """
        return delegated_admin_customers_request_builder.DelegatedAdminCustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delegated_admin_relationships(self) -> delegated_admin_relationships_request_builder.DelegatedAdminRelationshipsRequestBuilder:
        """
        Provides operations to manage the delegatedAdminRelationships property of the microsoft.graph.tenantRelationship entity.
        """
        return delegated_admin_relationships_request_builder.DelegatedAdminRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TenantRelationshipsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/tenantRelationships{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def delegated_admin_customers_by_id(self,id: str) -> delegated_admin_customer_item_request_builder.DelegatedAdminCustomerItemRequestBuilder:
        """
        Provides operations to manage the delegatedAdminCustomers property of the microsoft.graph.tenantRelationship entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_admin_customer_item_request_builder.DelegatedAdminCustomerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedAdminCustomer%2Did"] = id
        return delegated_admin_customer_item_request_builder.DelegatedAdminCustomerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def delegated_admin_relationships_by_id(self,id: str) -> delegated_admin_relationship_item_request_builder.DelegatedAdminRelationshipItemRequestBuilder:
        """
        Provides operations to manage the delegatedAdminRelationships property of the microsoft.graph.tenantRelationship entity.
        Args:
            id: Unique identifier of the item
        Returns: delegated_admin_relationship_item_request_builder.DelegatedAdminRelationshipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["delegatedAdminRelationship%2Did"] = id
        return delegated_admin_relationship_item_request_builder.DelegatedAdminRelationshipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[TenantRelationshipsRequestBuilderGetRequestConfiguration] = None) -> Optional[tenant_relationship.TenantRelationship]:
        """
        Get tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[tenant_relationship.TenantRelationship]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, tenant_relationship.TenantRelationship, error_mapping)
    
    async def patch(self,body: Optional[tenant_relationship.TenantRelationship] = None, request_configuration: Optional[TenantRelationshipsRequestBuilderPatchRequestConfiguration] = None) -> Optional[tenant_relationship.TenantRelationship]:
        """
        Update tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[tenant_relationship.TenantRelationship]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, tenant_relationship.TenantRelationship, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TenantRelationshipsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get tenantRelationships
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[tenant_relationship.TenantRelationship] = None, request_configuration: Optional[TenantRelationshipsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update tenantRelationships
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class TenantRelationshipsRequestBuilderGetQueryParameters():
        """
        Get tenantRelationships
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class TenantRelationshipsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TenantRelationshipsRequestBuilder.TenantRelationshipsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TenantRelationshipsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

