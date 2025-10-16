import argparse
import json
import sys
import time
import random

def main():
    """
    Parses command-line arguments, simulates a long-running task,
    and prints a JSON result to standard output.
    """
    parser = argparse.ArgumentParser(description='Simulate a complex biomedical task.')
    parser.add_argument('molecule_id', type=str, help='The ID of the molecule to analyze.')
    args = parser.parse_args()

    if not args.molecule_id:
        print("Error: molecule_id argument is required.", file=sys.stderr)
        sys.exit(1)

    print(f"Starting analysis for {args.molecule_id}...")

    # Simulate a long-running task
    sleep_duration = random.randint(10, 15)
    time.sleep(sleep_duration)

    print("Computation complete.")

    # Prepare the structured result
    result = {
        "molecule_id": args.molecule_id,
        "status": "SUCCESS",
        "data": {
            "screening_result": f"High Affinity (DO Score {random.randint(80, 95)}%)"
        }
    }

    # Output the result as a single-line JSON string
    print(json.dumps(result))

if __name__ == '__main__':
    main()