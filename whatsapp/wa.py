
from whatsapp import WhatsApp
messenger = WhatsApp('TOKEN',  phone_number_id='6369364262', logger=True)
messenger.send_template("hello_world", "6369364262", components=[], lang="en_US")
# def send_template(
#     self: Any,
#     template: str,
#     recipient_id: str,
#     components: str,
#     lang: str = "en_US"
# )