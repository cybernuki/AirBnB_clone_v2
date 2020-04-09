#!/usr/bin/python3
# this fabric script generates a .tgz archive
# from the contest of the web_static folder
# using the do_pack
from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
        now = datetime.utcnow()
        file_ = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                              now.month,
                                                              now.day,
                                                              now.hour,
                                                              now.minute,
                                                              now.second)

        if not path.isdir("versions"):
                if local("mkdir -p versions").failed:
                        return None
        if local('tar -cvzf {} web_static'.format(file_)).failed:
                return None
        return file_
