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

apps_request_builder = lazy_import('msgraph.generated.device_app_management.ios_managed_app_protections.item.apps.apps_request_builder')
managed_mobile_app_item_request_builder = lazy_import('msgraph.generated.device_app_management.ios_managed_app_protections.item.apps.item.managed_mobile_app_item_request_builder')
deployment_summary_request_builder = lazy_import('msgraph.generated.device_app_management.ios_managed_app_protections.item.deployment_summary.deployment_summary_request_builder')
ios_managed_app_protection = lazy_import('msgraph.generated.models.ios_managed_app_protection')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class IosManagedAppProtectionItemRequestBuilder():
    """
    Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
    """
    @property
    def apps(self) -> apps_request_builder.AppsRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.iosManagedAppProtection entity.
        """
        return apps_request_builder.AppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_summary(self) -> deployment_summary_request_builder.DeploymentSummaryRequestBuilder:
        """
        Provides operations to manage the deploymentSummary property of the microsoft.graph.iosManagedAppProtection entity.
        """
        return deployment_summary_request_builder.DeploymentSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    def apps_by_id(self,id: str) -> managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.iosManagedAppProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedMobileApp%2Did"] = id
        return managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IosManagedAppProtectionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/iosManagedAppProtections/{iosManagedAppProtection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property iosManagedAppProtections for deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ios_managed_app_protection.IosManagedAppProtection]:
        """
        iOS managed app policies.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ios_managed_app_protection.IosManagedAppProtection]
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
        return await self.request_adapter.send_async(request_info, ios_managed_app_protection.IosManagedAppProtection, error_mapping)
    
    async def patch(self,body: Optional[ios_managed_app_protection.IosManagedAppProtection] = None, request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ios_managed_app_protection.IosManagedAppProtection]:
        """
        Update the navigation property iosManagedAppProtections in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ios_managed_app_protection.IosManagedAppProtection]
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
        return await self.request_adapter.send_async(request_info, ios_managed_app_protection.IosManagedAppProtection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property iosManagedAppProtections for deviceAppManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        iOS managed app policies.
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
    
    def to_patch_request_information(self,body: Optional[ios_managed_app_protection.IosManagedAppProtection] = None, request_configuration: Optional[IosManagedAppProtectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property iosManagedAppProtections in deviceAppManagement
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
    class IosManagedAppProtectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class IosManagedAppProtectionItemRequestBuilderGetQueryParameters():
        """
        iOS managed app policies.
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
    class IosManagedAppProtectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IosManagedAppProtectionItemRequestBuilder.IosManagedAppProtectionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class IosManagedAppProtectionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

