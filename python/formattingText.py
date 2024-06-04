class formatObject(object):
    def __init__(self, text_message: str):
        self.tm = text_message

    @property
    def bold(self):
        return f"*{self.tm}*"
    
    @property
    def italic(self):
        return f"_{self.tm}_"
    
    def add_link(self, link: str):
        return f"[{self.tm}]({link})"
    
    def add_info(self, details: str):
        return f"```[{self.tm}]{details}```"