"""cicd"""

import dagger
from dagger import dag, function, object_type


@object_type
class Cicd:
    """cicd"""

    @function
    def test_and_publish(self, src: dagger.Directory) -> str:
        """main"""

        output = (
            dag.container()
            .from_("python:3.11-slim-bullseye")
            .with_mounted_directory("/mnt", src)
            .with_workdir("/mnt")
            .with_exec(["pip", "install", "poetry"])
            .with_exec(["poetry", "install"])
            .with_exec(["poetry", "run", "pytest"])
            .stdout()
        )

        return output

        # build python package
        # build_dir = (
        #     await runner.with_exec(
        #         ["python3", "-m", "pip", "install", "--upgrade", "build"]
        #     )
        #     .with_exec(["python3", "-m", "build"])
        #     .directory("dist")
        # )

        # await build_dir.export("dist")

        # build and publish image
        # image_ref = "marvelousmlops/dagger_example:latest"
        # secret = client.set_secret(
        #     name="dockerhub_secret", plaintext=os.environ["DOCKERHUB_TOKEN"]
        # )
        # build = (
        #     src.with_directory("/tmp/dist", client.host().directory("dist"))
        #     .docker_build(dockerfile="Dockerfile_dagger")
        #     .with_registry_auth(
        #         address=f"https://docker.io/{image_ref}",
        #         secret=secret,
        #         username=os.environ["DOCKERHUB_USER"],
        #     )
        # )
        # await build.publish(f"{image_ref}")

        # print(f"Published image to: {image_ref}")
