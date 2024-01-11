#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the web_static."""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['100.26.254.92', '54.145.79.81']


def do_pack():
    """Function to generate a .tgz archive."""
    local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(current_date)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception as execption:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_extension = filename.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_extension))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, no_extension))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(no_extension, no_extension))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_extension))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_extension))
        return True
    except Exception as e:
        return False


def deploy():
    """Create and distribute an archive to my web servers."""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
