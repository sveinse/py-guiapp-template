# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

basepath = os.path.dirname(os.path.abspath(SPEC))

# Updated from https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Setuptools-Entry-Point
def Entrypoint(dist, group, name, extraimports, **kwargs):
    import pkg_resources

    # Get toplevel packages of distribution from metadata
    def get_toplevel(dist):
        distribution = pkg_resources.get_distribution(dist)
        if distribution.has_metadata('top_level.txt'):
            return list(distribution.get_metadata('top_level.txt').split())
        else:
            return []

    kwargs.setdefault('hiddenimports', [])
    packages = []
    for distribution in kwargs['hiddenimports']:
        packages += get_toplevel(distribution)
    if extraimports:
        packages += extraimports

    kwargs.setdefault('pathex', [])
    # get the entry point
    ep = pkg_resources.get_entry_info(dist, group, name)
    # insert path of the egg at the verify front of the search path
    kwargs['pathex'] = [ep.dist.location] + kwargs['pathex']
    # script name must not be a valid module name to avoid name clashes on import
    script_path = os.path.join(workpath, name + '-script.py')
    print("creating script for entry point", dist, group, name)
    with open(script_path, 'w') as fh:
        print("import", ep.module_name, file=fh)
        print("%s.%s()" % (ep.module_name, '.'.join(ep.attrs)), file=fh)
        for package in packages:
            print("import", package, file=fh)

    return Analysis(
        [script_path] + kwargs.get('scripts', []),
        **kwargs
    )

a = Entrypoint(dist='guiapp',
               group='console_scripts',
               name='guiapp',
               extraimports=[],
               pathex=[],
               binaries=[],
               datas=[
                   # Note this mirros install files in pkg_win.sh
                   (basepath + '/guiapp/ui/*.ui', 'guiapp/ui'),
               ],
               hiddenimports=[],
               hookspath=[],
               runtime_hooks=[],
               excludes=[],
               win_no_prefer_redirects=False,
               win_private_assemblies=False,
               cipher=block_cipher,
               noarchive=False,
               )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='guiapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='guiapp')
