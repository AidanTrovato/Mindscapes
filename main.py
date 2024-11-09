@namespace
class SpriteKind:
    House = SpriteKind.create()
    HouseBlue = SpriteKind.create()
    Scene = SpriteKind.create()
    Food2 = SpriteKind.create()
    Food3 = SpriteKind.create()
    Food4 = SpriteKind.create()
    Food5 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    mySprite.say_text("I choose to focus on the present moment and let go of what I cannot control")
sprites.on_overlap(SpriteKind.player, SpriteKind.Food4, on_on_overlap)

def on_overlap_tile(sprite4, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile)

def on_on_overlap2(sprite22, otherSprite22):
    global Tree, Food22, Food32, Food42, Food52
    tiles.set_current_tilemap(tilemap("""
        level6
    """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.dark_ground_south_east1)
    scene.camera_follow_sprite(mySprite)
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(black_dot)
    mySprite.say_text("Collect the pearls to hear positive affirmations",
        5000,
        False)
    Tree = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.food)
    Tree.x = 70
    Tree.y = 50
    Food22 = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.Food2)
    Food22.x = 200
    Food22.y = 60
    Food32 = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.Food3)
    Food32.x = 150
    Food32.y = 220
    Food42 = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.Food4)
    Food42.x = 190
    Food42.y = 150
    Food52 = sprites.create(img("""
            . . . . . b b b b b b . . . . . 
                    . . . b b 9 9 9 9 9 9 b b . . . 
                    . . b b 9 9 9 9 9 9 9 9 b b . . 
                    . b b 9 d 9 9 9 9 9 9 9 9 b b . 
                    . b 9 d 9 9 9 9 9 1 1 1 9 9 b . 
                    b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b 
                    b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b 
                    b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b 
                    b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b 
                    b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b 
                    . b 5 3 3 3 d 9 9 9 9 d d 5 b . 
                    . b d 5 3 3 3 3 3 3 3 d 5 b b . 
                    . . b d 5 d 3 3 3 3 5 5 b b . . 
                    . . . b b 5 5 5 5 5 5 b b . . . 
                    . . . . . b b b b b b . . . . .
        """),
        SpriteKind.Food5)
    Food52.x = 50
    Food52.y = 130
sprites.on_overlap(SpriteKind.player, SpriteKind.House, on_on_overlap2)

def on_on_overlap3(sprite5, otherSprite4):
    mySprite.say_text("I am deserving of peace and happiness")
sprites.on_overlap(SpriteKind.player, SpriteKind.Food5, on_on_overlap3)

def on_on_overlap4(sprite3, otherSprite3):
    mySprite.say_text("I am enough just as I am, and I don't need to be perfect")
sprites.on_overlap(SpriteKind.player, SpriteKind.Food3, on_on_overlap4)

def on_on_overlap5(sprite6, otherSprite5):
    mySprite.say_text("I am in control of my thoughts and emotions", 5000, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.Food2, on_on_overlap5)

def on_on_overlap6(sprite2, otherSprite2):
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.dark_ground_north_west1)
    scene.camera_follow_sprite(mySprite)
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(black_dot)
    mySprite.say_text("Control your breathing whilst doing the maze", 5000, False)
    pause(3000)
    mySprite.say_text("Inhale and Exhale for 4 seconds at a time", 3000, False)
    pause(3000)
    info.start_countdown(30)
sprites.on_overlap(SpriteKind.player, SpriteKind.HouseBlue, on_on_overlap6)

def on_on_overlap7(sprite32, otherSprite32):
    mySprite.say_text("It's okay to seek help; I am strong for reaching out",
        5000,
        False)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap7)

Food52: Sprite = None
Food42: Sprite = None
Food32: Sprite = None
Food22: Sprite = None
Tree: Sprite = None
black_dot: Sprite = None
mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""level1"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite2 = sprites.create(img("""
        ....................e2e22e2e....................
            .................222eee22e2e222.................
            ..............222e22e2e22eee22e222..............
            ...........e22e22eeee2e22e2eeee22e22e...........
            ........eeee22e22e22e2e22e2e22e22e22eeee........
            .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
            ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
            4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
            6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
            46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
            46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
            4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
            6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
            4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
            6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
            46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
            6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
            46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
            46622e22e22e22eeecc6666666666cceee22e22e22e22664
            4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
            6c622e22eeecc66666cc64444446cc66666cceee22e226c6
            46622e22cc66666cc64444444444446cc66666cc22e22664
            46622cc6666ccc64444444444444444446ccc6666cc22664
            4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
            cccccccc6666666cb44444444444444bc6666666cccccccc
            64444444444446c444444444444444444c64444444444446
            66cb444444444cb411111111111111114bc444444444bc66
            666cccccccccccd166666666666666661dccccccccccc666
            6666444444444c116eeeeeeeeeeeeee611c4444444446666
            666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
            666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
            666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
            666edffdffde4c66f4effffffffff4ee66c4edffdffde666
            666edccdccde4c66f4effffffffffeee66c4edccdccde666
            666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
            c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
            c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
            cc66666666664c66e4e44e44e44feeee66c46666666666cc
            .c66444444444c66e4e44e44e44ffffe66c44444444466c.
            ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
            ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
            ....644444444c66f4e44e44e44e44ee66c444444446....
            .....64eee444c66f4e44e44e44e44ee66c444eee46.....
            ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
    """),
    SpriteKind.House)
mySprite2.x = 25
mySprite2.y = 25
mySprite2.set_scale(0.75, ScaleAnchor.MIDDLE)
mySprite3 = sprites.create(img("""
        ....................8a8aa8a8....................
            .................aaa888aa8a8aaa.................
            ..............aaa8aa8a8aa888aa8aaa..............
            ...........8aa8aa8888a8aa8a8888aa8aa8...........
            ........8888aa8aa8aa8a8aa8a8aa8aa8aa8888........
            .....aaa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aaa.....
            ...aa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aa...
            dccaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aaccd
            bcb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bcb
            dbbaa8aa8888aa8aa8888a8aa8a8888aa8aa8888aa8aabbd
            dbbaa8aa8aa8aa8888aa8a8aa8a8aa8888aa8aa8aa8aabbd
            dccaa8888aa8aa8aa8aa888aa888aa8aa8aa8aa8888aaccd
            bcbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabcb
            dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
            dbbaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aabbd
            dccaa8aa8aa8aa8aa8888a8aa8a8888aa8aa8aa8aa8aaccd
            bcbaa8888aa8aa8888aa888aa888aa8888aa8aa8888aabcb
            dbbaa8aa8aa8888aa8aa8a8aa8a8aa8aa8888aa8aa8aabbd
            dbb888aa8aa8aa8aa8aa8a8aa8a8aa8aa8aa8aa8aa888bbd
            dccaa8aa8888aa8aa8aa8a8aa8a8aa8aa8aa8888aa8aaccd
            bcbaa8aa8aa8aa8aa8aa888aa888aa8aa8aa8aa8aa8aabcb
            dbbaa8888aa8aa8aa888ccbbbbcc888aa8aa8aa8888aabbd
            dbbaa8aa8aa8aa888ccbbbbbbbbbbcc888aa8aa8aa8aabbd
            dcc888aa8aa888ccbbbbbccccccbbbbbcc888aa8aa888ccd
            bcbaa8aa888ccbbbbbccbddddddbccbbbbbcc888aa8aabcb
            dbbaa8aaccbbbbbccbddddddddddddbccbbbbbccaa8aabbd
            dbbaaccbbbbcccbddddddddddddddddddbcccbbbbccaabbd
            dcccbbbbcccbdddbccbbbbbbbbbbbbccbdddbcccbbbbcccd
            ccccccccbbbbbbbcbddddddddddddddbcbbbbbbbcccccccc
            bddddddddddddbcddddddddddddddddddcbddddddddddddb
            bbcbdddddddddcbd1111111111111111dbcdddddddddbcbb
            bbbcccccccccccd1bbbbbbbbbbbbbbbb1dcccccccccccbbb
            bbbbdddddddddc11beeeeeeeeeeeeeeb11cdddddddddbbbb
            bbb8aaaaaaa8dc1be3b33b33b33b33beb1cd8aaaaaaa8bbb
            bbb888888888dc1be3b33b33b33b33beb1cd888888888bbb
            bbb833333338dcbbf3b3effffffe33bebbcd833333338bbb
            bbb83ff3ff38dcbbf3bffffffffff3bebbcd83ff3ff38bbb
            bbb83cc3cc38dcbbf3effffffffffebebbcd83cc3cc38bbb
            bbb833333338dcbbf3eeeeeeeeeeeebebbcd833333338bbb
            cbb83ff3ff38dcbbe3b33b33b33b33bebbcd83ff3ff38bbc
            cbb83cc3cc38dcbbe3b33b33b33b33bebbcd83cc3cc38bbc
            ccbbbbbbbbbbdcbbe3b33b33b33feeeebbcdbbbbbbbbbbcc
            .cbbdddddddddcbbe3b33b33b33ffffebbcdddddddddbbc.
            ..cbdbbbdbbbdcbbf3b33b33b33f33febbcdbbbdbbbdbc..
            ...cdbbbdbbbdcbbf3b33b33b33bffeebbcdbbbdbbbdc...
            ....bddddddddcbbf3b33b33b33b33bebbcddddddddb....
            .....bdbbbdddcbbf3b33b33b33b33bebbcdddbbbdb.....
            ......bcccbbbcbbe3b33b33b33b33bebbcbbbcccb......
    """),
    SpriteKind.HouseBlue)
mySprite3.x = 135
mySprite3.y = 25
mySprite3.set_scale(0.75, ScaleAnchor.MIDDLE)
black_dot = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . f . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Scene)
black_dot.say_text("WELCOME TO MINDSCAPES, THE GAME TO HELP YOU WITH MENTAL HEALTH",
    5000,
    False)
pause(2000)
black_dot.say_text("IN THE HOUSES ARE TWO DIFFERENT GAMES, GO INSIDE!")
black_dot.x = 80
black_dot.y = 130