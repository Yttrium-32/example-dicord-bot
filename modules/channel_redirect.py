class ChannelRedirect:
    def __init__(self, channel_dict: dict, message: str) -> None:
        self.channel_dict = channel_dict
        self.message = message

    def get_relevant_channel(self):
        msg_word_list: list[str] = self.message.strip().split()
        relevant_channels: list[str] = []

        for word in msg_word_list:
            if channel := self.channel_dict.get(word):
                relevant_channels.append(channel)

        return relevant_channels

