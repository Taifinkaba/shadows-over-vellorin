"""Read-only inventory of ordinary unittest discovery; no test filtering."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
import unittest


def inventory(root):
    sys.path.insert(0,str(root))
    suite=unittest.defaultTestLoader.discover(str(root/'tests'))
    def flatten(group):
        for case in group:
            if isinstance(case,unittest.TestSuite):yield from flatten(case)
            else:yield case
    cases=list(flatten(suite))
    return dict(discovered_tests=len(cases),by_file=dict(sorted(Counter(c.__class__.__module__ for c in cases).items())),
                by_class=dict(sorted(Counter(c.__class__.__module__+'.'+c.__class__.__name__ for c in cases).items())),
                test_ids=sorted(c.id() for c in cases))


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check-range',action='store_true');args=parser.parse_args();result=inventory(args.root.resolve())
    print(json.dumps(result,indent=2))
    if args.check_range and not 180<=result['discovered_tests']<=220:parser.exit(1,'Expected180–220 ordinarily discovered tests\n')


if __name__=='__main__':main()
