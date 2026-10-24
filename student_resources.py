import os

resources = {
    "python": [
        {
            "title": "Python Basics Notes",
            "link": "https://www.w3schools.com/python/"
        }
    ],
    "physics": [
        {
            "title": "Physics Study Materials",
            "link": "https://www.khanacademy.org/science/physics"
        }
    ],
    "math": [
        {
            "title": "Math Study Materials",
            "link": "https://www.khanacademy.org/math"
        }
    ]
}

# Load saved resources
if os.path.exists("notes.txt"):
    file = open("notes.txt", "r", encoding="utf-8")
    for line in file:
        data = line.strip().split("|")

        if len(data) == 3:
            subject = data[0].lower()

            if subject not in resources:
                resources[subject] = []

            resources[subject].append({
                "title": data[1],
                "link": data[2]
            })

    file.close()


while True:
    print("\n===== Student Resource Directory =====")
    print("1. Search Notes")
    print("2. Add New Notes")
    print("3. Show All Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ").lower()

        if subject in resources:
            for note in resources[subject]:
                print("Title:", note["title"])
                print("Link:", note["link"])
        else:
            print("No notes found!")

    elif choice == "2":
        subject = input("Enter subject name: ").lower()
        title = input("Enter note title: ")
        link = input("Enter note link: ")

        if subject not in resources:
            resources[subject] = []

        resources[subject].append({
            "title": title,
            "link": link
        })

        file = open("notes.txt", "a", encoding="utf-8")
        file.write(subject + "|" + title + "|" + link + "\n")
        file.close()

        print("Notes added successfully!")

    elif choice == "3":
        for subject in resources:
            print("\nSubject:", subject)

            for note in resources[subject]:
                print("Title:", note["title"])
                print("Link:", note["link"])

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
