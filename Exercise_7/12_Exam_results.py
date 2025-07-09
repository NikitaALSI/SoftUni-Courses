results = {}
languages = {}

while (submission := input()) != "exam finished":
    if "banned" in submission:
        name = submission.split("-")[0]
        del results[name]
    else:
        name, lang, points = submission.split("-")
        if name not in results:
            results[name] = int(points)
        else:
            results[name] = max(results[name], int(points))

        languages[lang] = languages.get(lang, 0) + 1

print("Results:")
for student, points in results.items():
    print(f"{student} | {points}")
print("Submissions:")
for lang, count in languages.items():
    print(f"{lang} - {count}")

