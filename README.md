# Card Collection Viewer - Contribution Guide

This project lets you browse character cards categorized by series, with filtering by type (Video Game, Anime, Vtuber), and includes a 3D viewer for each card.

## 🧩 How to Add a New Character

If you'd like to contribute new characters to the project, follow these steps:

### 🔧 Files to Modify

- **Image Editing**: Use the GIMP file `card_template.xcf` to create the front image of the card.
- **Add Character**: Insert your new character into the proper category inside the `index.html` script, specifically within the `cardData` object.
- If the character has multiple card versions (e.g. "Ganyu_1.png", "Ganyu_2.png"), ensure they follow the naming convention so the navigation in the viewer works.

### 🔀 Branch Workflow

- **Do not fork** the repository unless you are contributing from outside the project.
- Instead, **create a new branch** from `main`.
  ```bash
  git checkout -b add-new-character
  ```
- After making changes, push your branch:
  ```bash
  git push origin add-new-character
  ```
- Then, **open a Pull Request** to propose your modifications.

### 📝 Example

To add a new character like "Hinagiku" from a video game:
- Add their card in the `card_template.xcf`.
- Export the image as `Hinagiku.png`.
- Add `"Hinagiku"` inside the correct category (e.g., `"New Game Series"`) in `cardData` in `index.html`.

---

## ❓ New to Git?
Here’s a basic workflow to contribute:
```bash
# Clone the project
git clone https://github.com/your-username/project-name.git
cd project-name

# Create a branch for your work
git checkout -b add-my-character

# Make your changes (edit index.html, add image files, etc.)

# Stage and commit
git add .
git commit -m "Added new character: Hinagiku"

# Push your branch
git push origin add-my-character
```
Then go to GitHub and open a Pull Request from your branch to `main`.

---

## 💬 Communication

If you want to ask a question or suggest an idea before contributing:
- You can open an **issue** on the GitHub repository.
- Or reach out directly via **Twitter**: [@SnowBunnBunn](https://twitter.com/SnowBunnBunn)

Please keep all communication respectful and constructive. Contributions are welcome from everyone!

---

Thank you for your contribution! 💖
