"""Super Tiny Icons command line interface"""

# stdlib
from argparse import ArgumentParser
from pathlib import Path
from os.path import commonprefix
import logging
import sys

# dependencies
from jinja2 import Environment, FileSystemLoader

# local
from .utils import get_icons_from, get_refs_from


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
        "-o",
        "--output",
        default="_site",
        help="output directory",
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
    current_dir = Path(__file__).absolute().parent
    git_root = current_dir.parents[1]
    svg_lib = {"refs": get_refs_from(git_root / "images/reference")} | get_icons_from(
        git_root / "images/svg"
    )
    tpl_loader = FileSystemLoader(current_dir / "templates")
    tpl_env = Environment(loader=tpl_loader)

    out = Path(args.output).resolve()
    if git_root in out.parents and not out.exists():
        out.mkdir(parents=True)

    for template_name in ("index", "list", "reference"):
        template = tpl_env.get_template(name=f"{template_name}.html")
        with (Path(args.output) / f"{template_name}.html").open(
                "w", encoding="utf8"
            ) as out:
            out.write(template.render(pagename=template_name, **svg_lib))
