

class MyDict(dict):
    def get_recursive(self, *keys):
        if keys and self:
            element  = keys[0]
            if element:
                value = self.get(element)
                return value
            if len(keys) == 1:
                return value
            else:
                self.get_recursive(value, *keys[1:])
        return None
