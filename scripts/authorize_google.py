"""
Run this locally ONCE PER ACCOUNT to obtain a Google OAuth refresh token.

The Drive folder and the YouTube channel can belong to two different
Google accounts. Run this script twice with --target drive / --target
youtube, logging in with the matching account's browser session each time
(use an incognito/private window, or log out first, to switch accounts).

Prerequisites:
  - A Google Cloud project with the "Google Drive API" and
    "YouTube Data API v3" enabled.
  - An OAuth 2.0 Client ID of type "Desktop app" created for that project
    (the SAME client_id/client_secret is reused for both accounts).
  - Both Google accounts added as test users on the OAuth consent screen
    (required while the app is in "Testing" publishing status).

Usage:
    python scripts/authorize_google.py \
        --client-id YOUR_CLIENT_ID \
        --client-secret YOUR_CLIENT_SECRET \
        --target drive

    python scripts/authorize_google.py \
        --client-id YOUR_CLIENT_ID \
        --client-secret YOUR_CLIENT_SECRET \
        --target youtube

A browser window will open for you to sign in and grant access. Afterward
the script prints the values to save as GitHub Actions secrets.
"""

import argparse

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES_BY_TARGET = {
    "drive": ["https://www.googleapis.com/auth/drive.readonly"],
    "youtube": ["https://www.googleapis.com/auth/youtube.upload"],
}
SECRET_NAME_BY_TARGET = {
    "drive": "DRIVE_REFRESH_TOKEN",
    "youtube": "YOUTUBE_REFRESH_TOKEN",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--client-id", required=True)
    parser.add_argument("--client-secret", required=True)
    parser.add_argument(
        "--target",
        choices=["drive", "youtube"],
        required=True,
        help="Which account you're about to log in with: the Drive folder owner or the YouTube channel owner.",
    )
    args = parser.parse_args()

    client_config = {
        "installed": {
            "client_id": args.client_id,
            "client_secret": args.client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost"],
        }
    }
    flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES_BY_TARGET[args.target])
    creds = flow.run_local_server(port=0)

    secret_name = SECRET_NAME_BY_TARGET[args.target]
    print(f"\n=== Save these as GitHub Actions secrets ({args.target} account) ===")
    print(f"GOOGLE_CLIENT_ID={args.client_id}")
    print(f"GOOGLE_CLIENT_SECRET={args.client_secret}")
    print(f"{secret_name}={creds.refresh_token}")


if __name__ == "__main__":
    main()
