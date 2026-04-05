"""
Information Field Theory (IFT) Core Library
============================================

A complete, parameter-free framework for unified physics:
- Spacetime geometry from Fisher information metric
- Particle masses as eigenvalues
- Standard Model gauge structure from topology
- Quantum coherence in biological systems
- Cosmological evolution and dark energy

Author: Juan Diego Vicente Gabancho
Version: 1.0.0
License: MIT
Date: April 2026
Status: Production Ready for Peer Review

Main modules:
    - fisher_metric: Spacetime metric from information geometry
    - eigensolve: Particle mass spectrum
    - gauge_structure: Yang-Mills from phase symmetry
    - cosmology: Friedmann equations and expansion
    - constants: Fundamental constant verification
    - quantum_biology: Coherence in biological systems
"""

__version__ = "1.0.0"
__author__ = "Juan Diego Vicente Gabancho"
__date__ = "April 2, 2026"
__license__ = "MIT"

# Core imports
from .fisher_metric import FisherMetric, spacetime_from_information
from .eigensolve import ParticleMassSpectrum, solve_eigenvalue_problem
from .gauge_structure import GaugeStructure, yang_mills_from_phase
from .cosmology import Cosmology, friedmann_equations
from .constants import FundamentalConstants, verify_all_constants
from .quantum_biology import QuantumBiology, coherence_super_ohmic

# Convenience functions
def verify_core_predictions():
    """Run all core verification tests"""
    print("="*80)
    print("INFORMATION FIELD THEORY - CORE VERIFICATION")
    print("="*80)
    
    # 1. Fundamental constants
    const = FundamentalConstants()
    print("\n1. FUNDAMENTAL CONSTANTS")
    print("-" * 80)
    const.verify_all()
    
    # 2. Particle masses
    masses = ParticleMassSpectrum()
    print("\n2. PARTICLE MASS SPECTRUM")
    print("-" * 80)
    masses.verify_lepton_hierarchy()
    
    # 3. Cosmology
    cosmo = Cosmology()
    print("\n3. COSMOLOGICAL PARAMETERS")
    print("-" * 80)
    cosmo.verify_hubble()
    
    print("\n" + "="*80)
    print("✓ VERIFICATION COMPLETE")
    print("="*80)

__all__ = [
    'FisherMetric',
    'ParticleMassSpectrum',
    'GaugeStructure',
    'Cosmology',
    'FundamentalConstants',
    'QuantumBiology',
    'spacetime_from_information',
    'solve_eigenvalue_problem',
    'yang_mills_from_phase',
    'friedmann_equations',
    'verify_all_constants',
    'coherence_super_ohmic',
    'verify_core_predictions'
]
