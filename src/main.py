from textnode import TextNode, TextType
def main():
    the_funny = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(the_funny)
main()