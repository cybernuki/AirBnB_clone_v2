#!/usr/bin/python3
# This fabscript deploys the web static content
from os import path
from fabric.api import run, env, put

env.hosts = ["127.0.0.1"]


def do_deploy(archive_path):
    """
    send and configure the web static content
    """
    # Assure that given parameter is a file
    if not path.isfile(archive_path):
        return False

    # Paths variables
    file_ = archive_path.split("/")[-1]
    name = file_.split(".")[0]
    tmp = "/tmp/{}".format(file_)
    data = "/data/web_static/releases/{}/".format(name)
    current = "/data/web_static/current"

    # Send compressed file
    if put(archive_path, tmp).failed:
        return False
    # Remove a previous release
    if run("rm -rf {}".format(data)).failed:
        return False
    # Create a directorty to allocate the new release
    if run("mkdir -p {}".format(data)).failed:
        return False
    # Uncompress archive
    if run("tar -xzf {} -C {}".format(tmp, data)).failed:
        return False
    # Remove compressed archive
    if run("rm {}".format(tmp)).failed:
        return False
    # Move uncomprresed data of web static to the release folder
    if run("mv {}web_static/* {}".format(data, data)).failed:
        return False
    # Remove uncompressed data from sistem
    if run("rm -rf {}web_static".format(data)).failed:
        return False
    # Remove previous link to web static content
    if run("rm -rf {}".format(current)).failed:
        return False
    # Create a new link to the new release content
    if run("ln -s {} {}".format(data, current)).failed:
        return False
    # Finish the deploy!
    print("New version deployed!")

    return True
