package io.skaihen;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.VertexAttributes.Usage;
import com.badlogic.gdx.graphics.g3d.Environment;
import com.badlogic.gdx.graphics.g3d.Material;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.ModelBatch;
import com.badlogic.gdx.graphics.g3d.ModelInstance;
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute;
import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight;
import com.badlogic.gdx.graphics.g3d.utils.CameraInputController;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.utils.Array;

import io.skaihen.Player.Camera;

public class Garoa extends ApplicationAdapter {
	private Environment environment;

	private PerspectiveCamera perspectiveCamera;
	private CameraInputController cameraController;

	private Model model;
	private ModelBatch modelBatch;

	private final Array<ModelInstance> instances = new Array<>();

	@Override
	public void create() {
		environment = new Environment();
		environment.set(new ColorAttribute(ColorAttribute.AmbientLight, 0.4f, 0.4f, 0.4f, 1f));
		environment.add(new DirectionalLight().set(0.8f, 0.8f, 0.8f, -1f, -0.8f, -0.2f));

		Camera.setup();

		ModelBuilder modelBuilder = new ModelBuilder();
		model = modelBuilder.createBox(5f, 5f, 5f,
				new Material(new Texture(Gdx.files.internal("plep.png"))),
				Usage.Position | Usage.Normal);

		for (int x = -10; x <= 10; x += 5) {
			for (int z = -10; z <= 10; z += 5) {
				instances.add(new ModelInstance(model, x, 0, z));
			}
		}

		modelBatch = new ModelBatch();
	}

	@Override
	public void render() {
		cameraController.update();

		Gdx.gl.glViewport(0, 0, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT | GL20.GL_DEPTH_BUFFER_BIT);

		modelBatch.begin(perspectiveCamera);
		for (ModelInstance instance : instances)
			modelBatch.render(instance, environment);
		modelBatch.end();

	}

	@Override
	public void dispose() {
		model.dispose();
		modelBatch.dispose();
		instances.clear();
	}
}
