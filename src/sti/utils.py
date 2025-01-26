from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass
import re


r_size = re.compile(
    rb'viewBox\s*=\s*"\s*([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s*"'
).search
r_label = re.compile(rb'aria-label="(?P<value>.*?)(?<!\\)(?:\\\\)*"', re.DOTALL).search


@dataclass(order=True, frozen=True, slots=True)
class Icon:
    name: str  #: filename without the extension
    size: int  #: file size in bytes
    label: str  #: the value of the aria-label, with fallback to `name` if not found
    dimension: (
        float | int
    )  #: the icon width/height (always the same as we are working with squares)
    path: Path | None = None

    @classmethod
    def from_path(cls, path: Path):
        data = path.read_bytes()
        width = 0
        height = 0
        if match := r_size(data):
            x0, y0, x1, y1 = match.groups()
            width = float(x1) - float(x0)
            height = float(y1) - float(y0)
        if width != height or width <= 0:
            raise ValueError(f"invalid size for: {path} ({width} / {height})")
        return cls(
            path.name.rpartition(".")[0],
            path.stat().st_size,
            match.group(1).decode("utf8")
            if (match := r_label(data))
            else path.name.rpartition(".")[0],
            int(width) if width.is_integer() else width,
            path,
        )


def get_icons_from(path: Path) -> dict:
    icons = {}
    size_min = float("inf")
    size_max = 0
    size_tot = 0
    for entry in path.glob("*.svg"):
        icon = Icon.from_path(entry)
        icons[icon.name] = icon
        if icon.size < size_min:
            size_min = icon.size
        if icon.size > size_max:
            size_max = icon.size
        size_tot += icon.size
    return {
        "size_min": size_min,
        "size_max": size_max,
        "size_avg": size_tot / len(icons) if icons else 0,
        "size_tot": size_tot,
        "icons": icons,
    }


def get_refs_from(path: Path) -> dict:
    refs = defaultdict(dict)
    for entry in path.glob("*.*"):
        if entry.suffix == ".url":
            refs[entry.name[:-4]]["url"] = entry.read_text(encoding="utf8")
        else:
            refs[entry.name.rpartition(".")[0]] |= {
                "filename": entry.name,
                "size": entry.stat().st_size,
            }
    return dict(refs)
