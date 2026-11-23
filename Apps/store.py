"""PyOs Store: install terminal applications from their official GitHub archives.

Run from any working directory: python Apps/store.py
"""
from pathlib import Path
import io
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent.parent
CATALOG = {
    "cookie": {
        "name": "Cookie",
        "description": "Terminal cookie-clicking game",
        "repo": "Xylin48/cookie",
        "branch": "main",
        "target": ROOT / "Home" / "Games" / "Cookie",
        "required": ("cookie.py", "guide.py", "news.py"),
    },
    "social": {
        "name": "Social",
        "description": "Connected terminal social network",
        "repo": "Xylin48/Social",
        "branch": "dev/social-network-overhaul",
        "target": ROOT / "Home" / "Social",
        "required": ("main.py", "api.py", "server.py", "accounts.py", "book.py", "shelf.py", "posts.py"),
    },
}
MAX_ARCHIVE_BYTES = 25 * 1024 * 1024
MAX_EXTRACTED_BYTES = 60 * 1024 * 1024


def archive_bytes(repo, branch):
    url = "https://github.com/{}/archive/refs/heads/{}.zip".format(repo, branch)
    request = urllib.request.Request(url, headers={"User-Agent": "PyOs-Store/1.0"})
    with urllib.request.urlopen(request, timeout=35) as response:
        data = response.read(MAX_ARCHIVE_BYTES + 1)
    if len(data) > MAX_ARCHIVE_BYTES:
        raise ValueError("Download exceeds the Store size limit.")
    return data


def unpack_archive(data, destination):
    """Extract ordinary files only; reject traversal, symlinks and oversized archives."""
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        files = archive.infolist()
        total = 0
        for entry in files:
            parts = Path(entry.filename).parts
            if len(parts) < 2 or any(part in ("", ".", "..") for part in parts):
                raise ValueError("Invalid archive path.")
            if entry.filename.startswith("/") or "\\" in entry.filename:
                raise ValueError("Unsafe archive path.")
            if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Archive contains a symbolic link.")
            total += entry.file_size
            if total > MAX_EXTRACTED_BYTES:
                raise ValueError("Archive exceeds the extracted size limit.")
        for entry in files:
            if entry.is_dir():
                continue
            relative = Path(*Path(entry.filename).parts[1:])
            if not relative.parts:
                continue
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(entry) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output)


SOCIAL_LAUNCHER = '''"""PyOs compatibility entry point for installed Social."""
from pathlib import Path
import os
import subprocess
import sys

if __name__ == "__main__":
    folder = Path(__file__).resolve().parent / "Social"
    entry = folder / "main.py"
    if not entry.is_file():
        print("Social is not installed. Open the PyOs Store to install it.")
        raise SystemExit(1)
    raise SystemExit(subprocess.call([sys.executable, str(entry)], cwd=str(folder)))
'''


def install(key, downloader=archive_bytes):
    app = CATALOG[key]
    target = app["target"]
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pyos-store-") as temp:
        staging = Path(temp) / "staging"
        staging.mkdir()
        unpack_archive(downloader(app["repo"], app["branch"]), staging)
        missing = [name for name in app["required"] if not (staging / name).is_file()]
        if missing:
            raise ValueError("Download is missing required files: " + ", ".join(missing))
        backup = target.with_name(target.name + ".pyos-backup")
        if backup.exists():
            raise ValueError("An earlier install backup exists; inspect it before retrying.")
        if target.exists():
            if not target.is_dir():
                raise ValueError("Install destination is not a directory.")
            target.rename(backup)
        try:
            shutil.move(str(staging), str(target))
            if key == "social":
                launcher = ROOT / "Home" / "social.py"
                launcher.write_text(SOCIAL_LAUNCHER, encoding="utf-8")
            if backup.exists():
                shutil.rmtree(backup)
        except Exception:
            if target.exists():
                shutil.rmtree(target)
            if backup.exists():
                backup.rename(target)
            raise
    return target


def menu():
    while True:
        print("\n" + "═" * 48)
        print(" PYOS  /  STORE")
        print("═" * 48)
        for index, key in enumerate(CATALOG, 1):
            app = CATALOG[key]
            installed = "Installed" if app["target"].is_dir() else "Available"
            print(" [{}] {:<12} {:<12} {}".format(index, app["name"], installed, app["description"]))
        print(" [0] Back")
        choice = input("\nstore>>> ").strip().lower()
        if choice in ("0", "back", "quit", "exit"):
            return
        key = {"1": "cookie", "2": "social"}.get(choice, choice)
        if key not in CATALOG:
            print("Choose an application number, or 0 to return.")
            continue
        app = CATALOG[key]
        if app["target"].exists():
            answer = input("{} is installed. Update/reinstall? [y/N] ".format(app["name"])).strip().lower()
            if answer not in ("y", "yes"):
                continue
        try:
            print("Downloading {}...".format(app["name"]))
            destination = install(key)
            print("Installed {} in {}".format(app["name"], destination.relative_to(ROOT)))
            if key == "social":
                print("Launch with: python Home/social.py")
            else:
                print("Launch with: python Home/Games/Cookie/cookie.py")
        except (OSError, ValueError, urllib.error.URLError, zipfile.BadZipFile) as exc:
            print("Installation failed: {}".format(exc))


if __name__ == "__main__":
    menu()
