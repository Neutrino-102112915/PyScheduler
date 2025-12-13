import sys
from pyscheduler.scheduler import Scheduler


def main():
    """
    Entry point for the pyscheduler CLI.
    """

    # No command provided
    if len(sys.argv) < 2:
        print("Usage: pyscheduler <command>")
        print("Available commands:")
        print("  run    Run the scheduler")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "run":
        scheduler = Scheduler()
        scheduler.run()
    else:
        print(f"Unknown command: {command}")
        print("Use: pyscheduler run")
        sys.exit(1)


if __name__ == "__main__":
    main()
