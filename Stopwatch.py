import simplegui

time = 0
message = "0:00.0"
tries = 0
success = 0
begun = False


def format(t):
    global message
    milli = t % 10
    x = t / 10
    min = int(x / 60)
    secs = int(x % 60)
    message = str(min) + ":" + ('%02d' % secs) + "." + str(milli)


def start_timer():
    timer.start()
    global begun
    begun = True


def stop_timer():
    timer.stop()
    global tries
    global success
    global label
    global begun
    if begun:
        if time % 10 == 0:
            success += 1
        begun = False
        tries += 1


def reset_timer():
    global time
    global begun
    global tries
    global success
    begun = 0
    tries = 0
    success = 0
    timer.stop()
    time = 0
    format(time)


def timer_handler():
    global time
    time += 1
    format(time)


def draw(canvas):
    canvas.draw_text(message, [60, 90], 30, "Black")
    canvas.draw_text(str(success) + "/" + str(tries), [150, 30], 20, "Green")


frame = simplegui.create_frame("Stopwatch: The Game", 200, 150)
frame.set_canvas_background("White")

frame.add_button("Start", start_timer, 100)
frame.add_button("Stop", stop_timer, 100)
frame.add_button("Reset", reset_timer, 100)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

frame.start()
