from ..._vendor.types import SimpleNamespace


class HOOKS(SimpleNamespace):
    PROFILE_UNLOAD: str = "unloadProfile"
    PROFILE_LOADED: str = "profileLoaded"
