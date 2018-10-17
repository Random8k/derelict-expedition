import libtcodpy as tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

font_path = 'arial10x10.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)

window_title = 'Derelict Expedition'
fullscreen = False
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)
con = tocd.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

def handle_keys():
    global player_x, player_y

    key = tcod.console_wait_for_keypress(True)
    if key.vk == tcod.KEY_ENTER and tcod.KEY_ALT:
        #Alt+Enter for toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    elif key.vk == tcod.KEY_ESCAPE:
        return True #exit game

    #movement, arrow keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y = player_y - 1

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y = player_y + 1

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x = player_x + 1

    #movement, numpad
    if tcod.console_is_key_pressed(tcod.KEY_KP1):
        player_y = player_y + 1
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP2):
        player_y = player_y + 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP3):
        player_y = player_y + 1
        player_x = player_x + 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP4):
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP6):
        player_x = player_x + 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP7):
        player_y = player_y - 1
        player_x = player_x - 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP8):
        player_y = player_y - 1

    elif tcod.console_is_key_pressed(tcod.KEY_KP9):
        player_y = player_y - 1
        player_x = player_x + 1

while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(0, tcod.white)
    tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)
    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    tcod.console_flush()
    tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)

    #handle keys and exit game if desired
    exit = handle_keys()
    if exit:
        break
