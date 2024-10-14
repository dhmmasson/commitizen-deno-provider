from __future__ import annotations

import json
from pathlib import Path
from typing import Any, ClassVar

from commitizen.providers import VersionProvider


class DenoProvider(VersionProvider):
    """
    deno deno.json and package-lock.json version management
    """

    indent: ClassVar[int] = 2
    package_filename = "deno.json"
    jsr_filename = "jsr.json"

    @property
    def package_file(self) -> Path:
        return Path() / self.package_filename

    @property
    def jsr_file(self) -> Path:
        return Path() / self.jsr_filename

    def get_version(self) -> str:
        """
        Get the current version from deno.json
        """
        package_document = json.loads(self.package_file.read_text())
        return self.get_package_version(package_document)

    def set_version(self, version: str) -> None:
        package_document = self.set_package_version(
            json.loads(self.package_file.read_text()), version
        )
        self.package_file.write_text(
            json.dumps(package_document, indent=self.indent) + "\n"
        )
        if self.jsr_file.exists():
            jsr_document = self.set_jsr_version(
                json.loads(self.jsr_file.read_text()), version
            )
            self.jsr_file.write_text(
                json.dumps(jsr_document, indent=self.indent) + "\n"
            )

    def get_package_version(self, document: dict[str, Any]) -> str:
        return document["version"]  # type: ignore

    def set_package_version(
        self, document: dict[str, Any], version: str
    ) -> dict[str, Any]:
        document["version"] = version
        return document

    def set_jsr_version(
        self, document: dict[str, Any], version: str
    ) -> dict[str, Any]:
        document["version"] = version
        return document
