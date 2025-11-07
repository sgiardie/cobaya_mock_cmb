#!/usr/bin/env python3
# Example script to create fiducial values for mock CMB likelihoods
from cobaya.model import get_model
import numpy as np
import cobaya_mock_cmb

# from best fit with fixed massless neutrinos and nuisance-marginalized high-l

fiducial_params = {"cosmomc_theta":0.0104092, "logA": 3.044, "ombh2": 0.02237, "omch2": 0.1200, "ns": 0.9649, "tau": 0.0544, "h": 0.6733981423479604} #,"As": 1e-10 * np.exp(3.044), "mnu": 0.06, "nnu": 3.044}

#fiducial_params_extra = { "N_ncdm": 1,  "m_ncdm": 0.06, "N_ur": 2.0308, "T_cmb": 2.7255, "lensing": "yes", "output": "tCl, pCl, lCl" }

accuracy_params = {"lens_potential_accuracy": 8, "lens_margin": 2050, "AccuracyBoost": 2.0, "lSampleBoost": 2.0, "lAccuracyBoost": 2.0, "kmax": 10, "k_per_logint": 130, "nonlinear": True, "DoLateRadTruncation": False}


fiducial_params_full = fiducial_params.copy()
fiducial_params_full.update(accuracy_params)

info_fiducial = {
    'params': fiducial_params,
    'likelihood': {'cobaya_mock_cmb.MockPlanck_lowell_T': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_lowell_T'},
                   'cobaya_mock_cmb.MockPlanck_lowell_E': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_lowell_E'},
                   'cobaya_mock_cmb.MockPlanck_highell': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_highell'},
                   'cobaya_mock_cmb.MockPlanck_highell_lensing': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_highell_lensing'},
                   'cobaya_mock_cmb.MockPlanck_only_highell': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_only_highell'},
                   'cobaya_mock_cmb.MockPlanck_only_highell_lensing': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_Planck_only_highell_lensing'},
                   'cobaya_mock_cmb.MockSO_lensing_1yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_1yr'},
                   'cobaya_mock_cmb.MockSO_lensing_2yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_2yr'},
                   'cobaya_mock_cmb.MockSO_lensing_3yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_3yr'},
                   'cobaya_mock_cmb.MockSO_lensing_4yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_4yr'},
                   'cobaya_mock_cmb.MockSO_lensing_5yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_5yr'},
                   'cobaya_mock_cmb.MockSO_lensing_6yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_6yr'},
                   'cobaya_mock_cmb.MockSO_lensing_7yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_7yr'},
                   'cobaya_mock_cmb.MockSO_lensing_8yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_8yr'},
                   'cobaya_mock_cmb.MockSO_lensing_9yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_9yr'},
                   'cobaya_mock_cmb.MockSO_lensing_10yr': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_10yr'},
                   'cobaya_mock_cmb.MockSO_lensing_baseline': {'python_path': '/nfshome/store01/groups/scw1361/sgiardie/mflike/cobaya_mock_cmb/cobaya_mock_cmb/mock_SO_lensing_baseline'},
                  # 'cobaya_mock_cmb.MockCMBS4sens0': {'python_path': '.'},
                  # 'cobaya_mock_cmb.MockPlanck': {'python_path': '.'}
                   },
    'theory': {"cosmopower":
    {"python_path": "/home/scw1361/sgiardie/mflike/cosmopower-itrharrison/",
    "package_file": "/home/scw1361/sgiardie/mflike/run_cp/networks/camb_networks/jense_2023_camb_lcdm.yaml",
    "root_dir": "/home/scw1361/sgiardie/mflike/run_cp/networks/camb_networks/jense_2023_camb_lcdm",
    "extra_args":
      {"lmax": {}},
    "renames":
      {"ombh2": "omega_b",
      "omch2": "omega_cdm",
      "logA": "ln10^{10}A_s",
      "ns": "n_s",
      "tau": "tau_reio",
      "zrei": "z_reio",
      "rdrag": "r_drag"},
    "speed": -1,
    "stop_at_error": True,
    "version": {},
    "input_params":
    {"ombh2","omch2","cosmomc_theta","logA","ns","tau","h"},
    "output_params": []}}}

model_fiducial = get_model(info_fiducial)

model_fiducial.logposterior({})

Cls = model_fiducial.provider.get_Cl(units="muK2")

for likelihood in model_fiducial.likelihood.values():
    likelihood.create_fid_values(Cls, fiducial_params_full, override=True)
