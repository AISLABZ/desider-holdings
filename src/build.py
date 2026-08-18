#!/usr/bin/env python3
"""Build the Desider Holdings programme dashboard.

Usage: python3 src/build.py   (from the repo root, or from src/)
Injects data.json into template.html between the /*__DATA__*/ markers.
To update after a meeting: edit data.json (or replace it with an exported
state file), bump meta.version, append to meta log, then re-run this.
"""
import json, sys, re, pathlib

base = pathlib.Path(__file__).parent
data_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else base / "data.json"
out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else base.parent / "index.html"

data = json.loads(data_path.read_text(encoding="utf-8"))
tpl = (base / "template.html").read_text(encoding="utf-8")

payload = json.dumps(data, indent=2, ensure_ascii=False).replace("</", "<\\/")
out = re.sub(
    r"/\*__DATA__\*/.*?/\*__ENDDATA__\*/",
    lambda _: "/*__DATA__*/" + payload + "/*__ENDDATA__*/",
    tpl,
    flags=re.S,
)
assert "/*__DATA__*/null" not in out, "data injection failed"
out_path.write_text(out, encoding="utf-8")
print(f"wrote {out_path} ({len(out):,} bytes) — {len(data['workPackages'])} work packages, "
      f"{sum(len(w['tasks']) for w in data['workPackages'])} sub-tasks")
