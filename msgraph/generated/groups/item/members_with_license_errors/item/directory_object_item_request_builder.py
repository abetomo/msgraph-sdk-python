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

graph_application_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_application.graph_application_request_builder')
graph_device_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_device.graph_device_request_builder')
graph_group_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_group.graph_group_request_builder')
graph_org_contact_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_org_contact.graph_org_contact_request_builder')
graph_service_principal_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_service_principal.graph_service_principal_request_builder')
graph_user_request_builder = lazy_import('msgraph.generated.groups.item.members_with_license_errors.item.graph_user.graph_user_request_builder')
directory_object = lazy_import('msgraph.generated.models.directory_object')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DirectoryObjectItemRequestBuilder():
    """
    Provides operations to manage the membersWithLicenseErrors property of the microsoft.graph.group entity.
    """
    @property
    def graph_application(self) -> graph_application_request_builder.GraphApplicationRequestBuilder:
        """
        Casts the previous resource to application.
        """
        return graph_application_request_builder.GraphApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_device(self) -> graph_device_request_builder.GraphDeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        return graph_device_request_builder.GraphDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_group(self) -> graph_group_request_builder.GraphGroupRequestBuilder:
        """
        Casts the previous resource to group.
        """
        return graph_group_request_builder.GraphGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_org_contact(self) -> graph_org_contact_request_builder.GraphOrgContactRequestBuilder:
        """
        Casts the previous resource to orgContact.
        """
        return graph_org_contact_request_builder.GraphOrgContactRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_service_principal(self) -> graph_service_principal_request_builder.GraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        return graph_service_principal_request_builder.GraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_user(self) -> graph_user_request_builder.GraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        return graph_user_request_builder.GraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryObjectItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/membersWithLicenseErrors/{directoryObject%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[DirectoryObjectItemRequestBuilderGetRequestConfiguration] = None) -> Optional[directory_object.DirectoryObject]:
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[directory_object.DirectoryObject]
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
        return await self.request_adapter.send_async(request_info, directory_object.DirectoryObject, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DirectoryObjectItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
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
    
    @dataclass
    class DirectoryObjectItemRequestBuilderGetQueryParameters():
        """
        A list of group members with license errors from this group-based license assignment. Read-only.
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
    class DirectoryObjectItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DirectoryObjectItemRequestBuilder.DirectoryObjectItemRequestBuilderGetQueryParameters] = None

    

