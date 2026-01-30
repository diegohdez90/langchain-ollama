"""Check if GPU is available and display its name.

Returns:
    _type_: None
"""

import sys
import torch
from log import LOG

is_available = torch.cuda.is_available()  # Should return True
gpu_name = torch.cuda.get_device_name(0)  # Shows GPU name
LOG.info("GPU Available: %s", is_available)
LOG.info("GPU Name: %s", gpu_name)
sys.exit(0)
