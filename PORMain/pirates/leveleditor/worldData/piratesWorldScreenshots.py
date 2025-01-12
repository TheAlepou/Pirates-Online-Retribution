from pandac.PandaModules import Point3, VBase3
objectStruct = {
    'Objects': {
        '1141410776.53sdnaik': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1135280776.06dzlu': {
                    'Type': 'Island',
                    'Name': 'Bilgewater',
                    'File': 'BilgewaterIsland',
                    'Hpr': VBase3(-60.0, 0.0, 0.0),
                    'Objects': {
                        '1141788542.31sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-6.2918, -135.71, 123.133),
                            'Radi': [
                                1055,
                                1355,
                                1655],
                            'Scale': VBase3(1.0, 1.0, 1.0) },
                        '1146285188.25jubutler': {
                            'Type': 'Cell Portal Area',
                            'Name': 'cell_green_area',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Objects': { },
                            'Pos': Point3(-55.951, 266.141, 0.0),
                            'Scale': VBase3(1.0, 1.0, 1.0) } },
                    'Pos': Point3(-43.8758, 266.485, -0.002),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/bilgewater_zero' } },
                '1142029127.2sdnaik': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '2',
                    'Pos': Point3(1396.3689999999999, -4470.4809999999998, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Merchant',
                    'Team': '2' },
                '1142029253.38sdnaik': {
                    'Type': 'Ship Movement Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '2',
                    'Pos': Point3(2480.799, -2172.1779999999999, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Merchant',
                    'Team': '2' },
                '1142029312.31sdnaik': {
                    'Type': 'Ship Movement Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(-279.973, -4300.9949999999999, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Warship',
                    'Team': '1' },
                '1142029640.48sdnaik': {
                    'Type': 'Ship Movement Node',
                    'Flagship': False,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(551.442, -6648.3159999999998, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Warship',
                    'Team': '1' },
                '1142029643.17sdnaik': {
                    'Type': 'Ship Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(2388.2339999999999, -4901.145, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0) },
                '1142029649.52sdnaik': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': False,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '3',
                    'Pos': Point3(1319.823, -1769.396, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Warship',
                    'Team': '1' },
                '1142029656.11sdnaik': {
                    'Type': 'Movement Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(121.723, -2864.748, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0) },
                '1146605142.08jubutler': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '2',
                    'Pos': Point3(4953.68, -693.755, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Merchant',
                    'Team': '2' },
                '1146605151.81jubutler': {
                    'Type': 'Ship Spawn Node',
                    'Flagship': True,
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Level': '2',
                    'Pos': Point3(-2873.576, -6131.773, 0.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'Merchant',
                    'Team': '2' } } } },
    'Node Links': [
        [
            '1142029312.31sdnaik',
            '1142029253.38sdnaik',
            'Bi-directional'],
        [
            '1142029312.31sdnaik',
            '1142029127.2sdnaik',
            'Bi-directional'],
        [
            '1142029640.48sdnaik',
            '1142029643.17sdnaik',
            'Bi-directional'],
        [
            '1142029643.17sdnaik',
            '1142029649.52sdnaik',
            'Bi-directional'],
        [
            '1142029649.52sdnaik',
            '1142029656.11sdnaik',
            'Bi-directional'],
        [
            '1142029640.48sdnaik',
            '1142029656.11sdnaik',
            'Bi-directional'],
        [
            '1142029253.38sdnaik',
            '1142029127.2sdnaik',
            'Bi-directional']],
    'Layers': { },
    'ObjectIds': {
        '1135280776.06dzlu': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1135280776.06dzlu"]',
        '1141410776.53sdnaik': '["Objects"]["1141410776.53sdnaik"]',
        '1141788542.31sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1135280776.06dzlu"]["Objects"]["1141788542.31sdnaik"]',
        '1142018473.22dxschafe': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142018473.22dxschafe"]',
        '1142029069.97sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142018473.22dxschafe"]["Objects"]["1142029069.97sdnaik"]',
        '1142029127.2sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029127.2sdnaik"]',
        '1142029253.38sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029253.38sdnaik"]',
        '1142029312.31sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029312.31sdnaik"]',
        '1142029640.48sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029640.48sdnaik"]',
        '1142029643.17sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029643.17sdnaik"]',
        '1142029649.52sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029649.52sdnaik"]',
        '1142029656.11sdnaik': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1142029656.11sdnaik"]',
        '1146285188.25jubutler': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1135280776.06dzlu"]["Objects"]["1146285188.25jubutler"]',
        '1146605142.08jubutler': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1146605142.08jubutler"]',
        '1146605151.81jubutler': '["Objects"]["1141410776.53sdnaik"]["Objects"]["1146605151.81jubutler"]' } }
