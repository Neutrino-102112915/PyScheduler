import time
from datetime import datetime, timedelta

_task_list = []

class Schedule:
    def _next_weekday_time(self, weekday, hour, minute):
        now = datetime.now()
        today_weekday = now.weekday()  # Monday=0 ... Sunday=6
        target_time_today = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        days_ahead = (weekday - today_weekday + 7) % 7
        if days_ahead == 0 and now >= target_time_today:
            days_ahead = 7

        next_run_date = now + timedelta(days=days_ahead)
        return next_run_date.replace(hour=hour, minute=minute, second=0, microsecond=0)

    def at(self, YYYY, MM, DD, HH, M):
        def decorator(func):
            _task_list.append((datetime(YYYY, MM, DD, HH, M), id(func), func, None))
            return func
        return decorator

    def every(self, seconds):
        def decorator(func):
            next_time = datetime.now() + timedelta(seconds=seconds)
            _task_list.append((next_time, id(func), func, seconds))
            return func
        return decorator

    def weekday(self, day_name, at="00:00"):
        day_map = {
            "monday": 0, "tuesday": 1, "wednesday": 2,
            "thursday": 3, "friday": 4, "saturday": 5,
            "sunday": 6
        }
        weekday_num = day_map[day_name.lower()]
        hour, minute = map(int, at.split(":"))

        def decorator(func):
            next_time = self._next_weekday_time(weekday_num, hour, minute)
            _task_list.append((next_time, id(func), func, ("weekly", weekday_num, hour, minute)))
            return func
        return decorator

    def run(self):
        tasks = _task_list.copy()
        tasks.sort(key=lambda x: x[0])

        while tasks:
            now = datetime.now()
            task_time, task_id, task_func, repeat = tasks[0]

            if now >= task_time:
                tasks.pop(0)
                try:
                    task_func()
                except Exception as e:
                    print(f"Error running task {task_id}: {e}")

                # Reschedule if repeating
                if isinstance(repeat, int):
                    next_time = task_time + timedelta(seconds=repeat)
                    tasks.append((next_time, task_id, task_func, repeat))

                elif isinstance(repeat, tuple) and repeat[0] == "weekly":
                    _, weekday_num, hour, minute = repeat
                    next_time = self._next_weekday_time(weekday_num, hour, minute)
                    tasks.append((next_time, task_id, task_func, repeat))

                tasks.sort(key=lambda x: x[0])
            else:
                sleep_time = (task_time - now).total_seconds()
                if sleep_time > 0:
                    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sleeping for {sleep_time:.2f} seconds until next task at {task_time}")
                    time.sleep(sleep_time)
