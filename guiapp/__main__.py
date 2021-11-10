import os
import sys
import asyncio
import qasync


def main():
    # Force darkmode
    os.environ['QT_QPA_PLATFORM'] = "windows:darkmode=1"

    try:
        from guiapp.main import main
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)


# To support -m guiapp
if __name__ == '__main__':
    main()
