"""
Copyright 2021 VincentRPS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import argparse
import platform
import sys
from pathlib import Path

import aiohttp
import pkg_resources

# heavily based upon discord.py.
import expo


def show_version():
    entries = []

    entries.append(
        "- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}".format(
            sys.version_info
        )
    )
    version_info = expo.version_info
    entries.append(
        "- hikari-expo v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}".format(
            version_info
        )
    )
    if version_info.releaselevel != "final":
        pkg = pkg_resources.get_distribution("hikari-expo")
        if pkg:
            entries.append(f"    - hikari-expo pkg_resources: v{pkg.version}")

    entries.append(f"- aiohttp v{aiohttp.__version__}")
    uname = platform.uname()
    entries.append("- system info: {0.system} {0.release} {0.version}".format(uname))
    print("\n".join(entries))


def core(parser, args):
    if args.version:
        show_version()


# A basic hikari gateway bot.
gateway_bot = """import config
import hikari


bot = hikari.GatewayBot(token=config.token)

bot.run()
"""

gitignore = """__pycache__/
.idea/
.vscode/
.vs/
.mypy_cache/
.nox/
build/
dist/
"""

_base_table = {
    "<": "-",
    ">": "-",
    ":": "-",
    '"': "-",
    "|": "-",
    "?": "-",
    "*": "-",
}

_translation_table = str.maketrans(_base_table)


def to_path(parser, name, *, replace_spaces=False):
    if isinstance(name, Path):
        return name

    if sys.platform == "win32":
        forbidden = (
            "CON",
            "PRN",
            "AUX",
            "NUL",
            "COM1",
            "COM2",
            "COM3",
            "COM4",
            "COM5",
            "COM6",
            "COM7",
            "COM8",
            "COM9",
            "LPT1",
            "LPT2",
            "LPT3",
            "LPT4",
            "LPT5",
            "LPT6",
            "LPT7",
            "LPT8",
            "LPT9",
        )
        if len(name) <= 4 and name.upper() in forbidden:
            parser.error("invalid directory name given, use a different one")

    name = name.translate(_translation_table)
    if replace_spaces:
        name = name.replace(" ", "-")
    return Path(name)


def hk_bot(parser, args):
    new_directory = to_path(parser, args.directory) / to_path(parser, args.name)
    try:
        new_directory.mkdir(exist_ok=True, parents=True)
    except OSError as exc:
        parser.error(f"EXCEPTION: Could not create our bot directory ({exc})")

    try:
        with open(str(new_directory / "config.py"), "w", encoding="utf-8") as fp:
            fp.write('token = "my_bot_token"')
    except OSError as exc:
        parser.error(f"Could not create config file! ({exc})")

    try:
        with open(str(new_directory / "bot.py"), "w", encoding="utf-8") as fp:
            fp.write(gateway_bot)
    except OSError as exc:
        parser.error(f"could not create bot file ({exc})")

    if not args.no_git:
        try:
            with open(str(new_directory / ".gitignore"), "w", encoding="utf-8") as fp:
                fp.write(gitignore)
        except OSError as exc:
            print(f"WARNING: could not create .gitignore file ({exc})")

    print("Made a new bot in %s", new_directory)


def add_newbot_args(subparser):
    parser = subparser.add_parser(
        "new-bot", help="creates a command bot project quickly"
    )
    parser.set_defaults(func=hk_bot)

    parser.add_argument("name", help="the bot project name")
    parser.add_argument(
        "directory",
        help="the directory to place it in (default: .)",
        nargs="?",
        default=Path.cwd(),
    )
    parser.add_argument(
        "--no-git",
        help="do not create a .gitignore file",
        action="store_true",
        dest="no_git",
    )


def parse_args():
    parser = argparse.ArgumentParser(prog="hikari-expo", description="expo commands.")
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Shows the version of hikari-expo installed.",
    )
    parser.set_defaults(func=core)

    subparser = parser.add_subparsers(dest="subcommand", title="subcommands")
    add_newbot_args(subparser)
    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    args.func(parser, args)


if __name__ == "__main__":
    main()
