
# Interactive 3D Card Viewer

This project allows you to view and interact with 3D anime character cards directly in the browser. You can rotate, zoom, and filter cards based on various categories.

## 🖼️ Images and Editing

All images are designed in **GIMP** using the `.xcf` file format.  
To add or modify a character card, open the file:

```
assets/card-template.xcf
```

You can use this template to place your character art, and export to `.png`.

## ➕ Adding a New Character (for beginners)

If you've **never used Git** before, don't worry! Follow these simple steps:

1. Go to the GitHub page of the project.
2. Click on **"Fork"** (top right) to make your own copy of the project.
3. In your fork, click on **"Add file" → "Upload files"** and upload your new card image(s) in Pic/Front/.
4. Edit the `index.html` file to add your new character manually.
5. When you're done, click **"Pull Request"** and submit your changes to the original project.

> ❗ You cannot create branches directly on this repository — use a **fork** instead.

## 🎴 Variants

If you want to submit **alternate versions** of a character card (e.g. outfit changes, special events), name your files like this:
- `Ganyu_1.png`
- `Ganyu_2.png`
- `Ganyu_3.png`

Each numbered version is considered a variant of the same character and should be referenced as separate entries in `index.html`.

### 📝 Example

To add a new character like "Hinagiku" from a video game:
- Add their card in the `card_template.xcf`.
- Export the image as `Hinagiku.png`.
- Add `"Hinagiku"` inside the correct category (e.g., `"New Game Series"`) in `cardData` in `index.html`.

---


## 💬 Communication

If you want to ask a question or suggest an idea before contributing:
- You can open an **issue** on the GitHub repository.
- Or reach out directly via **Twitter**: [@SnowBunnBunn](https://twitter.com/SnowBunnBunn)

Please keep all communication respectful and constructive. Contributions are welcome from everyone!

---

Thank you for your contribution! 💖