# room/management/commands/clear_room_table.py
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Clear all rows in the room_room table'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM room_room;")
        self.stdout.write(self.style.SUCCESS('Successfully cleared all rows in the room_room table.'))
