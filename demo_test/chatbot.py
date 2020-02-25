import os
import aiml

#Create the kernel and learn AIML files or load a brain file
kernel=aiml.Kernel()
if os.path.isfile('bot_brain.brn'):
    kernel.bootstrap(brainFile='bot_brain.brn')
else:
    kernel.bootstrap(learnFiles='startup.xml',commands='load aiml b')
    kernel.saveBrain('bot_brain.brn')

#Press CTRL-C to break this loop
while True:
    message=input('Enter your message to the bot: ')
    if message=='quit':
        exit()
    elif message=='save':
        kernel.saveBrain('bot_brain.brn')
    else:
        bot_response=kernel.respond(message)
        #Do something with bot_response
        print(bot_response)