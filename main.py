#!/usr/bin/env python3

from ne8000 import HuaweiGenerator
from perfiles import perfiles

hbng = HuaweiGenerator()

for perfil in perfiles:
    hbng.QoSProfile(perfil['nombre'], perfil['download'], perfil['upload'], perfil['unidad'])