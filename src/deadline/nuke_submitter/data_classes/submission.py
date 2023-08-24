# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import nuke
from nuke import Node

from ..assets import get_nuke_script_file


def _node_to_str(node: Node) -> str:
    return node.fullName() if node is not None and node != nuke.root() else ""


def _str_to_node(node_name: str) -> Node:
    return nuke.toNode(node_name) if node_name else nuke.root()


@dataclass
class RenderSubmitterUISettings:  # pylint: disable=too-many-instance-attributes
    """
    UI exposed settings for render submitter
    """

    name: str = field(
        default_factory=lambda: Path(get_nuke_script_file()).name if get_nuke_script_file() else ""
    )
    description: str = field(default="")
    override_installation_requirements: bool = field(default=True)
    installation_requirements: str = field(default="nuke-13 deadline_nuke")

    override_frame_range: bool = field(default=False)
    frame_list: str = field(default_factory=lambda: str(nuke.root().frameRange()))
    write_node_selection: Node = field(default_factory=lambda: nuke.root())
    view_selection: str = field(default="")
    is_proxy_mode: bool = field(default_factory=lambda: nuke.root().proxy())

    # settings with defaults
    submitter_name: str = field(default="Nuke")
    initial_status: str = field(default="READY")
    failed_tasks_limit: int = field(default=100)
    task_retry_limit: int = field(default=5)
    priority: int = field(default=50)

    input_filenames: list[str] = field(default_factory=list)
    input_directories: list[str] = field(default_factory=list)
    output_directories: list[str] = field(default_factory=list)

    # developer options
    include_adaptor_wheels: bool = False

    def to_render_submitter_settings(self) -> "RenderSubmitterSettings":
        return RenderSubmitterSettings(
            name=self.name,
            description=self.description,
            override_installation_requirements=self.override_installation_requirements,
            installation_requirements=self.installation_requirements,
            override_frame_range=self.override_frame_range,
            frame_list=self.frame_list,
            write_node_selection=_node_to_str(self.write_node_selection),
            view_selection=self.view_selection,
            is_proxy_mode=self.is_proxy_mode,
            initial_status=self.initial_status,
            failed_tasks_limit=self.failed_tasks_limit,
            task_retry_limit=self.task_retry_limit,
            priority=self.priority,
            input_filenames=self.input_filenames,
            input_directories=self.input_directories,
            output_directories=self.output_directories,
            include_adaptor_wheels=self.include_adaptor_wheels,
        )

    def apply_saved_settings(self, settings: RenderSubmitterSettings) -> None:
        self.name = settings.name
        self.description = settings.description
        self.override_installation_requirements = settings.override_installation_requirements
        self.installation_requirements = settings.installation_requirements
        self.override_frame_range = settings.override_frame_range
        self.frame_list = settings.frame_list
        self.write_node_selection = _str_to_node(settings.write_node_selection)
        self.view_selection = settings.view_selection
        self.is_proxy_mode = settings.is_proxy_mode
        self.initial_status = settings.initial_status
        self.failed_tasks_limit = settings.failed_tasks_limit
        self.task_retry_limit = settings.task_retry_limit
        self.priority = settings.priority
        self.input_filenames = settings.input_filenames
        self.input_directories = settings.input_directories
        self.output_directories = settings.output_directories
        self.include_adaptor_wheels = settings.include_adaptor_wheels


@dataclass
class RenderSubmitterSettings:  # pylint: disable=too-many-instance-attributes
    """
    Global settings for the Render Submitter
    """

    name: str
    description: str
    override_installation_requirements: bool
    installation_requirements: str

    override_frame_range: bool
    frame_list: str
    write_node_selection: str
    view_selection: str
    is_proxy_mode: bool

    initial_status: str
    failed_tasks_limit: int
    task_retry_limit: int
    priority: int

    # settings with defaults
    input_filenames: list[str] = field(default_factory=list)
    input_directories: list[str] = field(default_factory=list)
    output_directories: list[str] = field(default_factory=list)

    # developer options
    include_adaptor_wheels: bool = False
