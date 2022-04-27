import streamlit as st
import seirsplus

import numpy as np
import itertools
# seirsplus libraries
from seirsplus.models.preconfig_disease_models import *
from seirsplus.networks import *
from seirsplus import utils
from seirsplus.sim_loops import *
from seirsplus import scenarios

st.header('SEIRS+ Wrappers')

option = st.selectbox(
    'Which wrapper would you like to run?',
    ('', 'Community Scenario', 'Intervention Scenario', 'Primary School Scenario', 'Secondary School Scenario')
)


if option == 'Community Scenario':
    community_results, community_caselogs = scenarios.run_SARSCoV2_community_scenario()
    st.write('Community results:')
    st.write(community_results)

if option == 'Intervention Scenario':
    interventions_results, interventions_caselogs = scenarios.run_SARSCoV2_interventions_scenario()
    st.write('Interventions results')
    st.write(interventions_results)

if option == 'Primary School Scenario':
    primary_school_results, primary_school_caselogs = scenarios.run_SARSCoV2_primary_school_scenario()
    st.write('Primary School results')
    st.write(primary_school_results)

if option == 'Secondary School Scenario':
    secondary_school_results, secondary_school_caselogs = scenarios.run_SARSCoV2_secondary_school_scenario()
    st.write('Secondary School results')
    st.write(secondary_school_results)