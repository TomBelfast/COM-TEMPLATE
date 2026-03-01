/**
 * Nuvu Auth Bypass - loads before nuvu.js
 * Intercepts auth API calls and returns fake successful responses.
 */
(function () {
    const FAKE_USER_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJieXBhc3MtdXNlciIsImlzUHJlbWl1bSI6dHJ1ZSwiZXhwIjo5OTk5OTk5OTk5LCJpYXQiOjE3MDAwMDAwMDB9.bypass';
    const FAKE_API_TOKEN = FAKE_USER_TOKEN;

    // Auth_expires_at = "0" → parseInt = 0 → Date.now() > -60000 → TRUE → Be() gets called
    const NUVU_STORE = {
        'user_token': FAKE_USER_TOKEN,
        'api_token': FAKE_API_TOKEN,
        'auth_expires_at': '0',
        'nuvu_refresh_token': 'stub-refresh-token',
        'nuvu_user_id': 'bypass-user-123',
    };

    // --- localStorage patch ---
    const _getItem = Storage.prototype.getItem;
    const _setItem = Storage.prototype.setItem;
    const _removeItem = Storage.prototype.removeItem;

    Storage.prototype.getItem = function (key) {
        if (this === localStorage && Object.prototype.hasOwnProperty.call(NUVU_STORE, key)) {
            return NUVU_STORE[key];
        }
        return _getItem.call(this, key);
    };
    Storage.prototype.setItem = function (key, value) {
        if (this === localStorage && Object.prototype.hasOwnProperty.call(NUVU_STORE, key)) {
            return; // block nuvu from overwriting our tokens
        }
        _setItem.call(this, key, value);
    };
    Storage.prototype.removeItem = function (key) {
        if (this === localStorage && Object.prototype.hasOwnProperty.call(NUVU_STORE, key)) {
            return; // block nuvu from clearing our tokens
        }
        _removeItem.call(this, key);
    };

    // Initialize tokens in real localStorage
    for (const [k, v] of Object.entries(NUVU_STORE)) {
        _setItem.call(localStorage, k, v);
    }

    // --- fetch intercept ---
    const FAKE_AUTH_RESPONSE = {
        success: true,
        isLoggedIn: true,
        loggedIn: true,
        authenticated: true,
        user_token: FAKE_USER_TOKEN,
        api_token: FAKE_API_TOKEN,
        apiToken: FAKE_API_TOKEN,
        access_token: FAKE_USER_TOKEN,
        accessToken: FAKE_USER_TOKEN,
        userToken: FAKE_USER_TOKEN,
        token: FAKE_USER_TOKEN,
        isPremium: true,
        isSubscribed: true,
        plan: 'premium',
        session_id: 'bypass-session-123',
        expires_at: '2099-12-31T23:59:59Z',
        expiresAt: '2099-12-31T23:59:59Z',
        alive: true,
    };

    const _fetch = window.fetch.bind(window);
    window.fetch = function (url, options) {
        const urlStr = typeof url === 'string' ? url : (url instanceof Request ? url.url : String(url));

        // Intercept any auth-related external calls
        if (
            urlStr.includes('/api/auth/') ||
            urlStr.includes('nuvulabs.ai') ||
            urlStr.includes('/auth/token') ||
            urlStr.includes('/auth/refresh')
        ) {
            console.log('[BYPASS] Intercepted fetch:', urlStr);
            return Promise.resolve(new Response(JSON.stringify(FAKE_AUTH_RESPONSE), {
                status: 200,
                headers: { 'Content-Type': 'application/json' },
            }));
        }

        return _fetch(url, options);
    };

    console.log('[BYPASS] Auth bypass loaded. Tokens and fetch interceptor active.');
})();
