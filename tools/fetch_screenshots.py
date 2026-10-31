"""Fetch the screenshots a scale holds and save them as PNG under given names.

Take the pictures on the scale first: two fingers on a free spot of the
display for a second, until it blinks dark. The scale keeps up to six, oldest
first, until it restarts. Its web interface needs the section Maintenance
switched on (Settings > System > Web interface).

    python -I tools/fetch_screenshots.py 192.168.10.104 docs/assets/images/de main-create create-sources ...

The names are given in the order the pictures were taken. With fewer names
than pictures, the newest ones are taken; with more, the script stops before
saving anything. Nothing is deleted on the scale.
"""

import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image


def get(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return r.read()


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    host, out, names = argv[0], Path(argv[1]), argv[2:]
    shots = json.loads(get(f"http://{host}/api/screenshot/list")).get("shots", [])
    if len(names) > len(shots):
        print(f"{len(shots)} pictures on the scale, {len(names)} names given - nothing saved")
        return 1
    out.mkdir(parents=True, exist_ok=True)
    for shot, name in zip(shots[len(shots) - len(names):], names):
        bmp = get(f"http://{host}/api/screenshot.bmp?id={shot['id']}")
        img = Image.open(io.BytesIO(bmp)).convert("RGB")
        path = out / f"{name}.png"
        img.save(path, optimize=True)
        print(f"{shot['id']} -> {path} ({img.width}x{img.height}, {path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
