from datetime import date
import pytest
from calculator import add_days, days_breakdown, format_result


class TestDaysBreakdown:
    def test_zero(self):
        r = days_breakdown(0)
        assert r == {"total": 0, "weeks": 0, "remaining_days": 0, "direction": "none"}

    def test_positive_exact_weeks(self):
        r = days_breakdown(14)
        assert r["weeks"] == 2 and r["remaining_days"] == 0 and r["direction"] == "forward"

    def test_positive_mixed(self):
        r = days_breakdown(30)
        assert r["weeks"] == 4 and r["remaining_days"] == 2 and r["total"] == 30

    def test_negative(self):
        r = days_breakdown(-10)
        assert r["direction"] == "backward" and r["weeks"] == 1 and r["remaining_days"] == 3

    def test_single_day(self):
        r = days_breakdown(1)
        assert r["weeks"] == 0 and r["remaining_days"] == 1 and r["direction"] == "forward"


class TestAddDays:
    def test_positive_days(self):
        assert add_days(date(2026, 5, 7), 30) == date(2026, 6, 6)

    def test_negative_days(self):
        assert add_days(date(2026, 5, 7), -7) == date(2026, 4, 30)

    def test_zero_days(self):
        assert add_days(date(2026, 5, 7), 0) == date(2026, 5, 7)

    def test_leap_year(self):
        assert add_days(date(2024, 2, 28), 1) == date(2024, 2, 29)

    def test_end_of_year(self):
        assert add_days(date(2026, 12, 31), 1) == date(2027, 1, 1)

    def test_large_number(self):
        result = add_days(date(2026, 5, 7), 99999)
        assert isinstance(result, date)

    def test_overflow_raises(self):
        with pytest.raises(ValueError):
            add_days(date(9999, 12, 31), 1)


class TestFormatResult:
    def test_zero_days(self):
        d = date(2026, 5, 7)
        assert "no days added" in format_result(d, 0, d)

    def test_positive_summary(self):
        out = format_result(date(2026, 5, 7), 30, date(2026, 6, 6))
        assert "June 6, 2026" in out
        assert "Saturday" in out

    def test_negative_summary(self):
        out = format_result(date(2026, 5, 7), -7, date(2026, 4, 30))
        assert "before" in out

    def test_weekend_warning(self):
        out = format_result(date(2026, 5, 7), 30, date(2026, 6, 6))
        assert "weekend" in out

    def test_weekday_no_warning(self):
        # May 11, 2026 is a Monday
        out = format_result(date(2026, 5, 7), 4, date(2026, 5, 11))
        assert "weekend" not in out

    def test_exact_weeks(self):
        out = format_result(date(2026, 5, 7), 14, date(2026, 5, 21))
        assert "2 weeks" in out
