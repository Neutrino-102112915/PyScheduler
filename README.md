# PySchedular

PySchedular is a Python library for schedularling.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyScheduler.

```bash
pip install git+https://github.com/Neutrino-102112915/PyScheduler.git
```

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
