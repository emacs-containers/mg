#! /usr/bin/env python3

import os


os.chdir(os.path.dirname(__file__))


def symlink(name, target):
    try:
        os.remove(name)
    except FileNotFoundError:
        pass
    os.symlink(target, name)


def wr(dirname, basename, contents):
    open(os.path.join(dirname, basename), "w").write(contents)


def gen(system, version, sha256sum):
    dirname = "{}-{}".format(system, version)
    os.makedirs(dirname, exist_ok=True)
    t = open("Dockerfile.{}".format(system)).read()
    wr(dirname, "Dockerfile", t.replace("{{version}}", version))
    wr(dirname, "checksum", "{}  mg.tar.gz\n".format(sha256sum))
    print("docker build -t mg:{} {}".format(dirname, dirname))


gen(
    "openbsd",
    "6.5",
    "3e4bb4582c8d1a72fb798bc320a9eede04f41e7e72a1421193174b1a6fc43cd8",
)
gen(
    "openbsd",
    "6.6",
    "2a4590124f9d3cf287b0863e0b24945ae2e46081cef73f72b0ddab6c86a56e72",
)
symlink("openbsd", "openbsd-6.6")
symlink("latest", "openbsd")
