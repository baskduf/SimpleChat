# room/apps.py
from django.apps import AppConfig
from django.db import connection

class RoomConfig(AppConfig):
    name = 'room'

    def ready(self):
        # 서버 시작 시 실행할 코드
        self.clear_room_table()

    def clear_room_table(self):
        with connection.cursor() as cursor:
            # 모든 데이터 삭제 (테이블을 비우는 쿼리)
            cursor.execute("DELETE FROM room_room;")