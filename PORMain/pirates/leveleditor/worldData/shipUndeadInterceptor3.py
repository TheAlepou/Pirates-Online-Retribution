from pandac.PandaModules import Point3, VBase3, Vec4, Vec3
objectStruct = {
    'Objects': {
        '1189043800.81gjeon': {
            'Type': 'Ship Part',
            'Name': 'shipNavyInterceptor3',
            'Category': '38: Phantom',
            'File': '',
            'Flagship': True,
            'LogoOverride': '-1: Default',
            'Objects': {
                '1255998720.0jubutler': {
                    'Type': 'Spawn Node',
                    'AnimSet': 'default',
                    'AuraFX': 'None',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Min Population': '1',
                    'Patrol Radius': '12.0000',
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(1.5429, -17.163, 22.109),
                    'PoseAnim': '',
                    'PoseFrame': '',
                    'PropFXLeft': 'None',
                    'PropFXRight': 'None',
                    'PropLeft': 'None',
                    'PropRight': 'None',
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Area',
                    'Start State': 'Patrol',
                    'StartFrame': '0',
                    'Team': 'default',
                    'TrailFX': 'None',
                    'TrailLeft': 'None',
                    'TrailRight': 'None',
                    'VisSize': '',
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley' },
                    'spawnTimeBegin': 0.0,
                    'spawnTimeEnd': 0.0 },
                '1255998848.0jubutler': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(18.012, 9.6300000000000008, 23.530),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1255998848.0jubutler0': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-14.635, 3.6579, 23.536),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1255998848.0jubutler1': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(-12.938, -34.07, 22.155),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } },
                '1255998848.0jubutler2': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pause Chance': '100',
                    'Pause Duration': '30',
                    'Pos': Point3(14.147, -35.8818, 22.071),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'VisSize': '',
                    'Visual': {
                        'Color': (0.65, 0, 0, 1),
                        'Model': 'models/misc/smiley' } } },
            'Respawns': True,
            'StyleOverride': '-1: Default',
            'Team': 'EvilNavy',
            'Visual': {
                'Model': [
                    'models/shipparts/interceptorL3-geometry_High',
                    'models/shipparts/interceptorL3-collisions'] } } },
    'Node Links': [
        [
            '1255998720.0jubutler',
            '1255998848.0jubutler0',
            'Bi-directional'],
        [
            '1255998720.0jubutler',
            '1255998848.0jubutler',
            'Bi-directional'],
        [
            '1255998848.0jubutler',
            '1255998848.0jubutler0',
            'Bi-directional'],
        [
            '1255998848.0jubutler0',
            '1255998848.0jubutler1',
            'Bi-directional'],
        [
            '1255998848.0jubutler',
            '1255998848.0jubutler2',
            'Bi-directional'],
        [
            '1255998848.0jubutler1',
            '1255998848.0jubutler2',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1189043800.81gjeon': '["Objects"]["1189043800.81gjeon"]',
        '1255998720.0jubutler': '["Objects"]["1189043800.81gjeon"]["Objects"]["1255998720.0jubutler"]',
        '1255998848.0jubutler': '["Objects"]["1189043800.81gjeon"]["Objects"]["1255998848.0jubutler"]',
        '1255998848.0jubutler0': '["Objects"]["1189043800.81gjeon"]["Objects"]["1255998848.0jubutler0"]',
        '1255998848.0jubutler1': '["Objects"]["1189043800.81gjeon"]["Objects"]["1255998848.0jubutler1"]',
        '1255998848.0jubutler2': '["Objects"]["1189043800.81gjeon"]["Objects"]["1255998848.0jubutler2"]' } }
extraInfo = {
    'camPos': Point3(-173.398, -66.2502, 103.662),
    'camHpr': VBase3(-74.1058, -20.5578, 0),
    'focalLength': 1.3999999761599999,
    'skyState': 2,
    'fog': 0 }
