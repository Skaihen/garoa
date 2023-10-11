package io.skaihen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input.Keys;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.utils.ScreenUtils;


public class GameScreen implements Screen {
    final Garoa game;
    private final OrthographicCamera camera;
    private final Texture plepImg;
    private final Rectangle plep;

    public GameScreen(final Garoa game) {
        this.game = game;

        plepImg = new Texture("plep.jpg");

        camera = new OrthographicCamera(game.getWidthScreen(), game.getHeightScreen());
        camera.setToOrtho(false, game.getWidthScreen(), game.getHeightScreen());

        plep = new Rectangle();
        plep.x = (float) game.getWidthScreen() / 2 - 64f / 2;
        plep.y = 20f;

        plep.width = 64f;
        plep.height = 64f;
    }

    @Override
    public void render(float delta) {
        ScreenUtils.clear(1, 1, 1, 1);

        camera.update();

        game.getBatch().setProjectionMatrix(camera.combined);
        game.getBatch().begin();
        game.getBatch().draw(plepImg, plep.x, plep.y, plep.width, plep.height);
        game.getBatch().end();

        if (Gdx.input.isTouched()) {
            Vector3 touchPos = new Vector3();
            touchPos.set(Gdx.input.getX(), Gdx.input.getY(), 0);
            camera.unproject(touchPos);
            plep.x = touchPos.x - 64f / 2;
        }
        if (Gdx.input.isKeyPressed(Keys.A)) plep.x -= (int) (200 * Gdx.graphics.getDeltaTime());
        if (Gdx.input.isKeyPressed(Keys.D)) plep.x += (int) (200 * Gdx.graphics.getDeltaTime());

        if (plep.x < 0) plep.x = 0;
        if (plep.x > game.getWidthScreen() - 64f) plep.x = game.getWidthScreen() - 64f;
    }

    @Override
    public void resize(int width, int height) {
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
