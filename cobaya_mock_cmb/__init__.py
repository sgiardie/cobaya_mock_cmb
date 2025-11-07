"""
Mock CMB likelihoods for Cobaya
"""

# Base class
from .mock_cmb_likelihood import MockCMBLikelihood

# Particular examples
from .mock_Planck import MockPlanck
from .mock_SO import MockSO
from .mock_SO_baseline import MockSOBaseline
from .mock_SO_goal import MockSOGoal
from .mock_CMBS4 import MockCMBS4
from .mock_CMBS4sens0 import MockCMBS4sens0
from .mock_SO_clumping import MockSOClumping
from .mock_CMBS4_clumping import MockCMBS4Clumping
 
from .mock_Planck_lowell_T import MockPlanck_lowell_T
from .mock_Planck_lowell_E import MockPlanck_lowell_E
from .mock_Planck_highell import MockPlanck_highell
from .mock_Planck_highell_lensing import MockPlanck_highell_lensing
from .mock_Planck_only_highell import MockPlanck_only_highell
from .mock_Planck_only_highell_lensing import MockPlanck_only_highell_lensing
from .mock_SO_lensing_1yr import MockSO_lensing_1yr
from .mock_SO_lensing_2yr import MockSO_lensing_2yr
from .mock_SO_lensing_3yr import MockSO_lensing_3yr
from .mock_SO_lensing_4yr import MockSO_lensing_4yr
from .mock_SO_lensing_5yr import MockSO_lensing_5yr
from .mock_SO_lensing_6yr import MockSO_lensing_6yr
from .mock_SO_lensing_7yr import MockSO_lensing_7yr
from .mock_SO_lensing_8yr import MockSO_lensing_8yr
from .mock_SO_lensing_9yr import MockSO_lensing_9yr
from .mock_SO_lensing_10yr import MockSO_lensing_10yr
from .mock_SO_lensing_baseline import MockSO_lensing_baseline

# Metadata
__author__ = "Michael Rashkovetskyi, Julian B. Muñoz, Daniel J. Eisenstein and Cora Dvorkin"
__version__ = "0.1.0"
__obsolete__ = False
__year__ = "2021"
__url__ = "https://github.com/misharash/cobaya_mock_cmb"
