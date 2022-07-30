"""
Author:     David Walshe
Date:       30 July 2022
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, List

import requests

SOCIAL_DIR = Path(__file__).parent.parent / "hosts" / "social"

# Taken from https://raw.githubusercontent.com/StevenBlack/hosts/master/extensions/social/sinfonietta/hosts
SOCIAL_MEDIA_NAMES = [
    "# Google Plus",
    "# Facebook",
    "# Instagram",
    "# Whatsapp",
    "# Twitter",
    "# LinkedIn",
    "# MySpace",
    "# Pinterest",
    "# Tumblr",
    "# Reddit",
    "# TikTok",
    "# DateMeme",
    "# clubhouse",
    "# Dating sites",
]


def get_social_media_hosts() -> str:
    """
    Get the hosts from the hosts file.

    :return: List of hosts.
    """
    data = requests.get("https://raw.githubusercontent.com/StevenBlack/hosts/master/extensions/social/sinfonietta/hosts").text

    return data.split(SOCIAL_MEDIA_NAMES[0])[1]


def divide_content_based_on_provider() -> Dict[str, List[str]]:
    """
    Divide the content based on the provider.

    :return: The divided content.
    """
    items = {}
    data = get_social_media_hosts()
    for idx, name in enumerate(SOCIAL_MEDIA_NAMES[1:]):
        items[SOCIAL_MEDIA_NAMES[idx]], data = data.split(name)

    items[SOCIAL_MEDIA_NAMES[-1]] = data

    return items


def display_raw_links(names: List[str]):
    """
    Displays all the raw github links for the content.

    :param names: The names of the content.
    """
    for name in names:
        print(f"https://raw.githubusercontent.com/DavidWalshe93/hosts/main/hosts/social/{name}".replace(" ", ""), end=" ")

    print()


def write_out_divided_content(items: Dict[str, List[str]]) -> None:
    """
    Write out the divided content.

    :param items: The divided content.
    :return: None.
    """
    link_names = []
    for name, host_text in items.items():
        hosts = host_text.split("\n")
        hosts = [host.strip() for host in hosts if host.startswith("#") is False]
        hosts = [host.replace("127.0.0.1", "0.0.0.0") for host in hosts if host != ""]

        name = name.replace("# ", "")
        file_name = name.replace(" ", "_").lower()
        link_names.append(file_name)
        with open(SOCIAL_DIR / f"{file_name}", "w") as f:
            f.write(f"# Target: {name.capitalize()}\n")
            f.write(f"# Date:   {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("\n")
            f.write("\n".join(hosts))

    display_raw_links(link_names)


if __name__ == '__main__':
    data = divide_content_based_on_provider()
    write_out_divided_content(data)
