# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['20210709_ScrapingScript_GreenJapan.py'],
             pathex=['C:\\Users\\tong\\ipynb\\単発\\GreenJapan'],
             binaries=[('./driver/chromedriver.exe', './driver'), ('./browser', './browser')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ScrapingTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='fav.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ScrapingTool')
