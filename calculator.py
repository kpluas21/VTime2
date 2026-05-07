from datetime import date, timedelta
import platform


def _day(d: date) -> str:
    """Return day-of-month without a leading zero, cross-platform."""
    fmt = "%#d" if platform.system() == "Windows" else "%-d"
    return d.strftime(fmt)


def _fmt_date(d: date) -> str:
    return f"{d.strftime('%B')} {_day(d)}, {d.strftime('%Y')}"


def add_days(start_date: date, num_days: int) -> date:
    """Return the date that is num_days before or after start_date.

    Raises ValueError if the result would fall outside the supported date range.
    """
    try:
        return start_date + timedelta(days=num_days)
    except OverflowError:
        raise ValueError(
            f"The result date is out of range for {num_days:+} days from {start_date}."
        )


def days_breakdown(num_days: int) -> dict:
    """Break an integer number of days into weeks and remaining days.

    Returns a dict with keys: total, weeks, remaining_days, direction.
    direction is 'forward', 'backward', or 'none'.
    """
    if num_days == 0:
        return {"total": 0, "weeks": 0, "remaining_days": 0, "direction": "none"}
    abs_days = abs(num_days)
    weeks, remaining = divmod(abs_days, 7)
    return {
        "total": abs_days,
        "weeks": weeks,
        "remaining_days": remaining,
        "direction": "forward" if num_days > 0 else "backward",
    }


def format_result(start_date: date, num_days: int, result: date) -> str:
    """Return a human-readable summary of the date calculation."""
    if num_days == 0:
        return f"{_fmt_date(start_date)} - no days added or subtracted."

    bd = days_breakdown(num_days)
    direction = "from" if num_days > 0 else "before"
    abs_days, weeks, remaining = bd["total"], bd["weeks"], bd["remaining_days"]

    start_str = _fmt_date(start_date)
    result_str = _fmt_date(result)
    weekday = result.strftime("%A")

    lines = [
        f"{abs_days} day{'s' if abs_days != 1 else ''} {direction} {start_str} is {result_str} ({weekday}).",
    ]

    if weeks and remaining:
        lines.append(f"That's {weeks} week{'s' if weeks != 1 else ''} and {remaining} day{'s' if remaining != 1 else ''} {direction} your start date.")
    elif weeks:
        lines.append(f"That's exactly {weeks} week{'s' if weeks != 1 else ''} {direction} your start date.")
    else:
        lines.append(f"That's {remaining} day{'s' if remaining != 1 else ''} {direction} your start date.")

    if result.weekday() >= 5:
        lines.append(f"Note: {result.strftime('%B')} {_day(result)} falls on a weekend.")

    return "\n".join(lines)
