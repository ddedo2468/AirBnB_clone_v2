#!/usr/bin/python3
"""some backups"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """pack a folder"""
    try:
        tdate = datetime.now().strftime('%Y%m%d%H%M%S')
        fName = f'web_static_{tdate}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{fName} web_static')
        return f'versions/{fName}'
    except Exception:
        return None
