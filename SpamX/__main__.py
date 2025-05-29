from pyrogram import idle
from SpamX.functions.clients import TheSpamX

async def main():
    await TheSpamX.startup()
    TheSpamX.logs.info("-- TURBO SPAM ROBOT HAS STATRTED SOR⚡--")
    await idle()
    await TheSpamX.SpamX.stop()
    await TheSpamX.stopAllClients()

if __name__ == "__main__":
    TheSpamX.run(main())
