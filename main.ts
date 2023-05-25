namespace SpriteKind {
    export const lift = SpriteKind.create()
    export const on_screen = SpriteKind.create()
    export const pj2 = SpriteKind.create()
    export const boss = SpriteKind.create()
}
namespace StatusBarKind {
    export const ammo1 = StatusBarKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    gravity = mySprite.vy
    if (gravity != 0) {
        pause(200)
    } else {
        mySprite.setVelocity(0, -150)
    }
    if (gravity != 0) {
        pause(200)
    } else {
        health_show.setVelocity(0, -150)
    }
    if (gravity != 0) {
        pause(200)
    } else {
        ammo_count.setVelocity(0, -150)
    }
})
function spaw_enimies3 () {
    spaw_enimies2()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    ammo = 8
    if (ammo == 8) {
        ammo_count.setImage(assets.image`ammo`)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile12`, function (sprite3, location2) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(19, 8))
    tiles.placeOnTile(ammo_count, tiles.getTileLocation(19, 8))
    tiles.placeOnTile(health_show, tiles.getTileLocation(19, 8))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile46`, function (sprite, location) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    tiles.setCurrentTilemap(tilemap`level10`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(1, 9))
    tiles.placeOnTile(health_show, tiles.getTileLocation(1, 9))
    bhps = sprites.create(assets.image`Health8`, SpriteKind.on_screen)
    bosslvl()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (ammo == 0) {
    	
    } else if (direction == 0) {
        projectile = sprites.createProjectileFromSprite(assets.image`myImage12`, mySprite, 200, 0)
        projectile.ay = 5
        ammo += -1
    } else {
        projectile = sprites.createProjectileFromSprite(assets.image`myImage11`, mySprite, -200, 0)
        ammo += -1
    }
    if (ammo == 1) {
        ammo_count.setImage(assets.image`ammo6`)
    }
    if (ammo == 5) {
        ammo_count.setImage(assets.image`ammo2`)
    }
    if (ammo == 0) {
        ammo_count.setImage(assets.image`ammo7`)
    }
    if (ammo == 4) {
        ammo_count.setImage(assets.image`ammo3`)
    }
    if (ammo == 6) {
        ammo_count.setImage(assets.image`ammo1`)
    }
    if (ammo == 3) {
        ammo_count.setImage(assets.image`ammo4`)
    }
    if (ammo == 2) {
        ammo_count.setImage(assets.image`ammo5`)
    }
    if (ammo == 7) {
        ammo_count.setImage(assets.image`ammo0`)
    }
    if (ammo == 8) {
        ammo_count.setImage(assets.image`ammo`)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite8, otherSprite3) {
    if (projectile.overlapsWith(myEnemy)) {
        sprites.destroy(otherSprite3, effects.smiles, 500)
    }
    if (projectile.overlapsWith(myenemy2)) {
        sprites.destroy(otherSprite3, effects.smiles, 500)
    }
    if (projectile.overlapsWith(myEnemy)) {
        sprites.destroy(otherSprite3, effects.smiles, 500)
    }
})
function boss_health () {
    bosshp = 16
}
function spaw_enimies2 () {
    myEnemy = sprites.create(assets.image`myImage10`, SpriteKind.Enemy)
    myenemy2 = sprites.create(assets.image`myImage18`, SpriteKind.Enemy)
    tiles.placeOnTile(myenemy2, tiles.getTileLocation(13, 8))
    tiles.placeOnTile(myEnemy, tiles.getTileLocation(20, 13))
    myenemy2.ay = 500
    myEnemy.ay = 500
    chance = 75
}
scene.onOverlapTile(SpriteKind.Projectile, assets.tile`myTile35`, function (sprite7, location5) {
    sprites.destroy(sprite7)
    tiles.setTileAt(tiles.getTileLocation(4, 9), assets.tile`myTile39`)
    tiles.setTileAt(tiles.getTileLocation(4, 8), assets.tile`myTile38`)
    timer.after(500, function () {
        tiles.setTileAt(tiles.getTileLocation(4, 9), assets.tile`myTile41`)
        tiles.setTileAt(tiles.getTileLocation(4, 8), assets.tile`myTile40`)
        tiles.setWallAt(tiles.getTileLocation(4, 8), false)
        tiles.setWallAt(tiles.getTileLocation(4, 9), false)
    })
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    direction = 1
    mySprite.setImage(assets.image`myImage2`)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.boss, function (sprite6, otherSprite2) {
    if (projectile.overlapsWith(myEnemy)) {
        bosshp += -1
        sprites.destroy(sprite6)
    }
    if (projectile.overlapsWith(myEnemy)) {
        bosshp += -1
        sprites.destroy(sprite6)
    }
    if (bosshp == 0) {
        sprites.destroy(myEnemy, effects.ashes, 1000)
        timer.after(1000, function () {
            game.gameOver(true)
        })
    }
})
function bosslvl () {
    boss_lvl = 1
    myEnemy = sprites.create(assets.image`myImage3`, SpriteKind.boss)
    myEnemy.follow(mySprite, 20)
    tiles.placeOnTile(myEnemy, tiles.getTileLocation(10, 8))
    myEnemy.ay = 500
    chance = 75
    bhps.setStayInScreen(true)
    boss_health()
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`myImage5`)
    direction = 0
})
scene.onOverlapTile(SpriteKind.Projectile, assets.tile`myTile32`, function (sprite4, location3) {
    sprites.destroy(sprite4)
    tiles.setTileAt(tiles.getTileLocation(4, 9), assets.tile`myTile35`)
    tiles.setTileAt(tiles.getTileLocation(4, 8), assets.tile`myTile34`)
})
function spaw_enimies () {
    myEnemy = sprites.create(assets.image`myImage10`, SpriteKind.Enemy)
    myenemy2 = sprites.create(assets.image`myImage18`, SpriteKind.Enemy)
    tiles.placeOnTile(myenemy2, tiles.getTileLocation(13, 8))
    tiles.placeOnTile(myEnemy, tiles.getTileLocation(20, 13))
    myenemy2.ay = 500
    myEnemy.ay = 500
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile26`, function (sprite10, location7) {
    tiles.setCurrentTilemap(tilemap`level8`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 13))
    spaw_enimies2()
})
scene.onOverlapTile(SpriteKind.Projectile, assets.tile`myTile36`, function (sprite5, location4) {
    sprites.destroy(sprite5)
    tiles.setTileAt(tiles.getTileLocation(4, 9), assets.tile`myTile32`)
    tiles.setTileAt(tiles.getTileLocation(4, 8), assets.tile`myTile33`)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite2, otherSprite) {
    if (projectile2.overlapsWith(mySprite)) {
        sprites.destroy(sprite2)
        healthy += -1
    }
    if (projectile3.overlapsWith(mySprite)) {
        sprites.destroy(sprite2)
        healthy += -1
    }
    if (healthy == 8) {
        health_show.setImage(assets.image`Health`)
    }
    if (healthy == 7) {
        health_show.setImage(assets.image`Health5`)
    }
    if (healthy == 6) {
        health_show.setImage(assets.image`Health0`)
    }
    if (healthy == 5) {
        health_show.setImage(assets.image`Health1`)
    }
    if (healthy == 4) {
        health_show.setImage(assets.image`Health2`)
    }
    if (healthy == 3) {
        health_show.setImage(assets.image`Health3`)
    }
    if (healthy == 2) {
        health_show.setImage(assets.image`Health4`)
    }
    if (healthy == 1) {
        health_show.setImage(assets.image`Health6`)
    }
    if (healthy == 0) {
        health_show.setImage(assets.image`Health7`)
        sprites.destroy(mySprite, effects.ashes, 1000)
        timer.after(1000, function () {
            game.gameOver(false)
        })
    }
})
function start () {
    tiles.setCurrentTilemap(tilemap`level`)
    pills = sprites.create(assets.image`myImage9`, SpriteKind.Food)
    mySprite = sprites.create(assets.image`myImage2`, SpriteKind.Player)
    ammo_count = sprites.create(assets.image`ammo`, SpriteKind.on_screen)
    health_show = sprites.create(assets.image`Health`, SpriteKind.on_screen)
    chance = 50
    health_show.setPosition(24, 100)
    mySprite.setPosition(24, 100)
    controller.moveSprite(mySprite, 100, 0)
    controller.moveSprite(ammo_count, 100, 0)
    controller.moveSprite(health_show, 100, 0)
    mySprite.ay = 500
    scene.cameraFollowSprite(mySprite)
    ammo = 8
    scene.setBackgroundColor(6)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 12))
    healthy = 8
    ammo_count.setStayInScreen(true)
    health_show.setStayInScreen(true)
    spaw_enimies()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile11`, function (sprite9, location6) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(19, 13))
    tiles.placeOnTile(ammo_count, tiles.getTileLocation(19, 13))
    tiles.placeOnTile(health_show, tiles.getTileLocation(19, 13))
})
let bossg = 0
let pills: Sprite = null
let projectile3: Sprite = null
let healthy = 0
let projectile2: Sprite = null
let boss_lvl = 0
let chance = 0
let bosshp = 0
let myenemy2: Sprite = null
let myEnemy: Sprite = null
let projectile: Sprite = null
let direction = 0
let bhps: Sprite = null
let ammo = 0
let ammo_count: Sprite = null
let health_show: Sprite = null
let mySprite: Sprite = null
let gravity = 0
start()
game.onUpdateInterval(500, function () {
    if (boss_lvl == 1) {
    	
    } else if (spriteutils.isDestroyed(myEnemy)) {
    	
    } else if (Math.percentChance(chance)) {
        projectile2 = sprites.createProjectileFromSprite(assets.image`myImage15`, myEnemy, -100, 0)
    }
})
game.onUpdateInterval(500, function () {
    if (boss_lvl == 1) {
        if (myEnemy.vx > 0) {
            if (Math.percentChance(chance)) {
                myEnemy.setImage(assets.image`myImage3`)
                projectile3 = sprites.createProjectileFromSprite(assets.image`myImage14`, myEnemy, 100, 0)
            }
        } else if (myEnemy.vx < 0) {
            if (Math.percentChance(chance)) {
                myEnemy.setImage(assets.image`myImage19`)
                projectile3 = sprites.createProjectileFromSprite(assets.image`myImage15`, myEnemy, -100, 0)
            }
        } else {
        	
        }
    } else if (spriteutils.isDestroyed(myenemy2)) {
    	
    } else if (Math.percentChance(chance)) {
        projectile3 = sprites.createProjectileFromSprite(assets.image`myImage14`, myenemy2, 100, 0)
    }
})
game.onUpdateInterval(500, function () {
    if (boss_lvl == 1) {
        if (myEnemy.vx == 0) {
            bossg = myEnemy.vy
            if (bossg != 0) {
            	
            } else {
                myEnemy.setVelocity(0, -150)
            }
            if (bossg != 0) {
            	
            } else {
                bhps.setVelocity(0, -150)
            }
            if (bossg != 0) {
            	
            } else {
                ammo_count.setVelocity(0, -150)
            }
        }
    }
})
