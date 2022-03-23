from datetime import datetime, timezone



def now_utc():
    """Return a UTC-aware datetime object."""

    return datetime.now(timezone.utc)





