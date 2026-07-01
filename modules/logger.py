import datetime, json
class SystemLogger:
    def log(self, entry):
        with open("mission_log.json", "a", encoding="utf-8") as f:
            f.write(json.dumps({"time": str(datetime.datetime.now()), "result": entry}) + "\n")
