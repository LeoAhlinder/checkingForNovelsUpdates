import React from "react";
import "./App.css";

function NovelLibrary() {
  const books = [
    { title: "1984", author: "George Orwell" },
    { title: "To Kill a Mockingbird", author: "Harper Lee" },
    { title: "The Great Gatsby", author: "F. Scott Fitzgerald" },
    { title: "Brave New World", author: "Aldous Huxley" },
  ];

  return (
    <div className="library-container">
      <h1 className="library-title">My Book Library</h1>
      <div className="book-list">
        {books.map((book, index) => (
          <div key={index} className="book-card">
            <h3 className="book-title">{book.title}</h3>
            <p className="book-author">by {book.author}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default NovelLibrary;
