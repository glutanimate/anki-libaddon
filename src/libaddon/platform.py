# -*- coding: utf-8 -*-

# Libaddon for Anki
#
# Copyright (C) 2018-2019  Aristotelis P. <https//glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Provides information on Anki version and platform
"""

import os

from aqt import mw
from anki import version as anki_version
from anki.utils import isMac, isWin

from ._vendor.typing import Optional

from .utils import ensureExists

if isMac:
    PLATFORM = "mac"
elif isWin:
    PLATFORM = "win"
else:
    PLATFORM = "lin"

name_components = __name__.split(".")

MODULE_ADDON = name_components[0]
MODULE_LIBADDON = name_components[1]

PATH_ADDONS = mw.pm.addonFolder()
PATH_THIS_ADDON = os.path.join(PATH_ADDONS, MODULE_ADDON)

JSPY_BRIDGE = "pycmd"


def schedVer() -> Optional[int]:
    if not mw.col:  # collection not loaded
        return None
    return mw.col.schedVer()


def pathUserFiles() -> str:
    user_files = os.path.join(PATH_THIS_ADDON, "user_files")
    return ensureExists(user_files)


def pathMediaFiles() -> Optional[str]:
    return mw.col.media.dir()


def checkAnkiVersion(lower: str, upper: Optional[str]=None) -> bool:
    """Check whether anki version is in specified range

    By default the upper boundary is set to infinite

    Arguments:
        lower {str} -- minimum version (inclusive)

    Keyword Arguments:
        upper {str} -- maximum version (exclusive) (default: {None})

    Returns:
        bool -- Whether anki version is in specified range
    """
    return checkVersion(anki_version, lower, upper=upper)


def checkQtVersion(lower: str, upper: Optional[str]=None) -> bool:
    """Check whether Qt version is in specified range

    By default the upper boundary is set to infinite

    Arguments:
        lower {str} -- minimum version (inclusive)

    Keyword Arguments:
        upper {str} -- maximum version (exclusive) (default: {None})

    Returns:
        bool -- Whether Qt version is in specified range
    """
    from aqt.qt import QT_VERSION_STR
    return checkVersion(QT_VERSION_STR, lower, upper=upper)


def checkVersion(current: str, lower: str, upper: Optional[str]=None) -> bool:
    """Generic version checker

    Checks whether specified version is in specified range

    Arguments:
        current {str} -- current version
        lower {str} -- minimum version (inclusive)

    Keyword Arguments:
        upper {str} -- maximum version (exclusive) (default: {None})

    Returns:
        bool -- Whether current version is in specified range
    """
    from ._vendor.packaging import version

    if upper is not None:
        ankiv_parsed = version.parse(current)
        return (ankiv_parsed >= version.parse(lower) and
                ankiv_parsed < version.parse(upper))

    return version.parse(current) >= version.parse(lower)
