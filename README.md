# Introduction

The present implementations were developed using the software package employed for low-energy electron-molecule scattering calculations, specifically the Schwinger multichannel implementation (SMC), as the base.

Historically, Takatsuka and McKoy constructed the multichannel Schwinger method _ab initio_ in the 1980s [[1]](#1). Since then, the implementation of the method has followed several main stages [[2]](#2). The scattering cross sections are computed using the parallel version of the Schwinger multichannel method implemented with Bachelet-Hamann-Schlüter (BHS) pseudopotentials (SMCPP) [[3]](#3). A recent review of the method is available [[2]](#2). It is also important to mention that the implementation was done using the FORTRAN programming language, and the SMC version used for this construction is from 2018.

The application of the SMC method for scattering calculations involves five distinct steps. The first is called GAMESS-SMC, necessary for the target description using the BHS pseudopotentials implemented in SMC. Therefore, it is the first step to be executed during the scattering calculation. The second step, known as _part A_, involves the computation of matrix elements independent of the collision energy. The third, fourth, and fifth steps represent what we call _part B_ of the calculations. Here, the matrix elements (_off-shell_ and _on-shell_) are computed, a matrix inversion, and the cross-section is calculated (_3dk_). Each of these steps requires specific input. The contribution to the implementation made by _bash_ scripts that automatically generate all the necessary input files, asking the user only for strictly necessary information. Additionally, a script for installing is also provided, as it was necessary to compile each part of the code separately.

Subsequent analysis of the cross-section requires the pseudo-spectrum of the Hamiltonian of $N+1$ electrons to identify the nature of the states involved in electron capture. To this end, a script that identifies which states are important for a given energy of the cross-section and allows the visualization of this state through dedicated software.

## References

<a id="1">[1]</a> Takatsuka, K., & McKoy, V. (1981). Extension of the Schwinger variational principle beyond the static-exchange approximation. _Physical Review A, 24_(5), 2473.

<a id="2">[2]</a> Da Costa, R. F., Varella, M. T. N., Bettega, M. H. F., & Lima, M. A. P. (2015). Recent advances in the application of the Schwinger multichannel method with pseudopotentials to electron-molecule collisions. _The European Physical Journal D, 69_(6), 159.

<a id="3">[3]</a> Santos, J. S. D., Da Costa, R. F., & Varella, M. T. N. (2012). Low-energy electron collisions with glycine. _The Journal of Chemical Physics, 136_(8), 02B616.

# Tutorial

Here you can find a tiny tutorial to learn how you could employ this project.

## Calculate the anion-neutral vibronic excitation energies

1. You shoud have the anion's and neutral's G16 frequency .log file and comp_table file (if you just have the anharmonic .log files, you also will need a single point .log file for each anion and neutral). The comp_table file exemple can be found in exemple folder. Basically, you shoud indicate the neutral-anion normal modes correpondences. 

2. Creating nmode.dat files: 

For harmonic case: Use *split_frequencies.sh* script to each anion and neutral .log files to creatre the nmode.dat files
``` bash
./split_frequencies.sh neutral.log
mkdir neutral
mv nmode* neutral/

./split_frequencies.sh anion.log
mkdir anion
mv nmode* anion/
```

For anharmonic case: Use *split_anharm.sh* script to each anion and neutral .log files to creatre the nmode.dat files
``` bash
./split_anharm.sh neutral.log > freq_neutro.log

./split_anharm.sh anion.log > freq_anion.log
```

3. Creating the comparison file

For harmonic case: Use *join_data.sh* script to join anion and neutral infos 
``` bash
./join_sp.sh comp_table neutral/ anion/

./vibronic_excitation.py join_data.log neutral.log anion.log
```

For anharmonic case: Use *join_data.sh* script to join anion and neutral infos (here you can use single point .log files or harmonic .log files)
``` bash
./vibronic_excitation.py none sp_neutral.log sp_anion.log neutral.log anion.log
```

## Create .xyz files to PES calculation