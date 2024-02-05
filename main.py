import json

# 팔로워 읽기
with open('./inputs/followers_1.json', 'r') as file:
    followers = json.load(file)

# 팔로잉 읽기
with open('./inputs/following.json', 'r') as file:
    following = json.load(file)

# 제외할 사람 읽기
with open('./ignore_list.txt', 'r') as file:
    ignore_list = []
    for item in file.readlines():
        ignore_list.append(item.rstrip())

# 팔로워 닉네임 추가
list_followers = []
for item in followers:
    list_followers.append(item['string_list_data'][0]['value'])

# 팔로잉 닉네임 추가
list_following = []
for item in following['relationships_following']:
    list_following.append(item['string_list_data'][0]['value'])

# 팔로잉, 팔로워 비교
not_in_followers = sorted(((set(list_following) - set(ignore_list)) - set(list_followers)))

# 출력
print('팔로워 목록에 없음: \n')
for item in not_in_followers:
    print(item)
