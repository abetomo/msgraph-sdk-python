from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class VlookupPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    @property
    def col_index_num(self,) -> Optional[json.Json]:
        """
        Gets the colIndexNum property value. The colIndexNum property
        Returns: Optional[json.Json]
        """
        return self._col_index_num
    
    @col_index_num.setter
    def col_index_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the colIndexNum property value. The colIndexNum property
        Args:
            value: Value to set for the col_index_num property.
        """
        self._col_index_num = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vlookupPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The colIndexNum property
        self._col_index_num: Optional[json.Json] = None
        # The lookupValue property
        self._lookup_value: Optional[json.Json] = None
        # The rangeLookup property
        self._range_lookup: Optional[json.Json] = None
        # The tableArray property
        self._table_array: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VlookupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VlookupPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VlookupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "colIndexNum": lambda n : setattr(self, 'col_index_num', n.get_object_value(json.Json)),
            "lookupValue": lambda n : setattr(self, 'lookup_value', n.get_object_value(json.Json)),
            "rangeLookup": lambda n : setattr(self, 'range_lookup', n.get_object_value(json.Json)),
            "tableArray": lambda n : setattr(self, 'table_array', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def lookup_value(self,) -> Optional[json.Json]:
        """
        Gets the lookupValue property value. The lookupValue property
        Returns: Optional[json.Json]
        """
        return self._lookup_value
    
    @lookup_value.setter
    def lookup_value(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the lookupValue property value. The lookupValue property
        Args:
            value: Value to set for the lookup_value property.
        """
        self._lookup_value = value
    
    @property
    def range_lookup(self,) -> Optional[json.Json]:
        """
        Gets the rangeLookup property value. The rangeLookup property
        Returns: Optional[json.Json]
        """
        return self._range_lookup
    
    @range_lookup.setter
    def range_lookup(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the rangeLookup property value. The rangeLookup property
        Args:
            value: Value to set for the range_lookup property.
        """
        self._range_lookup = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("colIndexNum", self.col_index_num)
        writer.write_object_value("lookupValue", self.lookup_value)
        writer.write_object_value("rangeLookup", self.range_lookup)
        writer.write_object_value("tableArray", self.table_array)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def table_array(self,) -> Optional[json.Json]:
        """
        Gets the tableArray property value. The tableArray property
        Returns: Optional[json.Json]
        """
        return self._table_array
    
    @table_array.setter
    def table_array(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the tableArray property value. The tableArray property
        Args:
            value: Value to set for the table_array property.
        """
        self._table_array = value
    

