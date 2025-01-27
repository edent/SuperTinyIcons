from base64 import b64encode
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re


r_size = re.compile(
    rb'viewBox\s*=\s*"\s*([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s+([+-]?[0-9.]+)\s*"'
).search
r_label = re.compile(rb'aria-label="(?P<value>.*?)(?<!\\)(?:\\\\)*"', re.DOTALL).search
r_atlas = re.compile(r' xmlns="http://www\.w3\.org/2000/svg"|(role="img")').sub
r_reid = re.compile(r'id="([^"]+)"|href="#([^"]+)"|url\(#([^)]+)\)').sub


@dataclass(order=True, frozen=True, slots=True)
class Icon:
    name: str  #: filename without the extension
    size: int  #: file size in bytes
    label: str  #: the value of the aria-label, with fallback to `name` if not found
    dimension: (
        float | int
    )  #: the icon width/height (always the same as we are working with squares)
    path: Path | None = None
    data: bytes | None = None

    @classmethod
    def from_path(cls, path: Path, *, with_path=True, with_data=True):
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
            path if with_path else None,
            data if with_data else None,
        )

    @property
    def as_drawio(self) -> dict:
        return {
            "title": self.label,
            "data": f"data:image/svg+xml;base64,{b64encode(self.data).decode('ascii')}",
            "aspect": "fixed",
            "w": self.dimension,
            "h": self.dimension
        }

    def as_atlas_unit(self, reid=False) -> str:
        data = self.data.decode("utf8").replace("\n", " ")
        def _reid(match):
            id_, href, url = match.groups()
            if id_:
                return f'id="{reid}{id_}"'
            if href:
                return f'href="#{reid}{href}"'
            if url:
                return f'url(#{reid}{url})'
        if reid is not False:
            data = r_reid(
                _reid,
                data
            )
        return r_atlas(
            lambda _: f'id="{self.name}"' if _.group(1) else "",
            data,
            2
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
        "icons": {k: icons[k] for k in sorted(icons)},  # dict are sorted since Python 3.7
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



