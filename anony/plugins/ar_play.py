# Arabic Play Commands
# Safe – No Loop – No Conflict

from pyrogram import filters, types
from anony import app
from anony.plugins.play import play_hndlr


@app.on_message(
    filters.group
    & filters.text
    & ~filters.command(["play", "vplay", "playforce", "vplayforce"])
)
async def arabic_play_handler(_, m: types.Message):
    if not m.text:
        return

    text = m.text.strip()

    # ===== تشغيل صوت =====
    if text.startswith("تشغيل"):
        query = text.replace("تشغيل", "", 1).strip()
        if not query:
            return

        # تزوير أمر /play داخليًا
        m.command = ["play"] + query.split()
        await play_hndlr(_, m)
        return

    # ===== تشغيل فيديو =====
    if text.startswith("فيديو"):
        query = text.replace("فيديو", "", 1).strip()
        if not query:
            return

        m.command = ["vplay"] + query.split()
        await play_hndlr(_, m)
        return
