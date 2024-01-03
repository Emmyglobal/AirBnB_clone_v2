#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['	34.232.52.250', '100.24.237.16']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploy web files to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')
        # create target dir
        arc = archive_path.split("/")
        base = arc[-1].strip('.tgz')
        # timestamp = archive_path[-18:-4]
        sudo('mkdir -p /data/web_static/releases/{}/'
             .format(base))

        # uncompress archive and delete .tgz
        pat = '/data/web_static/releases/'
        sudo('tar -xzf /tmp/{0}.tgz -C {1}{0}/'.format(base, pat))

        # remove archive
        sudo('rm /tmp/{}.tgz'.format(base))

        # move contents into host web_static
        sudo('mv -f {1}{0}/web_static/* {1}{0}/'.format(base, pat))
        # remove extraneous web_static dir
        sudo('rm -rf {1}{0}/web_static'.format(base, pat))
        # delete pre-existing sym link
        sudo('rm -rf /data/web_static/current')

        # re-establish symbolic link
        sudo('sudo ln -s {1}{0} /data/web_static/current'.format(base, pat))
    except Exception as e:
        print(e)
        return False

    # return True on success
    return True
