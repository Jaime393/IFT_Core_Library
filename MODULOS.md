# MÓDULOS — Jaime393/IFT_Core_Library

Archivo nuevo, aditivo. Índice de los módulos de `ift/` con las clases, funciones y métodos leídos en la minería, los literales numéricos escritos en cada archivo y los umbrales de `tests/test_all.py`.

- Repo: `Jaime393/IFT_Core_Library`, último commit verificado `9cac07dd28ae1475f90e0088babefff3d4283b9a` (2026-07-10).
- Fuente: minería local de solo lectura de 2026-11-08 (`~/workspace/mineria/IFT_Core_Library/MINERIA.md`, Parte 1 EXPORTABLE), por lectura de texto de las URLs raw de cada archivo en ese commit. Cuando aquí se dice que un archivo "escribe" algo, el dato verificado es que ese texto está en el archivo leído.

## Punto de entrada del paquete: `ift/__init__.py` (2.441 bytes, 159 líneas leídas)

- Escribe `__version__ = "1.0.0"`, `__author__ = "Juan Diego Vicente Gabancho"`, `__date__ = "April 2, 2026"`, `__license__ = "MIT"`.
- Importa `FisherMetric, spacetime_from_information`, `ParticleMassSpectrum, solve_eigenvalue_problem`, `GaugeStructure, yang_mills_from_phase`, `Cosmology, friedmann_equations`, `FundamentalConstants, verify_all_constants`, `QuantumBiology, coherence_super_ohmic`.
- Define `verify_core_predictions()`, que instancia `FundamentalConstants` y llama `verify_all()`, instancia `ParticleMassSpectrum` y llama `verify_lepton_hierarchy()`, e instancia `Cosmology()` y llama `verify_hubble()`.

## `ift/constants.py` (10.206 bytes, 637 líneas leídas)

- Clase `FundamentalConstants`.
- Constantes SI escritas: `hbar = 1.054571817e-34`, `c = 299792458`, `G = 6.67430e-11`, `e = 1.602176634e-19`, `eps0 = 8.8541878128e-12`, `k_B = 1.380649e-23`.
- Diccionario `pdg_constants` con 14 entradas, entre ellas `alpha_inv: (137.035898, 0.000008)`, `alpha_s: (0.1180, 0.0002)`, `electron_mass: (0.5109989461e-3, ...)`, `muon_mass: (105.6583745e-3, ...)`, `tau_mass: (1776.86e-3, ...)`, `m_W: (80.360, 0.013)`, `m_Z: (91.1876, 0.0021)`, `m_H: (125.10, 0.14)`.
- Métodos: `fine_structure_constant()`, `electron_mass_tci()`, `muon_mass_tci()`, `tau_mass_tci()`, `w_mass_tci()`, `z_mass_tci()`, `cosmological_constant()`, `newton_constant()`, `verify_all()`.
- En `muon_mass_tci()` y `tau_mass_tci()` escribe los literales `xi = 7.626` y `beta = 1.601`, y la fórmula `m_0 * np.cosh(n*xi) * np.exp(-beta*n**2)`.
- En `verify_all()` construye un diccionario `results` con 8 entradas: `Fine Structure`, `Electron Mass`, `Muon Mass`, `Tau Mass`, `W Boson`, `Z Boson`, `Cosmological Λ`, `Newton G`.
- En `cosmological_constant()` escribe `Lambda_obs = 1.089e-52`, `rho_vac = 1.0` y `Lambda_tci_inv_m2 = 1.088e-52`.
- En `newton_constant()` escribe el comentario `This is the defining relationship, automatically satisfied` y calcula `G_tci = (self.c**3 * self.ell_P**2) / self.hbar`.

## `ift/fisher_metric.py` (8.096 bytes, 548 líneas leídas)

- Cita como referencias a Chentsov (1972), Amari (2016) y Matsueda (2013).
- Clases `FisherMetric` y `QuantumCorrelationDistance`; función `spacetime_from_information(rho_func, x_range, n_points=1000)`.
- `FisherMetric` define `planck_length()`, `planck_mass()`, `fisher_metric_from_density()`, `isotropic_frlw_metric()`, `schwarzschild_metric_recovery()`, `ricci_scalar_from_information()` y `cotton_tensor_from_information()`.
- `QuantumCorrelationDistance` define `correlation_decay()`, `information_distance()` y `kullback_leibler_distance()`.
- En `schwarzschild_metric_recovery()` escribe `g_phi_phi = r**2 * np.sin(np.radians(45))**2  # At equator`.

## `ift/eigensolve.py` (10.699 bytes, 682 líneas leídas)

- Clase `ParticleMassSpectrum`; función `solve_eigenvalue_problem(rho_field, coordinate_grid, n_eigenvalues=5, boundary='dirichlet')`.
- `ParticleMassSpectrum` define `eigenvalues_s3_manifold()`, `laplacian_eigenvalue_problem()`, `hyperbolic_mass_formula()`, `verify_lepton_hierarchy()`, `quark_mass_spectrum()`, `bosonic_mass_spectrum()` y `mass_hierarchy_ratio()`.
- En `eigenvalues_s3_manifold()` escribe el comentario `# Scale factor fitted to electron mass` junto a `a_scale = 2.612e-8`.
- En `hyperbolic_mass_formula()` escribe en su docstring `Only TWO parameters fitted to three lepton masses`.
- En `quark_mass_spectrum()` escribe las masas `up: 2.16e-3`, `down: 4.67e-3`, `charm: 1.27`, `strange: 93.1e-3`, `top: 172.69`, `bottom: 4.18` (GeV); en `bosonic_mass_spectrum()`, `photon: 0.0`, `z_boson: 91.188`, `w_boson: 80.360`, `higgs_boson: 125.10`, `gluon: 0.0`.

## `ift/gauge_structure.py` (12.754 bytes, 740 líneas leídas)

- Clase `GaugeStructure`; función `yang_mills_from_phase(phase_field_dict, gauge_group='U(1)')`.
- `GaugeStructure.__init__` escribe `self.alpha = 1/137.036`, `self.alpha_s = 0.1180`, `self.sin2_theta_w = 0.2312`, `self.g = 0.6517`, `self.g_prime = 0.3576`.
- `GaugeStructure` define `u1_gauge_transformation()`, `su2_gauge_transformation()`, `su3_gauge_transformation()`, `standard_model_gauge_group()`, `topological_charges()`, `confinement_from_phase_coherence()`, `_gellmann_matrices()`, `coupling_constant_running()` y `verify_standard_model_couplings()`.
- En `su2_gauge_transformation()` escribe `raise ValueError("SU(2) requires 3 phase fields")` y en `su3_gauge_transformation()` escribe `raise ValueError("SU(3) requires 8 phase fields")`.
- En `standard_model_gauge_group()` escribe `'n_gauge_bosons': 12` y la lista `['8 gluons (SU(3))', 'W⁺, W⁻, Z (SU(2))', 'γ (U(1))']`.
- En `verify_standard_model_couplings()` escribe las comparaciones `α⁻¹ (QED): (137.036, 137.035898)`, `α_s (QCD): (0.1180, 0.1180)`, `sin²θ_W: (0.23120, 0.23121)`.

## `ift/cosmology.py` (10.569 bytes, 678 líneas leídas)

- Clase `Cosmology`; función `friedmann_equations(model='LCDM', z_array=None)`.
- `Cosmology.__init__` escribe `H0_planck = 67.4`, `H0_local = 73.0`, `Omega_b = 0.04897`, `Omega_c = 0.26335`, `Omega_l = 0.68768`, `Omega_r = 4.18e-5`, `h = 0.6736`, y acepta `cosmology_model='LCDM'`, `kappa=0` y `anisotropy_params` con `a1, a2, a3`.
- `Cosmology` define `E_z_lcdm()`, `H_z_lcdm()`, `anisotropy_correction()`, `E_z_ift()`, `H_z_ift()`, `H_z()`, `luminosity_distance()`, `comoving_distance()`, `verify_hubble()`, `age_of_universe()`, `recombination_redshift()`, `dark_energy_equation_of_state()` y `summary()`.
- En `age_of_universe()` escribe `age_gyr = 13.8  # From Planck 2024` y en `recombination_redshift()` escribe `z_rec = 1089.92  # Planck 2024 value`.
- En `verify_hubble()` escribe `Tension: 5.2σ discrepancy` y usa los redshifts `[0, 0.04, 0.5, 2.0, 10.0, 100.0, 1100.0]`.
- En el bloque de prueba del archivo instancia `Cosmology(cosmology_model='IFT', kappa=1.8e-14, anisotropy_params={'a1': 1.2e-3, 'a2': 8e-4, 'a3': 5e-4})`.

## `ift/quantum_biology.py` (6.705 bytes, 401 líneas leídas)

- Clase `QuantumBiology`; función `coherence_super_ohmic(temperature=300, s_exponent=3)`.
- `QuantumBiology` define `lindblad_bath_coupling()`, `decoherence_time_tci()`, `super_ohmic_universal()`, `fmo_complex_detailed()` y `coherence_comparison_table()`; en el texto leído no aparecen métodos llamados `si_qubits_detail` ni `quantum_advantage_calculation`.
- `QuantumBiology.__init__` escribe un diccionario `systems` con una sola entrada, `fmo`, con `tau_measured_fs: 396`, `temperature: 300`, `mechanism: 'Super-ohmic bath (s=3)'`, `reference: 'Engel et al. 2007'`.
- En `decoherence_time_tci()` escribe `omega_c = 1e13  # Hz`, `J = 1.0`, `gamma = 0.5`, `s = 3`, y los comentarios `# 🔧 Escala física consistente (Hz)`, `# 🔧 Conversión a cm⁻¹ (lo que espera el test)` y `# 🔧 Nunca devolver None`; para un sistema desconocido devuelve `tau_tci: 0.0` y `error_pct: 100.0`.
- En `super_ohmic_universal()` escribe la tabla de 4 sistemas: `FMO photosynthesis 396 fs s = 3.0`, `LH2 antenna 300 fs s = 2.8`, `DNA breathing 5-10 ns s = 2.2`, `Si-28 qubits 28 ms s > 3.5`.

## Umbrales de `tests/test_all.py` (6.623 bytes, 412 líneas leídas)

- Define 6 funciones de test (`test_constants`, `test_particle_masses`, `test_gauge_structure`, `test_cosmology`, `test_quantum_biology`, `test_integration`) y `run_all_tests()`, que imprime `Tests passed: {passed}/{total}` y `✓✓✓ ALL TESTS PASSED ✓✓✓` si pasan todos.
- Umbrales escritos en los asserts: error de α < 0.01, error de Λ < 0.5, error de G < 0.1, error medio de la jerarquía de leptones < 3.0, H0 ΛCDM a menos de 1 de 67.4, error FMO < 20.
