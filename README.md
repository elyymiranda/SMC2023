# Introduction

The present implementations were developed using the software package employed for low-energy electron-molecule scattering calculations, specifically the Schwinger multichannel implementation (SMC), as the base.

Historically, Takatsuka and McKoy constructed the multichannel Schwinger method _ab initio_ in the 1980s [[1]](#1). Since then, the implementation of the method has followed several main stages [[2]](#2). The scattering cross sections are computed using the parallel version of the Schwinger multichannel method implemented with Bachelet-Hamann-Schlüter (BHS) pseudopotentials (SMCPP) [[3]](#3). A recent review of the method is available [[2]](#2), so we will briefly outline a few relevant aspects here.

The scattering electronic wave function is described by:

$|\Psi^{(\pm)}_{\textbf{k}_i}\rangle = \sum_\mu c_\mu^{(\pm)}(\textbf{k}_i) |\chi_\mu\rangle,$

where $\textbf{k}_i$ denotes the wave vector of the incident electron, and $+(-)$ corresponds to the boundary condition associated with outgoing (incoming) spherical waves [[4]](#4). The method utilizes square-integrable functions to construct the trial set $\{\chi_\mu\}$, which is computationally advantageous.

The basis vectors $|\chi_\mu\rangle$ are known as configuration state functions (CSFs) and represent spin-adapted ($N + 1$)-particle Slater determinants built on the closed-shell ground state of the neutral target, comprising $N$ electrons. This reference state is described at the restricted Hartree-Fock (RHF) level, using sets of Cartesian Gaussian basis functions. Specifically, a 6s5p2d basis set was used for chlorine, a 5s5p2d set for carbon, and a 4s basis set described by Dunning for hydrogen atoms [[5]](#5). A total of 270 basis functions were employed for the molecule. The RHF calculations were conducted using the GAMESS package.

The scattering calculations focused solely on the elastic channel, which is a reasonable approximation for electron energies below the excitation threshold. Two models were explored for constructing the CSF space:

1. **Static-Exchange (SE) Approximation:** The target remains frozen in the ground state $\ket{\Phi_0}$, while unoccupied (virtual) orbitals are used as scattering orbitals $\ket{\phi_m}$. In this context, $|\chi_m\rangle = \mathcal{A}_{N+1} \ket{\Phi_0} \otimes \ket{\phi_m}$, where $\mathcal{A}_{N+1}$ is the anti-symmetrization operator. This approximation does not account for the response of the target electrons to the incoming electron but is effective for collision energies above approximately 20 eV.

2. **Static-Exchange Plus Polarization (SEP) Approximation:** In this model, virtual excitations of the target are allowed. The CSF space is augmented with configurations of the type $|\chi_{im}\rangle = \mathcal{A}_{N+1} \ket{\Phi_i} \otimes \ket{\phi_m}$, where $\ket{\Phi_i}$ represents a single excitation of the target and $\ket{\phi_m}$ is a scattering orbital. This approximation considers both long-range polarization (induced dipole moment) and short-range correlation effects. The SEP functions require the selection of three orbitals: two associated with the target excitation (hole and particle) and the third being the scattering orbital. The CSF space is constructed based on the energy criterion proposed by Kossoski and Bettega [[6]](#6). Specifically, all single-particle orbitals whose energy eigenvalues satisfy $\epsilon_{\text{scat}}+\epsilon_{\text{part}}-\epsilon_{\text{hole}}<\Delta$ are included, where $\epsilon_{\text{scat}}$, $\epsilon_{\text{part}}$, and $\epsilon_{\text{hole}}$ represent the energies of the scattering, particle, and hole orbitals, respectively, and $\Delta$ is a cutoff parameter.

Finally, modified virtual orbitals (MVOs) [[7]](#7) were utilized as particle and scattering orbitals. These orbitals were generated from cationic Fock operators with a charge of +6 for the molecule.

It is also important to mention that the implementation was done using the FORTRAN programming language [[8]](#8), and the SMC version used for this construction was from 2018.

The application of the SMC method for scattering calculations involves five distinct steps. The first is called GAMESS-SMC, necessary for the target description using the BHS pseudopotentials implemented in SMC. Therefore, it is the first step to be executed during the scattering calculation. The second step, known as _part A_, involves the computation of matrix elements independent of the collision energy in Eq.~\ref{SMCfim}. The third, fourth, and fifth steps represent what we call _part B_ of the calculations. Here, the matrix elements (_off-shell_ and _on-shell_) are computed, the matrix $d_{\mu\nu}$ is inverted, and the cross-section is calculated (_3dk_). Each of these steps requires specific input. My contribution to the implementation is the production of _bash_ scripts that automatically generate all the necessary input files, asking the user only for strictly necessary information. Additionally, I created a script for installing the implementation, as it was necessary to compile each part of the code separately.

Subsequent analysis of the cross-section requires the pseudo-spectrum of the Hamiltonian of $N+1$ electrons to identify the nature of the states involved in electron capture. To this end, I developed a script that identifies which states are important for a given energy of the cross-section and another that allows the visualization of this state through dedicated software.

## References

<a id="1">[1]</a> Takatsuka, K., & McKoy, V. (1981). Extension of the Schwinger variational principle beyond the static-exchange approximation. _Physical Review A, 24_(5), 2473.

<a id="2">[2]</a> Da Costa, R. F., Varella, M. T. N., Bettega, M. H. F., & Lima, M. A. P. (2015). Recent advances in the application of the Schwinger multichannel method with pseudopotentials to electron-molecule collisions. _The European Physical Journal D, 69_(6), 159.

<a id="3">[3]</a> Santos, J. S. D., Da Costa, R. F., & Varella, M. T. N. (2012). Low-energy electron collisions with glycine. _The Journal of Chemical Physics, 136_(8), 02B616.

<a id="4">[4]</a> Joachain, C. J. (1975). _Quantum Collision Theory_. North-Holland Publishing Company.

<a id="5">[5]</a> Dunning, T. H. (1970). Gaussian basis functions for use in molecular calculations. _The Journal of Chemical Physics, 53_(7), 2823-2833.

<a id="6">[6]</a> Kossoski, F., & Bettega, M. H. F. (2013). Low-energy electron scattering from the aza-derivatives of pyrrole, furan, and thiophene. _The Journal of Chemical Physics, 138_(23), 234311.

<a id="7">[7]</a> Bauschlicher, C. W., & Partridge, H. (1980). Construction of modified virtual orbitals. _Journal of Chemical Physics, 72_(2), 878-884.

<a id="8">[8]</a> Markus, A. (2012). _Modern Fortran Explained_. Oxford University Press.




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