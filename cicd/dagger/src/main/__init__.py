"""cicd"""

import dagger
from dagger import dag, function, object_type


@object_type
class Cicd:
    """cicd"""

    @function
    def test(self, src: dagger.Directory) -> str:
        """Test with pytest"""

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

    @function
    async def build_and_publish(
        self,
        src: dagger.Directory,
        registry_username: str,
        registry_password: dagger.Secret,
        secret_key: dagger.Secret,
        ynab_access_token: dagger.Secret,
        budget_id: dagger.Secret,
        category_id: dagger.Secret,
    ) -> dagger.Container:
        """Build and publish"""

        requirements_file = (
            dag.container()
            .from_("python:3.11")
            .with_mounted_directory("/app", src)
            .with_workdir("/app")
            .with_exec(["pip", "install", "poetry"])
            .with_exec(
                [
                    "poetry",
                    "export",
                    "-f",
                    "requirements.txt",
                    "--output",
                    "requirements.txt",
                    "--without-hashes",
                ]
            )
            .file("requirements.txt")
        )

        container_with_app = (
            dag.container()
            .from_("python:3.11")
            .with_env_variable("SECRET_KEY", await secret_key.plaintext())
            .with_env_variable("YNAB_ACCESS_TOKEN", await ynab_access_token.plaintext())
            .with_env_variable("BUDGET_ID", await budget_id.plaintext())
            .with_env_variable("CATEGORY_ID", await category_id.plaintext())
            .with_directory("/app", src)
            .with_workdir("/app")
            .with_file("requirements.txt", requirements_file)
            .with_exec(
                [
                    "pip",
                    "install",
                    "--no-cache-dir",
                    "--upgrade",
                    "-r",
                    "requirements.txt",
                ]
            )
            .with_default_args(["fastapi", "run", "howmuch/main.py", "--port", "80"])
        )

        await container_with_app.with_registry_auth(
            "ghcr.io/thedoublejo/howmuch:latest", registry_username, registry_password
        ).publish("ghcr.io/thedoublejo/howmuch:latest")

        return container_with_app
