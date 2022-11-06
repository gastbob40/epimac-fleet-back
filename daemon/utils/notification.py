import os

from discord_webhook import DiscordWebhook, DiscordEmbed

from daemon.models import IMacModel


def __imac_status_to_color(imac: IMacModel) -> str:
    if imac.status == IMacModel.MacStatus.UNAVAILABLE:
        return 'e96d76'
    elif imac.status == IMacModel.MacStatus.AVAILABLE:
        return '18be94'
    elif imac.status == IMacModel.MacStatus.IN_USE:
        return 'afd5f0'

    raise ValueError('Invalid status.')


def send_imac_status_notification(imac: IMacModel):
    embed = DiscordEmbed(
        title=f'{imac.label} status changed',
        description=f'{imac.label} is now {imac.status}',
        color=__imac_status_to_color(imac)
    )

    webhook = DiscordWebhook(
        url=os.environ.get('DISCORD_MAC_STATUS_WEBHOOK_URL'),
        username="EpiMac Bot",
        avatar_url="https://cdn.discordapp.com/icons/501407992818958377/a_8d192eb9c2143f2914124345b28bbc1f.webp?size=1024",)

    webhook.add_embed(embed)
    webhook.execute()
