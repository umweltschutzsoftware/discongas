# Compute the discharge conditions for exhaust gases for small and medium combustion systems and other installations (Berechnung der Ableitbedingungen für Abgase von kleinen und mittleren Feuerungsanlagen sowie andere als Feuerungsanlagen)

We aim at making standards accessible to everyone. However, this effort is only possible if you are involved in such projects in some way. Do not hesitate to contact us <info@richtershuels.de>.

## Introduction
This library computes the discharge conditions for exhaust gases according to VDI 3781 Part 4 (07/2017). It is well-suited to compute the outlet height taking into account section 6 of VDI 3781 Part 4. The library is separted into three parts:

- outletheight: Computation of the outlet height according to Flowchart defined in Section 6.1. 
- undisturbedremoval: Considering the fluid mechanical requirements for the undisturbed removal of exhaust gases, which is defined in Section 6.2.
- adequatedilution: Taking into account surrounding buildings, hillside location etc. to examine the requirements for adequate dilution as defined in Section 6.3.

The idea of this library is to implement the core definitions of the standard. It is up to the users of this library to add extra functionality like visualizations, creation of reports etc.

## Usage

This software is a python module with the main data types **Roof** and **Model**. The **Roof** data type defines the type of the roof and all parameters corresponding to a roof. These parameters are independent of the exact position of the outlet or whether the roof is belonging to the outlet or not. For every computation of an exact outlet height, a **Model** is needed. The model also describes the parameters which are dependent on the exact outlet position. 

### Roof
In base roof type has the following constructor is defined by the parameter
- **name:** The name descriptor of the current roof.
alpha: roof pith angle. In case of a mansard roof, this is the angle of the lower roof. (in degree)
- **H_First** ridge height of the building with the outlet (in m)
- **H_Dach** the buildings actual roof height (in m)
- **b** width of the buildings gable, or the side of the building in direction to the building with the outlet. In case of a mansard roof, this is the width of the lower roof. (in m)
- **l** length of the building. (in m)
- **h** height of the ground of the building of the roof. (in m)
- **nominalheatoutput** nominal heat output. Default: 400 (in kW)
- **ratedthermalinput** Rated thermal input. Default 0.9 (in MW)
- **alpha_O** in case of a mansard roof, this is the angle of the upper roof. Default: None (in degree)
- **b_O** in case of a mansard roof, this is the width of the upper roof. Default: None (in m)
- **address** Adress of the current building

There are seven types of roof: **SymmetricPitchedRoof**, **AsymmetricPitchedRoof**, **FlatRoof**, **SinglePitchRoof**, **SawToothRoof**, **HippedRoof** and **MansardRoof**. Creating a roof is as easy as:

```
spr = SymmetricPitchedRoof(name="", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)
fr = FlatRoof(name="", alpha=0, H_First=8, H_Dach=0, b=15, l=28, h=0)
```

### Model
A model is needed whenever the height of the outlet at a specific position needs to be obtained. In general, a roof is either the source roof (i.e. the roof at which the outlet is placed) or an upstream roof. A model always is created for:

- **a**, i.e. the horizontal distance beween the centre of the outlet cross-section and the ridge (in m) and
- **sourceroof**, i.e. the roof instance at which the outlet is placed.

```
b3 = SymmetricPitchedRoof("b3", alpha=33, H_First=10.4, H_Dach=3.7, b=11.3, l=16.3, h=0)
m = Model(a=0, sourceroof=b3)
```
#### Adding upstream roofs
Upstream roofs are created and added to the model iteratively.
```
b1 = SymmetricPitchedRoof("b1", alpha=31, H_First=11.5, H_Dach=4, b=17.9, l=13.4, h=0)
m.add_upstreamroof(beta=90, l_A=17.4, upstreamroof=b1)
```
#### Getting the outlet height
For a model, the outlet height can be obtained by the function **height**.
```
m.height()
```
The height is returned, however to retrace how the height is obtained the method **height_with_dict** shall be used. This method returns a four-tuple, with the following items:

1. the outlet height,
2. the source of the outlet height, i.e. "AD" if the height is defined by the adequate dilution and "UR" if the height is defined by the undisturbed removal, 
3. the name of the building that defines the height and
4. a dictionary of data for all buildings which contains all given and computed parameters.