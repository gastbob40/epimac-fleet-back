import os




def send_imac_status_notification(imac):
    print(os.environ.get('DISCORD_MAC_STATUS_WEBHOOK_URL'))
