from enum import Enum

class DelegatedAdminRelationshipStatus(Enum):
    Activating = "activating",
    Active = "active",
    ApprovalPending = "approvalPending",
    Approved = "approved",
    Created = "created",
    Expired = "expired",
    Expiring = "expiring",
    Terminated = "terminated",
    Terminating = "terminating",
    TerminationRequested = "terminationRequested",
    UnknownFutureValue = "unknownFutureValue",

