#!/usr/bin/env python3
"""Super Tiny Icons Atlas generator"""
# stdlib
from argparse import ArgumentParser
from base64 import b64encode
from pathlib import Path
import json
import logging
import sys

# dependencies
from jinja2 import Environment, FileSystemLoader

# local
from .utils import Icon

current_dir = Path(__file__).absolute().parent
tpl = Environment(loader=FileSystemLoader(current_dir / "templates"))

class Atlas:
    lib: list[Icon] = None

    def __init__(self):
        self.lib = []

    def add(self, path: Path):
        self.lib.append(Icon.from_path(path, with_path=False, with_data=True))
        return self

    def write_drawio(self, fp):
        fp.write("<mxlibrary>")
        json.dump([
            {
                "title": entry.label,
                "data": f"data:image/svg+xml;base64,{b64encode(entry.data).decode('ascii')}",
                "aspect": "fixed",
                "w": entry.dimension,
                "h": entry.dimension,
            } for entry in self.lib
        ], fp, indent=1, sort_keys=True)
        fp.write("</mxlibrary>")

    def write_svg(self, fp):
        template = tpl.get_template(name="atlas.svg")
        fp.write(template.render(library=self.lib))

def parse_args():
    """parse arguments, initialize logging"""
    parser = ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_const",
        const=0,
        default=2,
        dest="verbose",
    )
    parser.add_argument("-v", "--verbose", action="count")

    group = parser.add_argument_group("Configuration")
    group.add_argument(
        "-f",
        "--format",
        choices=["drawio", "svg"],
        default=None,
        required=True,
    )
    args = parser.parse_args()
    loglevel = min(
        max(logging.CRITICAL - (args.verbose * 10), logging.DEBUG), logging.CRITICAL
    )
    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        level=loglevel,
        stream=sys.stderr,
    )
    return args

def main():
    args = parse_args()
    atlas = Atlas()
    for entry in Path(__file__).parents[1].with_name("images").glob("svg/*.svg"):
        atlas.add(entry)
    if args.format == "drawio":
        atlas.write_drawio(sys.stdout)
    if args.format == "svg":
        atlas.write_svg(sys.stdout)

if __name__ == "__main__":
    main()
