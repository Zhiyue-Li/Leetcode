def reorderLogFiles(self, logs: list[str]) -> list[str]:
    def keysort(log):
        ident, vals = log.split(" ", maxsplit=1)
        return [0, vals, ident] if vals[0].isalpha() else [1]
    # key takes a single argument and returns a key to use for sorting purposes
    return sorted(logs, key=keysort)