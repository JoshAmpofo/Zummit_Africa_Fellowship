"""
Author: Joshua Ampofo Yentumi

Problem 3: File Extensions

Description: Implement a program that prompts the user for the name of a file and then outputs the file's media type 
             if the file's name ends, case-insentively, in any of these suffixes: ".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip".
             If the file's name ends with some other suffix or has no suffix at all, output "application/octet-stream" instead, which is a common default.
"""

def main():
    filename = input("File name: ").lower().strip()
    return exten(filename)


def exten(filename):
    """Prints out the media type of a file inputted by a user using its extension"""
    if filename.endswith(".gif"):
        return "image/gif"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        return "image/jpeg"
    elif filename.endswith(".png"):
        return "image/png"
    elif filename.endswith(".pdf"):
        return "application/pdf"
    elif filename.endswith(".txt"):
        return "text/plain"
    elif filename.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


if __name__ == '__main__':
    print(main())
