#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers.
"""

from fabric.api import local, task
from os.path import isfile
from datetime import datetime
from fabric.operations import put, run, sudo

env.hosts = ['34.229.49.70', '54.172.112.10']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


@task
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the timestamp for the archive name
        time_format = "%Y%m%d%H%M%S"
        timestamp = datetime.utcnow().strftime(time_format)

        # Set the archive name
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into a .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error: {}".format(e))
        return None


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not isfile(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to the /data/web_static/releases/ directory
        archive_filename = archive_path.split("/")[-1]
        folder_name = archive_filename.split(".")[0]
        release_path = "/data/web_static/releases/"

        sudo("mkdir -p {}{}".format(release_path, folder_name))
        sudo("tar -xzf /tmp/{} -C {}{}/".format(archive_filename, release_path, folder_name))

        # Remove the archive from the web server
        sudo("rm /tmp/{}".format(archive_filename))

        # Move the files to the appropriate directory
        sudo("mv {0}{1}/web_static/* {0}{1}/".format(release_path, folder_name))

        # Remove the empty web_static directory
        sudo("rm -rf {}{}/web_static".format(release_path, folder_name))

        # Delete the old symbolic link
        sudo("rm -rf /data/web_static/current")

        # Create a new symbolic link
        sudo("ln -s {}{} /data/web_static/current".format(release_path, folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False


@task
def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)

