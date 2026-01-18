const form = document.getElementById("bookForm");
const bookList = document.getElementById("bookList");
const submitBtn = document.getElementById("submit-btn");

const bookId = document.getElementById("bookId");
const title = document.getElementById("title");
const author = document.getElementById("author");
const price = document.getElementById("price");

const API_URL = "/books";

document.addEventListener("DOMContentLoaded", loadBooks);

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const book = {
        title: title.value,
        author: author.value,
        price: parseFloat(price.value)
    };

    if(bookId.value === ""){
        await axios.post(API_URL, book);
    } else {
        await axios.put(`${API_URL}/${bookId.value}`, book);
    }

    form.reset();
    bookId.value = "";
    submitBtn.innerText = "Add Book";
    loadBooks();
});

async function loadBooks() {
    const response = await axios.get(API_URL);
    const books = response.data;

    bookList.innerHTML = "";

    books.forEach(book => {
        const card = document.createElement("div");
        card.className = "book-card";

        card.innerHTML = `
            <h3>${book.title}</h3>
            <p>${book.author}</p>
            <p>₹${book.price}</p>
            <button class="update-btn">Update</button>
            <button class="delete-btn">Delete</button>
        `;

        card.querySelector(".update-btn").onclick = () => updateBook(book);

        card.querySelector(".delete-btn").onclick = () => deleteBook(book.id);

        bookList.appendChild(card);
    });
}

async function updateBook(book) {
    bookId.value = book.id;
    title.value = book.title;
    author.value = book.author;
    price.value = book.price;

    submitBtn.innerText = "Update Book";
}

async function deleteBook(id) {
    await axios.delete(`${API_URL}/${id}`);
    loadBooks();
}