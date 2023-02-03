from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CopyNotebookPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new copyNotebookPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupId property
        self._group_id: Optional[str] = None
        # The notebookFolder property
        self._notebook_folder: Optional[str] = None
        # The renameAs property
        self._rename_as: Optional[str] = None
        # The siteCollectionId property
        self._site_collection_id: Optional[str] = None
        # The siteId property
        self._site_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyNotebookPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CopyNotebookPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CopyNotebookPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "notebookFolder": lambda n : setattr(self, 'notebook_folder', n.get_str_value()),
            "renameAs": lambda n : setattr(self, 'rename_as', n.get_str_value()),
            "siteCollectionId": lambda n : setattr(self, 'site_collection_id', n.get_str_value()),
            "siteId": lambda n : setattr(self, 'site_id', n.get_str_value()),
        }
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The groupId property
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The groupId property
        Args:
            value: Value to set for the group_id property.
        """
        self._group_id = value
    
    @property
    def notebook_folder(self,) -> Optional[str]:
        """
        Gets the notebookFolder property value. The notebookFolder property
        Returns: Optional[str]
        """
        return self._notebook_folder
    
    @notebook_folder.setter
    def notebook_folder(self,value: Optional[str] = None) -> None:
        """
        Sets the notebookFolder property value. The notebookFolder property
        Args:
            value: Value to set for the notebook_folder property.
        """
        self._notebook_folder = value
    
    @property
    def rename_as(self,) -> Optional[str]:
        """
        Gets the renameAs property value. The renameAs property
        Returns: Optional[str]
        """
        return self._rename_as
    
    @rename_as.setter
    def rename_as(self,value: Optional[str] = None) -> None:
        """
        Sets the renameAs property value. The renameAs property
        Args:
            value: Value to set for the rename_as property.
        """
        self._rename_as = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("notebookFolder", self.notebook_folder)
        writer.write_str_value("renameAs", self.rename_as)
        writer.write_str_value("siteCollectionId", self.site_collection_id)
        writer.write_str_value("siteId", self.site_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def site_collection_id(self,) -> Optional[str]:
        """
        Gets the siteCollectionId property value. The siteCollectionId property
        Returns: Optional[str]
        """
        return self._site_collection_id
    
    @site_collection_id.setter
    def site_collection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteCollectionId property value. The siteCollectionId property
        Args:
            value: Value to set for the site_collection_id property.
        """
        self._site_collection_id = value
    
    @property
    def site_id(self,) -> Optional[str]:
        """
        Gets the siteId property value. The siteId property
        Returns: Optional[str]
        """
        return self._site_id
    
    @site_id.setter
    def site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteId property value. The siteId property
        Args:
            value: Value to set for the site_id property.
        """
        self._site_id = value
    

