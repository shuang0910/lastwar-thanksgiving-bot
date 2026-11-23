from typing import Optional


def can_join_rally(limit_reached: Optional[bool]) -> bool:
    """
    Check whether Thanksgiving rally joining is allowed.

    limit_reached:
        True  = Daily collection limit reached
        False = Collection limit not reached
        None  = Unable to determine status
    """

    if limit_reached is None:
        return False

    return not limit_reached