"""
Level 4 Classification Layers for modified scheme specific for LE4LD implementation

All outputs are expressed in terms of degradation/desertification risk's score. 
For each parameter, risk categories are constructed and a score ranging from 1 to 2 is associated with them. 
To avoid using decimals, the scores are multiplied by 100: outputs range from low/minimal risk (D100) with an associated score of 100 (i.e. 1), to high/maximal risk (D200) with an associated score of 200 (i.e. 2). An intermediate category, for example D165, is then associated with a score of 165 (i.e. 1.65), etc.
When 201...255, classes are considered the same level of degradation as class D200. 

Currently used layers: 
* indicates modification from LCCS layers base
PrecipitAtmEnvCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Rainfall (LDDSI)
AridindexAtmCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Aridity index (LDDSI)
RainerosiAtmCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Rainfall erosivity (LDDSI)
WindspeedAtmCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Wind speed (LDDSI)
ParentmatPhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Parent materials (ESAI)
RockfragmPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Rock fragment (LDDSI)
SoildepthPhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil depth (LDDSI)
SoiltextPhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil texture (LDDSI)
SoildrainPhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil drainage (ESAI)
SoilsaltyPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil salinity (LDDSI)
SoilalkaPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil alkalinity (LDDSI)
FireriskVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Fire risk (LDDSI)
ErosprotcVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Erosion protection (LDDSI)
DryresistVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Drought resistance (LDDSI)
CanopycoVegCatL4d* (modified to desagraggate NDVI values in 11 classes) - Canopy cover (LDDSI)   
AgriintyAgrCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Agricultural intensity (LDDSI)
PolicyenfAgrCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Policy enforcement (LDDSI)
GradientTerEnvCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Terrain slope (LDDSI)
SlopeaspTerCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Slope aspect (LDDSI)
PlancurvTerCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Plan curvature (LDDSI)
ProfilecurvTerCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Profile curvature (LDDSI)
DraindensWatCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Drainage density (LDDSI)
GrndwtrdpWatCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Groundwater depth (LDDSI)
PopudensUrbCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Population density (LDDSI)
PopgrowthUrbCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Population growth (LDDSI)
SoilerodiPhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Soil erodibility (LDDSI)
TillerosiAgrCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Tillage erosion (EUSO)
HarverosiAgrCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Harvesting erosion (EUSO)
AsexcessPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Arsenic excess (EUSO)
CuexcessPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Copper excess (EUSO)
HgexcessPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Mercury excess (EUSO)
ZnexcessPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Zinc excess (EUSO)
CdexcessPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Cadmium excess (EUSO)
Nitrogen surplus (EUSO) ***
PcontentPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Phosphorus deficiency and excess (EUSO)(EUSO)
Distance to max SOC (EUSO) ***
Potential threat to biological functions (EUSO) ***
BulkdensPhyCatL4d* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Bulk density (EUSO)
Secondary salinization (EUSO) ***
Peatland degradation (EUSO) ***
Soil sealing (EUSO) ***
SocchangePhyCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - SOC change (SDG15.3.1)
LptrendVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Land productivity trend (SDG15.3.1)
LpstateVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Land productivity state (SDG15.3.1)
LpperformVegCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Land productivity performance (SDG15.3.1)
lcchangeCatL4a* (new level 4 class specific for LE4LD implementation, not part of LCCS layers base) - Land Cover change (SDG15.3.1)

*** will be implemented

Docstrings for each class below detail modifications from l4_layers_lccs.py
If no explanation given, assume identical to relevant class in l4_layers_lccs.py
"""

import logging
import numpy
import xarray

from . import l4_base

# Load standard l4 layers
from . import l4_layers_lccs


class PrecipitAtmEnvCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Annual precipitation amount (precipit_atm_env_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continuous data representing accumulated precipitation amount over 1 year in mm.
    The amount of precipitation is translated into levels of degradation/desertification risk (low to high).
    * D100: More than 650 mm/yr
    * D105: Amount of precipitation ranging between 570-650 mm/yr
    * D115: Amount of precipitation ranging between 490-570 mm/yr
    * D125: Amount of precipitation ranging between 440-490 mm/yr
    * D135: Amount of precipitation ranging between 390-440 mm/yr
    * D150: Amount of precipitation ranging between 345-390 mm/yr
    * D165: Amount of precipitation ranging between 310-345 mm/yr
    * D180: Amount of precipitation ranging between 280-310 mm/yr
    * D200: Less than 280 mm/yr

    Categories within precipit_atm_env_cat_l4d_ld have been taken from: 
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
     
    """
    def __init__(self):
        self.input_layer_name = "precipit_atm_env_con"
        self.output_layer_name = "precipit_atm_env_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "> 650 mm/yr"),
                                           105 : ("D105", "570-650 mm/yr"),
                                           115 : ("D115", "490-570 mm/yr"),
                                           125 : ("D125", "440-490 mm/yr"),
                                           135 : ("D135", "390-440 mm/yr"),
                                           150 : ("D150", "345-390 mm/yr"),
                                           165 : ("D165", "310-345 mm/yr"),
                                           180 : ("D180", "280-310 mm/yr"),
                                           200 : ("D200", "< 280 mm/yr")}
        self.class_boundaries = { 100 : (650, None),
                                  105 : (570, 650),
                                  115 : (490, 570),
                                  125 : (440, 490),
                                  135 : (390, 440),
                                  150 : (345, 390),
                                  165 : (310, 345),
                                  180 : (280, 310),
                                  200 : (0, 280)}
        # Set valid level3 classes
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216, 220, 227, 228]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE                          

class AridindexAtmCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Aridity index (aridindex_atm_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
   
    Input class is envisaged to be continous data representing Aridity Index annual average values (unitless). 
    Aridity Index represent the ratio between precipitation and ET0, thus rainfall over vegetation water demand (aggregated on annual basis). 
    Aridity Index is translated into levels of degradation/desertification risk (low to high).
    * D100: Ratio higher than 1
    * D105: AI ranging between 0.75 and 1
    * D115: AI ranging between 0.65 and 0.75
    * D125: AI ranging between 0.50 and 0.65
    * D135: AI ranging between 0.35 and 0.50
    * D145: AI ranging between 0.20 and 0.35
    * D155: AI ranging between 0.10 and 0.20
    * D175: AI ranging between 0.03 and 0.10
    * D200: AI lower than 0.03
    
    Categories within aridindex_atm_cat_l4d_ld have been taken from 
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
     
    """
    def __init__(self):
        self.input_layer_name = "aridindex_atm_con"
        self.output_layer_name = "aridindex_atm_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "> 1"),
                                           105 : ("D105", "0.75 - 1"),
                                           115 : ("D115", "0.65 - 0.75"),
                                           125 : ("D125", "0.50 - 0.65"),
                                           135 : ("D135", "0.35 - 0.50"),
                                           145 : ("D145", "0.20 - 0.35"),
                                           155 : ("D155", "0.10 - 0.20"),
                                           175 : ("D175", "0.03 - 0.10"),
                                           200 : ("D200", "< 0.03")}
        # AI's value                                    
        self.class_boundaries = { 100 : (1, None),
                                  105 : (0.75, 1),
                                  115 : (0.65, 0.75),
                                  125 : (0.50, 0.65),
                                  135 : (0.35, 0.50),
                                  145 : (0.20, 0.35),
                                  155 : (0.10, 0.20),
                                  175 : (0.03, 0.10),
                                  200 : (None,0.03)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class RainerosiAtmCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Rainfall erosivity (rainerosi_atm_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be continous data representing R-Factor in MJ mm ha-1 h-1 yr-1.
    R-Factor index showing the capacity of rainfalls to erode. 
    Potential of rainfall erositvity is translated into levels of degradation/desertification risk (low to high).
    * D100: < 610 MJ mm ha-1 h-1 yr-1
    * D150: Values between 610 and 730 MJ mm ha-1 h-1 yr-1
    * D200: > 730 MJ mm ha-1 h-1 yr-1
    
    Categories within rainerosi_atm_cat_l4d_ld have been taken from: 
    Perovic et al., (2021). Major drivers of land degradation risk in Western Serbia: Current trends and future scenarios. Ecological Indicators, 123, 107377. https://doi.org/10.1016/j.ecolind.2021.107377 

    """
    def __init__(self):
        self.input_layer_name = "rainerosi_atm_con"
        self.output_layer_name = "rainerosi_atm_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "< 610 MJ mm ha-1 h-1 yr-1"),
                                           150 : ("D150", "610-730 MJ mm ha-1 h-1 yr-1"),
                                           200 : ("D200", "> 730 MJ mm ha-1 h-1 yr-1")}
        self.class_boundaries = { 100 : (None, 610),
                                  150 : (610, 730),
                                  200 : (730, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class WindspeedAtmCatL4d_ld(l4_base.Level4ClassificationContinuousLayer) : 
    """
    Wind velocity (windspeed_atm_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be continuous data representing wind speed in m/s. 
    Wind speed is translated into levels of degradation/desertification risk (low to high).
    * D100: Less than 4.1 m/s
    * D150: Wind speed between 4.1 and 5 m/s
    * D200: Higher than 5 m/s

    Categories within windspeed_atm_cat_l4d_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  

    """
    def __init__(self):
        self.input_layer_name = "windspeed_atm_con"
        self.output_layer_name = "windspeed_atm_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "< 4.1 m/s"),
                                           150 : ("D150", "4.1 - 5 m/s"),
                                           200 : ("D200", "> 5 m/s")}
        self.class_boundaries = { 100 : (0, 4.1),
                                  150 : (4.1, 5),
                                  200 : (5, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class ParentmatPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Parent material (parentmat_phy_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing dominant parent material. 
    Type of parent material are translated into levels of degradation/desertification risk (low to high).
    * D100: Unsconsolidate sediments
    * D120: Basic volcanic rocks, siliciclastic sedimentary rocks, basic plutonic rocks, evaporites
    * D140: Mixed sedimentary rocks
    * D150: Intermediate volcanic rocks, intermediate plutonic rocks, metamorphic rocks
    * D160: Acid plutonic rocks, acid volcanic rocks
    * D170: Carbonate sedimentary rocks
    * D200: Pyroclastics
    
    Categories within parentmat_phy_cat_l4a_ld have been taken from:
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
    
    """
    def __init__(self):
        self.input_layer_name = "parentmat_phy_cat"
        self.output_layer_name = "parentmat_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Unsconsolidate sediments"),
                                           120 : ("D120", "Basic volcanic rocks, siliciclastic sedimentary rocks, basic plutonic rocks, evaporites"),
                                           140 : ("D140", "Mixed sedimentary rocks"),
                                           150 : ("D150", "Intermediate volcanic rocks, intermediate plutonic rocks, metamorphic rocks"),
                                           160 : ("D160", "Acid plutonic rocks, acid volcanic rocks"),
                                           170 : ("D170", "Carbonate sedimentary rocks"),
                                           200 : ("D200", "Pyroclastics")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN     

class RockfragmPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    
    Rock fragment content (rockfragm_phy_cat_l4d_ld)
    
    Input class is envisaged to be continuous data representing coarse fragments content in %.
    Rock fragment content categories are translated into levels of degradation/desertification risk (low to high).
    * D100: coarse fragments volumetric higer than 60%
    * D110: coarse fragments volumetric between 40 and 60%
    * D130: coarse fragments volumetric between 30 and 40%
    * D150: coarse fragments volumetric between 20 and 30%
    * D170: coarse fragments volumetric bewteen 10 and 20%
    * D200: coarse fragments volumetric lower than 10%
    
   Categories within rockfragm_phy_cat_l4d_ld have been taken from: 
   Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 

    """
    def __init__(self):
        self.input_layer_name = "rockfragm_phy_con"
        self.output_layer_name = "rockfragm_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "> 60%"),
                                          110 : ("D110", "40 - 60%"),
                                          130 : ("D130", "30 - 40%"),
                                          150 : ("D150", "20 - 30%"),
                                          170 : ("D170", "10 - 20%"),
                                          200 : ("D200", "< 10%")}
        # coarse fragments volumetric expressed in %                                   
        self.class_boundaries = { 100 : (60, None),
                                  110 : (40, 60),
                                  130 : (30, 40),
                                  150 : (20, 30),
                                  170 : (10, 20),
                                  200 : (None,10)}
        # Set valid level3 classes to 216                                  
        self.valid_level3_classes = [216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class SoildepthPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Soil depth (soildepth_phy_cat_l4a_ld) to rock.  
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing depth to rock according to the categories hereafter.
    Soil depth is translated into levels of degradation/desertification risk (low to high).
    * D100: Very deep (> 120 cm)
    * D120: Deep (80 - 120cm)
    * D160: Moderate (40 - 80cm)
    * D200: Shallow ( < 40cm)
    
    Categories within soildepth_phy_cat_l4a_ld have been taken from:
    Panagos et al., (2022). European Soil Data Centre 2.0: Soil data and knowledge in support of the EU policies. European Journal of Soil Science, 73(6), e13315. DOI: 10.1111/ejss.13315
    """
    def __init__(self):
        self.input_layer_name = "soildepth_phy_cat"
        self.output_layer_name = "soildepth_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "Very deep (> 120 cm)"),
                                          120 : ("D120", "Deep (80 - 120cm)"), 
                                          160 : ("D160", "Moderate (40 - 80cm)"),
                                          200 : ("D200", "Shallow ( < 40cm)")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class SoiltextPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Soil texture (soiltext_phy_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be categorical data representing USDA classes based on relative proportion of sand, silt and clay (https://www.nrcs.usda.gov/resources/education-and-teaching-materials/soil-texture-calculator).
    Categories are translated into degradation/desertification risk level (low to high).
    * D100: Loam, Sandy Clay Loam, Sandy Loam, Loamy Sand, Clay Loam 
    * D120: Sandy Clay, Silt Loam, Silt Clay Loam
    * D160: Silt, Clay, Silty Clay
    * D200: Sand
    
    Categories within soiltext_phy_cat_l4a_ld have been taken from: 
    Kosmas et al., (1999). Methodology for mapping Environmentally Sensitive Areas (ESAs) to desertification. 'The Medalus Model'. In (pp. 31-47). https://www.researchgate.net/publication/262374822_Methodology_for_mapping_Environmentally_Sensitive_Areas_ESAs_to_desertification_%27The_Medalus_Model%27 
    
    """
    def __init__(self):
        self.input_layer_name = "soiltext_phy_cat"
        self.output_layer_name = "soiltext_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "L, SCL, SL, LS, CL"), 
                                          120 : ("D120", "SC, SiL, SiCL"),
                                          160 : ("D160", "Si, C, SiC"),
                                          200 : ("D200", "S")}
        # Set valid level3 classes to exclude water components (220, 227, 228) OR all should be excluded except 216?
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class SoildrainPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Soil drainage (soildrain_phy_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing potential drainage according to the categories hereafter.
    Soils are grouped according to their drainage potential and translated into levels of degradation/desertification risk (low to high).
    * D100: high runoff potential (<50% sand and >40% clay)
    * D120: moderately high runoff potential (<50% sand and 20-40% clay)
    * D160: moderately low runoff potential (50-90% sand and 10-20% clay)
    * D200: Low runoff potential (>90% sand and <10% clay) 
    
    Categories within soildrain_phy_cat_l4a_ld have been taken from https://daac.ornl.gov/SOILS/guides/Global_Hydrologic_Soil_Group.html#acqmatmethods
    
    """
    def __init__(self):
        self.input_layer_name = "soildrain_phy_cat"
        self.output_layer_name = "soildrain_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "High runoff potential (<50% sand and >40% clay)"), 
                                          120 : ("D120", "moderately high runoff potential (<50% sand and 20-40% clay)"), 
                                          160 : ("D160", "moderately low runoff potential (50-90% sand and 10-20% clay)"), 
                                          200 : ("D200", "Low runoff potential (>90% sand and <10% clay) ")} 
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Should also include valid level4 classes according to soiltex_cat_l4a_ld?
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN 

class SoilsaltyPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Soil salinity (soilsalty_phy_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continous data representing electrical conductivity, epxressed in dS/m. 
    Electrical conductivity is used as a proxy of soluble salt concentration in soil. 
    Categories are translated into levels of degradation/desertification risk (low to high).
    * D100: Electrical conductivity lower than 2 dS/m
    * D120: Electrical conductivity between 2 and 4 dS/m
    * D140: Electrical conductivity between 4 and 8 dS/m
    * D170: Electrical conductivity between 8 and 16 dS/m
    * D200: Electrical conductivity higher than 16 dS/m
    
    Categories within soilsalty_phy_cat_l4d_ld have been taken taken from: 
    https://openknowledge.fao.org/server/api/core/bitstreams/1b8b05e9-a7dc-4883-a631-f5299f273d4e/content
    
    """
    def __init__(self):
        self.input_layer_name = "soilsalty_phy_con"
        self.output_layer_name = "soilsalty_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "< 2 dS/m"),
                                           120 : ("D120", "2 - 4 dS/m"),
                                           140 : ("D140", "4 - 8 dS/m"),
                                           170 : ("D170", "8 - 16 dS/m"),
                                           200 : ("D200", "> 16 dS/m")}
        self.class_boundaries = { 100 : (0, 2),
                                  120 : (2, 4),
                                  140 : (4, 8),
                                  170 : (8, 16),
                                  200 : (16, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class SoilalkaPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Soil alkalinity (soilalka_phy_cat_l4d_ld) 

    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continous data representing pH in soil (unitless).
    Alkalin soils (with negative associated impacts) are usually associated with pH > 8.5. 
    pH values are reclassified into levels of degradation/desertification risk (low to high).
    * D100: pH lower than 7
    * D170: pH between 7 and 8
    * D200: pH higher than 8 
        
    """
    def __init__(self):
        self.input_layer_name = "soilalka_phy_con"
        self.output_layer_name = "soilalka_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "pH < 7"),
                                           170 : ("D170", "7 < pH < 8"),
                                           200 : ("D200", "pH > 8")}
        # as water pH value in soil, mulitplied by 10                                        
        self.class_boundaries = { 100 : (0, 70),
                                  170 : (70, 80), 
                                  200 : (80, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set valid level4 classes based on electrical conductivity value (soil salinity) - Alkalin if EC > 4 dS/m ?
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class FireriskVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Fire risk (firerisk_veg_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing land classes.
    Land classes are grouped according to their sensibility to fire and their capacity to recover from wildfire events. 
    These categories are reclassified into levels of degradation/desertification risk (low to high).
    * D100: Mineral extraction sites, permanently irrigated land, rice fields, beaches, dunes, sands, bare rocks, sparsely vegetated areas
    * D130: Non-irrigated arable land, vineyards, pastures,annual crops associated with permanent crops, complex cultivation patterns, broad-leaved forest, natural grasslands
    * D160: Land principally occupied by agriculture, with significant areas of natural vegetation, mixed forest, moors and heathland, transitional woodland-shrub, inland marshes
    * D200: Fruit trees and berry plantations, agroforestry areas,coniferous forest, sclerophyllous vegetation, burnt areas, peat bogs
    
    Categories within firerisk_veg_cat_l4a_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "firerisk_veg_cat"
        self.output_layer_name = "firerisk_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "CORINE's classes: 131,212,213,331,332,333"),
                                           130 : ("D130", "CORINE's classes: 211,221, 231,241,242,311,321"),
                                           160 : ("D160", "CORINE's classes: 243,313,322,324,411"),
                                           200 : ("D200", "CORINE's classes: 222,244,312,323,334,421")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class ErosprotcVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Erosion protection (erosprotc_veg_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be categorical data representing land classes.
    Land classes are grouped according to their capacity to protect the soil from linear and non-linear greomorphological erosion processes.
    These categories are reclassified into levels of degradation/desertification risk (low to high).
    * D100: Rice fields, broad-leaved forest, coniferous forest, mixed forest, moors and heathland, inland marshes, peat bogs
    * D130: Fruit trees and berry plantations, pastures, land principally occupied by agriculture, with significant areas of natural vegetation, natural grasslands, transitional woodland-shrub
    * D160: Annual crops associated with permanent crops, complex cultivation patterns, agroforestry areas
    * D200: Mineral extraction sites, non-irrigated arable land, permanently irrigated land, vineyards, sclerophyllous vegetation, beaches, dunes, sands, bare rocks, sparsely vegetated areas, burnt areas
    
    Categories within erosprotc_veg_cat_l4a_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "erosprotc_veg_cat"
        self.output_layer_name = "erosprotc_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "CORINE's classes: 213,311,312,313,322,411,421"),
                                           130 : ("D130", "CORINE's classes: 222,231,243,321,324"),
                                           160 : ("D160", "CORINE's classes: 241,242,244"),
                                           200 : ("D200", "CORINE's classes: 131,211,212,221,323,331,332,333,334")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class DryresistVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Drought resistance (dryresist_veg_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be categorical data representing land classes.
    Land classes are grouped according to their drought's resistance. 
    These categories are reclassified into levels of degradation/desertification risk (low to high).
    * D100: Mineral extraction sites, permanently irrigated land, rice fields, agroforestry areas, broad-leaved forest, coniferous forest, mixed forest, moors and heathland, transitional woodland-shrub, inland marshes, peat bogs
    * D120: Natural grasslands
    * D140: Vineyards, fruit trees and berry plantations, land principally occupied by agriculture, with significant areas of natural vegetation
    * D170: Pastures, annual crops associated with permanent crops,complex cultivation patterns
    * D200: Non-irrigated arable land, sclerophyllous vegetation,beaches, dunes, sands, bare rocks, sparsely vegetated areas, burnt areas
    
    Categories within dryresist_veg_cat_l4a_ld have been taken from from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "dryresist_veg_cat"
        self.output_layer_name = "dryresist_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "CORINE's classes: 131,212,213,244,311,312,313,322,324,411,421"),
                                           120 : ("D120", "CORINE's classes: 321"),
                                           140 : ("D140", "CORINE's classes: 221,222,243"),
                                           170 : ("D170", "CORINE's classes: 231,241,242"),
                                           200 : ("D200", "CORINE's classes: 211,323,331,332,333,334")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class CanopycoVegCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Canopy cover (canopyco_veg_cat_l4d_ld) DERIVATIVE
    
    Input class is envisaged to be continuous data representing NDVI values, and used as proxy of vegetation cover (%).
    Categories are translated into levels of degradation/desertification risk (low to high).
    * D100: NDVI > 0.80
    * D110: 0.70 < NDVI < 0.80
    * D120: 0.62 < NDVI < 0.70
    * D130: 0.50 < NDVI < 0.62
    * D140: 0.38 < NDVI < 0.50
    * D150: 0.26 < NDVI < 0.38
    * D160: 0.18 < NDVI < 0.26
    * D170: 0.13 < NDVI < 0.18 
    * D180: 0.11 < NDVI < 0.13
    * D190: 0.10 < NDVI < 0.11
    * D200: NDVI < 0.10
    
    Categories within rainfall_cqi_cat_l4d have been taken from: 
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
    
    Tier 1 class (111, 112, 123, 124)
    
    """
    def __init__(self):
        self.input_layer_name = "canopyco_veg_con"
        self.output_layer_name = "canopyco_veg_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "NDVI > 0.80"),
                                          110 : ("D110", "0.70 < NDVI < 0.80"),
                                          120 : ("D120", "0.62 < NDVI < 0.70"),
                                          130 : ("D130", "0.50 < NDVI < 0.62"),
                                          140 : ("D140", "0.38 < NDVI < 0.50"),
                                          150 : ("D150", "0.26 < NDVI < 0.38"),
                                          160 : ("D160", "0.18 < NDVI < 0.26"),
                                          170 : ("D170", "0.13 < NDVI < 0.18"),
                                          180 : ("D180", "0.11 < NDVI < 0.13"),
                                          190 : ("D190", "0.10 < NDVI < 0.11"),
                                          200 : ("D200", "NDVI < 0.10")}
        self.class_boundaries = {100 : (0.80, 1),
                                 110 : (0.70, 0.80),
                                 120 : (0.62, 0.70),
                                 130 : (0.50, 0.62),
                                 140 : (0.38, 0.50),
                                 150 : (0.26, 0.38),
                                 160 : (0.18, 0.26),
                                 170 : (0.13, 0.18),
                                 180 : (0.11, 0.13),
                                 190 : (0.10, 0.11),
                                 200 : (None, 0.10)}
        # Set valid level3 classes
        self.valid_level3_classes = [111, 112, 123, 124] # or only vegetation? and exclude agricultural/...?
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class AgriintyAgrCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Agricultural intensity (agriinty_agr_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing land classes. 
    Land classes are grouped according to the degree of anthropic intervention, mainly through agricultural activity.
    These categories are reclassified into levels of degradation/desertification risk (low to high).
    * D100: mineral extraction sites, fruit trees and berry plantations, agroforestry areas, broad-leaved forest, coniferous forest, mixed forest, natural grasslands, moors and heathland, sclerophyllous vegetation, transitional woodland-shrub, beaches, dunes, sands, bare rocks, sparsely vegetated areas, burnt areas, inland marshes, peat bogs
    * D150: pastures, annual crops associated with permanent crops, land principally occupied by agriculture, with significant areas of natural vegetation
    * D200: non-irrigated arable land, permanently irrigated land, rice fields, vineyards, complex cultivation patterns
    
    Categories within agriinty_agr_cat_l4a_ld have been taken from 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "agriinty_agr_cat"
        self.output_layer_name = "agriinty_agr_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "CORINE's classes: 131,222,244,311,312,313,321,322,323,324,331,332,333,334,411,421"),
                                           150 : ("D150", "CORINE's classes: 231,241,243"),
                                           200 : ("D200", "CORINE's classes: 211,212,213,221,242")}
        # Set valid level3 classes
        self.valid_level3_classes = [111, 112, 123, 124, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN
        
class PolicyenfAgrCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Policy ennforcement (policyenf_agr_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be categorical data representing land classes.
    Land classes are grouped according to the degree of anthropic intervention to improve restrictive environmental conditions and to ensure land protection against various degradation processes. 
    * D100: permanently irrigated land, rice fields, broad-leaved forest, coniferous forest, mixed forest, natural grasslands,moors and heathland, sclerophyllous vegetation, transitional woodland-shrub, beaches, dunes, sands,bare rocks, sparsely vegetated areas, inland marshes, peat bogs
    * D150: vineyards, fruit trees and berry plantations, pastures, land principally occupied by agriculture, with significant areas of natural vegetation, agroforestry areas, burnt areas
    * D200: mineral extraction sites, non-irrigated arable land, annual crops associated with permanent crops, complex cultivation patterns
    
    Categories within policyenf_agr_cat_l4a_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "policyenf_agr_cat"
        self.output_layer_name = "policyenf_agr_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "CORINE's classes: 212,213,311,312,313,321,322,323,324,331,332,333,411,421"),
                                          150 : ("D150", "CORINE's classes: 221,222,231,243,244,334"),
                                          200 : ("D200", "CORINE's classes: 131,211,241,242")} 
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class GradientTerEnvCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Slope (gradient_ter_env_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continuous data representing slope steepness percentage (%).
    Slope gradient is translated into levels of degradation/desertification risk (low to high).
    * D100: Slope less steep than 3%
    * D110: Slope between 3 and 6%
    * D120: Slope between 6 and 12%
    * D130: Slope between 12 and 18%
    * D140: Slope between 18 and 24%
    * D150: Slope between 24 and 30%
    * D170: Slope between 30 and 36%
    * D200: Slope steeper than 36%
    
    Categories within gradient_ter_env_cat_l4d_ld have been taken from: 
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
    
    """
    def __init__(self):
        self.input_layer_name = "gradient_ter_env_con"
        self.output_layer_name = "gradient_ter_env_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 3%"),
                                          110 : ("D110", "3 - 6%"),
                                          120 : ("D120", "6 - 12%"),
                                          130 : ("D130", "12 - 18%"),
                                          140 : ("D140", "18 - 24%"),
                                          150 : ("D150", "24 - 30%"),
                                          170 : ("D170", "30 - 36%"),
                                          200 : ("D200", "> 36%")} 
        self.class_boundaries = {100 : (0, 3),
                                 110 : (3, 6),
                                 120 : (6, 12),
                                 130 : (12, 18),
                                 140 : (18, 24),
                                 150 : (24, 30),
                                 170 : (30, 36),
                                 200 : (36, 100)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class SlopeaspTerCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer): 
    """
    Slope aspect (slopeasp_ter_cat_l4a_ld)
    
    An additional level 4 class specific for ld implementation.

    Input class is envisaged to be categorical data representing slope orientation to the sun in degree, according to the categories hereafter. 
    Slope orientation/aspect is translated into levels of degradation/desertification risk (low to high).
    * D100: North (337.5 to 360 or 0 to 22.5 degree) , Northeast (22.5 to 67.5 degree), Northwest (292.5 to 337.5 degree), West (247.5 to 292.5 degree), and flat area.
    * D200: South (157.5 to 202.5 degree), Southeast (112.5 to 157.5 degree), Southwest (202.5 to 247.5 degree), East (67.5 to 112.5 degree)

    Categories within slopeasp_ter_cat_l4a_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "slopeasp_ter_cat"
        self.output_layer_name = "slopeasp_ter_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "N, NE, NW, W, Flat area"),
                                           200 : ("D200", "S, SE, SW, E")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class PlancurvTerCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Plan curvature (plancurv_ter_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continuous data representing slope curvature degree horizontally, in radians/m. 
    Plan curvature is translated into levels of degradation/desertification risk (low to high).
    * D100: Convex (> 0.11 rad/m)
    * D150: Plane or slightly concave/convexe (between -0.50 and 0.11 rad/m)
    * D200: Concave (< -0.50 rad/m)
    
    Categories within plancurv_ter_cat_l4d_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
   
    """
    def __init__(self):
        self.input_layer_name = "plancurv_ter_con"
        self.output_layer_name = "plancurv_ter_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "> 0.11 rad/m"),
                                          150 : ("D150", "-0.50 to 0.11 rad/m)"),
                                          200 : ("D200", "< -0.50 rad/m")}
        self.class_boundaries = {100 : (0.11, None),
                                 150 : (-0.50, 0.11),
                                 200 : (None, -0.50)
                                }
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class ProfilecurvTerCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Profile curvature (profilecurv_ter_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continuous data representing slope curvature degree vertically, in radians/m.
    Profile curvature is translated into levels of degradation/desertification risk (low to high).
    * D100: Convexe (> 0.02 rad/m) 
    * D150: Plane or slighly concave/convexe (between -0.39 and 0.02 rad/m)
    * D200: Concave (< -0.39 rad/m)
    
    Categories within profilecurv_ter_cat_l4d_ld have been taken from:
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
   
    """
    def __init__(self):
        self.input_layer_name = "profilecurv_ter_con"
        self.output_layer_name = "profilecurv_ter_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "> 0.02 rad/m"),
                                          150 : ("D150", "-0.39 to 0.02 rad/m"),
                                          200 : ("D200", "< -0.39 rad/m")}
        self.class_boundaries = {100 : (0.02, None),
                                 150 : (-0.39, 0.02),
                                 200 : (None, -0.39)
                                }
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class DraindensWatCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Drainage density (draindens_wat_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
    
    Input class is envisaged to be continous data representing density of rivers (km/km2).
    Density of river network is translated into levels of degradation/desertification risk (low to high).
    * D100: Density higher than 1.50 km/km2
    * D150: Density between 0.70 and 1.50 km/km2
    * D200: Density lower than 0.70 km/km2
    
    Categories within draindens_wat_cat_l4d_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
   
    """
    def __init__(self):
        self.input_layer_name = "draindens_wat_con"
        self.output_layer_name = "draindens_wat_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "> 1.50 km/km2"),
                                          150 : ("D150", "0.70 to 1.50 km/km2"),
                                          200 : ("D200", "< 0.70 km/km2")} 
        self.class_boundaries = {100 : (1.50, None),
                                 150 : (0.70, 1.50),
                                 200 : (0, 0.70)}
        # Set valid level3 classes
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216, 220, 227, 228] #no exclusion of water content?
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class GrndwtrdpWatCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Groundwater depth (grndwtrdp_wat_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
   
    Input class is envisaged to be continous data of groundwater depth (m above surface).
    The depth to groundwater is translated into levels of degradation/desertification risk (low to high).
    * D100: Groudwater table depth between 2 and 3 m
    * D130: Groudwater table depth between 1 and 2 m
    * D160: Groudwater table depth between 0.50 and 1 m
    * D2001: Groudwater table depth less than 0.50
    * D2002: Groundwater table depth deeper than 3m
    
    Categories within grndwtrdp_wat_cat_l4d_ld have been adapted from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
    
    """
    def __init__(self):
        self.input_layer_name = "grndwtrdp_wat_con"
        self.output_layer_name = "grndwtrdp_wat_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "2 to 3m"),
                                          130 : ("D130", "1 to 2m"),
                                          160 : ("D160", "0.50 to 1m"),
                                          201 : ("D200", "< 0.5m"), #to be adapted 
                                          202 : ("D200", "> 3m")}  # to be adatped
        self.class_boundaries = {100 : (2, 3),
                                 130 : (1, 2),
                                 160 : (0.50, 1),
                                 201 : (None, 0.50),
                                 202 : (3, None)}
        # Set valid level3 classes
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216, 220, 227, 228]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class PopudensUrbCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Population density (popudens_urb_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
   
    Input class is envisaged to be continous data representing density of population (people/km2) for a targeted time.
    Population densitiy is translated into levels of degradation/desertification risk (low to high). 
    * D100: Population density lower than 4 people/km2
    * D110: Population density between 4 and 30 people/km2
    * D120: Population density between 30 and 80 people/km2
    * D130: Population density between 80 and 170 people/km2
    * D140: Population density between 170 and 300 people/km2
    * D150: Population density between 300 and 500 people/km2
    * D160: Population density between 500 and 850 people/km2
    * D170: Population density between 850 and 1400 people/km2
    * D180: Population density between 1400 and 2000 people/km2
    * D190: Population density between 2000 and 2700 people/km2
    * D200: Population density higher than 2700 people/km2
    
    Categories within popudens_urb_cat_l4d_ld have been taken from: 
    Ferrara et al., (2020). Updating the MEDALUS-ESA Framework for Worldwide Land Degradation and Desertification Assessment. Land Degradation & Development, 31(12), 1593-1607. https://doi.org/https://doi.org/10.1002/ldr.3559 
    
    """
    def __init__(self):
        self.input_layer_name = "popudens_urb_con"
        self.output_layer_name = "popudens_urb_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 4 people/km2"),
                                          110 : ("D110", "4 - 30 people/km2"),
                                          120 : ("D120", "30 - 80 people/km2"),
                                          130 : ("D130", "80 - 170 people/km2"),
                                          140 : ("D140", "170 - 300 people/km2"),
                                          150 : ("D150", "300 - 500 people/km2"),
                                          160 : ("D160", "500 - 850 people/km2"),
                                          170 : ("D170", "850 - 1400 people/km2"),
                                          180 : ("D180", "1400 - 2000 people/km2"),
                                          190 : ("D190", "2000 - 2700 people/km2"),
                                          200 : ("D200", "> 2700 people/km2")} 
        self.class_boundaries = {100 : (0, 4),
                                 110 : (4, 30),
                                 120 : (30, 80),
                                 130 : (80, 170),
                                 140 : (170, 300),
                                 150 : (300, 500),
                                 160 : (500, 850),
                                 170 : (850, 1400),
                                 180 : (1400, 2000),
                                 190 : (2000, 2700),
                                 200 : (2700, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class PopgrowthUrbCatL4d_ld(l4_base.Level4ClassificationContinuousLayer): 
    """
    Population growth rate (popgrowth_urb_cat_l4d_ld)
    
    An additional level 4 class specific for ld implementation.
   
    Input class is envisaged to be continous data representing population growth rate (%).
    Population growth rate is translated into degradation/desertification risk level (low to high).
    * D100: Population growth rate lower than 2%
    * D120: Population growth rate between 2 and 4%
    * D140: Population growth rate between 4 and 6%
    * D160: Population growth rate between 6 and 8%
    * D180: Population growth rate between 8 and 10%
    * D200: Population growth rate higher than 10%
    
    Categories within popgrowth_urb_cat_l4d_ld have been taken from: 
    Pravalie et al. (2020). Spatial assessment of land sensitivity to degradation across Romania. A quantitative approach based on the modified MEDALUS methodology. CATENA 2020 Vol. 187 Pages 104407. https://doi.org/10.1016/j.catena.2019.104407  
   
    """
    def __init__(self):
        self.input_layer_name = "popgrowth_urb_con"
        self.output_layer_name = "popgrowth_urb_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 2%"),
                                          120 : ("D120", "2 - 4%"),
                                          140 : ("D140", "4 - 6%"),
                                          160 : ("D160", "6 - 8%"),
                                          180 : ("D180", "8 - 10%"),
                                          200 : ("D200", ">10 %")} 
        self.class_boundaries = {100 : (0, 2),
                                 120 : (2, 4),
                                 140 : (4, 6),
                                 160 : (6, 8),
                                 180 : (8, 10),
                                 200 : (10, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class SoilerodiPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Soil erodibility (soilerodi_phy_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data representing soil erodibility potential.
    Soil erodibility categories are translated into degradation/desertification risk level (low to high).
    * D100: Very weak
    * D125: Weak
    * D150: Moderate
    * D175: Strong
    * D200: Very strong
    
    Categories within soilerodi_phy_cat_l4a_ld have been based on Remuse Pravalie's work within MONALISA project.
   
    """
    def __init__(self):
        self.input_layer_name = "soilerodi_phy_cat"
        self.output_layer_name = "soilerodi_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "Very weak"),
                                          125 : ("D125", "Weak"),
                                          150 : ("D150", "Moderate"),
                                          175 : ("D175", "Strong"),
                                          200 : ("D200", "Very strong")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class TillerosiAgrCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Tillage erosion (tillerosi_agr_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing tillage erosion rate (ton/ha/year).
    A degradation is considered for a value higher than 2 ton/ha/year.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "tillerosi_agr_con"
        self.output_layer_name = "tillerosi_agr_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 2 ton/ha/year"),
                                          200 : ("D200", "> 2 ton/ha/year")} 
        self.class_boundaries = {100 : (0, 2),
                                 200 : (2, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class HarverosiAgrCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Harvest erosion (harverosi_agr_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing soil loss by harvesting root crops (ton/ha/year).
    A degradation is considered for a value higher than 2 ton/ha/year.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "harverosi_agr_con"
        self.output_layer_name = "harverosi_agr_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 2 ton/ha/year"),
                                          200 : ("D200", "> 2 ton/ha/year")} 
        self.class_boundaries = {100 : (0, 2),
                                 200 : (2, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class AsexcessPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Arsenic excess (asexcess_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing exceedance probabilities of Aresenic in topsoil for the threshold of 45 mg/kg.
    A degradation is considered for a value higher than 5%.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "asexcess_phy_con"
        self.output_layer_name = "asexcess_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "P([As] > 45 mg kg-1) < 5%"),
                                          200 : ("D200", "P([As] > 45 mg kg-1) > 5%")} 
        self.class_boundaries = {100 : (0, 0.05),
                                 200 : (0.05, 1)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class CuexcessPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Copper excess (cuexcess_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing Copper concentration in topsoil, in mg kg-1.
    A degradation is considered for a value higher than 100 mg/kg.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "cuexcess_phy_con"
        self.output_layer_name = "cuexcess_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 100 mg/kg"),
                                          200 : ("D200", "> 100 mg/kg")} 
        self.class_boundaries = {100 : (0, 100),
                                 200 : (100, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class HgexcessPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Mercury excess (hgexcess_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing Mercury concentration in topsoil, in mg kg-1.
    A degradation is considered for a value higher than 0.5 mg kg-1.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "hgexcess_phy_con"
        self.output_layer_name = "hgexcess_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 0.5 mg kg-1"),
                                          200 : ("D200", "> 0.5 mg kg-1")} 
        self.class_boundaries = {100 : (0, 0.5),
                                 200 : (0.5, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class ZnexcessPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Zinc excess (znexcess_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing Zinc concentration in topsoil, in mg kg-1.
    A degradation is considered for a value higher than 100 mg kg-1.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "znexcess_phy_con"
        self.output_layer_name = "znexcess_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 100 mg kg-1"),
                                          200 : ("D200", "> 100 mg kg-1")} 
        self.class_boundaries = {100 : (0, 100),
                                 200 : (100, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class CdexcessPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Cadmium excess (cdexcess_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing Cadmium concentration in topsoil, in mg kg-1.
    A degradation is considered for a value higher than 1 mg kg-1.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "cdexcess_phy_con"
        self.output_layer_name = "cdexcess_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 1 mg kg-1"),
                                          200 : ("D200", "> 1 mg kg-1")} 
        self.class_boundaries = {100 : (0, 1),
                                 200 : (1, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class PcontentPhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Phosphorus deficiency and excess (pcontent_phy_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data representing phosphorus deficiency or excess in soil.
    A degradation is considered for a value lower than 20 mg kg- 1 (deficiency) or higher than 50 mg kg-1 (excess).

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "pcontent_phy_cat"
        self.output_layer_name = "pcontent_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "20 mg kg-1 < P < 50 mg kg-1"),
                                          200 : ("D200", "< 20 mg kg-1 or > 50 mg kg-1")} 
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216] 
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class BulkdensPhyCatL4d_ld(l4_base.Level4ClassificationContinuousLayer):
    """
    Bulk density (bulkdens_phy_cat_l4d_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be continuous data representing bulk density expressed in g cm-3.
    A degradation is considered for a value higher than 1.75 g cm-3.

    Threshold values and classes have been adapted from: https://esdac.jrc.ec.europa.eu/euso/euso-dashboard-sources
    """
    def __init__(self):
        self.input_layer_name = "bulkdens_phy_con"
        self.output_layer_name = "bulkdens_phy_cat_l4d_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = {100 : ("D100", "< 1.75 g cm-3"),
                                          200 : ("D200", "> 1.75 g cm-3")} 
        self.class_boundaries = {100 : (0, 1.75),
                                 200 : (1.75, None)}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.DERIVATIVE

class SocchangePhyCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Soil organic carbon change (socchange_phy_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data with binary classification "degraded" and "not degraded".
    """
    def __init__(self):
        self.input_layer_name = "socchange_phy_cat"
        self.output_layer_name = "socchange_phy_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Not degraded"),
                                           200 : ("D200", "Degraded")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class LptrendVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Land productivity trend (lptrend_veg_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data with binary classification "degraded" and "not degraded".
    """
    def __init__(self):
        self.input_layer_name = "lptrend_veg_cat"
        self.output_layer_name = "lptrend_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Not degraded"),
                                           200 : ("D200", "Degraded")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class LpstateVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Land productivity state (lpstate_veg_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data with binary classification "degraded" and "not degraded".
    """
    def __init__(self):
        self.input_layer_name = "lpstate_veg_cat"
        self.output_layer_name = "lpstate_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Not degraded"),
                                           200 : ("D200", "Degraded")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class LpperformVegCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Land productivity performance (lpperform_veg_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data with binary classification "degraded" and "not degraded".
    """
    def __init__(self):
        self.input_layer_name = "lpperform_veg_cat"
        self.output_layer_name = "lpperform_veg_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Not degraded"),
                                           200 : ("D200", "Degraded")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN

class LcchangeCatL4a_ld(l4_base.Level4ClassificationCatergoricalLayer):
    """
    Land cover change (lcchange_cat_l4a_ld)
    An additional level 4 class specific for LD implementation.

    Input class is envisaged to be categorical data with binary classification "degraded" and "not degraded".
    """
    def __init__(self):
        self.input_layer_name = "lcchange_cat"
        self.output_layer_name = "lcchange_cat_l4a_ld"
        self.input_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.input_layer_name)
        self.output_layer_uncertainty_name = self.get_uncertainty_layer_name(
            self.output_layer_name)
        self.output_codes_descriptions = { 100 : ("D100", "Not degraded"),
                                           200 : ("D200", "Degraded")}
        # Set valid level3 classes to exclude water components (220, 227, 228)
        self.valid_level3_classes = [111, 112, 123, 124, 215, 216]
        # Set type for class
        self.layer_type = l4_base.ClassificationLayerTypes.MAIN


#: List of standard and modified layers used for ld classification
ALL_L4_LAYER_CLASSES_ld_MODIFIED = [l4_layers_lccs.LCCSLevel3,
                                       l4_layers_lccs.LifeformVegCatL4a,
                                       l4_layers_lccs.MlifefrmVegCatL4m,
                                       CanopycoVegCatL4d_ld,
                                       l4_layers_lccs.CanopyhtVegCatL4d,
                                       l4_layers_lccs.WaterdayAgrCatL4a,
                                       l4_layers_lccs.WaterseaVegCatL4a,
                                       l4_layers_lccs.LeaftypeVegCatL4a,
                                       l4_layers_lccs.PhenologVegCatL4a,
                                       l4_layers_lccs.MphenlogVegCatL4m,
                                       l4_layers_lccs.UrbanvegUrbCatL4a,
                                       l4_layers_lccs.SpatdistVegCatL4a,
                                       l4_layers_lccs.Strat2ndVegCatL4a,
                                       l4_layers_lccs.Lifef2ndVegCatL4a,
                                       l4_layers_lccs.Cover2ndVegCatL4d,
                                       l4_layers_lccs.Heigh2ndVegCatL4d,
                                       l4_layers_lccs.SpatsizeAgrCatL4a,
                                       l4_layers_lccs.CropcombAgrCatL4a,
                                       l4_layers_lccs.Croplfc2AgrCatL4a,
                                       l4_layers_lccs.Croplfc3AgrCatL4a,
                                       l4_layers_lccs.CropseqtAgrCatL4a,
                                       l4_layers_lccs.CropseqaAgrCatL4a,
                                       l4_layers_lccs.WatersupAgrCatL4a,
                                       l4_layers_lccs.TimefactAgrCatL4a,
                                       l4_layers_lccs.WatersttWatCatL4a,
                                       l4_layers_lccs.InttidalWatCatL4a,
                                       l4_layers_lccs.WaterperWatCatL4d,
                                       l4_layers_lccs.SnowcperWatCatL4d,
                                       l4_layers_lccs.WaterdptWatCatL4a,
                                       l4_layers_lccs.MwatrmvtWatCatL4m,
                                       l4_layers_lccs.WsedloadWatCatL4a,
                                       l4_layers_lccs.MsubstrtWatCatL4m,
                                       l4_layers_lccs.BaresurfPhyCatL4a,
                                       l4_layers_lccs.MbarematPhyCatL4m,
                                       l4_layers_lccs.MustonesPhyCatL4m,
                                       l4_layers_lccs.MhardpanPhyCatL4m,
                                       l4_layers_lccs.MacropatPhyCatL4a,
                                       l4_layers_lccs.ArtisurfUrbCatL4a,
                                       l4_layers_lccs.MtclineaUrbCatL4m,
                                       l4_layers_lccs.MnolineaUrbCatL4m,
                                       l4_layers_lccs.MartdensUrbCatL4m,
                                       l4_layers_lccs.MnobuiltUrbCatL4m,
                                       PrecipitAtmEnvCatL4d_ld,
                                       AridindexAtmCatL4d_ld,
                                       RainerosiAtmCatL4d_ld,
                                       WindspeedAtmCatL4d_ld,
                                       ParentmatPhyCatL4a_ld,
                                       RockfragmPhyCatL4d_ld,
                                       SoildepthPhyCatL4a_ld,
                                       SoiltextPhyCatL4a_ld,
                                       SoildrainPhyCatL4a_ld,
                                       SoilsaltyPhyCatL4d_ld,
                                       SoilalkaPhyCatL4d_ld,
                                       FireriskVegCatL4a_ld,
                                       ErosprotcVegCatL4a_ld,
                                       DryresistVegCatL4a_ld,
                                       AgriintyAgrCatL4a_ld,
                                       PolicyenfAgrCatL4a_ld,
                                       GradientTerEnvCatL4d_ld,
                                       SlopeaspTerCatL4a_ld,
                                       PlancurvTerCatL4d_ld,
                                       ProfilecurvTerCatL4d_ld,
                                       DraindensWatCatL4d_ld,
                                       GrndwtrdpWatCatL4d_ld,
                                       PopudensUrbCatL4d_ld,
                                       PopgrowthUrbCatL4d_ld,
                                       SoilerodiPhyCatL4a_ld,
                                       TillerosiAgrCatL4d_ld,
                                       HarverosiAgrCatL4d_ld,
                                       AsexcessPhyCatL4d_ld,
                                       CuexcessPhyCatL4d_ld,
                                       HgexcessPhyCatL4d_ld,
                                       ZnexcessPhyCatL4d_ld,
                                       CdexcessPhyCatL4d_ld,
                                       PcontentPhyCatL4a_ld,
                                       BulkdensPhyCatL4d_ld,
                                       SocchangePhyCatL4a_ld,
                                       LptrendVegCatL4a_ld,
                                       LpstateVegCatL4a_ld,
                                       LpperformVegCatL4a_ld,
                                       LcchangeCatL4a_ld]