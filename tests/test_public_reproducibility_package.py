import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_publication_files_exist():
    for path in [
        "README.md",
        "CITATION.cff",
        "paperVII.pdf",
        "arxiv_submission_source.zip",
        "paperVII_submission_source/main.tex",
        "paperVII_submission_source/joint_terminal_main.tex",
        "paperVII_submission_source/dependency_certificate_body.tex",
        "paperVII_submission_source/refs.bib",
        "data/derived/joint_terminal_ledger_audit.json",
        "data/derived/theorem_certificates.json",
    ]:
        assert (ROOT / path).exists(), path


def test_scope_and_claim_boundary():
    main = (ROOT / "paperVII_submission_source/main.tex").read_text()
    body = (ROOT / "paperVII_submission_source/joint_terminal_main.tex").read_text()
    text = main + "\n" + body
    normalized = " ".join(text.split())
    for marker in [
        "Foundation Paper VII-A",
        "Inputs from earlier papers",
        "Conditional morphology-conditioned representation",
        "Same-reduct selection no-go",
        "Conditional ROOT--TT common preparation",
        "Exact source-rank criterion",
        "De-duplicated P1--ROOT rank",
        "Technical-paper handoffs",
        "joint-projective-body-connector",
        "does not quantize geometry",
        "Charged Hodge state and the common-cone boundary",
    ]:
        assert marker in text
    assert "common M4 metrological quotient" in normalized
    assert "do not construct a full projective/body measure connector" in normalized
    assert "may not add a separate spin-root selector or cone-matching gain" in normalized
    assert "does not assume that the physical base is homogeneous" in normalized
    assert "Support--port reconstruction and class-minimal enriched-law realization" not in body
    assert "Type does not imply occupation" not in body


def test_joint_terminal_ledger():
    data = json.loads((ROOT / "data/derived/joint_terminal_ledger_audit.json").read_text())
    assert data["verdict"].startswith("CONDITIONAL_COMMON_SOURCE_ASSEMBLY")
    assert data["duplicated_mode_stress_factor"] == 2
    assert data["quantized_geometry"] is False
    assembly = data["morphology_conditioned_assembly"]
    assert assembly["source_is_direct_sum"] is False
    assert assembly["terminal_maps_may_overlap_on_source"] is True
    assert assembly["terminal_specific_gain"] is False
    assert assembly["nature_selects_representation"] is False


def test_joint_terminal_numerical_certificates():
    data = json.loads((ROOT / "data/derived/theorem_certificates.json").read_text())
    assert data["verdict"] == "FINITE_THEOREM_WITNESSES_PASS"
    assert data["schur_witness"]["positive_schur"] is True
    assert data["root_tt"]["jacobian_rank"] == 2
    assert data["root_tt"]["certificate_rank"] == 2
    assert data["same_reduct_counterpair"]["same_physical_state"] is True


def test_arxiv_archive_is_self_contained():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as archive:
        names = set(archive.namelist())
    assert "main.tex" in names
    assert "joint_terminal_main.tex" in names
    assert "dependency_certificate_body.tex" in names
    assert "refs.bib" in names
    assert "appendices/p3_technical_derivations.tex" not in names
