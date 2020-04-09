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

    # Send compressed file
    if put(archive_path, tmp).failed:
        return False
