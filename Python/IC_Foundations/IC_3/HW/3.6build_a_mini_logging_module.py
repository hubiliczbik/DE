import mylog

mylog.info("starting")
mylog.warn("disk 80% full")
mylog.error("connection refused")

mylog.set_level("WARN")

mylog.info("not shown")
mylog.warn("shown")

mylog.set_output("/tmp/app.log")

mylog.error("saved to file")
