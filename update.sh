#!/bin/bash
set -e -o pipefail -u

PKG=runc
REPO=https://github.com/opencontainers/runc

git pull --ff-only > /dev/null

LATEST_VER=$(git ls-remote $REPO \
	| grep -o 'refs/tags/.*[0-9]$' \
	| sed 's|.*/v||' \
	| sed '/-rc/d' \
	| sort --version-sort \
	| tail -1)

if [[ -z "$LATEST_VER" ]]; then
	echo "Unable to find latest version upstream."
	exit 1
fi

CURRENT_VER=$(grep "^Version" $PKG.spec | awk '{ print $3 }')

if [[ "$LATEST_VER" = "$CURRENT_VER" ]]; then
	echo "Already up to date at version $CURRENT_VER."
	exit
fi

# The tarball and sig are unversioned, so remove them in order for autospec to
# download fresh files for the latest release.
rm -f ./runc.tar.xz
rm -f ./runc.tar.xz.asc

if ! make autospec URL="$REPO/releases/download/v$LATEST_VER/runc.tar.xz"; then
	echo "Autospec failed for version $LATEST_VER."
	exit 3
fi

if [[ -z "$NO_KOJI" ]] && ! make koji; then
	echo "Koji submission failed."
	exit 4
fi
