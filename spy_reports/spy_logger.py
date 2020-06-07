from player.messages.spy_message_detail import SpyMessageDetail


class SpyLogger():
    @staticmethod
    def save_into_file(spy_messages: [SpyMessageDetail], planet_name:str):
        report = ""
        for spy_message in spy_messages:
            report += str(spy_message)

        file_path = "spy_reports/{}.txt".format(planet_name)
        with open(file_path, "w") as f:
            f.write(report)

