from londonriots.scripts import environment
import sys

def main():
    with environment(sys.argv) as env:
        print env
