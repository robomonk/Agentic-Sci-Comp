
import uuid
from google.cloud import batch_v1
from google_adk.tools import AgentTool, ToolDefinition

def submit_molecular_screening_job(project_id: str, location: str, molecule_id: str) -> str:
    """
    Submits a molecular screening job to Google Cloud Batch.

    Args:
        project_id: The Google Cloud project ID.
        location: The Google Cloud region or zone for the job.
        molecule_id: The ID of the molecule to be screened.

    Returns:
        The resource name of the created Batch job.
    """
    batch_client = batch_v1.BatchServiceClient()

    # Define the container runnable
    runnable = batch_v1.Runnable()
    runnable.container = batch_v1.Runnable.Container()
    # Replace with your actual image URI from Artifact Registry
    runnable.container.image_uri = f"us-central1-docker.pkg.dev/{project_id}/tx-agent-repo/tooluniverse-hpc:latest"
    runnable.container.commands = ["python", "batch_runner.py", molecule_id]

    # Define the task spec
    task = batch_v1.TaskSpec()
    task.runnables = [runnable]

    # Define the logs policy
    logs_policy = batch_v1.LogsPolicy()
    logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING
    task.logs_policy = logs_policy

    # Create a task group
    group = batch_v1.TaskGroup()
    group.task_count = 1
    group.task_spec = task

    # Define the job
    job = batch_v1.Job()
    job.task_groups = [group]
    job.allocation_policy = batch_v1.AllocationPolicy()
    job.allocation_policy.instances = [batch_v1.AllocationPolicy.InstancePolicyOrTemplate()]
    job.logs_policy = logs_policy

    # Create a unique job ID
    job_id = f"tx-agent-job-{uuid.uuid4()}"

    # Create the job request
    request = batch_v1.CreateJobRequest()
    request.parent = f"projects/{project_id}/locations/{location}"
    request.job_id = job_id
    request.job = job

    # Create the job
    created_job = batch_client.create_job(request=request)

    return created_job.name

# Create the AgentTool
TherapeuticComputeTool = AgentTool.from_callable(
    tool_definition=ToolDefinition(
        name="submit_molecular_screening_job",
        description="Submits a heavy computational job for molecular screening and returns a job_name for tracking.",
        parameters={
            "project_id": {"type": "string", "description": "The Google Cloud project ID."},
            "location": {"type": "string", "description": "The Google Cloud region for the job."},
            "molecule_id": {"type": "string", "description": "The ID of the molecule to screen."}
        }
    ),
    callable_fn=submit_molecular_screening_job
)

if __name__ == "__main__":
    # Replace with your actual project ID and location
    PROJECT_ID = "gcp-project-id"
    LOCATION = "us-central1"
    MOLECULE_ID = "MOL-XYZ-123"

    print(f"Submitting job for molecule: {MOLECULE_ID}")
    job_name = submit_molecular_screening_job(PROJECT_ID, LOCATION, MOLECULE_ID)
    print(f"Job created: {job_name}")
