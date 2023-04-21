def main() -> None:
    names0: dict[str,str] = {"pres.": "lily", "VP": "ruby" }
    names1: dict[str,str] = {"VP": "Carlos", "Sec": "lin"}
    officers: dict[str,str] = merge(names0, names1)
    print(officers)

def merge(a: dict[str,str], b: dict[str,str]) -> dict[str,str]:
    result: dict[str,str] = {}
    for key in a:
        result[key] = a[key]
    for key in b:
        result[key] = b[key]
    return result

if __name__ == "__main__":
    main()