#!/usr/bin/env python3

class HuaweiConfig(object):
    def __init__(self):
        pass

class HuaweiGenerator(object):
    def __init__(self):
        pass
    
    @staticmethod
    def QoSProfile(nombre, download, upload, unidad='m'):
        """
        Genera los profiles de QoS para aplicar a los clientes PPPoE
        El in y el out debe ser ingresado en mbps
        """
        
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
        
        print(f'qos-profile {nombre}')
        print(f' car cir {cir_download} pir {pir_download} green pass yellow pass red discard outbound')
        print(f' car cir {cir_upload} pir {pir_upload} green pass yellow pass red discard inbound')
        print()