import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_publication_files_exist():
    for path in ["README.md", "paperVII.pdf", "arxiv_submission_source.zip",
                 "paperVII_submission_source/main.tex", "paperVII_submission_source/refs.bib"]:
        assert (ROOT / path).exists(), path


def test_claim_boundaries_and_title():
    tex = (ROOT / "paperVII_submission_source/main.tex").read_text()
    assert "Gravity, Matter, and Abelian Gauge Terminals" in tex
    assert "does not quantize geometry" in tex
    assert "present Tau source laws do not entail occupation" in tex
    assert "Duplicate-stress no-go" in tex
    assert "Effective common-source construction" in tex
    assert "Same-reduct selection no-go" in tex


def test_audit_ledger():
    data = json.loads((ROOT / "data/derived/joint_terminal_ledger_audit.json").read_text())
    assert data["role_count"] == 7
    assert data["duplicated_mode_stress_factor"] == 2
    assert data["nature_selection"] == "not_entailed_by_current_reduct"
    assert data["quantized_geometry"] is False
    assert data["effective_source_owners"]["metric_g"] == "renormalized stress"
    assert data["bookkeeping"]["green_operator"] == "inverse_hessian_not_action_summand"
    assert data["same_reduct_selection_counterpair"]["target_differs"] is True


def test_arxiv_archive_is_source_only():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = zf.namelist()
    assert "main.tex" in names and "refs.bib" in names
    assert "figures/fig_joint_ledger.pdf" in names
    assert not any(name.endswith("main.pdf") for name in names)
