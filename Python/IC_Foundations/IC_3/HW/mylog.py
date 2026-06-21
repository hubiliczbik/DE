from datetime import datetime

LVLS = {
    "INFO": 10,
    "WARN": 20,
    "ERROR": 30
}

current_level = "INFO"
output_path = None


def set_level(lvl):
    global current_level

    lvl = lvl.upper()

    if lvl not in LVLS:
        raise ValueError("Unknown level")

    current_level = lvl


def set_output(path):
    global output_path
    output_path = path


def _should_log(lvl):
    return LVLS[lvl] >= LVLS[current_level]


def _write_line(line):
    if output_path is None:
        print(line)
    else:
        with open(output_path, "a") as file:
            file.write(line + "\n")


def _log(level, mess):
    if not _should_log(level):
        return

    timestamp = datetime.now().isoformat(timespec="seconds")
    line = f"{timestamp} [{level}] {mess}"
    _write_line(line)


def info(message):
    _log("INFO", message)


def warn(message):
    _log("WARN", message)


def error(message):
    _log("ERROR", message)
