from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
email_sender = lazy_import('msgraph.generated.models.security.email_sender')

class AnalyzedMessageEvidence(alert_evidence.AlertEvidence):
    @property
    def anti_spam_direction(self,) -> Optional[str]:
        """
        Gets the antiSpamDirection property value. Direction of the email relative to your network. The possible values are: inbound, outbound or intraorg.
        Returns: Optional[str]
        """
        return self._anti_spam_direction
    
    @anti_spam_direction.setter
    def anti_spam_direction(self,value: Optional[str] = None) -> None:
        """
        Sets the antiSpamDirection property value. Direction of the email relative to your network. The possible values are: inbound, outbound or intraorg.
        Args:
            value: Value to set for the anti_spam_direction property.
        """
        self._anti_spam_direction = value
    
    @property
    def attachments_count(self,) -> Optional[int]:
        """
        Gets the attachmentsCount property value. Number of attachments in the email.
        Returns: Optional[int]
        """
        return self._attachments_count
    
    @attachments_count.setter
    def attachments_count(self,value: Optional[int] = None) -> None:
        """
        Sets the attachmentsCount property value. Number of attachments in the email.
        Args:
            value: Value to set for the attachments_count property.
        """
        self._attachments_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AnalyzedMessageEvidence and sets the default values.
        """
        super().__init__()
        # Direction of the email relative to your network. The possible values are: inbound, outbound or intraorg.
        self._anti_spam_direction: Optional[str] = None
        # Number of attachments in the email.
        self._attachments_count: Optional[int] = None
        # Delivery action of the email. The possible values are: delivered, deliveredAsSpam, junked, blocked, or replaced.
        self._delivery_action: Optional[str] = None
        # Location where the email was delivered. The possible values are: inbox, external, junkFolder, quarantine, failed, dropped, deletedFolder or forwarded.
        self._delivery_location: Optional[str] = None
        # Public-facing identifier for the email that is set by the sending email system.
        self._internet_message_id: Optional[str] = None
        # Detected language of the email content.
        self._language: Optional[str] = None
        # Unique identifier for the email, generated by Microsoft 365.
        self._network_message_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The P1 sender.
        self._p1_sender: Optional[email_sender.EmailSender] = None
        # The P2 sender.
        self._p2_sender: Optional[email_sender.EmailSender] = None
        # Date and time when the email was received.
        self._received_date_time: Optional[datetime] = None
        # Email address of the recipient, or email address of the recipient after distribution list expansion.
        self._recipient_email_address: Optional[str] = None
        # IP address of the last detected mail server that relayed the message.
        self._sender_ip: Optional[str] = None
        # Subject of the email.
        self._subject: Optional[str] = None
        # Collection of methods used to detect malware, phishing, or other threats found in the email.
        self._threat_detection_methods: Optional[List[str]] = None
        # Collection of detection names for malware or other threats found.
        self._threats: Optional[List[str]] = None
        # Number of embedded URLs in the email.
        self._url_count: Optional[int] = None
        # Collection of the URLs contained in this email.
        self._urls: Optional[List[str]] = None
        # Uniform resource name (URN) of the automated investigation where the cluster was identified.
        self._urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnalyzedMessageEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedMessageEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AnalyzedMessageEvidence()
    
    @property
    def delivery_action(self,) -> Optional[str]:
        """
        Gets the deliveryAction property value. Delivery action of the email. The possible values are: delivered, deliveredAsSpam, junked, blocked, or replaced.
        Returns: Optional[str]
        """
        return self._delivery_action
    
    @delivery_action.setter
    def delivery_action(self,value: Optional[str] = None) -> None:
        """
        Sets the deliveryAction property value. Delivery action of the email. The possible values are: delivered, deliveredAsSpam, junked, blocked, or replaced.
        Args:
            value: Value to set for the delivery_action property.
        """
        self._delivery_action = value
    
    @property
    def delivery_location(self,) -> Optional[str]:
        """
        Gets the deliveryLocation property value. Location where the email was delivered. The possible values are: inbox, external, junkFolder, quarantine, failed, dropped, deletedFolder or forwarded.
        Returns: Optional[str]
        """
        return self._delivery_location
    
    @delivery_location.setter
    def delivery_location(self,value: Optional[str] = None) -> None:
        """
        Sets the deliveryLocation property value. Location where the email was delivered. The possible values are: inbox, external, junkFolder, quarantine, failed, dropped, deletedFolder or forwarded.
        Args:
            value: Value to set for the delivery_location property.
        """
        self._delivery_location = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "antiSpamDirection": lambda n : setattr(self, 'anti_spam_direction', n.get_str_value()),
            "attachmentsCount": lambda n : setattr(self, 'attachments_count', n.get_int_value()),
            "deliveryAction": lambda n : setattr(self, 'delivery_action', n.get_str_value()),
            "deliveryLocation": lambda n : setattr(self, 'delivery_location', n.get_str_value()),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "networkMessageId": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
            "p1Sender": lambda n : setattr(self, 'p1_sender', n.get_object_value(email_sender.EmailSender)),
            "p2Sender": lambda n : setattr(self, 'p2_sender', n.get_object_value(email_sender.EmailSender)),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipientEmailAddress": lambda n : setattr(self, 'recipient_email_address', n.get_str_value()),
            "senderIp": lambda n : setattr(self, 'sender_ip', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "threats": lambda n : setattr(self, 'threats', n.get_collection_of_primitive_values(str)),
            "threatDetectionMethods": lambda n : setattr(self, 'threat_detection_methods', n.get_collection_of_primitive_values(str)),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_primitive_values(str)),
            "urlCount": lambda n : setattr(self, 'url_count', n.get_int_value()),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internet_message_id(self,) -> Optional[str]:
        """
        Gets the internetMessageId property value. Public-facing identifier for the email that is set by the sending email system.
        Returns: Optional[str]
        """
        return self._internet_message_id
    
    @internet_message_id.setter
    def internet_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the internetMessageId property value. Public-facing identifier for the email that is set by the sending email system.
        Args:
            value: Value to set for the internet_message_id property.
        """
        self._internet_message_id = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. Detected language of the email content.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. Detected language of the email content.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def network_message_id(self,) -> Optional[str]:
        """
        Gets the networkMessageId property value. Unique identifier for the email, generated by Microsoft 365.
        Returns: Optional[str]
        """
        return self._network_message_id
    
    @network_message_id.setter
    def network_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the networkMessageId property value. Unique identifier for the email, generated by Microsoft 365.
        Args:
            value: Value to set for the network_message_id property.
        """
        self._network_message_id = value
    
    @property
    def p1_sender(self,) -> Optional[email_sender.EmailSender]:
        """
        Gets the p1Sender property value. The P1 sender.
        Returns: Optional[email_sender.EmailSender]
        """
        return self._p1_sender
    
    @p1_sender.setter
    def p1_sender(self,value: Optional[email_sender.EmailSender] = None) -> None:
        """
        Sets the p1Sender property value. The P1 sender.
        Args:
            value: Value to set for the p1_sender property.
        """
        self._p1_sender = value
    
    @property
    def p2_sender(self,) -> Optional[email_sender.EmailSender]:
        """
        Gets the p2Sender property value. The P2 sender.
        Returns: Optional[email_sender.EmailSender]
        """
        return self._p2_sender
    
    @p2_sender.setter
    def p2_sender(self,value: Optional[email_sender.EmailSender] = None) -> None:
        """
        Sets the p2Sender property value. The P2 sender.
        Args:
            value: Value to set for the p2_sender property.
        """
        self._p2_sender = value
    
    @property
    def received_date_time(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTime property value. Date and time when the email was received.
        Returns: Optional[datetime]
        """
        return self._received_date_time
    
    @received_date_time.setter
    def received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTime property value. Date and time when the email was received.
        Args:
            value: Value to set for the received_date_time property.
        """
        self._received_date_time = value
    
    @property
    def recipient_email_address(self,) -> Optional[str]:
        """
        Gets the recipientEmailAddress property value. Email address of the recipient, or email address of the recipient after distribution list expansion.
        Returns: Optional[str]
        """
        return self._recipient_email_address
    
    @recipient_email_address.setter
    def recipient_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientEmailAddress property value. Email address of the recipient, or email address of the recipient after distribution list expansion.
        Args:
            value: Value to set for the recipient_email_address property.
        """
        self._recipient_email_address = value
    
    @property
    def sender_ip(self,) -> Optional[str]:
        """
        Gets the senderIp property value. IP address of the last detected mail server that relayed the message.
        Returns: Optional[str]
        """
        return self._sender_ip
    
    @sender_ip.setter
    def sender_ip(self,value: Optional[str] = None) -> None:
        """
        Sets the senderIp property value. IP address of the last detected mail server that relayed the message.
        Args:
            value: Value to set for the sender_ip property.
        """
        self._sender_ip = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("antiSpamDirection", self.anti_spam_direction)
        writer.write_int_value("attachmentsCount", self.attachments_count)
        writer.write_str_value("deliveryAction", self.delivery_action)
        writer.write_str_value("deliveryLocation", self.delivery_location)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_str_value("language", self.language)
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_object_value("p1Sender", self.p1_sender)
        writer.write_object_value("p2Sender", self.p2_sender)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_str_value("recipientEmailAddress", self.recipient_email_address)
        writer.write_str_value("senderIp", self.sender_ip)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_primitive_values("threats", self.threats)
        writer.write_collection_of_primitive_values("threatDetectionMethods", self.threat_detection_methods)
        writer.write_collection_of_primitive_values("urls", self.urls)
        writer.write_int_value("urlCount", self.url_count)
        writer.write_str_value("urn", self.urn)
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. Subject of the email.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. Subject of the email.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def threat_detection_methods(self,) -> Optional[List[str]]:
        """
        Gets the threatDetectionMethods property value. Collection of methods used to detect malware, phishing, or other threats found in the email.
        Returns: Optional[List[str]]
        """
        return self._threat_detection_methods
    
    @threat_detection_methods.setter
    def threat_detection_methods(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the threatDetectionMethods property value. Collection of methods used to detect malware, phishing, or other threats found in the email.
        Args:
            value: Value to set for the threat_detection_methods property.
        """
        self._threat_detection_methods = value
    
    @property
    def threats(self,) -> Optional[List[str]]:
        """
        Gets the threats property value. Collection of detection names for malware or other threats found.
        Returns: Optional[List[str]]
        """
        return self._threats
    
    @threats.setter
    def threats(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the threats property value. Collection of detection names for malware or other threats found.
        Args:
            value: Value to set for the threats property.
        """
        self._threats = value
    
    @property
    def url_count(self,) -> Optional[int]:
        """
        Gets the urlCount property value. Number of embedded URLs in the email.
        Returns: Optional[int]
        """
        return self._url_count
    
    @url_count.setter
    def url_count(self,value: Optional[int] = None) -> None:
        """
        Sets the urlCount property value. Number of embedded URLs in the email.
        Args:
            value: Value to set for the url_count property.
        """
        self._url_count = value
    
    @property
    def urls(self,) -> Optional[List[str]]:
        """
        Gets the urls property value. Collection of the URLs contained in this email.
        Returns: Optional[List[str]]
        """
        return self._urls
    
    @urls.setter
    def urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the urls property value. Collection of the URLs contained in this email.
        Args:
            value: Value to set for the urls property.
        """
        self._urls = value
    
    @property
    def urn(self,) -> Optional[str]:
        """
        Gets the urn property value. Uniform resource name (URN) of the automated investigation where the cluster was identified.
        Returns: Optional[str]
        """
        return self._urn
    
    @urn.setter
    def urn(self,value: Optional[str] = None) -> None:
        """
        Sets the urn property value. Uniform resource name (URN) of the automated investigation where the cluster was identified.
        Args:
            value: Value to set for the urn property.
        """
        self._urn = value
    

