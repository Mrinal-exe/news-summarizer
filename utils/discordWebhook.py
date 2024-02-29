from discord_webhook import DiscordWebhook, DiscordEmbed

def send_discord_notification(title, summary, link):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1212452418193981450/dMDAfUpBYWr4TfBzCMkztVW5qbm87hn3oTTD4D-H9mWT5RX9H-wgaeh9Y0KjMMsdhsrj", rate_limit_retry=True)

    embed = DiscordEmbed(description=summary, color=0x42f468)
    embed.set_author(name=title, url=link)
    webhook.add_embed(embed)

    response = webhook.execute()



    
