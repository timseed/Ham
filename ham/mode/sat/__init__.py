from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
from .vubirds import VuBirds, SatFM
