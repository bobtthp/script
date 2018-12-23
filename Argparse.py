import argparse
args = argparse.ArgumentParser()
args.add_argument('--test',help="test bobtthp",action="count")
arg = args.parse_args()
print arg.test
