# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

"""
DO NOT CHANGE THIS FILE's NAME

Nuke loads this "init.py" or "menu.py" when looking in its plugin folder.

You can inform nuke to look in additional locations by setting via the
NUKE_PATH environment variable.
"""

try:
    import nuke
    import os

    from deadline.nuke_submitter import (
        show_nuke_render_submitter_noargs,
        run_nuke_render_submitter_job_bundle_output_test,
    )

    menu_bar = nuke.menu("Nuke")
    thinkbox_menu = menu_bar.addMenu("&Thinkbox")
    thinkbox_menu.addCommand("Submit Nuke To Deadline", show_nuke_render_submitter_noargs, "")
    # Set the environment variable DEADLINE_NUKE_ENABLE_DEVELOPER_OPTIONS to "true" to get this menu.
    if os.environ.get("DEADLINE_NUKE_ENABLE_DEVELOPER_OPTIONS", "").upper() == "TRUE":
        thinkbox_menu.addCommand(
            "Run Nuke Submitter Job Bundle Output Tests...",
            run_nuke_render_submitter_job_bundle_output_test,
            "",
        )

except BaseException:
    import sys
    import traceback

    print("Failed to load deadline.nuke_submitter. Reason:", file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
