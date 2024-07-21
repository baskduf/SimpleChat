from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection


class Command(BaseCommand):
    help = 'Drops and recreates the Room table'

    def handle(self, *args, **kwargs):
        table_name = 'room_room'

        with connection.cursor() as cursor:
            # 외래 키 제약 조건 비활성화 (SQLite에서만 적용됨)
            cursor.execute('PRAGMA foreign_keys = OFF;')

            try:
                # 테이블 존재 여부 확인
                cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{table_name}";')
                if cursor.fetchone():
                    # 테이블 드롭
                    cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
                    self.stdout.write(self.style.SUCCESS(f'Table {table_name} dropped.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Table {table_name} does not exist.'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error dropping table: {e}'))

            # 외래 키 제약 조건 활성화 (SQLite에서만 적용됨)
            cursor.execute('PRAGMA foreign_keys = ON;')

        # 마이그레이션 적용
        call_command('migrate', 'room', 'zero')
        call_command('migrate', 'room')
        self.stdout.write(self.style.SUCCESS(f'Table {table_name} reset and migrations applied.'))
