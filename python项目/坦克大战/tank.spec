# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['tank.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/lijinshuai/Documents/个人文档/python历史/python项目/坦克大战/images','images'),('/Users/lijinshuai/Documents/个人文档/python历史/python项目/坦克大战/musics','musics')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='tank',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    manifest='akespec',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='tank',
)
app = BUNDLE(
    coll,
    name='tank.app',
    icon='/Users/lijinshuai/Documents/个人文档/python历史/python项目/坦克大战/images/logo.jpeg',
    bundle_identifier=None,
)
