import re
from enum import Enum

import requests


class ActionType(Enum):
    ADDED = 1
    MOVED = 2
    DELETED = 3
    SCORED = 4


class CollectionType(Enum):
    NONE = 0
    PLANNED = 1
    WATCHING = 2
    DROPPED = 3
    WATCHED = 4
    DELAYED = 5


class TitleType(Enum):
    ANIME = 1
    MANGA = 2


class ShikiLog(object):
    def __init__(self, data: dict, username: str):
        super().__init__()
        self.id: int = data['id']
        self.username = username
        self.data = data
        self.description: str = re.sub('</?\\w+>', '', data['description'])
        self.title: str = data['target']['name']
        self.russian_title: str = data['target']['russian']

    def get_message(self):
        message = f"{self.username}: {self.description}:"
        message += f" {self.russian_title} / {self.title}"
        return message


class ShikiClient(object):
    def __init__(self):
        super().__init__()
        self._cached_ids: dict[str, list[int]] = {}
        self._headers = {
            'User-Agent': 'SiliciumBotChan/0.1.0 Discord' +
                          ' bot for me and my friends'
        }

    # region public

    def retrieve_user_logs(self, username: str) -> list[ShikiLog]:
        url = f"https://shikimori.one/api/users/{username}/history?limit=5"
        res = requests.get(url=url, headers=self._headers)
        logs = {d['id']: ShikiLog(d, username) for d in res.json()}
        if username in self._cached_ids:
            for cached_id in self._cached_ids[username]:
                if cached_id in logs:
                    del logs[cached_id]
        else:
            self._cached_ids[username] = []
        self._cached_ids[username] += logs.keys()
        return [log for log_id, log in logs.items()]

    # endregion public