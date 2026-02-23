from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=5)

date1= datetime(2026, 2, 23, 10, 30, 0)
date2= datetime(2026, 2, 23, 16, 45, 30)

difference =date2-date1
seconds = difference.total_seconds()
print(future-now)

print(seconds)