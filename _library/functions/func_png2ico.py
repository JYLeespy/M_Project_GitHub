from PIL import Image

logo = Image.open("D:/ProgramData/Project/Super Jinyoung/ico/4.png")
logo.save("D:/ProgramData/Project/Super Jinyoung/ico/4.ico", format='ICO')

print('''
프로그램이 실행되었습니다                          UPDATE 2024 02 23
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    ┎───────┐┎──┐   ┎──┐   ┎──┐       ┎─────────┐┎─────────┐  ┃
┃    ┗━━━━┓  │┃  │   ┃  │   ┃  │       ┃  ┍━━━━━━┙┃  ┍━━━━━━┙  ┃
┃         ┃  │┃  │   ┃  │   ┃  │       ┃  │       ┃  │         ┃
┃         ┃  │┃  └───┚  │   ┃  │       ┃  └──────┐┃  └──────┐  ┃
┃  ┎──┐   ┃  │┗━━━━━━┓  │   ┃  │       ┃  ┍━━━━━━┙┃  ┍━━━━━━┙  ┃
┃  ┃  │   ┃  │┎──┐   ┃  │   ┃  │       ┃  │       ┃  │         ┃
┃  ┃  └───┚  │┃  └───┚  │┎─┐┃  └──────┐┃  └──────┐┃  └──────┐  ┃
┃  ┗━━━━━━━━━┙┗━━━━━━━━━┙┗━┙┗━━━━━━━━━┙┗━━━━━━━━━┙┗━━━━━━━━━┙  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
# while True:
#     print(f'파일명을 입력하세요(확장자포함) : ',end="")
#     fullfilename = input()
#     filename = fullfilename.split('.')[0]
#     extension = fullfilename.split('.')[1]
#     logo = Image.open(f'./{filename}.{extension}')
#     logo.save(f'./{filename}.ico', format='ICO')
#     print('변환 완료')