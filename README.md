# An General Breakdown of the Audio Microservice
Please check the main microservice file for more details on a specific step-by-step guide of what each line of code do.

## Description
The goal of this microservice is to provide dynamic audioplay back features (with adjustable volume level & mute capability), for interactable buttons (UIs) on the main software application. That being said, the main things
to look out for would be the event (button action), button type (varying with respective SE audio), volume (customed for each UIs), and mute status (to be played, or not to be played.) Each interactable UIs will be assigned 
an audio design based on these four values, which could be dynamically used whenever, through calling this microservice.

## Testing Instruction
- Execute 'python test.py' in terminal (testing only)
- MUST BE RUN IN WINDOW POWERSHELL (testing only)

===========================================
  
### Process Overview
- Interaction Trigger [Initating send_request()]
  - Passing of request through write & read (transit: request.txt)
  - Await for microservice WAV selection & values adjustment
  - Passing of response through write & read (transit: response.txt)
- Event Execution [returning of play()]

===========================================
  
## Request
This microservice utilizes communication through text files (read & write), to transmit data between main server/program and the main microservice code/scripts.
Request is obtained by audio.py through reading the request.txt (modified by main program).
1. Given an interaction conquered with an UI, main program prepare to file a SE playback request by documenting details of expected audio values.
2. Said playback request (with expected values) are written into request.txt (after opening it)
3. audio.py open the request.txt, and read its content (sets of values) for comparison.

Coded example for sending request:  
  
    
    def send_request(event, button_type, volume, muted):  
      with open('audio_request.txt', 'w') as file:
        file.write(f'event={event}\n')
        file.write(f'button_type={button_type}\n')
        file.write(f'volume={volume}\n')
        file.write(f'muted={str(muted).lower()}\n')

## Response
1. Microservice, after deciding how the SE will be executed (values modified), the execution response will be sent back via the response.txt.
2. [Contents (the values) are decided by ifs comparison for modification prior to return]
3. Audio.py open the response.txt, and write new order (playability after modification of values).
   
Coded example for returning response:  

    with open('audio_response.txt', 'w') as file: file.write(response)
  
## Audio Microservice Sequence UML
<img width="3244" height="2582" alt="CS361 Audio MS UML class (Ver 2)" src="https://github.com/user-attachments/assets/27cbeaf1-93b6-4a37-a4fb-7954c62f541f" />
