import argparse
import json
import sys
import time
import random

def main():
    """
    Simulates a complex biomedical task, accepting a molecule ID from the
    command line, simulating a long-running computation, and printing a JSON
    result to stdout.
    """
    parser = argparse.ArgumentParser(description="Simulated biomedical compute task.")
    parser.add_argument(
        "molecule_id",
        type=str,
        help="The identifier for the molecule to be analyzed."
    )
    args = parser.parse_args()

    molecule_id = args.molecule_id

    # The argparse setup ensures that if the argument is not provided,
    # it will exit before this point with an informative error message.
    # However, an explicit check can be added if needed.

    print(f"Starting analysis for {molecule_id}...")

    # Simulate a long-running task
    sleep_duration = random.randint(10, 15)
    print(f"Simulating computation for {sleep_duration} seconds...")
    time.sleep(sleep_duration)

    print("Computation complete.")

    # Prepare the structured JSON output
    output_data = {
        "molecule_id": molecule_id,
        "status": "SUCCESS",
        "data": {
            "screening_result": f"High Affinity (DO Score {random.randint(80, 95)}%)"
        }
    }

    # Output the result as a single-line JSON string
    print(json.dumps(output_data))

if __name__ == "__main__":
    main()
