# ESTRUCTURA VERIFICADA — Jaime393/IFT_Core_Library

Archivo nuevo, aditivo. Comparación, solo con lo leído en la minería, entre lo que escribe `PROJECT_STRUCTURE.md` (y `README.md` donde se indica) y lo verificado en los archivos del repo. Cada fila da la fuente de ambos lados. No se añade juicio: solo lo que dice la documentación y lo que se leyó.

- Repo: `Jaime393/IFT_Core_Library`, último commit verificado `9cac07dd28ae1475f90e0088babefff3d4283b9a` (2026-07-10).
- Fuente: minería local de solo lectura de 2026-11-08 (`~/workspace/mineria/IFT_Core_Library/MINERIA.md`, Parte 1 EXPORTABLE), por lectura de texto de las URLs raw de cada archivo en ese commit y listado de la raíz con `get_file_contents`.

## 1. Líneas por archivo: la tabla de `PROJECT_STRUCTURE.md` frente a las líneas leídas

`PROJECT_STRUCTURE.md` contiene una tabla `Code Statistics`. Estas son sus cifras frente a las líneas de los archivos leídos en esta minería (los mismos 9 archivos):

| Archivo | Líneas según la tabla | Funciones / clases según la tabla | Líneas leídas en la minería |
|---|---|---|---|
| `fisher_metric.py` | 320 | 12 / 2 | 548 |
| `eigensolve.py` | 400 | 15 / 1 | 682 |
| `gauge_structure.py` | 420 | 18 / 1 | 740 |
| `cosmology.py` | 450 | 16 / 1 | 678 |
| `constants.py` | 380 | 12 / 1 | 637 |
| `quantum_biology.py` | 380 | 14 / 1 | 401 |
| `__init__.py` | 120 | 2 / 0 | 159 |
| `test_all.py` | 280 | 8 / 0 | 412 |
| `tutorial.py` | 450 | 8 / 0 | 808 |
| **TOTAL** | **3.380** | **105 / 7** | **5.065** |

- La tabla escribe `TOTAL` 3.380 líneas, 105 funciones, 7 clases. La suma de los 9 archivos leídos es 5.065 líneas.
- La tabla escribe para `ift/` 6 módulos; el listado de `ift/` en el mismo commit tiene 7 archivos (`__init__.py` más los 6 módulos).

## 2. `data/`: anunciado frente a listado

- `PROJECT_STRUCTURE.md` dibuja un árbol con `data/` y la nota `(Will be created during execution)`.
- En la raíz listada por `get_file_contents` en el mismo commit (9 entradas: 5 archivos y 4 directorios `docs`, `ift`, `notebooks`, `tests`) no hay directorio `data`.
- `.gitignore` contiene `data/` en su sección de salidas de investigación (`results/`, `data/`, `*.pkl`, `*.h5`, `*.npy`, `*.npz`).

## 3. `LICENSE`: mencionado frente a listado

- `README.md` dice `MIT License - See LICENSE file for details`.
- En la raíz listada por `get_file_contents` en el mismo commit no hay archivo `LICENSE`.
- `ift/__init__.py` escribe `__license__ = "MIT"` y `setup.py` no escribe campo de licencia en lo leído (escribe `name="ift-core"`, `version="1.0.0"`, `author="Juan Diego Vicente Gabancho"`, `author_email="jdvg@physics.org"`, `description="Information Field Theory: Unified framework for physics"`, `url="https://github.com/JuanDiegoVG/IFT"`, `python_requires=">=3.7"`).

## 4. Métodos `si_qubits_detail()` y `quantum_advantage_calculation()`

- `PROJECT_STRUCTURE.md` lista para `quantum_biology.py` los métodos `si_qubits_detail()` y `quantum_advantage_calculation()`.
- `notebooks/tutorial.py` llama a `bio.si_qubits_detail()` y a `bio.quantum_advantage_calculation()` dentro de `tutorial_quantum_biology()`.
- En el texto leído de `ift/quantum_biology.py` en el mismo commit (401 líneas) no aparecen esos dos nombres. Los métodos que sí define `QuantumBiology` son `lindblad_bath_coupling()`, `decoherence_time_tci()`, `super_ohmic_universal()`, `fmo_complex_detailed()` y `coherence_comparison_table()`.

## 5. `requirements.txt`: lo que dice `PROJECT_STRUCTURE.md` y lo leído

- `PROJECT_STRUCTURE.md` dice que `requirements.txt` contiene numpy >= 1.19.0, scipy >= 1.5.0, matplotlib >= 3.3.0 y jupyter >= 1.0.0.
- El texto leído de `requirements.txt` en el mismo commit contiene 4 líneas: `numpy>=1.19.0`, `scipy>=1.5.0`, `matplotlib>=3.3.0`, `jupyter>=1.0.0`.
- `README.md` dice que los requisitos son Python 3.7+, numpy >= 1.19, scipy >= 1.5 y matplotlib opcional.

## 6. `docs/MIU_BIBLIOGRAPHY_LINKAGE.md`: la frase y su texto

- El archivo tiene 322 bytes y una sola línea. Su texto completo es la frase transcrita en `BIBLIOGRAFIA-MIU.md`.
- En el texto leído de ese archivo no aparece ninguna URL ni ningún enlace.
