#!/usr/bin/python3
""" creating some backups """

from fabric.api import local
from datetime import datetime

def do_pack():
    """ generating .tgz archive """
    local("mkdir -p versions")

    tdate = datetime.now().strftime("%Y%m%d%H%M%S")
    
    file_name = "versions/web_static_{}.tgz".format(tdate)

    try:
        locals("tar -cvzf {} webstatic".format(file_name))
        return file_name
    
    except Exception as excetion:
        return None
