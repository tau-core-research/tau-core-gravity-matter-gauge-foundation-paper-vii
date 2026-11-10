"""Read-only receipt/manuscript consistency, not a replay of private science."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_hsl_receipt_and_bounded_manuscript():
    path = ROOT / 'data/derived/HSL_unequal_time_common_retarded_kernel.json'
    # apply_patch adds one final LF; the original exclusive receipt has none.
    assert hashlib.sha256(path.read_bytes().rstrip(b'\n')).hexdigest() == 'aff0d38f08698c5538429c0693136e1c5b494c5df5c1ae9cb07411a5f528af12'
    result = json.loads(path.read_text())['result']
    assert len(result['checks']) == 8 and all(result['checks'].values())
    assert 16 < result['refinement_ratio'] < 17
    assert result['max_state_transport_error'] < 1e-15
    text = (ROOT / 'paperVII_submission_source/main.tex').read_text()
    for marker in ['sec:finite-retarded-source', '16.4278', 'not as a portable replay', 'Volterra response remain open', 'original upper endpoint']:
        assert marker in text
