class ResourceExistsError(RuntimeError):
    """
    This class signifies the errors caused when a particular resource already exists
    """
    def __init__(self, msg: str):
        super().__init__(msg)

