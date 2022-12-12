class ResourceNotFoundError(RuntimeError):
    """
    This class signifies the errors caused when a particular resource is not found
    """
    def __init__(self, msg: str):
        super().__init__(msg)

