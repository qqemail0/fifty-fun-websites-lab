from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(r"window\.PORTAL_DATA = (.*?);\s*</script>", index, re.S)
    assert_true(bool(match), "portal data missing")
    data = json.loads(re.sub(r'([,{]\s*)([A-Za-z][A-Za-z0-9_]*)\s*:', r'\1"\2":', match.group(1)))
    links = data.get("links", [])
    assert_true(len(links) >= 10, "previous website links missing")
    assert_true("sites" not in data, "50-site dataset should be removed")
    assert_true(not (ROOT / "sites").exists(), "sites directory should be deleted")
    assert_true(not (ROOT / "assets" / "site.js").exists(), "site runtime should be deleted")
    assert_true(not (ROOT / "scripts" / "build_sites.py").exists(), "50-site generator should be deleted")
    for phrase in ["作品导航", "之前做过的网站", "项目目录", "访问网站", "查看源码"]:
        assert_true(phrase in index or phrase in (ROOT / "assets" / "home.js").read_text(encoding="utf-8"), f"missing phrase: {phrase}")
    for item in links:
        for key in ["title", "category", "description", "url", "repo"]:
            assert_true(item.get(key), f"missing {key} in link")
    for required in ["README.md", "docs/SITE_MAP.md", "assets/home.js", "assets/style.css", ".github/workflows/pages.yml"]:
        assert_true((ROOT / required).exists(), f"missing {required}")
    forbidden = [
        "C:" + "\\Users",
        "M:" + "\\",
        "Users" + "/mo",
        "test" + "chatcpt",
        "public" + "-apis" + "-master",
    ]
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix.lower() not in {".html", ".css", ".js", ".md", ".py", ".yml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for marker in forbidden:
            assert_true(marker not in text, f"{marker} leaked in {path}")
    print("OK: archive-only website navigation verified; 50 generated sites are removed.")


if __name__ == "__main__":
    main()
