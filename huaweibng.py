#!/usr/bin/env python3
import os
import yaml
import re
from termtools import TerminalTools as TT
class HuaweiConfig(object):
    def __init__(self):
        self.term = TT()
        with open('perfiles.yaml', 'r') as f:
            self.config = yaml.safe_load(f)
            self.profiles = []
            keys = self.config.keys()
            self.profile_names = keys
            for key in keys:
                mydict = self.config[key]
                mydict['nombre'] = key
                self.profiles.append(mydict)
    
    def GetProfiles(self):
        return self.profiles
    
    def HuaweiQoSProfile(self, nombre, download, upload, unidad):
        """
        Genera los profiles de QoS en Huawei para aplicar a los clientes
        """
        
        if not re.search('[km]', unidad.lower()):
            return None

        multiplicador_download = 1.25 * 1000
        multiplicador_upload = 1.25 * 1000
        multiplicador_pir_download = 1.25
        multiplicador_pir_upload = 1.25
        
        if unidad.lower() == 'k':
            multiplicador_upload = multiplicador_upload / 1000
            multiplicador_download = multiplicador_download / 1000
        
        cir_download = int(download * multiplicador_download)
        cir_upload = int(upload * multiplicador_upload)
        pir_download = int(cir_download * multiplicador_pir_download)
        pir_upload = int(cir_upload * multiplicador_pir_upload)
        
        self.term.Red(f'qos-profile {nombre}')
        self.term.Yellow(f' car cir {cir_download} pir {pir_download} green pass yellow pass red discard outbound')
        self.term.Yellow(f' car cir {cir_upload} pir {pir_upload} green pass yellow pass red discard inbound')
        print()
    
    def GetSQLQoSProfiles(self):
        """
        Genera los INSERT SQL para agregar los profiles en la base de RADIUS
        """

        for profile in self.profile_names:
            self.term.Green(f"INSERT INTO radgroupreply (GroupName, Attribute, Op, Value) VALUES ('{profile}', 'Huawei-Qos-Profile-Name', ':=', '{profile}');")
        
        print(f'\n{len(self.profile_names)} INSERTs generados\n')
