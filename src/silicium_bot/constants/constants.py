import os


def get_log_print_time(var_name):
    var: str = os.getenv(var_name)
    if var is not None:
        return var.strip().lower() == "true"
    return True


class Constants(object):
    shiki_url = 'https://shikimori.one'
    shiki_api = f"{shiki_url}/api"
    version = '1.7.0'
    anek_api = 'https://baneks.ru/random'
    github = 'https://github.com/thisUsernameIsAlredyTaken/ShikimoriDiscordBot'
    deploy = 'https://dashboard.heroku.com/apps/silicium-bot/resources'
    my_discord_id = int(os.getenv("MY_USER_ID") or "-1")
    discord_token = os.getenv("DISCORD_BOT_TOKEN")
    database_url = os.getenv("DATABASE_URL")
    log_print_time = get_log_print_time("LOG_PRINT_TIME")
    vk_login = os.getenv('LOGIN')
    vk_password = os.getenv('PASSWORD')
    youtube_token = os.getenv('YTTOKEN')
    balaboba_api = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    request_headers = {
        'User-Agent': f'SiliciumBotChan/{version} Discord' +
                      ' bot for me and my friends'
    }
    readycheck_embed_title = '============ READY CHECK ============'
    accept_emoji = '✅'
    decline_emoji = '❌'
    undecide_emoji = '⌚'