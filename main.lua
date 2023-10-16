local bump = require("libraries/bump")
local world = bump.newWorld()

local camera = require("libraries/camera")
local cam = camera()

local anim8 = require("libraries/anim8")
love.graphics.setDefaultFilter("nearest", "nearest")

local sti = require("libraries/sti")
local gameMap = sti("assets/maps/testMap.lua", { "bump" })
gameMap:bump_init(world)

local function drawBox(box, r, g, b)
    love.graphics.setColor(r, g, b, 0.25)
    love.graphics.rectangle("fill", box.x, box.y, box.w, box.h)
    love.graphics.setColor(r, g, b)
    love.graphics.rectangle("line", box.x, box.y, box.w, box.h)
end

local player = {
    x = 400,
    y = 350,
    width = 12,
    height = 18,
    speed = 200,
    spriteSheet = love.graphics.newImage("assets/sprites/player-sheet.png"),
    grid = anim8.newGrid(width, height, spriteSheet:getWidth(), spriteSheet:getHeight())
}

local function updatePlayer(dt)
    local speed = player.speed

    local dx, dy = 0, 0
    if love.keyboard.isDown('right') then
        dx = speed * dt
    elseif love.keyboard.isDown('left') then
        dx = -speed * dt
    end
    if love.keyboard.isDown('down') then
        dy = speed * dt
    elseif love.keyboard.isDown('up') then
        dy = -speed * dt
    end

    if dx ~= 0 or dy ~= 0 then
        local cols
        player.x, player.y, cols, cols_len = world:move(player, player.x + dx, player.y + dy)
        for i = 1, cols_len do
            local col = cols[i]
            consolePrint(("col.other = %s, col.type = %s, col.normal = %d,%d"):format(col.other, col.type, col.normal.x, col.normal.y))
        end
    end
end

function love.load()
    world:add(player, player.x, player.y, 12, 18)

    player.animations = {}
    player.animations.down = anim8.newAnimation(player.grid("1-4", 1), 0.2)
    player.animations.left = anim8.newAnimation(player.grid("1-4", 2), 0.2)
    player.animations.right = anim8.newAnimation(player.grid("1-4", 3), 0.2)
    player.animations.up = anim8.newAnimation(player.grid("1-4", 4), 0.2)

    player.anim = player.animations.down
end

function love.update(dt)
    local isMoving = false

    local goalX, goalY = player.x, player.y

    if love.keyboard.isDown("s") then
        goalY = player.y + player.speed
        player.anim = player.animations.down
        isMoving = true
    end
    if love.keyboard.isDown("a") then
        goalX = player.x - player.speed
        player.anim = player.animations.left
        isMoving = true
    end
    if love.keyboard.isDown("d") then
        goalX = player.x + player.speed
        player.anim = player.animations.right
        isMoving = true
    end
    if love.keyboard.isDown("w") then
        goalY = player.y - player.speed
        player.anim = player.animations.up
        isMoving = true
    end

    local actualX, actualY = world:move(player, goalX, goalY, slide)
    player.x, player.y = actualX, actualY

    if isMoving == false then
        player.anim:gotoFrame(2)
    end

    player.anim:update(dt)

    cam:lookAt(player.x, player.y)

    local w = love.graphics.getWidth()
    local h = love.graphics.getHeight()

    if cam.x < w / 2 then
        cam.x = w / 2
    end

    if cam.y < h / 2 then
        cam.y = h / 2
    end

    local mapW = gameMap.width * gameMap.tilewidth
    local mapH = gameMap.height * gameMap.tileheight

    if cam.x > (mapW - w / 2) then
        cam.x = (mapW - w / 2)
    end
    if cam.y > (mapH - h / 2) then
        cam.y = (mapH - h / 2)
    end

end

function love.draw()
    cam:attach()
    gameMap:drawLayer(gameMap.layers["Ground"])
    gameMap:drawLayer(gameMap.layers["Trees"])
    player.anim:draw(player.spriteSheet, player.x, player.y, nil, 4, nil, 6, 9)
    cam:detach()
end