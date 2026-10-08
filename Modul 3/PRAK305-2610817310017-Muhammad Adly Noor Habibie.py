total_seconds = int(input())

days = (total_seconds // 86400)
remaining_seconds = (total_seconds % 86400)

hours = (remaining_seconds // 3600)

remaining_seconds %= 3600

minutes = (remaining_seconds // 60)
seconds = (remaining_seconds % 60)

if (days > 0):
    print(f"{days} hari {hours:02d}:{minutes:02d}:{seconds:02d}")
else:
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")