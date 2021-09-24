# Compute the discharge conditions for exhaust gases for small and medium combustion systems and other installations
## Berechnung der Ableitbedingungen für Abgase von kleinen und mittleren Feuerungsanlagen sowie andere als Feuerungsanlagen

This library computes the discharge conditions for exhaust gases according to VDI 3781 Part 4 (07/2017). It is well-suited to compute the outlet height taking into account section 6 of VDI 3781 Part 4. The library is separted into three parts:

- outletheight: Computation of the outlet height according to Flowchart defined in Section 6.1. 
- undisturbedremoval: Considering the fluid mechanical requirements for the undisturbed removal of exhaust gases, which is defined in Section 6.2.
- adequatedilution: Taking into account surrounding buildings, hillside location etc. to examine the requirements for adequate dilution as defined in Section 6.3.

The idea of this library is to implement the core definitions of the standard. It is up to the users of this library to add extra functionality like visualizations, creation of reports etc.

We aim at making standards accessible to everyone. However, this effort is only possible if you are involved in such projects in some way. Do not hesitate to contact us <info@richtershuels.de>.