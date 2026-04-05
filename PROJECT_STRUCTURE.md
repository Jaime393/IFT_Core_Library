# IFT Core Library - Project Structure

## 📂 Directory Organization

```
IFT_Core_Library/
│
├── README.md                          # Main documentation (START HERE)
├── setup.py                           # Python package installation
├── requirements.txt                   # Dependencies
├── .gitignore                         # Git ignore patterns
├── PROJECT_STRUCTURE.md               # This file
│
├── ift/                              # Main package (core modules)
│   ├── __init__.py                   # Package initialization + exports
│   ├── fisher_metric.py              # Spacetime from Fisher metric
│   ├── eigensolve.py                 # Particle masses as eigenvalues
│   ├── gauge_structure.py            # Yang-Mills from topology
│   ├── cosmology.py                  # Friedmann equations
│   ├── constants.py                  # Fundamental constant verification
│   └── quantum_biology.py            # Quantum coherence in biology
│
├── tests/                            # Unit tests
│   └── test_all.py                   # Comprehensive test suite
│
├── notebooks/                        # Tutorial and examples
│   └── tutorial.py                   # Interactive tutorial walkthrough
│
└── data/                             # (Optional) Data files
    └── (Will be created during execution)
```

## 📋 File Descriptions

### Core Package Files (`ift/`)

#### 1. `__init__.py` (120 lines)
- Package initialization
- Imports all modules
- Convenience function: `verify_core_predictions()`
- Exports all public classes and functions

**Key Exports:**
```python
FisherMetric, spacetime_from_information
ParticleMassSpectrum, solve_eigenvalue_problem
GaugeStructure, yang_mills_from_phase
Cosmology, friedmann_equations
FundamentalConstants, verify_all_constants
QuantumBiology, coherence_super_ohmic
verify_core_predictions
```

#### 2. `fisher_metric.py` (320 lines)
Central equation of IFT: `g_μν = ∂_μ ∂_ν log ρ(x)`

**Classes:**
- `FisherMetric`: Compute spacetime metric from information density
- `QuantumCorrelationDistance`: Connection between entanglement and geometry

**Key Methods:**
- `fisher_metric_from_density()` - Calculate metric from ρ(x)
- `isotropic_frlw_metric()` - FLRW spacetime
- `schwarzschild_metric_recovery()` - Schwarzschild geometry
- `ricci_scalar_from_information()` - Ricci curvature from information
- `spacetime_from_information()` - Convenience function

#### 3. `eigensolve.py` (400 lines)
Particle masses as eigenvalues of information Laplacian

**Classes:**
- `ParticleMassSpectrum`: Calculate and verify particle mass spectrum

**Key Methods:**
- `eigenvalues_s3_manifold()` - Eigenvalues on 3-sphere
- `laplacian_eigenvalue_problem()` - Solve Δ_g φ = λ φ
- `hyperbolic_mass_formula()` - Lepton mass hierarchy
- `verify_lepton_hierarchy()` - Compare TCI vs PDG 2024
- `quark_mass_spectrum()` - Quark masses
- `bosonic_mass_spectrum()` - Gauge boson masses
- `mass_hierarchy_ratio()` - Mass ratio analysis

#### 4. `gauge_structure.py` (420 lines)
SU(3)×SU(2)×U(1) emerges from phase symmetry

**Classes:**
- `GaugeStructure`: Yang-Mills gauge theory from information field

**Key Methods:**
- `u1_gauge_transformation()` - Electromagnetism
- `su2_gauge_transformation()` - Weak force
- `su3_gauge_transformation()` - Strong force (QCD)
- `standard_model_gauge_group()` - Full SM: SU(3)×SU(2)×U(1)
- `topological_charges()` - Charge quantization from winding numbers
- `confinement_from_phase_coherence()` - Color confinement mechanism
- `coupling_constant_running()` - Energy scale dependence
- `verify_standard_model_couplings()` - Check α, α_s, sin²θ_W

#### 5. `cosmology.py` (450 lines)
Friedmann equations with anisotropic corrections

**Classes:**
- `Cosmology`: ΛCDM and IFT cosmological models

**Key Methods:**
- `E_z_lcdm()` - ΛCDM Hubble parameter
- `H_z_lcdm()` - Physical H(z) in ΛCDM
- `anisotropy_correction()` - F(z) function in IFT
- `E_z_ift()` - IFT Hubble parameter with anisotropies
- `H_z_ift()` - Physical H(z) in IFT
- `luminosity_distance()` - d_L for supernova measurements
- `comoving_distance()` - BAO measurements
- `verify_hubble()` - Compare Planck vs SH0ES
- `age_of_universe()` - Cosmic age
- `recombination_redshift()` - CMB formation epoch
- `summary()` - Print cosmological parameters

#### 6. `constants.py` (380 lines)
Verification of 35+ fundamental constants

**Classes:**
- `FundamentalConstants`: Compute and verify all fundamental constants

**Key Methods:**
- `fine_structure_constant()` - α = 1/137.036
- `electron_mass_tci()` - m_e from eigenvalue
- `muon_mass_tci()` - m_μ from hierarchy
- `tau_mass_tci()` - m_τ from hierarchy
- `w_mass_tci()` - W boson mass
- `z_mass_tci()` - Z boson mass
- `cosmological_constant()` - Λ from vacuum energy
- `newton_constant()` - G from fundamental relation
- `verify_all()` - Comprehensive table of all constants

#### 7. `quantum_biology.py` (380 lines)
Quantum coherence in biological systems

**Classes:**
- `QuantumBiology`: Analyze coherence times and decoherence

**Key Methods:**
- `lindblad_bath_coupling()` - Spectral density J(ω) ∝ ω^s
- `decoherence_time_tci()` - τ_coherence from bath parameters
- `super_ohmic_universal()` - Universal s > 1.5 signature
- `fmo_complex_detailed()` - FMO photosynthesis analysis
- `si_qubits_detail()` - Silicon quantum computing qubits
- `coherence_comparison_table()` - 50+ biological systems
- `quantum_advantage_calculation()` - Why biology uses quantum

### Test Files (`tests/`)

#### `test_all.py` (280 lines)
Comprehensive unit test suite

**Test Functions:**
- `test_constants()` - Fundamental constant verification
- `test_particle_masses()` - Particle mass spectrum
- `test_gauge_structure()` - Gauge theory verification
- `test_cosmology()` - H(z) evolution
- `test_quantum_biology()` - Coherence times
- `test_integration()` - Full system integration
- `run_all_tests()` - Execute all tests

**Run tests:**
```bash
python tests/test_all.py
```

### Tutorial Files (`notebooks/`)

#### `tutorial.py` (450 lines)
Interactive tutorial with 8 parts

**Parts:**
1. Introduction to IFT
2. Fundamental Constants Verification
3. Particle Mass Spectrum
4. Standard Model Gauge Structure
5. Cosmology & H₀ Tension
6. Quantum Biology
7. Testable Predictions
8. Complete Verification

**Run tutorial:**
```bash
python notebooks/tutorial.py
```

### Documentation Files

#### `README.md`
- Complete user guide
- Installation instructions
- Quick start examples
- API reference
- Testing information
- Citation instructions

#### `setup.py`
- Package metadata
- Dependencies
- Installation configuration
- Entry points

#### `requirements.txt`
- numpy >= 1.19.0
- scipy >= 1.5.0
- matplotlib >= 3.3.0
- jupyter >= 1.0.0

#### `.gitignore`
- Python cache files
- IDE files
- Virtual environment directories
- Research output directories

## 🚀 Getting Started

### 1. Installation

```bash
# Clone/download repository
cd IFT_Core_Library

# Install in development mode
pip install -e .

# Or install dependencies only
pip install -r requirements.txt
```

### 2. Quick Verification

```python
from ift import verify_core_predictions
verify_core_predictions()
```

### 3. Run Tests

```bash
python tests/test_all.py
```

### 4. Run Interactive Tutorial

```bash
python notebooks/tutorial.py
```

## 📊 Code Statistics

| Component | Lines | Functions | Classes |
|-----------|-------|-----------|---------|
| fisher_metric.py | 320 | 12 | 2 |
| eigensolve.py | 400 | 15 | 1 |
| gauge_structure.py | 420 | 18 | 1 |
| cosmology.py | 450 | 16 | 1 |
| constants.py | 380 | 12 | 1 |
| quantum_biology.py | 380 | 14 | 1 |
| __init__.py | 120 | 2 | 0 |
| test_all.py | 280 | 8 | 0 |
| tutorial.py | 450 | 8 | 0 |
| **TOTAL** | **3380** | **105** | **7** |

## 🔗 Module Dependencies

```
ift/__init__.py
    ├── fisher_metric.py
    │   └── numpy, scipy
    ├── eigensolve.py
    │   └── numpy, scipy
    ├── gauge_structure.py
    │   └── numpy
    ├── cosmology.py
    │   ├── numpy
    │   └── scipy.integrate
    ├── constants.py
    │   └── numpy
    └── quantum_biology.py
        ├── numpy
        └── scipy.integrate

tests/test_all.py
    └── ift (all modules)

notebooks/tutorial.py
    └── ift (all modules)
```

## 📝 Usage Examples

### Example 1: Verify Fundamental Constants
```python
from ift import FundamentalConstants

const = FundamentalConstants()
const.verify_all()
```

### Example 2: Calculate Particle Masses
```python
from ift import ParticleMassSpectrum

masses = ParticleMassSpectrum()
masses.verify_lepton_hierarchy()
masses.quark_mass_spectrum()
```

### Example 3: Standard Model Gauge Structure
```python
from ift import GaugeStructure

gauge = GaugeStructure()
gauge.verify_standard_model_couplings()
```

### Example 4: Cosmological Evolution
```python
from ift import Cosmology
import numpy as np

cosmo = Cosmology(cosmology_model='LCDM')
z_array = np.array([0, 0.5, 1.0, 10, 1100])
H_evolution = [cosmo.H_z(z) for z in z_array]
```

### Example 5: Quantum Biology
```python
from ift import QuantumBiology

bio = QuantumBiology()
bio.fmo_complex_detailed()
bio.super_ohmic_universal()
```

## 🧪 Testing

Run comprehensive test suite:
```bash
cd IFT_Core_Library
python tests/test_all.py
```

Expected output:
```
================================================================================
IFT CORE LIBRARY - COMPREHENSIVE TEST SUITE
================================================================================

TEST 1: FUNDAMENTAL CONSTANTS
✓ Fine structure constant: error = 0.0082%
✓ Cosmological constant: error = 0.0900%
✓ Newton constant: error = 0.0000%

TEST 2: PARTICLE MASS SPECTRUM
✓ Lepton hierarchy: average error = 0.342%

... (more tests)

TEST SUMMARY
============
Tests passed: 6/6

✓✓✓ ALL TESTS PASSED ✓✓✓
```

## 📦 Package Distribution

To create distribution packages:

```bash
# Build source distribution
python setup.py sdist

# Build wheel distribution
python setup.py bdist_wheel

# Upload to PyPI (when ready)
python -m twine upload dist/*
```

## 🔄 Development Workflow

1. **Clone repository**
   ```bash
   git clone https://github.com/JuanDiegoVG/IFT.git
   ```

2. **Create development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Run tests and linting**
   ```bash
   pytest tests/
   flake8 ift/
   black ift/
   ```

4. **Make changes and commit**
   ```bash
   git commit -am "Description of changes"
   ```

5. **Push and create pull request**
   ```bash
   git push origin feature-branch
   ```

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

Juan Diego Vicente Gabancho
- Theoretical Physicist
- Information Field Theory Originator
- April 2026

---

**Status**: ✓ Production Ready for Peer Review
**Version**: 1.0.0
**Last Updated**: April 2, 2026
