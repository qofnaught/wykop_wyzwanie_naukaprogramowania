from argparse import ArgumentParser
from collections import namedtuple
from glob import glob
from os.path import getsize, isfile
import sys

from sqlalchemy import Table, Column, Integer, String, \
        create_engine, MetaData
from sqlalchemy.sql import select


AccumulatedSize = namedtuple('AccumulatedSize', 'extension size files')


def get_files(directory):
    yield from (f for f in glob("{}/**".format(directory), recursive=True) if isfile(f))


def get_files_info(directory):
    yield from ((extract_extension(f), getsize(f)) for f in get_files(directory))


def extract_extension(filename):
    return filename.split('.')[-1]


def accumulate_size_by_extension(files):
    d = {}
    for (ext, size) in files:
        acc = d.get(ext, AccumulatedSize(ext, 0, 0))
        d[ext] = AccumulatedSize(acc.extension, acc.size + size, acc.files + 1)
    yield from d.values()


def render_row(extension, size, histogram):
    return '{extension:>5}{size:>14}B{histogram:>60}\n'.format(**locals())


def get_his(value, total):
    return '#' * round(50 * value / total)


def main(directory):
    total_files, extensions = 0, set()
    for accumulated in accumulate_size_by_extension(get_files_info(directory)):
        total_files += accumulated.files
        extensions |= {accumulated}

    for (ext, size, files) in sorted(extensions, key=lambda acc: acc.files, reverse=True):
        yield render_row(ext, size, get_his(files, total_files))


def test_answer(operating_dir, output_file):
    rows = [r.strip() for r in main(operating_dir)]
    with open(output_file, 'r') as inp:
        to_be_tested = [r.strip() for r in inp.readlines()]

    if len(rows) != len(to_be_tested):
        print('Row count doesn\'t match.\n'
              'Expected: {}, got: {}.'.format(len(rows), len(to_be_tested)))
        return False

    rows, to_be_tested = sorted(rows), sorted(to_be_tested)

    for (expected, got) in zip(rows, to_be_tested):
        if expected != got:
            print('Invalid extension data.\n'
                  '<"{}"\n'
                  '>"{}"'.format(expected, got))
            return False

    return True


def load_tables(meta, engine, *names):
    tables = []
    for name in names:
        table = None
        try:
            table = Table(name, meta, autoload=True, autoload_with=engine)
        except sqlalchemy.ext.NoSuchTableError:
            print('Cannot read {} table from db.'.format(name))
            raise
        tables.append(table)
    return tables


def check_objects_table(rows):
    pass


def test_db(operating_dir, db_path):
    engine = create_engine('sqlite:///{}'.format(db_path))
    meta = MetaData()
    objects, cardinality, checksums = load_tables(
        meta, engine, 'objects', 'cardinality', 'checksums')
    conn = engine.connect()
    s = select([objects])
    res = engine.execute(s)
    check_objects_table(res)
    return True


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('operating_dir', metavar='operating_dir', type=str)
    parser.add_argument('output_file', metavar='output_file', type=str)
    parser.add_argument('version', default='easy', type=str)
    args = parser.parse_args()

    if args.version == 'easy':
        result = test_answer(args.operating_dir, args.output_file)
    elif args.version == 'hard':
        result = test_db(args.operating_dir, args.output_file)
    else:
        print('Invalid option value: only "easy" (default)/"hard" '
              'version allowed.''', file=sys.stderr)
        sys.exit(1)

    if result:
        print('All checks OK.')
    else:
        print('Errors found.')
