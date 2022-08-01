#!/usr/bin/env python3

if __name__ == '__main__':
    from huaweibng import HuaweiConfig

    hbng = HuaweiConfig()

    for perfil in hbng.GetProfiles():
        hbng.HuaweiQoSProfile(perfil['nombre'], perfil['download'], perfil['upload'], perfil['unidad'])
    
    print(f'{len(hbng.GetProfiles())} perfiles generados \n')

    hbng.GetSQLQoSProfiles()