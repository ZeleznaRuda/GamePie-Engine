# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\PC\\Documents\\Python\\gamepie\\src\\gamepie\\commands\\template-2025-08-12.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\gamepie\\assets', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='template-2025-08-12',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\gamepie\\assets\\icon\\icon700x700.ico'],
)
