room_total = int(input())
zetsu = list(map(int, input().split()))

result = []
for room_number in range(len(zetsu)):
	result.append(zetsu[room_number] * (room_number + 1))
print(*result)