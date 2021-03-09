from doing.utils import run_command


def get_iterations(team_id: str, project: str, organization: str):
    """
    Find iterations belonging to a certain team.

    Example:

    ```python
    team_id = "Your team name"
    get_iterations(team_id)
    ```
    """
    assert team_id.startswith("T")

    az_cmd = f"az boards iteration team list --team '{team_id}' --org '{organization}' --p '{project}'"
    # From the team, find all iterations
    all_iterations = run_command(az_cmd)

    return [i.get("name") for i in all_iterations]
