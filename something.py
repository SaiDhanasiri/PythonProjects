import curses

def main(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.addstr(0, 0, "Press keys (Press 'q' to quit): ")

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        stdscr.addstr(1, 0, f"Key pressed: {key}")
        stdscr.refresh()

curses.wrapper(main)