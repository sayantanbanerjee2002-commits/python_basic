class Book:
    
    
    # Class variable
    total_books = 0
    
    def __init__(self, title, author, isbn, copies):
        """Initialize a book"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self._available = copies
        Book.total_books += 1
    
    @property
    def available(self):
        """Get available copies"""
        return self._available
    
    def borrow(self):
        """Borrow a book"""
        if self._available > 0:
            self._available -= 1
            return True
        return False
    
    def return_book(self):
        """Return a book"""
        if self._available < self.copies:
            self._available += 1
            return True
        return False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"
    
    @classmethod
    def from_string(cls, book_string):
        """Create book from string: 'Title|Author|ISBN|Copies'"""
        title, author, isbn, copies = book_string.split('|')
        return cls(title, author, isbn, int(copies))


class Member:
    """Represents a library member"""
    
    member_count = 0
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        Member.member_count += 1
    
    def borrow_book(self, book):
        """Borrow a book"""
        if book.borrow():
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'"
        return f"Sorry, '{book.title}' is not available"
    
    def return_book(self, book):
        """Return a book"""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'"
        return f"{self.name} doesn't have '{book.title}'"
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"
    
    def __len__(self):
        """Number of books currently borrowed"""
        return len(self.borrowed_books)


class Library:
    """Represents the library"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """Add a book to library"""
        self.books.append(book)
        return f"Added '{book.title}' to library"
    
    def register_member(self, member):
        """Register a new member"""
        self.members.append(member)
        return f"Registered {member.name}"
    
    def find_book(self, title):
        """Find a book by title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def display_books(self):
        """Display all books"""
        print(f"\n{self.name} - Books:")
        print("-" * 50)
        for book in self.books:
            print(f"{book} - Available: {book.available}/{book.copies}")
    
    def display_members(self):
        """Display all members"""
        print(f"\n{self.name} - Members:")
        print("-" * 50)
        for member in self.members:
            print(f"{member} - Books borrowed: {len(member)}")
    
    def __len__(self):
        """Total number of books in library"""
        return len(self.books)
    
    def __str__(self):
        return f"{self.name} Library ({len(self)} books, {len(self.members)} members)"


# Using the Library Management System
if __name__ == "__main__":
    # Create library
    library = Library("City Central Library")
    
    # Add books
    book1 = Book("Harry Potter", "J.K. Rowling", "123456", 3)
    book2 = Book("1984", "George Orwell", "789012", 2)
    book3 = Book.from_string("The Hobbit|J.R.R. Tolkien|345678|1")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Register members
    member1 = Member("Rahul", "M001")
    member2 = Member("Priya", "M002")
    
    library.register_member(member1)
    library.register_member(member2)
    
    # Display library status
    print(library)
    library.display_books()
    library.display_members()
    
    # Borrow books
    print("\n" + "="*50)
    print("BORROWING BOOKS")
    print("="*50)
    print(member1.borrow_book(book1))
    print(member1.borrow_book(book2))
    print(member2.borrow_book(book1))
    print(member2.borrow_book(book3))
    
    # Display updated status
    library.display_books()
    library.display_members()
    
    # Return books
    print("\n" + "="*50)
    print("RETURNING BOOKS")
    print("="*50)
    print(member1.return_book(book1))
    print(member2.return_book(book3))
    
    # Final status
    library.display_books()
    library.display_members()
    
    # Statistics
    print("\n" + "="*50)
    print("STATISTICS")
    print("="*50)
    print(f"Total books in system: {Book.total_books}")
    print(f"Total members: {Member.member_count}")
