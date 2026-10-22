# -*- coding: utf-8 -*-
"""
    Token Helper Route - Korean Fix
    Shows step-by-step guide to extract auth-token from Twitch website.
    Also provides manual token input dialog.

    SPDX-License-Identifier: GPL-3.0-only
"""

import xbmc
import xbmcgui
import xbmcaddon

from ..addon.common import kodi
from ..addon.strings import STRINGS


def token_helper():
    """Show step-by-step token extraction guide and accept manual token input."""
    translations = kodi.Translations(STRINGS)
    i18n = translations.i18n

    # Show the instruction dialog
    instructions = i18n('30511')
    dialog = xbmcgui.Dialog()
    dialog.textviewer(i18n('30510'), instructions)

    # Now ask if user wants to input token now
    if not dialog.yesno(i18n('30510'), "지금 토큰을 입력하시겠습니까?\nWould you like to enter the token now?"):
        return

    # Get token from user
    keyboard = xbmc.Keyboard('', i18n('30502'))
    keyboard.doModal()
    if not keyboard.isConfirmed():
        return

    token = keyboard.getText().strip()
    if not token:
        dialog.ok(i18n('30510'), i18n('30513'))
        return

    # Clean token - remove "oauth:" prefix if present
    if token.lower().startswith('oauth:'):
        token = token[6:]

    # Save token to settings
    kodi.set_setting('manual_oauth_token', token)

    # Also set it as the helix token (legacy fallback)
    kodi.set_setting('oauth_token_helix', token)

    # Show success
    dialog.ok(i18n('30510'), i18n('30512'))

    # Optionally open settings to verify
    if dialog.yesno(i18n('30510'), "설정을 열어 확인하시겠습니까?\nOpen settings to verify?"):
        kodi.show_settings()


def apply_manual_token():
    """Apply the manually entered token immediately."""
    translations = kodi.Translations(STRINGS)
    i18n = translations.i18n

    dialog = xbmcgui.Dialog()

    # Get token from settings
    token = kodi.get_setting('manual_oauth_token') or ''
    token = token.strip()

    if not token:
        # Fallback to oauth_token_helix setting
        token = (kodi.get_setting('oauth_token_helix') or '').strip()

    if not token:
        dialog.ok(i18n('30510'), i18n('30513'))
        kodi.show_settings()
        return

    # Clean token
    if token.lower().startswith('oauth:'):
        token = token[6:]

    # Validate token by calling Twitch API
    try:
        import requests
        r = requests.get(
            'https://id.twitch.tv/oauth2/validate',
            headers={'Authorization': f'OAuth {token}'},
            timeout=10
        )
        if r.status_code == 200:
            data = r.json()
            login = data.get('login', 'unknown')
            # Save to multiple places for maximum compatibility
            kodi.set_setting('oauth_token_helix', token)
            kodi.set_setting('manual_oauth_token', token)

            # Also store in oauth_tokens.json for the device flow fallback
            try:
                from ..addon.utils import store_oauth_tokens
                store_oauth_tokens(token, '', 60 * 60 * 24 * 60)  # 60 days
            except Exception:
                pass  # Not critical if this fails

            dialog.ok(i18n('30510'), i18n('30515') % login)
        else:
            dialog.ok(i18n('30510'), i18n('30514'))
            kodi.show_settings()
    except Exception as e:
        # If validation fails (network issue), still apply the token
        kodi.set_setting('oauth_token_helix', token)
        kodi.set_setting('manual_oauth_token', token)
        try:
            from ..addon.utils import store_oauth_tokens
            store_oauth_tokens(token, '', 60 * 60 * 24 * 60)
        except Exception:
            pass
        dialog.ok(i18n('30510'), i18n('30512') + "\n\n(검증 건너뜀 - 네트워크 오류)")
