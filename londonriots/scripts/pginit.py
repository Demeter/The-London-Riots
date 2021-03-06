from londonriots.scripts import environment
import sys
import os
import os.path as opath
import logging
import subprocess as subp

log = None

pgdata_path = opath.join(sys.exec_prefix, "pgdata")

os.environ["PATH"] = ":".join((os.environ["PATH"], "/usr/lib/postgresql/8.4/bin"))

postgres_options = "-h localhost -k ./ -p 5488"
log_file = opath.join(pgdata_path, "initlog.log")

pg_ctl = ("pg_ctl", "--pgdata", pgdata_path, "-l", log_file, "-W")

def initdb():
    subp.check_call(("initdb", "--pgdata", pgdata_path, "--username", "postgres", "--encoding", "UTF8"))
    createdb()

def startdb():
    subp.check_call(pg_ctl + ("start",))

def stopdb():
    subp.check_call(pg_ctl + ("stop",))

def createdb():
    subp.check_call(("createdb", "--host", "localhost", "--port", "5488", "--username", "postgres", "devlondonriots"))

commands = {"initdb": initdb,
            "startdb": startdb,
            "stopdb": stopdb,
            "createdb": createdb,
            }

def main():
    global log

    log = logging.getLogger(__name__)

    cmd = sys.argv[2]
    commands[cmd]()
