class DevOpsError(Exception):
    """Base exception for DevOps automation errors."""
    pass


class DeploymentError(DevOpsError):
    """Raised when a deployment configuration is invalid."""
    def __init__(self, message="Deployment failed"):
        super().__init__(message)
        self.message = message


class KubernetesError(DevOpsError):
    """Raised for Kubernetes-related failures."""
    pass


class AWSConnectionError(DevOpsError):
    """Raised when connecting to AWS fails."""
    pass


replicas = 0
if replicas <= 0:
    raise DeploymentError("Replica count must be greater than zero")


# DevOpsError
# │
# ├── DeploymentError
# ├── KubernetesError
# └── AWSConnectionError