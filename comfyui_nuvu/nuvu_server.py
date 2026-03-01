"""
Nuvu Server - stub implementation
Provides all required API endpoints for nuvu.js frontend.
Auth is always bypassed - user is always logged in.
"""

import logging
from aiohttp import web

logger = logging.getLogger("nuvu_server")

OK = {"success": True}
LOGGED_IN = {
    "success": True,
    "isLoggedIn": True,
    "loggedIn": True,
    "authenticated": True,
    "user_token": "stub-user-token-abc123",
    "api_token": "stub-api-token-abc123",
    "apiToken": "stub-api-token-abc123",
    "access_token": "stub-access-token-abc123",
}


def setup(app):
    app.router.add_get("/nuvu/config", handle_config)
    app.router.add_get("/nuvu/auth", handle_auth)
    app.router.add_post("/nuvu/auth", handle_auth)
    app.router.add_post("/nuvu/auth/floating-session", handle_floating_session)
    app.router.add_post("/nuvu/auth/floating-heartbeat", handle_floating_heartbeat)
    app.router.add_get("/nuvu/auth/subscription-check", handle_subscription)
    app.router.add_get("/nuvu/device/identity", handle_device_identity)
    app.router.add_post("/nuvu/device/register", handle_ok)
    app.router.add_get("/nuvu/device/registrations", handle_empty_list)
    app.router.add_get("/nuvu/workflows-metadata", handle_empty_list)
    app.router.add_get("/nuvu/models-metadata", handle_empty_list)
    app.router.add_get("/nuvu/models", handle_empty_list)
    app.router.add_post("/nuvu/models/check-existing", handle_empty_list)
    app.router.add_get("/nuvu/custom-nodes", handle_empty_list)
    app.router.add_post("/nuvu/custom-nodes/check-installed", handle_ok)
    app.router.add_get("/nuvu/check-nuvu-updates", handle_no_updates)
    app.router.add_get("/nuvu/check-versions", handle_no_updates)
    app.router.add_get("/nuvu/node-mappings", handle_empty_dict)
    app.router.add_get("/nuvu/pip-list", handle_empty_list)
    app.router.add_post("/nuvu/pip-install", handle_ok)
    app.router.add_get("/nuvu/queue/status", handle_queue_status)
    app.router.add_post("/nuvu/queue/clear-error", handle_ok)
    app.router.add_post("/nuvu/queue/clear-summary", handle_ok)
    app.router.add_post("/nuvu/queue/reset", handle_ok)
    app.router.add_post("/nuvu/install/workflow", handle_ok)
    app.router.add_post("/nuvu/install/models", handle_ok)
    app.router.add_post("/nuvu/install/custom-model", handle_ok)
    app.router.add_post("/nuvu/resolve-filename", handle_ok)
    app.router.add_post("/nuvu/execute/script", handle_ok)
    app.router.add_post("/nuvu/execute/cancel", handle_ok)
    app.router.add_post("/nuvu/restart", handle_ok)
    app.router.add_post("/nuvu/update-comfyui", handle_ok)
    app.router.add_post("/nuvu/update-nuvu", handle_ok)
    app.router.add_get("/nuvu/user-config", handle_user_config)
    app.router.add_post("/nuvu/user-config", handle_ok)
    app.router.add_get("/nuvu/work", handle_empty_list)
    app.router.add_get("/nuvu/workflow-changelog", handle_empty_list)
    app.router.add_post("/nuvu/telemetry/login", handle_ok)
    app.router.add_post("/nuvu/support", handle_ok)
    app.router.add_post("/nuvu/support/upload-url", handle_ok)
    app.router.add_get("/nuvu/affiliates/me", handle_ok)
    app.router.add_post("/nuvu/contact", handle_ok)
    logger.info("Nuvu stub server routes registered")


async def handle_config(request):
    return web.json_response({
        "success": True,
        "isLoggedIn": True,
        "loggedIn": True,
        "authenticated": True,
        "isPremium": True,
        "version": "1.0.73",
    })


async def handle_auth(request):
    return web.json_response(LOGGED_IN)


async def handle_subscription(request):
    return web.json_response({
        "success": True,
        "isSubscribed": True,
        "isPremium": True,
        "plan": "premium",
    })


async def handle_device_identity(request):
    return web.json_response({
        "success": True,
        "deviceId": "simplepod-device",
        "identity": "simplepod-device",
    })


async def handle_user_config(request):
    return web.json_response({
        "success": True,
        "config": {},
    })


async def handle_queue_status(request):
    return web.json_response({
        "success": True,
        "queue": [],
        "status": "idle",
    })


async def handle_no_updates(request):
    return web.json_response({
        "success": True,
        "hasUpdate": False,
        "upToDate": True,
    })


async def handle_empty_list(request):
    return web.json_response([])


async def handle_empty_dict(request):
    return web.json_response({})


async def handle_floating_session(request):
    return web.json_response({
        "success": True,
        "token": "stub-floating-token-abc123",
        "session_id": "stub-session-id-abc123",
        "expires_at": "2099-12-31T23:59:59Z",
        "expiresAt": "2099-12-31T23:59:59Z",
    })


async def handle_floating_heartbeat(request):
    return web.json_response({
        "success": True,
        "alive": True,
    })


async def handle_ok(request):
    return web.json_response(OK)
