@namespace
class SpriteKind:
    lift = SpriteKind.create()
    on_screen = SpriteKind.create()
    pj2 = SpriteKind.create()
    boss = SpriteKind.create()
@namespace
class StatusBarKind:
    ammo1 = StatusBarKind.create()

def on_up_pressed():
    global gravity
    gravity = mySprite.vy
    if gravity != 0:
        pause(200)
    else:
        mySprite.set_velocity(0, -150)
    if gravity != 0:
        pause(200)
    else:
        health_show.set_velocity(0, -150)
    if gravity != 0:
        pause(200)
    else:
        ammo_count.set_velocity(0, -150)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global ammo
    ammo = 8
    if ammo == 8:
        ammo_count.set_image(assets.image("""
            ammo
        """))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def boss_health():
    global bosshp
    bosshp = 16

def on_overlap_tile(sprite, location):
    global bhps
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    tiles.set_current_tilemap(tilemap("""
        level10
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 9))
    tiles.place_on_tile(health_show, tiles.get_tile_location(1, 9))
    bhps = sprites.create(assets.image("""
        Health8
    """), SpriteKind.on_screen)
    bosslvl()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile46
    """),
    on_overlap_tile)

def on_a_pressed():
    global projectile, ammo
    if ammo == 0:
        pass
    else:
        if direction == 0:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                myImage12
            """), mySprite, 200, 0)
            projectile.ay = 5
            ammo += -1
        else:
            projectile = sprites.create_projectile_from_sprite(assets.image("""
                myImage11
            """), mySprite, -200, 0)
            ammo += -1
    if ammo == 1:
        ammo_count.set_image(assets.image("""
            ammo6
        """))
    if ammo == 5:
        ammo_count.set_image(assets.image("""
            ammo2
        """))
    if ammo == 0:
        ammo_count.set_image(assets.image("""
            ammo7
        """))
    if ammo == 4:
        ammo_count.set_image(assets.image("""
            ammo3
        """))
    if ammo == 6:
        ammo_count.set_image(assets.image("""
            ammo1
        """))
    if ammo == 3:
        ammo_count.set_image(assets.image("""
            ammo4
        """))
    if ammo == 2:
        ammo_count.set_image(assets.image("""
            ammo5
        """))
    if ammo == 7:
        ammo_count.set_image(assets.image("""
            ammo0
        """))
    if ammo == 8:
        ammo_count.set_image(assets.image("""
            ammo
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite):
    global healthy
    if projectile2.overlaps_with(mySprite):
        sprites.destroy(sprite2)
        healthy += -1
    if projectile3.overlaps_with(mySprite):
        sprites.destroy(sprite2)
        healthy += -1
    if healthy == 8:
        health_show.set_image(assets.image("""
            Health
        """))
    if healthy == 7:
        health_show.set_image(assets.image("""
            Health5
        """))
    if healthy == 6:
        health_show.set_image(assets.image("""
            Health0
        """))
    if healthy == 5:
        health_show.set_image(assets.image("""
            Health1
        """))
    if healthy == 4:
        health_show.set_image(assets.image("""
            Health2
        """))
    if healthy == 3:
        health_show.set_image(assets.image("""
            Health3
        """))
    if healthy == 2:
        health_show.set_image(assets.image("""
            Health4
        """))
    if healthy == 1:
        health_show.set_image(assets.image("""
            Health6
        """))
    if healthy == 0:
        health_show.set_image(assets.image("""
            Health7
        """))
        sprites.destroy(mySprite, effects.ashes, 1000)
        
        def on_after():
            game.game_over(False)
        timer.after(1000, on_after)
        
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_overlap_tile2(sprite3, location2):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(19, 8))
    tiles.place_on_tile(ammo_count, tiles.get_tile_location(19, 8))
    tiles.place_on_tile(health_show, tiles.get_tile_location(19, 8))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
    """),
    on_overlap_tile2)

def on_left_pressed():
    global direction
    direction = 1
    mySprite.set_image(assets.image("""
        myImage2
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile3(sprite4, location3):
    sprites.destroy(sprite4)
    tiles.set_tile_at(tiles.get_tile_location(4, 9),
        assets.tile("""
            myTile35
        """))
    tiles.set_tile_at(tiles.get_tile_location(4, 8),
        assets.tile("""
            myTile34
        """))
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile32
    """),
    on_overlap_tile3)

def bosslvl():
    global boss_lvl, myEnemy, chance
    boss_lvl = 1
    myEnemy = sprites.create(assets.image("""
        myImage3
    """), SpriteKind.boss)
    myEnemy.follow(mySprite, 20)
    tiles.place_on_tile(myEnemy, tiles.get_tile_location(10, 8))
    myEnemy.ay = 500
    chance = 75
    bhps.set_stay_in_screen(True)
    boss_health()

def on_right_pressed():
    global direction
    mySprite.set_image(assets.image("""
        myImage5
    """))
    direction = 0
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def spaw_enimies3():
    spaw_enimies2()
def spaw_enimies():
    global myEnemy, myenemy2
    myEnemy = sprites.create(assets.image("""
        myImage10
    """), SpriteKind.enemy)
    myenemy2 = sprites.create(assets.image("""
        myImage18
    """), SpriteKind.enemy)
    tiles.place_on_tile(myenemy2, tiles.get_tile_location(13, 8))
    tiles.place_on_tile(myEnemy, tiles.get_tile_location(20, 13))
    myenemy2.ay = 500
    myEnemy.ay = 500

def on_overlap_tile4(sprite5, location4):
    sprites.destroy(sprite5)
    tiles.set_tile_at(tiles.get_tile_location(4, 9),
        assets.tile("""
            myTile32
        """))
    tiles.set_tile_at(tiles.get_tile_location(4, 8),
        assets.tile("""
            myTile33
        """))
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile36
    """),
    on_overlap_tile4)

def on_on_overlap2(sprite6, otherSprite2):
    global bosshp
    if projectile.overlaps_with(myEnemy):
        bosshp += -1
        sprites.destroy(sprite6)
    if projectile.overlaps_with(myEnemy):
        bosshp += -1
        sprites.destroy(sprite6)
    if bosshp == 0:
        sprites.destroy(myEnemy, effects.ashes, 1000)
        
        def on_after2():
            game.game_over(True)
        timer.after(1000, on_after2)
        
sprites.on_overlap(SpriteKind.projectile, SpriteKind.boss, on_on_overlap2)

def on_overlap_tile5(sprite7, location5):
    sprites.destroy(sprite7)
    tiles.set_tile_at(tiles.get_tile_location(4, 9),
        assets.tile("""
            myTile39
        """))
    tiles.set_tile_at(tiles.get_tile_location(4, 8),
        assets.tile("""
            myTile38
        """))
    
    def on_after3():
        tiles.set_tile_at(tiles.get_tile_location(4, 9),
            assets.tile("""
                myTile41
            """))
        tiles.set_tile_at(tiles.get_tile_location(4, 8),
            assets.tile("""
                myTile40
            """))
        tiles.set_wall_at(tiles.get_tile_location(4, 8), False)
        tiles.set_wall_at(tiles.get_tile_location(4, 9), False)
    timer.after(500, on_after3)
    
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile35
    """),
    on_overlap_tile5)

def start():
    global pills, mySprite, ammo_count, health_show, chance, ammo, healthy
    tiles.set_current_tilemap(tilemap("""
        level
    """))
    pills = sprites.create(assets.image("""
        myImage9
    """), SpriteKind.food)
    mySprite = sprites.create(assets.image("""
        myImage2
    """), SpriteKind.player)
    ammo_count = sprites.create(assets.image("""
        ammo
    """), SpriteKind.on_screen)
    health_show = sprites.create(assets.image("""
        Health
    """), SpriteKind.on_screen)
    chance = 50
    health_show.set_position(24, 100)
    mySprite.set_position(24, 100)
    controller.move_sprite(mySprite, 100, 0)
    controller.move_sprite(ammo_count, 100, 0)
    controller.move_sprite(health_show, 100, 0)
    mySprite.ay = 500
    scene.camera_follow_sprite(mySprite)
    ammo = 8
    scene.set_background_color(6)
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, 12))
    healthy = 8
    ammo_count.set_stay_in_screen(True)
    health_show.set_stay_in_screen(True)
    spaw_enimies()

def on_on_overlap3(sprite8, otherSprite3):
    if projectile.overlaps_with(myEnemy):
        sprites.destroy(otherSprite3, effects.smiles, 500)
    if projectile.overlaps_with(myenemy2):
        sprites.destroy(otherSprite3, effects.smiles, 500)
    if projectile.overlaps_with(myEnemy):
        sprites.destroy(otherSprite3, effects.smiles, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def spaw_enimies2():
    global myEnemy, myenemy2, chance
    myEnemy = sprites.create(assets.image("""
        myImage10
    """), SpriteKind.enemy)
    myenemy2 = sprites.create(assets.image("""
        myImage18
    """), SpriteKind.enemy)
    tiles.place_on_tile(myenemy2, tiles.get_tile_location(13, 8))
    tiles.place_on_tile(myEnemy, tiles.get_tile_location(20, 13))
    myenemy2.ay = 500
    myEnemy.ay = 500
    chance = 75

def on_overlap_tile6(sprite9, location6):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(19, 13))
    tiles.place_on_tile(ammo_count, tiles.get_tile_location(19, 13))
    tiles.place_on_tile(health_show, tiles.get_tile_location(19, 13))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile11
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite10, location7):
    tiles.set_current_tilemap(tilemap("""
        level8
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, 13))
    spaw_enimies2()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile26
    """),
    on_overlap_tile7)

bossg = 0
pills: Sprite = None
myenemy2: Sprite = None
chance = 0
myEnemy: Sprite = None
boss_lvl = 0
projectile3: Sprite = None
healthy = 0
projectile2: Sprite = None
projectile: Sprite = None
direction = 0
bhps: Sprite = None
bosshp = 0
ammo = 0
ammo_count: Sprite = None
health_show: Sprite = None
mySprite: Sprite = None
gravity = 0
start()

def on_update_interval():
    global projectile2
    if boss_lvl == 1:
        pass
    else:
        if spriteutils.is_destroyed(myEnemy):
            pass
        else:
            if Math.percent_chance(chance):
                projectile2 = sprites.create_projectile_from_sprite(assets.image("""
                    myImage15
                """), myEnemy, -100, 0)
game.on_update_interval(500, on_update_interval)

def on_update_interval2():
    global projectile3
    if boss_lvl == 1:
        if myEnemy.vx > 0:
            if Math.percent_chance(chance):
                myEnemy.set_image(assets.image("""
                    myImage3
                """))
                projectile3 = sprites.create_projectile_from_sprite(assets.image("""
                    myImage14
                """), myEnemy, 100, 0)
        elif myEnemy.vx < 0:
            if Math.percent_chance(chance):
                myEnemy.set_image(assets.image("""
                    myImage19
                """))
                projectile3 = sprites.create_projectile_from_sprite(assets.image("""
                    myImage15
                """), myEnemy, -100, 0)
        else:
            pass
    else:
        if spriteutils.is_destroyed(myenemy2):
            pass
        else:
            if Math.percent_chance(chance):
                projectile3 = sprites.create_projectile_from_sprite(assets.image("""
                    myImage14
                """), myenemy2, 100, 0)
game.on_update_interval(500, on_update_interval2)

def on_update_interval3():
    global bossg
    if boss_lvl == 1:
        if myEnemy.vx == 0:
            bossg = myEnemy.vy
            if bossg != 0:
                pass
            else:
                myEnemy.set_velocity(0, -150)
            if bossg != 0:
                pass
            else:
                bhps.set_velocity(0, -150)
            if bossg != 0:
                pass
            else:
                ammo_count.set_velocity(0, -150)
game.on_update_interval(500, on_update_interval3)
