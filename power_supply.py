from eaps2000 import eaps2k

with eaps2k('COM4') as ps:
    cfg = eaps2k.get_config_template()
    cfg['ACK'] = True
    cfg['OVP'] = 10.0
    cfg['OCP'] = 5.0 
    cfg['Iset'] = 0.5
    cfg['Vset'] = 4.0

    ps.set_output_state(False)
    ps.configure(cfg)
    ps.set_output_state(True)

    ps.print_info()