"""
ComfyUI-Nuvu Extension
Custom node entrypoint for ComfyUI.

This file is only loaded by ComfyUI when discovering custom nodes.
It imports the server module from the comfyui_nuvu package (installed via pip)
to register the API routes.
"""

import logging
import sys
import os

# Add this node's directory to sys.path so comfyui_nuvu package can be found
_node_dir = os.path.dirname(os.path.abspath(__file__))
if _node_dir not in sys.path:
    sys.path.insert(0, _node_dir)

WEB_DIRECTORY = "web"

# Define empty mappings so the module imports successfully and the web folder is registered.
# This follows the same pattern used by ComfyUI-Manager and ComfyUI-SubgraphSearch.
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Import server module and register routes
try:
    from comfyui_nuvu import nuvu_server
    from server import PromptServer
    nuvu_server.setup(PromptServer.instance.app)
    logging.info("Nuvu: Server routes registered successfully")
except Exception as err:
    logging.error("Nuvu: Failed to register server routes: %s", err)
    import traceback
    traceback.print_exc()

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

