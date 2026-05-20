import time

def send_request(event, button_type, volume, muted):
    with open('audio_request.txt', 'w') as file:
        file.write(f'event={event}\n')
        file.write(f'button_type={button_type}\n')
        file.write(f'volume={volume}\n')
        file.write(f'muted={str(muted).lower()}\n')


# test 1: play digital.wav sound
send_request(
    event='button_clicked',
    button_type='digital',
    volume=70,
    muted=False
)
'''
time.sleep(1)

# test 2: play generic sound
send_request(
    event='button_clicked',
    button_type='undo',
    volume=50,
    muted=False
)

time.sleep(1)

# test 3: muted sound should not play
send_request(
    event='button_clicked',
    button_type='material_sand',
    volume=70,
    muted=True
)

time.sleep(1)

# Test 4: invalid button type
send_request(
    event='button_clicked',
    button_type='fake_button',
    volume=70,
    muted=False
)
'''