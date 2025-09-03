# Introduction

The present implementations were developed using the software package employed for low-energy electron-molecule scattering calculations, specifically the Schwinger multichannel implementation (SMC), as the base.

Historically, Takatsuka and McKoy constructed the multichannel Schwinger method _ab initio_ in the 1980s [[1]](#1). Since then, the implementation of the method has followed several main stages [[2]](#2). The scattering cross sections are computed using the parallel version of the Schwinger multichannel method implemented with Bachelet-Hamann-Schlüter (BHS) pseudopotentials (SMCPP) [[3]](#3). A recent review of the method is available [[2]](#2). It is also important to mention that the implementation was done using the FORTRAN programming language, and the SMC version used for this construction is from 2018.

The application of the SMC method for scattering calculations involves five distinct steps. The first is called GAMESS-SMC, necessary for the target description using the BHS pseudopotentials implemented in SMC. Therefore, it is the first step to be executed during the scattering calculation. The second step, known as _part A_, involves the computation of matrix elements independent of the collision energy. The third, fourth, and fifth steps represent what we call _part B_ of the calculations. Here, the matrix elements (_off-shell_ and _on-shell_) are computed, a matrix inversion, and the cross-section is calculated (_3dk_). Each of these steps requires specific input. The contribution to the implementation made by _bash_ scripts that automatically generate all the necessary input files, asking the user only for strictly necessary information. Additionally, a script for installing is also provided, as it was necessary to compile each part of the code separately.

Subsequent analysis of the cross-section requires the pseudo-spectrum of the Hamiltonian of $N+1$ electrons to identify the nature of the states involved in electron capture. To this end, a script that identifies which states are important for a given energy of the cross-section and allows the visualization of this state through dedicated software.

## References

<a id="1">[1]</a> Takatsuka, K., & McKoy, V. (1981). Extension of the Schwinger variational principle beyond the static-exchange approximation. _Physical Review A, 24_(5), 2473.

<a id="2">[2]</a> Da Costa, R. F., Varella, M. T. N., Bettega, M. H. F., & Lima, M. A. P. (2015). Recent advances in the application of the Schwinger multichannel method with pseudopotentials to electron-molecule collisions. _The European Physical Journal D, 69_(6), 159.

<a id="3">[3]</a> Santos, J. S. D., Da Costa, R. F., & Varella, M. T. N. (2012). Low-energy electron collisions with glycine. _The Journal of Chemical Physics, 136_(8), 02B616.

# Installation Guide

This guide provides step-by-step instructions to install **SMCPP code** and its dependencies.

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
mkdir ~/smcpp
cd ~/smcpp

# Copy installsmc script and .tar file to this directory
chmod +x installsmc
./installsmc
```

---

## Notes
- Make sure all dependencies are correctly installed before running `installsmc`.
- If you encounter errors with library paths, verify your `LD_LIBRARY_PATH` exports.


# Tutorial

Here you can find a tiny tutorial to learn how you could use this project.

## Organizing the calculations