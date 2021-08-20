#Optimising code by creating parent class which hold all common utilities

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass