from enum import Enum

class ManagedAppFlaggedReason(Enum):
    # No issue.
    None_ = "none",
    # The app registration is running on a rooted/unlocked device.
    RootedDevice = "rootedDevice",

