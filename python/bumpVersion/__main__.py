import bumpVersion
import argparse

parser = argparse.ArgumentParser(description="bump the value of a string assigned to a variable called version")
parser.add_argument('--file-loc', '-f', required=True)
parser.add_argument('--update-type', '-u', default='patch')
parser.add_argument('--dry_run', '-d', default=False)
parser.add_argument('--all_matching_lines', '-a', default=False)
parser.add_argument('--write_loc', '-w', default=None)
args = parser.parse_args()

bumpVersion(args.file_loc, which=args.update_type, dry_run = args.dry_run, all_matching_lines = args.all_matching_lines, write_loc = args.write_loc)