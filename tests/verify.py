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
    match = re.search(r"window\.PORTAL_DATA = (.*?);</script>", index)
    assert_true(bool(match), "portal data missing")
    data = json.loads(match.group(1))
    sites = data["sites"]
    assert_true(len(sites) == 50, "site count must be 50")
    assert_true(len({site["kind"] for site in sites}) >= 38, "not enough distinct tool types")
    assert_true(len({site["skin"] for site in sites}) >= 18, "not enough visual skins")
    assert_true(len(data["previousLinks"]) >= 10, "previous links missing")
    for site in sites:
        path = ROOT / "sites" / site["slug"] / "index.html"
        assert_true(path.exists(), f"missing site page: {site['slug']}")
        text = path.read_text(encoding="utf-8")
        assert_true("repo-orb" in text and "source-footer-link" in text, f"source badge missing: {site['slug']}")
        assert_true(f'data-kind="{site["kind"]}"' in text, f"kind missing: {site['slug']}")
        assert_true(f'skin-{site["skin"]}' in text, f"skin missing: {site['slug']}")
    for required in ["assets/style.css", "assets/site.js", "assets/home.js", ".github/workflows/pages.yml", "README.md", "docs/SITE_MAP.md"]:
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
    print("OK: rebuilt 50 sites with distinct tool types, visual skins, archive links, source badges, and path hygiene.")


if __name__ == "__main__":
    main()
