
""" set permissions to users """

import os

from pyrogram import ChatPermissions, Filters, Message

from nana import app, Command
from nana.helpers.admincheck import admin_check

__MODULE__ = "Admin"
__HELP__ = """
Module for Group Admins

──「 **Locks/Unlocks** 」──
-> `lock`
locks permission in the group

-> `unlock`
unlocks permission in the group

Supported Locks/Unlocks:
`msg` | `media` | `stickers` | `animations` | `games` | `inlinebots` |
`webprev` | `polls` | `info`  | `invite` | `pin` | `all`

-> `vlock`
view group permissions
"""


@app.on_message(Filters.me & Filters.command(["lock"], Command))
async def lock_permission(client, message):
    """locks group permission"""
    cmd = message.command

    is_admin = await admin_check(message)
    if not is_admin:
        await message.delete()
        return

    msg = ""
    media = ""
    stickers = ""
    animations = ""
    games = ""
    inlinebots = ""
    webprev = ""
    polls = ""
    info = ""
    invite = ""
    pin = ""
    perm = ""

    lock_type = " ".join(cmd[1:])
    chat_id = message.chat.id

    if not lock_type:
        await message.edit("`can't lock the void`")
        return

    get_perm = await client.get_chat(chat_id)

    msg = get_perm.permissions.can_send_messages
    media = get_perm.permissions.can_send_media_messages
    stickers = get_perm.permissions.can_send_stickers
    animations = get_perm.permissions.can_send_animations
    games = get_perm.permissions.can_send_games
    inlinebots = get_perm.permissions.can_use_inline_bots
    webprev = get_perm.permissions.can_add_web_page_previews
    polls = get_perm.permissions.can_send_polls
    info = get_perm.permissions.can_change_info
    invite = get_perm.permissions.can_invite_users
    pin = get_perm.permissions.can_pin_messages

    if lock_type == "all":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.edit("`Locked all permission from this Chat!`")

        except Exception as e:
            await message.edit(
                text="`permission denied`\n\n"
                f"**ERROR:** `{e}`")

        return

    if lock_type == "msg":
        msg = False
        perm = "messages"

    elif lock_type == "media":
        media = False
        perm = "audios, documents, photos, videos, video notes, voice notes"

    elif lock_type == "stickers":
        stickers = False
        perm = "stickers"

    elif lock_type == "animations":
        animations = False
        perm = "animations"

    elif lock_type == "games":
        games = False
        perm = "games"

    elif lock_type == "inlinebots":
        inlinebots = False
        perm = "inline bots"

    elif lock_type == "webprev":
        webprev = False
        perm = "web page previews"

    elif lock_type == "polls":
        polls = False
        perm = "polls"

    elif lock_type == "info":
        info = False
        perm = "info"

    elif lock_type == "invite":
        invite = False
        perm = "invite"

    elif lock_type == "pin":
        pin = False
        perm = "pin"

    else:
        await message.edit(text=r"`Invalid Lock Type!`")
        return

    try:
        await client.set_chat_permissions(chat_id,
                                          ChatPermissions(can_send_messages=msg,
                                                          can_send_media_messages=media,
                                                          can_send_stickers=stickers,
                                                          can_send_animations=animations,
                                                          can_send_games=games,
                                                          can_use_inline_bots=inlinebots,
                                                          can_add_web_page_previews=webprev,
                                                          can_send_polls=polls,
                                                          can_change_info=info,
                                                          can_invite_users=invite,
                                                          can_pin_messages=pin))

        await message.edit(text=f"`Locked {perm} for this chat!`")

    except Exception as e:
        await message.edit(
            text=r"`permission denied`\n\n"
            f"**ERROR:** `{e}`")



@app.on_message(Filters.me & Filters.command(["unlock"], Command))
async def unlock_permission(client, message):
    """unlocks group permission"""
    cmd = message.command
    is_admin = await admin_check(message)
    if not is_admin:
        await message.delete()
        return

    umsg = ""
    umedia = ""
    ustickers = ""
    uanimations = ""
    ugames = ""
    uinlinebots = ""
    uwebprev = ""
    upolls = ""
    uinfo = ""
    uinvite = ""
    upin = ""
    uperm = ""

    unlock_type = " ".join(cmd[1:])
    chat_id = message.chat.id

    if not unlock_type:
        await message.edit("`can't lock the void`")
        return

    get_uperm = await client.get_chat(chat_id)

    umsg = get_uperm.permissions.can_send_messages
    umedia = get_uperm.permissions.can_send_media_messages
    ustickers = get_uperm.permissions.can_send_stickers
    uanimations = get_uperm.permissions.can_send_animations
    ugames = get_uperm.permissions.can_send_games
    uinlinebots = get_uperm.permissions.can_use_inline_bots
    uwebprev = get_uperm.permissions.can_add_web_page_previews
    upolls = get_uperm.permissions.can_send_polls
    uinfo = get_uperm.permissions.can_change_info
    uinvite = get_uperm.permissions.can_invite_users
    upin = get_uperm.permissions.can_pin_messages

    if unlock_type == "all":
        try:
            await client.set_chat_permissions(chat_id,
                                              ChatPermissions(can_send_messages=True,
                                                              can_send_media_messages=True,
                                                              can_send_stickers=True,
                                                              can_send_animations=True,
                                                              can_send_games=True,
                                                              can_use_inline_bots=True,
                                                              can_send_polls=True,
                                                              can_change_info=True,
                                                              can_invite_users=True,
                                                              can_pin_messages=True,
                                                              can_add_web_page_previews=True))

            await message.edit("`Unlocked all permission from this Chat!`")

        except Exception as e:
            await message.edit(
                text=r"`permission denied`\n\n"
                f"**ERROR:** `{e}`")
        return

    if unlock_type == "msg":
        umsg = True
        uperm = "messages"

    elif unlock_type == "media":
        umedia = True
        uperm = "audios, documents, photos, videos, video notes, voice notes"

    elif unlock_type == "stickers":
        ustickers = True
        uperm = "stickers"

    elif unlock_type == "animations":
        uanimations = True
        uperm = "animations"

    elif unlock_type == "games":
        ugames = True
        uperm = "games"

    elif unlock_type == "inlinebots":
        uinlinebots = True
        uperm = "inline bots"

    elif unlock_type == "webprev":
        uwebprev = True
        uperm = "web page previews"

    elif unlock_type == "polls":
        upolls = True
        uperm = "polls"

    elif unlock_type == "info":
        uinfo = True
        uperm = "info"

    elif unlock_type == "invite":
        uinvite = True
        uperm = "invite"

    elif unlock_type == "pin":
        upin = True
        uperm = "pin"

    else:
        await message.edit("`Invalid Unlock Type!`")
        return

    try:
        await client.set_chat_permissions(chat_id,
                                          ChatPermissions(can_send_messages=umsg,
                                                          can_send_media_messages=umedia,
                                                          can_send_stickers=ustickers,
                                                          can_send_animations=uanimations,
                                                          can_send_games=ugames,
                                                          can_use_inline_bots=uinlinebots,
                                                          can_add_web_page_previews=uwebprev,
                                                          can_send_polls=upolls,
                                                          can_change_info=uinfo,
                                                          can_invite_users=uinvite,
                                                          can_pin_messages=upin))

        await message.edit("`Unlocked {uperm} for this chat!`")

    except Exception as e:
        await message.edit(
            text="`permission denied`\n\n"
            f"**ERROR:** `{e}`")


@app.on_message(Filters.me & Filters.command(["vlock"], Command))
async def view_perm(client, message):
    """view group permission"""
    is_admin = await admin_check(message)
    if not is_admin:
        await message.delete()
        return

    v_perm = ""
    vmsg = ""
    vmedia = ""
    vstickers = ""
    vanimations = ""
    vgames = ""
    vinlinebots = ""
    vwebprev = ""
    vpolls = ""
    vinfo = ""
    vinvite = ""
    vpin = ""

    v_perm = await client.get_chat(message.chat.id)

    def convert_to_emoji(val: bool):
        if val is True:
            return "<code>True</code>"
        return "<code>False</code>"

    vmsg = convert_to_emoji(v_perm.permissions.can_send_messages)
    vmedia = convert_to_emoji(v_perm.permissions.can_send_media_messages)
    vstickers = convert_to_emoji(v_perm.permissions.can_send_stickers)
    vanimations = convert_to_emoji(v_perm.permissions.can_send_animations)
    vgames = convert_to_emoji(v_perm.permissions.can_send_games)
    vinlinebots = convert_to_emoji(v_perm.permissions.can_use_inline_bots)
    vwebprev = convert_to_emoji(v_perm.permissions.can_add_web_page_previews)
    vpolls = convert_to_emoji(v_perm.permissions.can_send_polls)
    vinfo = convert_to_emoji(v_perm.permissions.can_change_info)
    vinvite = convert_to_emoji(v_perm.permissions.can_invite_users)
    vpin = convert_to_emoji(v_perm.permissions.can_pin_messages)

    if v_perm is not None:
        try:
            permission_view_str = ""

            permission_view_str += "<b>Chat permissions:</b>\n"
            permission_view_str += f"<b>Send Messages:</b> {vmsg}\n"
            permission_view_str += f"<b>Send Media:</b> {vmedia}\n"
            permission_view_str += f"<b>Send Stickers:</b> {vstickers}\n"
            permission_view_str += f"<b>Send Animations:</b> {vanimations}\n"
            permission_view_str += f"<b>Can Play Games:</b> {vgames}\n"
            permission_view_str += f"<b>Can Use Inline Bots:</b> {vinlinebots}\n"
            permission_view_str += f"<b>Webpage Preview:</b> {vwebprev}\n"
            permission_view_str += f"<b>Send Polls:</b> {vpolls}\n"
            permission_view_str += f"<b>Change Info:</b> {vinfo}\n"
            permission_view_str += f"<b>Invite Users:</b> {vinvite}\n"
            permission_view_str += f"<b>Pin Messages:</b> {vpin}\n"

            await message.edit(permission_view_str)

        except Exception as e:
            await message.edit(
                text="`Something went wrong!`\n\n"
                f"**ERROR:** `{e}`")