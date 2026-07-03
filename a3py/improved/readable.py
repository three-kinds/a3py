# -*- coding: utf-8 -*-


def get_readable_size(size: float, round_number: int = 2) -> str:
    """
    Usage::
        >>> get_readable_size(0)
        '0B'
        >>> get_readable_size(1000)
        '1000B'
        >>> get_readable_size(1024)
        '1.0KB'
        >>> get_readable_size(2000)
        '1.95KB'
        >>> get_readable_size(1024 * 1024)
        '1.0MB'
        >>> get_readable_size(int(1024 * 1024 * 1.94))
        '1.94MB'
        >>> get_readable_size(1024 * 1024 * 1024 * 3)
        '3.0GB'
        >>> get_readable_size(1024 * 1024 * 1024 * 1024 * 4)
        '4.0TB'
        >>> get_readable_size(1024 * 1024 * 1024 * 1024 * 1024 * 5)
        '5.0PB'
        >>> get_readable_size(1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 10)
        '10240.0PB'
    """
    unit_list = ["B", "KB", "MB", "GB", "TB", "PB"]
    index = 0

    while size >= 1024 and index < len(unit_list) - 1:
        size /= 1024
        index += 1

    return f"{round(size, round_number)}{unit_list[index]}"


def get_readable_duration(seconds: float, round_number: int = 2) -> str:
    """
    Usage::
        >>> get_readable_duration(0)
        '0s'
        >>> get_readable_duration(1)
        '1s'
        >>> get_readable_duration(60)
        '1.0m'
        >>> get_readable_duration(3600)
        '1.0h'
        >>> get_readable_duration(86400)
        '1.0d'
    """
    unit_info_list = [("s", 60), ("m", 60), ("h", 24), ("d", 0)]
    duration = seconds
    index = 0
    while True:
        unit, threshold = unit_info_list[index]
        if duration < threshold or threshold == 0:
            return f"{round(duration, round_number)}{unit}"
        else:
            duration /= threshold
            index += 1
