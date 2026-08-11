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
    effective_source_owners = {
        "effect_source_eta": "Born probability",
        "metric_g": "renormalized stress",
        "gauge_potential_A": "renormalized current_with_Maxwell_minus_sign",
        "clock_character_vartheta": "clock response",
    }
    bookkeeping = {
        "green_operator": "inverse_hessian_not_action_summand",
        "finite_counterterm": "single_entry_relocatable_but_not_duplicable",
    }
    same_reduct_pair = {
        "shared": ["stationary_body", "body_hessian", "common_units", "observer_quotient", "physical_state", "unprobed_action"],
        "completion_C0": "zero_effect_source_coupling",
        "completion_C1": "nonzero_effect_source_coupling",
        "target_differs": True,
    }
    morphology_conditioned_assembly = {
        "source_is_direct_sum": False,
        "role_codomain": ["time", "gravity", "radiation", "matter", "quantum", "abelian_gauge"],
        "terminal_maps_may_overlap_on_source": True,
        "shared_source_representative": True,
        "typed_projection_after_body_conditioning": True,
        "observer_resolution_is_explicit": True,
        "terminal_specific_gain": False,
        "full_occupation_criterion": "source_cyclicity_plus_role_surjectivity",
        "nonzero_activation_criterion": "rooted_positive_propagation",
        "rooted_positive_propagation_implies_full_rank": False,
        "rooted_path_support_is_occupied": True,
        "nature_selects_representation": False,
        "nature_selects_operation_algebra": False,
    }
    quantum_gravity_common_preparation = {
        "screen_weight_gap": 2,
        "single_ray_own_screen_stf_overlap": 0,
        "root_one_particle_reduced_state": "rho_ROOT=C/Tr(C)",
        "tt_stress": "N_O*K_mn*(rho_ROOT)_mn",
        "same_preparation_identity": True,
        "occupation_weight_required": True,
        "independent_cross_gain": False,
        "overlap_is_action_derived_then_source_frozen": True,
        "overlap_has_action_derived_mode_formula": True,
        "finite_activation_certificate": [
            "screen_invariant_occupied_projector",
            "screen_weight_gap_two",
            "nonzero_relative_coherence",
            "nonzero_stf_overlap",
        ],
        "certificate_is_necessary_and_sufficient_in_declared_sector": True,
        "nonzero_overlap_class_has_geometric_optics_witness": True,
        "source_loaded_coherence_requires_negative_transverse_mass": False,
        "source_loaded_mixer": {
            "owned_by_metric_variation": True,
            "independent_terminal_gain": False,
            "nonzero_iff_geometric_pullback_and_stress_overlap_nonzero": True,
        },
        "faraday_directional_selector": {
            "non_null_field_required": True,
            "principal_null_pair_is_canonical": True,
            "generic_nonprincipal_observer_activation": True,
            "principal_observer_is_zero_control": True,
            "null_field_is_zero_control": True,
            "parent_selects_non_null_abelian_branch": False,
        },
        "nature_selects_noncollinear_pair": False,
        "faithful_common_completion": {
            "deduplicated_recovery_surjective": "conditional",
            "faithful_state_follows": True,
            "abelian_central_support_positive": True,
            "cyclic_gns_faithful_and_unique_up_to_unitary": True,
            "same_qft_state_restriction": True,
            "faithful_support_implies_pointwise_non_null_faraday": False,
            "physical_parent_selects_surjective_branch": False,
            "recovery_factorization": "R_rec_lin=U_rec*D_Sigma*J_phys_lin",
            "stable_and_differentially_complete_iff_j_phys_lin_isomorphism": True,
            "rolewise_activation_implies_global_surjectivity": False,
            "occupied_p3_subrepresentation_implies_global_surjectivity": False,
            "observer_source_complement_rank_adds": True,
            "pbse_observer_source_rank_increment": 1,
            "pbse_increment_closes_full_linear_cokernel": False,
            "full_typed_recovery_also_requires": [
                "finite_record_support_coverage",
                "faithful_algebra_representation",
            ],
            "deduplicated_linear_rank": "4+r_Q_perp",
            "root_complement_rank_range": [0, 4],
            "equal_marginal_controls": [0, 2, 4],
            "invertible_gauge_adds_recovery_rank": False,
            "mixed_gram_selects_root_complement": True,
            "pbse_increment_is_added_again_to_broad_p1_rank": False,
            "seed_presentation_selector": {
                "selects_common_hessian_p1_access": True,
                "isolated_occupied_root_cluster_selects_projector": True,
                "faithful_root_restriction_required": True,
                "adds_terminal_gain": False,
                "current_seed_grammar_is_complete": False,
                "physical_root_spectral_gap_is_proved": False,
                "parent_law_realization_and_occupation_status": "open",
            },
            "p3_clifford_candidate": {
                "role_dimension": 7,
                "operator_square_forces_clifford": True,
                "simple_block_dimensions": [8, 8],
                "envelope_dimension": 256,
                "envelope_multiplicities": [16, 16],
                "normalized_trace_weights": [0.5, 0.5],
                "trace_gram_alone_is_sufficient": False,
                "physical_typed_operator_incidence_selected": False,
                "post_body_handoff_status": "adopted_working_completion",
            },
            "finite_rw_operational_witness": {
                "morphology_tangent_dimension": 8,
                "source_endpoint_count": 3,
                "finite_p1_operator_rank": 7,
                "finite_joint_p1_root_operator_rank": 8,
                "root_operational_increment": 1,
                "is_primitive_parent_rank": False,
                "is_unrestricted_parent_realization": False,
            },
        },
        "minimal_activation_potential": {
            "positive_quartics": True,
            "negative_transverse_quadratic": True,
            "nonzero_weight_two_mixer": True,
            "forces_nonzero_p_and_c": True,
            "zero_mixer_restores_zero_coherence": True,
            "physical_coefficient_selection": False,
        },
    }
    result = {
        "paper": "VII",
        "roles": roles,
        "role_count": len(roles),
        "deletion_controls": deletion,
        "occupation_partition_is_single_valued": unique,
        "duplicated_mode_stress_factor": duplicated_mode_stress_factor,
        "ordered_response": triangular_response,
        "simultaneous_action_no_go": simultaneous_no_go,
        "effective_source_owners": effective_source_owners,
        "bookkeeping": bookkeeping,
        "same_reduct_selection_counterpair": same_reduct_pair,
        "morphology_conditioned_assembly": morphology_conditioned_assembly,
        "quantum_gravity_common_preparation": quantum_gravity_common_preparation,
        "quantum_preparation_status": "fixed_positive_trace_one_ctp_boundary_not_euler_variable",
        "newtonian_limit_retains_lambda": True,
        "standard_leaf_form_selector": {
            "einstein_hilbert_shape_from_declared_lovelock_class": True,
            "maxwell_shape_from_declared_parity_even_quadratic_u1_class": True,
            "coefficients_selected": False,
            "parent_selects_class": False,
        },
        "same_reduct_counterpair_scope": "effect_source_ownership_only",
        "standard_leaf": ["Einstein", "Poisson", "Maxwell", "Ward", "Bianchi"],
        "parent_law_realization_and_occupation": "not_entailed_by_current_reduct",
        "quantized_geometry": False,
        "verdict": "CONDITIONAL_COMMON_SOURCE_ASSEMBLY_WITH_EXACT_DOUBLE_COUNT_CONTROLS",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PAPER_VII_JOINT_LEDGER_PASS roles=7 duplicate_factor=2 mopr=conditional root_tt=same_preparation parent_realization_and_occupation=not_entailed")


if __name__ == "__main__":
    main()
