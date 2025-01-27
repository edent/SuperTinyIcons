# stdlib
from io import BytesIO
from zlib import crc32
from pathlib import Path
from base64 import b64encode

# dependencies
from flask import Flask, Response, render_template, send_file

# local
from .utils import get_icons_from, get_refs_from

git_root = Path(__file__).absolute().parents[2]
app = Flask(
    __name__,
    static_folder=git_root / "images",
)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

svg_lib = {
    "refs": get_refs_from(git_root / "images/reference"),
}
svg_lib |= get_icons_from(git_root / "images/svg")

with Path(__file__).absolute().with_name("templates").joinpath("favicon.ico").open(mode="rb") as file:
    FAVICON = file.read()
    FAVETAG = f"{crc32(FAVICON):x}"

@app.template_filter()
def b2s(b: bytes) -> str:
    return b.decode("utf8")

@app.route("/favicon.ico")
def favicon():
    return send_file(BytesIO(FAVICON), mimetype='image/x-icon', etag=FAVETAG)

@app.route("/atlas.svg")
def svglib():
    return Response(
        render_template(
            "atlas.svg", library=svg_lib["icons"].values()
    ),
        mimetype="image/svg+xml",
    )

@app.route("/mxlibrary.xml")
def mxlibrary():
    return Response(
        render_template(
            "mxlibrary.xml", library=svg_lib["icons"].values()
        ),
        mimetype="application/xml",
    )

@app.route("/", defaults={"path": "index"})
@app.route("/<string:path>.html")
@app.route("/<string:path>")
def render(path):
    return render_template(f"{path}.html", pagename=path, **svg_lib)
