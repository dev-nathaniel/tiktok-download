import subprocess
import time

result = []
start = time.time()

while len(result) < 1:
    print('started:', start)
    print('running')
    completed_process = subprocess.run(["python3", "index.py"], capture_output=True, text=True)
    output = completed_process.stdout
    print(output)
    for line in output.splitlines():
        line = line.strip()
        if line:
            result.append(line)
    # print(result)
    if len(result) > 0:
        print("Finished running process")
        end = time.time()
        print('ended:', end)
        print(end - start)


# https://p16-sign-va.tiktokcdn.com/tos-maliva-i-photomode-us/3b7c7cace08c46e9bbcdef5b6c0251ea~tplv-photomode-image.jpeg?lk3s=81f88b70&amp;nonce=59425&amp;refresh_token=0d16bf48e645fb6019003012b23225e9&amp;x-expires=1721829600&amp;x-signature=nsL3s9P5yrdbj%2B8hAH476bzJeKg%3D&amp;shp=81f88b70&amp;shcp=-
# https://p16-sign-va.tiktokcdn.com/tos-maliva-i-photomode-us/3b7c7cace08c46e9bbcdef5b6c0251ea~tplv-photomode-image.jpeg?lk3s=81f88b70&amp;nonce=59425&amp;refresh_token=0d16bf48e645fb6019003012b23225e9&amp;x-expires=1721829600&amp;x-signature=nsL3s9P5yrdbj%2B8hAH476bzJeKg%3D&amp;shp=81f88b70&amp;shcp=-


# https://v19-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-v-2370-euttp/oAQduEHrmD9gelliCDBnxA0PFGtQPYfJ2U7p48/?a=1988&amp;bti=ODszNWYuMDE6&amp;ch=0&amp;cr=0&amp;dr=0&amp;er=0&amp;lr=default&amp;cd=0%7C0%7C0%7C0&amp;br=250&amp;bt=125&amp;ft=GNDpcInz7ThIJC~rXq8Zmo&amp;mime_type=audio_mpeg&amp;qs=6&amp;rc=Zzg4Zjw3OjVmZWg1ODYzNkBpM2xxaWs5cnM6cjMzZjU8M0AvMTFgXy01Ni8xMjZgYWIzYSNzYmJeMmRjanJgLS1kMWNzcw%3D%3D&amp;btag=e00088000&amp;expire=1721666428&amp;l=20240722154014286DE1456AA2547B745A&amp;ply_type=3&amp;policy=3&amp;signature=8a4f0cf2bf7d449cffb5241993a47d56&amp;tk=0
# https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-v-2370-euttp/oglmCKZBi89TunAuPz6IpxwIKhPvKoiXT0M6U/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ft=GNDpcInz7ThltC~rXq8Zmo&mime_type=audio_mpeg&qs=6&rc=OTM8ZDw3NGc4aDlkZTZnNkBpanR1dXY5cjo3dDMzZjU8M0BiNmNjNmFfX2IxYTRgNjViYSNfMGlyMmRrczJgLS1kMWNzcw%3D%3D&btag=e00088000&expire=1721664626&l=20240722150952766C3B0F0837A87B9A23&ply_type=3&policy=3&signature=caff4507f29b61c53f44bb01710833f8&tk=0