title = input()
content = input()
print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")
while (cmd:=input()) != "end of comments":
    print(f"<div>\n    {cmd}\n</div>")


