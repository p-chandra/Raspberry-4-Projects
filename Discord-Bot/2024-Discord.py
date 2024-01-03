import discord

class MyClient(discord.Client):
    #on ready tells us the bot is live
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTE5MTg3ODIyNDcwNDE5MjUyMw.GKhc1k.VLIqSfnIgnEvR-pC4RdT_fyCjqj-blzeqiIiOw')