package io.skaihen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input.Keys;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.ExtendViewport;
import com.badlogic.gdx.utils.viewport.Viewport;


public class GameScreen implements Screen {
    final Garoa game;
    private final OrthographicCamera camera;
    private final Texture plepImg;
    private final Rectangle plep;
    private final Viewport extendedViewport;

    public GameScreen(final Garoa game) {
        this.game = game;

        plepImg = new Texture("plep.jpg");

        camera = new OrthographicCamera();
        camera.setToOrtho(false, 640, 480);
        extendedViewport = new ExtendViewport(camera.viewportWidth, camera.viewportHeight, camera);

        plep = new Rectangle();

        plep.width = 32f;
        plep.height = 64f;

        plep.x = (float) game.getWidthScreen() / 2 - plep.width / 2;
        plep.y = 20f;
    }

    @Override
    public void render(float delta) {
        ScreenUtils.clear(0, 0, 0, 1);

        camera.update();

        game.getBatch().setProjectionMatrix(camera.combined);
        game.getBatch().begin();
        game.getBatch().draw(plepImg, plep.x, plep.y, plep.width, plep.height);
        game.getBatch().end();

        if (Gdx.input.isTouched()) {
            Vector3 touchPos = new Vector3();
            touchPos.set(Gdx.input.getX(), Gdx.input.getY(), 0);
            camera.unproject(touchPos);
            plep.x = touchPos.x - plep.width / 2;
        }
        if (Gdx.input.isKeyPressed(Keys.A)) plep.x -= (int) (200 * Gdx.graphics.getDeltaTime());
        if (Gdx.input.isKeyPressed(Keys.D)) plep.x += (int) (200 * Gdx.graphics.getDeltaTime());

        if (plep.x < 0) plep.x = 0;
        if (plep.x > game.getWidthScreen() - plep.width) plep.x = game.getWidthScreen() - plep.width;
    }

    @Override
    public void resize(int width, int height) {
        extendedViewport.update(width, height);
    }

    @Override
    public void show() {
    }

    @Override
    public void hide() {
    }

    @Override
    public void pause() {
    }

    @Override
    public void resume() {
    }

    @Override
    public void dispose() {
        plepImg.dispose();
    }
}
