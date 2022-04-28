from json import JSONEncoder

class Encoder(JSONEncoder):
    def default(self, obj):
        if type(obj) == Player:
            return {"id":obj.id,"dice":obj.dice}
        elif type(obj) == Scores:
            return {"wins":obj.wins, "losses":obj.losses, 
                    "ties":obj.ties}
        else:
            return JSONEncoder.default(self,obj)

