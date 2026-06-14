# hi

---
# ⏱️ Task Timer & Notifier

A lightweight CLI wrapper that runs any shell command, tracks its execution time, and sends a desktop notification when it finishes.

## Features

- Run any shell command via a simple `--run` flag
- Displays start time, end time, and total duration after execution
- Sends a desktop notification when the task completes
- Prints a visual separator line scaled to your terminal width

## Requirements

- Python 3.x
- [`plyer`](https://pypi.org/project/plyer/) for desktop notifications

Install dependencies:

```bash
pip install plyer
```

> **Note:** On Linux you may also need `libnotify` or a compatible notification daemon. On macOS and Windows, `plyer` works out of the box.

## Usage

```bash
python script.py --run "<your command>"
```

### Examples

```bash
# Run a Python script
python script.py --run "python train.py"

# Run a shell command
python script.py --run "sleep 5"

# Run a build command
python script.py --run "make build"
```

## Output

After the command finishes, you'll see something like:

```
hi!:--------------------------------------------------------------
Start : 14:03:21
End   : 14:07:45
Diff  : 0:04:24.103412
```

A desktop notification will also pop up with the total elapsed time.

## Arguments

| Argument | Type   | Description                  |
|----------|--------|------------------------------|
| `--run`  | string | The shell command to execute |

## Notes

- Commands are executed via `shell=True`, so standard shell syntax (pipes, redirects, etc.) is supported.
- If the desktop notification fails (e.g., unsupported platform or missing backend), the error is printed to stdout and execution continues normally.
- To use a custom app icon for the notification, set the `app_icon` parameter in the `notification.notify()` call inside the script.
