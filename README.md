# SMC2023 - User-Friendly Interface

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Fortran](https://img.shields.io/badge/Fortran-2018-purple.svg)](https://fortran-lang.org/)
[![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)](https://www.linux.org/)

**User-friendly interface for the Schwinger Multichannel Method with Pseudopotentials (SMCPP) for low-energy electron-molecule scattering calculations.**

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [References](#references)
- [Acknowledgments](#acknowledgments)
- [Installation Guide](#installation-guide)
  - [Obtaining the SMC Base Code](#obtaining-the-smc-base-code)
  - [Requirements](#requirements)
- [Tutorial](#tutorial)

---

## Introduction

The present implementations were developed using the software package employed for low-energy electron-molecule scattering calculations, specifically the Schwinger multichannel implementation (SMC), as the base.

Historically, Takatsuka and McKoy constructed the multichannel Schwinger method _ab initio_ in the 1980s [[1]](#1). Since then, the implementation of the method has followed several main stages [[2]](#2). The scattering cross sections are computed using the parallel version of the Schwinger multichannel method implemented with Bachelet-Hamann-Schlüter (BHS) pseudopotentials (SMCPP) [[3]](#3). A recent review of the method is available [[2]](#2). It is also important to mention that the implementation was done using the FORTRAN programming language, and the SMC version used for this construction is from 2018.

The application of the SMC method for scattering calculations involves five distinct steps. The first is called GAMESS-SMC, necessary for the target description using the BHS pseudopotentials implemented in SMC. Therefore, it is the first step to be executed during the scattering calculation. The second step, known as _part A_, involves the computation of matrix elements independent of the collision energy. The third, fourth, and fifth steps represent what we call _part B_ of the calculations. Here, the matrix elements (_off-shell_ and _on-shell_) are computed, a matrix inversion, and the cross-section is calculated (_3dk_). Each of these steps requires specific input. The contribution to the implementation made by _bash_ scripts that automatically generate all the necessary input files, asking the user only for strictly necessary information. Additionally, a script for installing is also provided, as it was necessary to compile each part of the code separately.

Subsequent analysis of the cross-section requires the pseudo-spectrum of the Hamiltonian of $N+1$ electrons to identify the nature of the states involved in electron capture. To this end, a script that identifies which states are important for a given energy of the cross-section and allows the visualization of this state through dedicated software.

## Features

- **Automated workflow**: Bash scripts handle input file generation for all calculation steps
- **Comprehensive coverage**: Implements all five SMC calculation steps (GAMESS-SMC, Part A, Part B components)
- **Flexible basis sets**: Support for multiple atoms with BHS pseudopotentials (C, N, O, F, Cl, Br, I, S, Si, Ge, Sn, Sb, P)
- **Symmetry support**: Handles various molecular symmetry groups (Cs, Cnh, Cnv, Dnh, C1)
- **Modified Virtual Orbitals (MVOs)**: Enhanced orbital analysis for resonance identification
- **Pseudo-spectrum analysis**: Tools for identifying and visualizing resonance states
- **Installation automation**: Streamlined installation script for all dependencies

## References

<a id="1">[1]</a> Takatsuka, K., & McKoy, V. (1981). Extension of the Schwinger variational principle beyond the static-exchange approximation. _Physical Review A, 24_(5), 2473.

<a id="2">[2]</a> Da Costa, R. F., Varella, M. T. N., Bettega, M. H. F., & Lima, M. A. P. (2015). Recent advances in the application of the Schwinger multichannel method with pseudopotentials to electron-molecule collisions. _The European Physical Journal D, 69_(6), 159.

<a id="3">[3]</a> Santos, J. S. D., Da Costa, R. F., & Varella, M. T. N. (2012). Low-energy electron collisions with glycine. _The Journal of Chemical Physics, 136_(8), 02B616.

<a id="4">[4]</a> Abdoul-Carime, H., E. G. F. de Miranda, and M. T. do N Varella. "Low-energy (0–9 eV) electron interaction with gas phase 1, 3-dichlorobenzene: an experimental and theoretical study." Physica Scripta 99.12 (2024): 125401.

---

## Acknowledgments

**What this repository provides:**

This repository contains a **user-friendly interface** for the Schwinger Multichannel Method with Pseudopotentials (SMCPP), developed by Ely Miranda. The contributions include:

- **Bash scripts** for automated input file generation for all calculation steps
- **Installation script** (`installsmc`) that compiles all code components
- **Pseudo-spectrum analysis tools** for resonance identification
- **Complete documentation and tutorials** with working examples

**Original SMC code:**

The underlying FORTRAN implementation of the SMC method represents decades of development by the scientific community, particularly:
- UNICAMP (Universidade Estadual de Campinas) version
- Contributions from researchers cited in references [[1]](#1), [[2]](#2), [[3]](#3)

**The base SMC code is NOT included in this repository.** To obtain it, please contact the researchers listed in the [Obtaining the SMC Base Code](#obtaining-the-smc-base-code) section.

This interface was inspired by workflow automation seen in Columbus and NewtonX software packages.

**Citation:**

If you use these scripts in your research, please cite this repository and the relevant SMC method papers above.

---

# Installation Guide

This guide provides step-by-step instructions to install **SMCPP code** and its dependencies.

---

## Obtaining the SMC Base Code

**IMPORTANT:** The SMC base code is proprietary and not included in this repository. To obtain the code base (`SMC2023_v7.tar`), you must send an email to one of the following researchers:

- **Prof. Dr. Sergio d'Almeida Sanchez** - ssanchez@fisica.ufpr.br
- **Prof. Dr. Márcio Henrique Franco Bettega** - bettega@fisica.ufpr.br
- **Prof. Dr. Márcio Teixeira do Nascimento Varella** - mvarella@if.usp.br
- **Dr. Fábris Kossoski** - fkossoski@irsamc.ups-tlse.fr

Once you obtain the `SMC2023_v7.tar` file, place it in the `install/` directory. You will then be able to compile the SMC code using the `installsmc` script provided in the `install/` folder by following the instructions in this documentation.

---

## Requirements

### 1) Intel Fortran Compiler (ifort)

The SMC programs are written in FORTRAN, requiring `ifort`.

- Installation help: [StackOverflow Guide](https://stackoverflow.com/questions/65570841/install-ifort-on-ubuntu-20)  
- Download: [Intel oneAPI Fortran Compiler](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#fortran)

#### Installation Steps:
```bash
# Navigate to the instalation folder
cd /path/to/folder

# Make the installer executable
sudo chmod +x ifort_instaler.sh

# Run the installer
./ifort_instaler.sh

# Follow the installation instructions (pay attention to the chosen installation path)


# Add the following line to your ~/.bashrc:
. /path/to/oneapi/setvars.sh
```

**Note:** After this, you don’t need to call the library every time you use `ifort`.

---

### 2. gcc

**Installation:**
```bash
sudo apt install gcc
```

---

### 3. Intel Math Kernel Library (MKL)

- Download: [Intel OneMKL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-download.html)

**Installation Steps:**
```bash
# Navigate to the download folder:
cd /path/to/folder

# Make the file executable:
sudo chmod +x mkl_installer.sh

# Execute the installer:
./mkl_installer.sh

# Follow the installation instructions (pay attention to the chosen installation path)

# Add the following line to your ~/.bashrc:
. /path/to/oneapi/setvars.sh
```
**Note:** After this, you don’t need to call the library every time you use `ifort`.

---

### 4. csh

**Installation:**
```bash
sudo apt install csh
```

---

### 5. libatlas-base-dev

**Installation:**
```bash
sudo apt-get update
sudo apt-get install libatlas-base-dev
```

---


### 6. libg2c
- Download: [libg2c RPM](https://rpmfind.net/linux/rpm2html/search.php?query=libg2c.so.0()(64bit))


**Installation Steps:**
```bash
# Navigate to the download folder:
cd /path/to/folder

# Add repository:
sudo add-apt-repository universe

# Update:
sudo apt-get update

# Install alien:
sudo apt-get install alien

# Convert and install RPM:
sudo alien -i compat-libf2c-34-3.4.6-32.el7.x86_64.rpm

# Update database:
sudo updatedb
```

---

### 7. Export Libraries

You need to locate two important libraries: `libf77blas.so.3` and `libg2c`.

**Steps:**
```bash
# Install locate if not installed
sudo apt install locate

# Locate libraries
locate libf77blas.so.3
locate libg2c

# Export paths
export LD_LIBRARY_PATH=/path/to/libf77blas.so.3/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/path/to/libg2c/:$LD_LIBRARY_PATH
```

---

### 8. Verify
Ensure **BIB1** and **BIB2** are in the correct directories in installsmc file.

---


### 9. Install SMCPP

**Steps:**
```bash
# Create installation directory
mkdir /path/to/folder/smcpp
cd /path/to/folder/smcpp

# Copy installsmc script and .tar file to this directory
chmod +x installsmc
./installsmc
```

---

## Notes
- Make sure all dependencies are correctly installed before running `installsmc`.
- If you encounter errors with library paths, verify your `LD_LIBRARY_PATH` exports.

---
---
# Tutorial

Here you can find a tiny tutorial to learn how you could use this project. We are going to use 1,3-dichlorobenzene molecule as an example. This system work was published, you can find it in the reference bellow [[4]](#4).

<a id="4">[4]</a> Abdoul-Carime, H., E. G. F. de Miranda, and M. T. do N Varella. "Low-energy (0–9 eV) electron interaction with gas phase 1, 3-dichlorobenzene: an experimental and theoretical study." Physica Scripta 99.12 (2024): 125401.

## Organizing the calculations

When you begin a new project, we recomend the creation of a folder. 

```bash
# Create project directory
mkdir /path/to/folder/dichlorobenzene
cd /path/to/folder/dichlorobenzene
```

Now, create other 3 folder: for GAMESS, part A and part B.

```bash
# Create project directory
mkdir gms partA partB
```

As we explained in introduction, we begin our calculation in gms directory. Our goal here is to describe the target using the BHS pseudopotentials. For this step we just need the **input_nucgms** file, i.e.

```bash
#!/bin/bash

# DO NOT LEAVE ANY FREE SPACE AFTER THE ARGUMENT

# If necessary, enter the number of extra centers.
EXTRAC = 0

# Symmetry group of the molecule
GROUP  = Cnv 2

# Reflection plane of the symmetry group
RPLANE = X	

# Modified Virtual Orbitals (all you wanted to use)
MVO    = 2 4 6 8

# Molecule's name
MNAME  = m-2ClB

# Geometry numbers type: Angstrom (ANGS) or Bohr (BOHR)
GMODE  = ANGS

 BEGIN_GEO
C     1.216918719380      1.443081722788      0.000000000000
C     1.196331401305      0.047281051048      0.000000000000
C    -1.196331401305      0.047281051048      0.000000000000
C     0.000000000000      2.130709197805      0.000000000000
H    -2.164903655200      1.977120046915      0.000000000000
H     0.000000000000     -1.758552205393      0.000000000000
C     0.000000000000     -0.671761849324      0.000000000000
Cl   -2.717247172888     -0.839814710913      0.000000000000
Cl    2.717247172888     -0.839814710913      0.000000000000
H     2.164903655200      1.977120046915      0.000000000000
C    -1.216918719380      1.443081722788      0.000000000000
H     0.000000000000      3.220564490290      0.000000000000
 END_GEO

# Remember to respect the order in geometry 

 BEGIN_BASIS
C1 C 5s5p2d
C2 C 5s5p2d
C3 C 5s5p2d
C4 C 5s5p2d
H1 H 4s
H2 H 4s
C5 C 5s5p2d
Cl1 Cl 6s5p2d
Cl2 Cl 6s5p2d
H3 H 4s
C6 C 5s5p2d
H4 H 4s
 END_BASIS
```

Here each flag has a important informaion: 
- Extract:  Specifies the number of **extra centers** introduced in the calculation, i.e., the inclusion of ghost atoms to use auxiliary basis functions in some part of the space.  


- Molecule symmetry group: Defines the **molecular symmetry group** to be applied in the calculation. It must be consistent with the `RPLANE` flag. Options available:

    - `Cs`  (reflection plane `X` or `Z`)  
    - `Cnh` (order 2, reflection plane `X` or `Z`)  
    - `Cnv` (order 2, reflection plane `XZ`)  
    - `Dnh` (order 2, reflection plane `XZ`)  
    - `C1`  (no symmetry)  

- Reflection plane of the symmetry group: Specifies the **reflection plane** associated with the chosen symmetry group. Must be consistent with `GROUP`. Not required for `C1`.  Options:  

    - `X`  
    - `Z`  
    - `XZ`  

- Modified Virtual Orbitals (MVOs): yields more compact orbitals compared to the canonical virtual orbitals obtained directly. Such compact orbitals are particularly advantageous for subsequent analysis, as they provide a clearer description of the electronic structure and facilitate the interpretation of resonances. MVOs are generated by introducing additional positive charges into the molecular system, in even numbers, in order to modify the virtual orbital space. 

- Project name: Specifies the **project name**.

- Geometry unit: Specifies the **unit system** for the molecular geometry.

    - `ANGS` → Angstrom  
    - `BOHR` → Bohr  

- Molecule geometry: Contains the **molecular geometry** block. The geometry must be provided in Cartesian coordinates of all atoms, written in the chosen unit system (`ANGS` or `BOHR`).  

- Basis of all centers (atoms and extra): Specifies the **basis set assignment** for each center (atom or extra center). The atoms order should be the same of the geometry. 
    - Atoms with available pseudopotentials (PP): C, N, O, F, Cl, Br, I, S, Si, Ge, Sn, Sb, P.
        - H: 4s, 4s1p  
        - C:   6s5p2d, 5s5p3d, 5s5p2d, 5s4p2d
        - N:   6s5p2d, 5s5p3d, 5s5p2d, 5s4p2d  
        - O:   6s5p2d, 5s5p3d, 5s5p2d, 5s4p2d 
        - F:   6s5p2d, 5s5p3d  
        - Cl:  6s5p2d  
        - Br:  6s5p2d  
        - I:   6s5p2d  
        - S:   5s5p2d  
        - Si:  6s4p3d  
        - Ge:  6s5p2d, 6s5p3d  
        - Sn:  6s5p3d  
        - Sb:  6s6p4d  
        - P:   6s6p4d

With that in mind, we can proceed with the first step. Go to the gms folder and run **nucgms** script.

```bash
# Go to gms directory
cd /path/to/folder/dichlorobenzene/gms

# Run nucgms script
$SMC/nucgms input_nucgms
```