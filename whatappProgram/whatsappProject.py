#import modules
import pywhatkit as py 


def send_message_and_image():
#py calls the module pywhatkit, send.whatmsg_instantly sends message 
#to the indicated number
    py.sendwhats_image(f"+1{3054696959}", img_path="C:/Users/isabelrosero/Portfolio/whatsappProgram/capybaraCute.jpeg",
                                                    caption=":)")

    py.sendwhatmsg_instantly(f"+1{3054696959}", "Hi mami :)")

send_message_and_image()