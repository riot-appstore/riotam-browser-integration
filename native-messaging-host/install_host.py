#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import argparse
import errno
import os
import stat
import sys
from os.path import expanduser
from shutil import copyfile

from common import get_target_dir, BrowserNotSupportedException


def main(argv):

    parser = init_argparse()

    try:
        args = parser.parse_args(argv)

    except Exception as e:
        print (str(e))
        return

    current_dir = os.getcwd()
    home_dir = expanduser("~")

    try:
        target_dir = get_target_dir(home_dir, args.browser)

    except BrowserNotSupportedException as e:
        print(str(e))
        return

    host_name = "de.fu_berlin.mi.riot_app_market"

    # Create directory to store native messaging host
    create_directories(target_dir)

    # Copy native messaging host manifest
    json_manifest = "%s.json" % host_name
    copyfile(json_manifest, os.path.join(target_dir, json_manifest))

    # Update host path in the manifest
    host_path = "%s/riot_app_market.py" % current_dir
    replace_host_path(os.path.join(target_dir, json_manifest), host_path)

    # Set permissions for the manifest so that all users can read it
    file = "{0}/{1}.json".format(target_dir, host_name)
    st = os.stat(file)
    os.chmod(file, st.st_mode | stat.S_IROTH)

    print ("Native messaging host {0} has been installed for {1}".format(host_name, args.browser))


def init_argparse():

    parser = argparse.ArgumentParser(description="Build RIOT OS")

    parser.add_argument("--browser",
                        dest="browser", action="store",
                        required=True,
                        help="the browser to install the host for. (chrome or chromium)")

    return parser


def create_directories(path):
    try:
        os.makedirs(path)

    except OSError as e:

        if e.errno != errno.EEXIST:
            raise


def replace_host_path(path, host_path):

    copyfile(path, path + ".old")

    with open(path + ".old", "r") as old_file:
        with open(path, "w") as file:

            for line in old_file.readlines():
                if "HOST_PATH" in line:
                    line = line.replace("HOST_PATH", host_path)

                file.write(line)

    os.remove(path + ".old")


if __name__ == "__main__":

    main(sys.argv[1:])