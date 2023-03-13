def tokenize(input_string):
    delimiter = [
        "(",
        ")",
        ":",
        ",",
        ".",
        "=",
        "+",
        "-",
        "*",
        "/",
        "<",
        ">",
        "!",
        "&",
        "|",
        "~",
        "%",
        " ",
        "[",
        "]",
        "{",
        "}",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        '"',
    ]
    # Initialize list of tokens
    tokens = []
    # Initialize temporary string buffer
    buffer = ""
    # Iterate over input string one character at a time
    for ch in input_string:
        # Check if character is a delimiter
        if ch in delimiter:
            # If so, add preceding characters to list of tokens
            if buffer != "":
                tokens.append(buffer)
                buffer = ""
            if ch != " ":
                tokens.append(ch)
            case  # if ch != " ":
            #    buffer += ch
        else:
            # Otherwise, add character to buffer
            buffer += ch
    # Add any remaining characters in buffer to list of tokens
    if buffer != "":
        tokens.append(buffer)

    # Return list of tokens
    return tokens


def _init():
    pass
