class WhatsAppV1:
    def __init__(self, name):
        self.name = name
        print(f"Welcome to WhatsApp V1, {self.name}!")

    def message(self):
        print("You can send messages.")


class WhatsAppV2(WhatsAppV1):
    def __init__(self, name):
        super().__init__(name)
        print(f"Welcome to WhatsApp V2, {self.name}!")

    def calls(self):
        print("You can make audio and video calls.")


pavani = WhatsAppV1("Pavani")
pavani.message()

print()


ammu = WhatsAppV2("Ammu")
ammu.message()
ammu.calls()