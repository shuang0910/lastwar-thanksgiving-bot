
import re
import subprocess
from typing import Optional


def parse_ingredient_limit(text: str) -> Optional[bool]:
    """
    Convert OCR text into a collection-limit status.

    True:  Ingredient limit reached
    False: Ingredients can still be collected
    None:  Cannot determine the status
    """

    matches = []

    for line in text.splitlines():
        match = re.fullmatch(
            r"\s*(\d+)\s*/\s*(\d+)\s*",
            line
        )

        if not match:
            continue

        collected = int(match.group(1))
        limit = int(match.group(2))

        # The daily allowance starts at 300.
        # Ignore unrelated counters, such as 7/15.
        if limit < 300:
            continue

        if collected > limit:
            return None

        matches.append((collected, limit))

    if len(matches) != 1:
        return None

    collected, limit = matches[0]
    return collected >= limit


def read_ingredient_limit(image_path: str) -> Optional[bool]:
    """
    Read Thanksgiving ingredients from a screenshot.
    """

    try:
        result = subprocess.run(
            [
                "tesseract",
                image_path,
                "stdout",
                "-l", "eng",
                "--psm", "11",
                "-c",
                "tessedit_char_whitelist=0123456789/",
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=15,
        )
    except (
        OSError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
    ):
        return None

    return parse_ingredient_limit(result.stdout)
