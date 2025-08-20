# PySchedular

PySchedular is a Python library for schedularling.

## Usage

```python
import PyScheduler

schedule = schedule()

@schedule.at(2025, 8, 21, 12, 30)
def hello_world():
  print("Hello World!")

# or
schedule.at(2025, 8, 21, 12, 30)(hello_world)

@schedule.every(10) # every 10 seconds
def hello_world():
  print("Hello World!")

# or
schedule.every(10)(hello_world)

@schedule.weekday("monday", "12:30")
def hello_world():
  print("Hello World!")

# or
schedule.weekday("monday", "12:30")(hello_world)

schedule.run()
```
