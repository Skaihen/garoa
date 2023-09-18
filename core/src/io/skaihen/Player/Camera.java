package io.skaihen.Player;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController;

public class Camera {
    private static PerspectiveCamera perspectiveCamera;
    private static CameraInputController cameraController;

    private Camera() {
    }

    public static void setup() {

        perspectiveCamera = new PerspectiveCamera(90, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
        perspectiveCamera.position.set(7f, 7f, 7f);
        perspectiveCamera.lookAt(0, 0, 0);
        perspectiveCamera.near = 1f;
        perspectiveCamera.far = 300f;
        perspectiveCamera.update();

        cameraController = new CameraInputController(perspectiveCamera);
        Gdx.input.setInputProcessor(cameraController);
    }

}
