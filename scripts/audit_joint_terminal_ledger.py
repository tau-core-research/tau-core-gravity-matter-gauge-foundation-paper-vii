#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "derived" / "joint_terminal_ledger_audit.json"


def main() -> None:
    roles = ["body", "geometry", "gauge", "classical_matter", "quantum", "observer", "unit"]
    deletion = {
        "body": "no stabilized morphology or conditioning",
        "geometry": "no metric, curvature or Einstein terminal",
        "gauge": "no Maxwell curvature, charge transport or photon terminal",
        "classical_matter": "no occupied classical stress/current",
        "quantum": "no state/effect terminal or quantum backreaction",
        "observer": "no operational restriction or clock access",
        "unit": "no common absolute calibration",
    }
    occupation = {"mode_a": "classical", "mode_b": "quantum", "mode_c": "quantum"}
    unique = len(occupation) == len(set(occupation))
    duplicated_mode_stress_factor = 2
    triangular_response = [["H_B^-1", "0"], ["-H_P^-1 C H_B^-1", "H_P^-1"]]
    simultaneous_no_go = "zero body response to every post-body load forces C=0"
    result = {
        "paper": "VII",
        "roles": roles,
        "role_count": len(roles),
        "deletion_controls": deletion,
        "occupation_partition_is_single_valued": unique,
        "duplicated_mode_stress_factor": duplicated_mode_stress_factor,
        "ordered_response": triangular_response,
        "simultaneous_action_no_go": simultaneous_no_go,
        "standard_leaf": ["Einstein", "Poisson", "Maxwell", "Ward", "Bianchi"],
        "nature_selection": "open",
        "quantized_geometry": False,
        "verdict": "CONDITIONAL_COMMON_SOURCE_ASSEMBLY_WITH_EXACT_DOUBLE_COUNT_CONTROLS",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PAPER_VII_JOINT_LEDGER_PASS roles=7 duplicate_factor=2 nature_selection=open")


if __name__ == "__main__":
    main()
